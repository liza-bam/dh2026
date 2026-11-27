"""D26-2. Architecture 2026, simple: one way in, three paths (fixed flows, domain agents, team agents), the systems, and the rules every agent follows."""
from rich import Rich, Z
from svg import SECOND
from transition import TEAL, TINT

G = '#9aa5aa'
PURPLE = '#6b4fa0'


def chip(d, x, y, text, fill='#fff', stroke='#c9d1d4', color=None, size=12):
    w = len(text) * size * 0.58 + 18
    d.rect(x, y, w, 24, fill, stroke, rx=12)
    d.t(x + w / 2, y + 16, text, size, 600, 'middle', fill=color or SECOND)
    return x + w + 6


def system(d, x, y, key, name):
    if key:
        d.logo(key, x, y, 28)
        d.t(x + 36, y + 19, name, 13, 600)
    else:
        d.el.append(f'<circle cx="{x + 14}" cy="{y + 14}" r="14" fill="#eceff0"/>')
        d.t(x + 14, y + 19, name[0], 13, 700, 'middle')
        d.t(x + 36, y + 19, name, 13, 600)


def band(d, y, h, n, title, sub, fill='#f7fafb', stroke='#dce4e7'):
    d.rect(20, y, 1130, h, fill, stroke, rx=14)
    d.el.append(f'<circle cx="46" cy="{y + 30}" r="14" fill="{TEAL}"/>')
    d.t(46, y + 35, str(n), 13, 700, 'middle', fill='#fff')
    d.t(70, y + 36, title, 17, 600)
    if sub:
        d.t(70 + len(title) * 9.6 + 14, y + 36, sub, 13, 400, fill=SECOND)


def column(d, x, y, w, h, title, model, sub, items, note=None, dark=False):
    d.rect(x, y, w, h, TINT if dark else '#f7fafb', TEAL if dark else '#dce4e7', rx=14, sw=1.5)
    d.t(x + 18, y + 34, title, 18, 600)
    if model:
        mw = len(model) * 12 * 0.58 + 18
        chip(d, x + w - mw - 14, y + 16, model, TEAL if model == 'Large model' else '#fff', TEAL, '#fff' if model == 'Large model' else TEAL)
    yy = d.lines(x + 18, y + 60, sub, w - 36, 13, 400, SECOND, lh=18) + 10
    for it in items:
        d.rect(x + 18, yy, w - 36, 34, '#fff', '#dce4e7', rx=8)
        d.t(x + 32, yy + 22, it, 14, 600)
        yy += 42
    if note:
        d.lines(x + 18, yy + 14, note, w - 36, 13, 400, SECOND, lh=18)


def build():
    d = Rich('a26', 1200, 932, 'Digital Hub 2026 architecture: one way in; three paths: fixed flows, domain agents on small models, '
             'team agents on a large model; the systems they reach; and the rules every agent follows, with people at every level')

    # channels
    d.rect(20, 20, 1160, 76, '#f7fafb', '#dce4e7', rx=14)
    d.t(40, 64, 'The employee asks', 16, 600)
    x = 230
    for icon, name in [('teams', 'Teams'), (None, 'Digital Hub website'), ('email', 'Email'), ('voice', 'Voice')]:
        d.rect(x, 34, 220, 48, '#fff', '#dce4e7', rx=10)
        if icon:
            d.image(icon, x + 12, 42, 30)
        else:
            d.rect(x + 12, 46, 30, 22, '#f5c000', '#f5c000', rx=6)
        d.t(x + 54, 64, name, 14, 600)
        x += 236
    d.arrow((600, 96), (600, 124), color=TEAL)

    # intake
    d.rect(330, 124, 540, 84, '#fff', TEAL, rx=14, sw=1.5)
    d.t(350, 156, 'Intake agent', 17, 600)
    chip(d, 870 - 14 - (len('Small model') * 12 * 0.58 + 18), 136, 'Small model', '#fff', TEAL, TEAL)
    d.t(350, 186, 'Reads what the employee writes and picks the path.', 14, 400, fill=SECOND)
    for cx in (205, 600, 995):
        d.arrow((600, 208), (cx, 236), color=TEAL)

    # three paths
    column(d, 20, 240, 370, 372, 'Fixed flows', None, 'Simple actions. No model decides anything: the employee chooses, the systems act.',
           ['A new device', 'An assistant\u2019s access', 'A Teams channel', 'A password reset', 'A meeting room'])
    column(d, 415, 240, 370, 372, 'Domain agents', 'Small models', 'Problems that need a decision. One agent leads each case.',
           ['Security', 'Devices', 'Software', 'Mail and calendar', 'Workplace'],
           'A watcher agent finds problems before anyone asks.', dark=True)
    column(d, 810, 240, 370, 372, 'Team agents', 'Large model', 'Nothing fits: a ticket goes to the right team, and its agent helps the engineers.',
           ['Network', 'Messaging', 'End-user computing'],
           'What the engineers solve comes back to the domain agents as a new fix.')

    # systems: what the agents work with
    d.rect(20, 632, 1160, 176, '#f7fafb', '#dce4e7', rx=14)
    d.t(40, 664, 'Systems the agents work with', 16, 600)
    SYS = [('now', 'ServiceNow', 'Tickets and requests'), ('workday', 'Workday', 'Who the employee is: role, team'),
           ('azure', 'Entra ID', 'Accounts, passwords, access'), (None, 'Intune', 'Laptops: installs, locks, wipes'),
           ('nexthink', 'Nexthink', 'How each laptop is doing'), ('office', 'Office 365', 'Mail, calendar, Teams'),
           ('ariba', 'SAP Ariba', 'Ordering devices')]
    for k, (key, name, what) in enumerate(SYS):
        x = 40 + (k % 4) * 284
        y = 680 + (k // 4) * 62
        d.rect(x, y, 270, 54, '#fff', '#dce4e7', rx=10)
        if key:
            d.logo(key, x + 12, y + 13, 28)
        else:
            d.el.append(f'<circle cx="{x + 26}" cy="{y + 27}" r="14" fill="#eceff0"/>')
            d.t(x + 26, y + 32, name[0], 13, 700, 'middle')
        d.t(x + 50, y + 24, name, 14, 600)
        d.t(x + 50, y + 42, what, 12, 400, fill=SECOND)

    # rules and people
    d.rect(20, 824, 700, 96, '#fff', '#223640', rx=14, sw=1.5)
    d.t(40, 852, 'Every agent', 15, 600)
    d.lines(40, 876, 'Has its own identity, touches only its own systems, answers only from approved knowledge, and every action is logged. Risky actions wait for a yes.', 660, 13, 400, SECOND, lh=17)
    d.rect(736, 824, 444, 96, Z['agent'][0], Z['agent'][1], dashed=True, rx=14)
    for i in range(3):
        d.image(f'agent{i + 1}', 752 + i * 34, 852, 40, round_=True, ring=Z['agent'][1])
    d.lines(880, 866, 'People at every level: they approve, take over and decide.', 286, 14, 600, lh=19)
    d.H = 932
    return d

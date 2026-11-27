"""D19-12b / D26-17. The bad update as a blueprint in Sandy's 2019 style: people on top, systems below,
the data written on the arrows between them. Same seven steps in 2019 and 2026."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import symbol

W = 1180
X0, COL = 140, 160            # first column centre, column width
TOP, BOT = 96, 470            # top of the people band, top of the systems band
PY, R = 250, 44               # people circles
SY1, SY2, SY3, SR = 560, 690, 820, 34   # system circles
H = 990
GREY = '#f4f7f8'
LINE = '#5d6b72'
RED = '#c0392b'


def cx(i):
    return X0 + i * COL


def glyph(d, name, x, y, s, fill=TEAL):
    k = s / 960
    d.el.append(f'<path d="{symbol(name)}" fill="{fill}" transform="translate({x - s / 2:.1f} {y + s / 2:.1f}) scale({k:.4f})"/>')


def person(d, i, kind, badge=None):
    """kind: peter (a laptop) or engineer (a person at work). badge: alert, message or done."""
    x = cx(i)
    if kind == 'peter':
        d.el.append(f'<circle cx="{x}" cy="{PY}" r="{R}" fill="{TINT}"/>')
        glyph(d, 'laptop_mac', x, PY, 50)
    else:
        d.el.append(f'<circle cx="{x}" cy="{PY}" r="{R}" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
        glyph(d, 'engineering', x, PY, 50)
    if badge:
        bx, by = x + 32, PY - 32
        col = RED if badge == 'alert' else TEAL
        d.el.append(f'<circle cx="{bx}" cy="{by}" r="15" fill="{col}" stroke="#fff" stroke-width="2"/>')
        glyph(d, {'alert': 'notifications', 'message': 'chat_bubble', 'done': 'check_circle'}[badge], bx, by, 18, '#fff')


def robot(d, x, y, name):
    """An agent: a system with its own account, drawn as a robot with its platform's name."""
    d.el.append(f'<circle cx="{x}" cy="{y}" r="{SR}" fill="{TINT}" stroke="{TEAL}" stroke-width="1.5"/>')
    glyph(d, 'smart_toy', x, y - 4, 38)
    w = len(name) * 8.2 + 18
    d.rect(x - w / 2, y + SR - 12, w, 22, TEAL, TEAL, rx=11, sw=0)
    d.t(x, y + SR + 4, name, 14, 600, 'middle', fill='#fff')


def system(d, x, y, key, name=None):
    if key == 'intune':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{SR}" fill="#fff" stroke="#dce4e7"/>')
        d.t(x, y + 9, 'Intune', 15, 700, 'middle')
    elif key == 'hub':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{SR}" fill="#fff" stroke="#dce4e7"/>')
        d.rect(x - 20, y - 14, 40, 28, '#f5c000', '#f5c000', rx=0, sw=0)
    elif key == 'cloud':
        d.logo('office', x - SR, y - SR, 2 * SR)
    else:
        d.logo(key, x - SR, y - SR, 2 * SR)
    if name:
        for k, ln in enumerate(name.split('\n')):
            d.t(x, y + SR + 21 + k * 19, ln, 15, 600, 'middle', fill=SECOND)


def vline(d, x, y1, y2, label=None, ly=None, dashed=False):
    da = ' stroke-dasharray="6 5"' if dashed else ''
    d.el.append(f'<path d="M{x:.0f} {y1:.0f}V{y2:.0f}" fill="none" stroke="{TEAL}" stroke-width="2"{da} marker-end="url(#m{d.uid})"/>')
    if label:
        ls = label.split('\n')
        w = max(len(s) for s in ls) * 8.4 + 14
        h = 22 * len(ls) + 6
        d.rect(x - w / 2, ly - h / 2, w, h, '#fff', '#fff', rx=0, sw=0)
        for k, s in enumerate(ls):
            d.t(x, ly - h / 2 + 20 + k * 22, s, 15, 700, 'middle', fill=TEAL)


def pair(d, x, up, down, ly=400, down_first=False):
    """Two arrows between a person and a system: up brings data to the person, down takes their answer back."""
    for dx, y1, y2 in [(-10, SY1 - SR - 6, PY + R + 4), (10, PY + R + 4, SY1 - SR - 6)]:
        d.el.append(f'<path d="M{x + dx:.0f} {y1:.0f}V{y2:.0f}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    u, dn = [('up', t) for t in up.split('\n')], [('down', t) for t in down.split('\n')]
    lines = dn + u if down_first else u + dn
    w = max(len(t) for _, t in lines) * 8.4 + 34
    h = 22 * len(lines) + 8
    y0 = ly - h / 2
    d.rect(x - w / 2, y0, w, h, '#fff', '#fff', rx=0, sw=0)
    first = {}
    for k, (way, t) in enumerate(lines):
        ty = y0 + 20 + k * 22
        if way not in first:
            first[way] = 1
            tx = x - w / 2 + 10
            tri = f'{tx},{ty - 3} {tx + 10},{ty - 3} {tx + 5},{ty - 12}' if way == 'up' else f'{tx},{ty - 12} {tx + 10},{ty - 12} {tx + 5},{ty - 3}'
            d.el.append(f'<polygon points="{tri}" fill="{TEAL}"/>')
        d.t(x - w / 2 + 26, ty, t, 15, 700, 'start', fill=TEAL)


def path(d, *pts, label=None, at=None):
    p = 'M' + ' L'.join(f'{a:.0f} {b:.0f}' for a, b in pts)
    d.el.append(f'<path d="{p}" fill="none" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round" marker-end="url(#m{d.uid})"/>')
    if label:
        d.t(at[0], at[1], label, 15, 600, 'middle', fill=SECOND)


def hline(d, x1, x2, y):
    d.el.append(f'<path d="M{x1:.0f} {y:.0f}H{x2:.0f}" fill="none" stroke="{LINE}" stroke-width="1.8" marker-end="url(#m{d.uid})"/>')


def head(d, i, n, title, text):
    x = cx(i)
    d.el.append(f'<circle cx="{x - COL / 2 + 22}" cy="{TOP + 4}" r="13" fill="{TEAL}"/>')
    d.t(x - COL / 2 + 22, TOP + 9, str(n), 14, 700, 'middle', fill='#fff')
    d.t(x - COL / 2 + 42, TOP + 10, title, 16, 700, fill=TEAL)
    d.lines(x - COL / 2 + 10, TOP + 40, text, COL - 16, 15, 400, INK, lh=20)


def frame(d, label, agents=True):
    d.rect(60, TOP - 36, W - 80, BOT - TOP + 26, '#fff', '#dce4e7', rx=0, sw=1)
    d.rect(60, BOT, W - 80, H - BOT - 70, GREY, GREY, rx=0, sw=0)
    for y0, y1, s in [(TOP - 36, BOT - 10, 'PEOPLE'), (BOT, H - 70, 'SYSTEMS')]:
        cy = (y0 + y1) / 2
        d.el.append(f'<text x="36" y="{cy:.0f}" transform="rotate(-90 36 {cy:.0f})" font-family="\'Inter\', sans-serif" font-size="14" '
                    f'font-weight="600" letter-spacing="3" fill="{SECOND}" text-anchor="middle">{s}</text>')
    # key
    y = H - 40
    d.el.append(f'<path d="M64 {y}h34" stroke="{TEAL}" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    d.t(108, y + 5, 'The words on an arrow: the data that moves, and which way', 15, 400, fill=SECOND)
    if agents:
        d.el.append(f'<circle cx="640" cy="{y}" r="13" fill="{TINT}" stroke="{TEAL}" stroke-width="1.5"/>')
        glyph(d, 'smart_toy', 640, y - 1, 16)
        d.t(662, y + 5, 'An agent: a system with its own account', 15, 400, fill=SECOND)
    d.t(W - 20, y + 5, label, 15, 700, 'end', fill=INK)


STEPS = [
    ('Crash', 'Visio won’t start after the update'),
    ('Ticket', 'A ticket opens. Peter does nothing'),
    ('Workaround', 'Peter keeps working'),
    ('Cause', 'The engineer finds out why'),
    ('Hold', 'The update stops for everyone else'),
    ('Fix', 'The fix is written and approved'),
    ('Fixed', 'Peter hears back and rates it'),
]


def base(uid, label, year):
    d = Rich(uid, W, H, label)
    frame(d, year, agents=year != '2019')
    for i, (t, s) in enumerate(STEPS):
        head(d, i, i + 1, t, s)
    return d


def build19():
    d = base('bu19', 'A bad Visio update in 2019: Peter is told at each step, the engineer searches for the cause and writes the fix, Digital Hub scripts do the rest', '2019')
    # 1 crash
    person(d, 0, 'peter', 'alert'); system(d, cx(0), SY1, 'nexthink', 'Nexthink')
    vline(d, cx(0), PY + R + 4, SY1 - SR - 6, 'Crash\nand version', 400)
    # 2 ticket
    system(d, cx(1), SY1, 'hub', 'Digital Hub'); system(d, cx(1), SY2, 'now', 'ServiceNow')
    hline(d, cx(0) + SR + 6, cx(1) - SR - 8, SY1)
    vline(d, cx(1), SY1 + SR + 28, SY2 - SR - 6)
    # 3 workaround
    person(d, 2, 'peter', 'message'); system(d, cx(2), SY1, 'hub', 'Digital Hub')
    vline(d, cx(2), SY1 - SR - 6, PY + R + 4, 'Virtual\nmachine', 400)
    # 4 cause
    person(d, 3, 'engineer'); system(d, cx(3), SY1, 'nexthink', 'Nexthink'); system(d, cx(3), SY2, 'now', '3 similar tickets')
    pair(d, cx(3), 'The cause:\nthe update', 'She searches', down_first=True)
    # 5 hold
    person(d, 4, 'peter', 'message'); system(d, cx(4), SY1, 'hub', 'Holds the update')
    vline(d, cx(4), SY1 - SR - 6, PY + R + 4, 'Update held,\nfix underway', 400)
    # 6 fix
    person(d, 5, 'engineer'); system(d, cx(5), SY1, 'hub', 'Runs her steps')
    vline(d, cx(5), PY + R + 4, SY1 - SR - 6, 'Steps she\nwrote', 400)
    # 7 fixed
    person(d, 6, 'peter', 'done'); system(d, cx(6), SY1, 'hub', 'Digital Hub'); system(d, cx(6), SY2, 'now', 'ServiceNow')
    pair(d, cx(6), '\u201cWe fixed it\u201d', 'Rating')
    vline(d, cx(6), SY1 + SR + 28, SY2 - SR - 6)
    return d


def build26():
    d = base('bu26', 'A bad Visio update in 2026: Peter sees the same steps; agents and flows do the work; the engineer only confirms the cause and approves the fix', '2026')
    # 1 crash
    person(d, 0, 'peter', 'alert'); system(d, cx(0), SY1, 'nexthink', 'Nexthink')
    vline(d, cx(0), PY + R + 4, SY1 - SR - 6, 'Crash\nand version', 400)
    # 2 ticket: a webhook opens an incident
    system(d, cx(1), SY1, 'now', 'Incident')
    hline(d, cx(0) + SR + 6, cx(1) - SR - 8, SY1)
    d.t((cx(0) + cx(1)) / 2, SY1 - 10, 'Webhook', 15, 600, 'middle', fill=SECOND)
    # 3 workaround: the Software agent, from the knowledge base
    person(d, 2, 'peter', 'message'); robot(d, cx(2), SY1, 'Digital Hub'); system(d, cx(2), SY2, 'now', 'Knowledge base')
    vline(d, cx(2), SY1 - SR - 6, PY + R + 4, 'Visio in\nthe browser', 400)
    vline(d, cx(2), SY2 - SR - 6, SY1 + SR + 14)
    # 4 cause: ServiceNow's problem agent, with Nexthink's crashes by version
    person(d, 3, 'engineer'); robot(d, cx(3), SY1, 'ServiceNow'); system(d, cx(3), SY2, 'nexthink', 'Nexthink')
    vline(d, cx(3), SY2 - SR - 6, SY1 + SR + 14)
    pair(d, cx(3), 'Analysis,\nready', 'Yes')
    # 5 hold: a flow pauses the update; Teams tells Peter
    person(d, 4, 'peter', 'message'); system(d, cx(4), SY1, 'teams', 'Teams'); system(d, cx(4), SY3, 'cloud', 'Cloud Update\npaused')
    vline(d, cx(4), SY1 - SR - 6, PY + R + 4, 'Update held,\nfix underway', 400)
    path(d, (cx(3) + SR + 4, SY1 + 6), (cx(3) + 70, SY1 + 6), (cx(3) + 70, SY3), (cx(4) - SR - 8, SY3), label='Pause', at=(cx(3) + 98, SY3 - 10))
    # 6 fix: Intune sets the settings, Cloud Update rolls the update out
    person(d, 5, 'engineer'); robot(d, cx(5), SY1, 'ServiceNow'); system(d, cx(5), SY2, 'intune', 'Settings'); system(d, cx(5), SY3, 'cloud', 'Cloud Update\nin waves')
    pair(d, cx(5), 'Steps,\nready', 'Yes')
    vline(d, cx(5), SY1 + SR + 14, SY2 - SR - 6)
    vline(d, cx(5), SY2 + SR + 26, SY3 - SR - 6)
    # 7 fixed: closing the problem closes every incident; Teams tells Peter
    person(d, 6, 'peter', 'done'); system(d, cx(6), SY1, 'teams', 'Teams'); system(d, cx(6), SY2, 'now', 'Closes all')
    pair(d, cx(6), '\u201cWe fixed it\u201d', 'Rating')
    vline(d, cx(6), SY2 - SR - 6, SY1 + SR + 26)
    return d

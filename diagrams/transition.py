"""Visual transition map: Digital Hub 2019 -> 2026."""
import pathlib
from html import escape
from rich import Rich, Z
from svg import SECOND, INK

TEAL, TINT = '#2c6e7e', '#e3eef1'
G = '#9aa5aa'
OK = '#3d8b2f'

AGENTS = {
    'front': ('Intake agent', 'chat'), 'identity': ('Identity agent', 'lock'), 'workplace': ('Workplace agent', 'room'),
    'access': ('Access agent', 'approve'), 'devices': ('Devices agent', 'hardware'), 'fix': ('Fix agent', 'tools'),
    'defender': ('Microsoft Defender', 'alert'), 'watcher': ('Watcher agent', 'software'),
}


def agent_badge(d, key, x, y, w=190, sub=None):
    from svg import wrap
    name, icon = AGENTS[key]
    ent = key == 'defender'
    if ent and not sub:
        sub = 'Enterprise agent'
    h = 56 if not sub else 58 + 17 * len(wrap(sub, w - 66, 12))
    d.rect(x, y, w, h, '#fff' if ent else TINT, '#9aa5aa' if ent else TEAL, rx=12, sw=2)
    d.el.append(f'<circle cx="{x + 28}" cy="{y + 28}" r="18" fill="#fff" stroke="{'#9aa5aa' if ent else TEAL}" stroke-width="1.5"/>')
    d.image(icon, x + 17, y + 17, 22)
    d.t(x + 56, y + 33, name, 15, 600)
    if sub:
        d.lines(x + 56, y + 54, sub, w - 66, 12, 400, SECOND)
    return y + h


# A. What changes ----------------------------------------------------------------------
def what_changes():
    rows = [
        ('Avaamo bot and NLP library', 'Answered 40+ cases written in advance', 'bot', ['avaamo'], 'front', 'Replaces the bot. Routes any request to a fixed journey, or fills a ticket'),
        ('AI scripts library', 'Fixed issues found in discovery', 'grey', ['holmes'], 'fix', 'Replaces Holmes. Runs approved fixes through Nexthink and Intune; an engineer approves new ones'),
        ('Preventive measures', 'Monitoring found problems early', 'grey', ['nexthink'], 'watcher', 'Reads the same telemetry and opens cases itself'),
        ('Self-help UI', 'The employee did the steps', 'hub', ['azure', 'ariba', 'office'], 'access', 'Does the steps in the same systems for the employee'),
        ('AI issue triage', 'Urgency and sentiment decided when to call a person', 'bot', ['avaamo'], 'front', 'Reads urgency and mood from the conversation; handoff rules decide when to call a person'),
        ('Live agent session', 'A person took over with all the data', 'agent', ['genesys'], None, 'Same. The card also shows what the agents already did'),
    ]
    d = Rich('wc', 1120, 60 + len(rows) * 104, 'What changes from 2019 to 2026')
    d.t(20, 30, '2019', 20, 600)
    d.t(620, 30, '2026', 20, 600, fill=TEAL)
    y = 56
    for title, sub, kind, logos, agent, after in rows:
        fill, stroke = Z[kind]
        d.rect(20, y, 470, 84, fill, stroke, dashed=True, rx=12)
        lx = 36
        for lg in logos:
            if lg in ('holmes', 'genesys'):
                d.wordmark(lg, lx, y + 26, 86, 32)
                lx += 92
            else:
                d.logo(lg, lx, y + 22, 40)
                lx += 46
        d.t(lx + 10, y + 36, title, 16, 600)
        d.lines(lx + 10, y + 58, sub, 470 - lx - 20, 13, 400, SECOND)
        d.arrow((500, y + 42), (600, y + 42), color=TEAL)
        if agent:
            agent_badge(d, agent, 620, y + 4, 480, after)
        else:
            d.rect(620, y + 4, 480, 74, '#fff', TEAL, rx=12, sw=2)
            d.t(640, y + 36, 'Kept: Genesys', 15, 600, fill=TEAL)
            d.lines(640, y + 58, after, 440, 12, 400, SECOND)
        y += 104
    return d


# B. Architecture ------------------------------------------------------------------------
def architecture():
    d = Rich('ar', 1500, 900, 'Digital Hub 2026 architecture: channels, front door agent, specialist agents, systems, people')
    # employees and channels
    d.zone(20, 20, 230, 840, 'Employees', 'grey', 'Same channels as 2019')
    for i in range(4):
        d.image(f'cust{i + 1}', 40 + (i % 2) * 90, 76 + (i // 2) * 84, 64, round_=True, ring='#b7c1c5')
    y = 260
    for icon, name in [('email', 'Email'), ('chat', 'Chat'), ('voice', 'Voice'), (None, 'Digital Hub app')]:
        d.rect(40, y, 190, 60, '#fff', '#dce4e7', rx=10)
        if icon:
            d.image(icon, 54, y + 14, 32)
        else:
            d.rect(54, y + 17, 32, 26, '#f5c000', '#f5c000', rx=6)
        d.t(100, y + 36, name, 15, 600)
        d.arrow((230, y + 30), (300, y + 30), (300, 430), (330, 430), color=G)
        y += 74
    d.card(40, 580, 190, 'Employee context', [('workday', 'Profile and role'), ('office', 'Calendar'), ('nexthink', 'Device'), ('now', 'Tickets')], kind='cust', size=13)

    # agents
    d.zone(330, 20, 620, 840, 'Agents', 'grey', 'Claude agents with tools')
    d.rect(350, 70, 580, 2, TEAL, TEAL)
    pos = {'identity': (360, 110), 'workplace': (650, 110), 'access': (360, 230), 'devices': (650, 230),
           'fix': (360, 560), 'defender': (650, 560), 'watcher': (505, 700)}
    for k, (x, y) in pos.items():
        d.el.append(f'<line x1="640" y1="{416}" x2="{x + 135}" y2="{y + 28}" stroke="{TEAL}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    for k, (x, y) in pos.items():
        agent_badge(d, k, x, y, 270)
    agent_badge(d, 'front', 490, 370, 300, 'Loads the context, understands, routes')
    d.lines(360, 790, 'The watcher works without anyone asking: it reads telemetry and opens cases itself.', 560, 13, 400, SECOND)

    # systems as tools
    d.zone(980, 20, 220, 840, 'Systems as tools', 'grey', 'Mock versions in the demo')
    systems = [('now', 'ServiceNow', 'Tickets, catalogue, CMDB'), ('nexthink', 'Nexthink', 'Telemetry, remote fixes'), ('azure', 'Azure AD', 'Identity, passwords'),
               ('workday', 'Workday', 'Profiles, approvals'), ('office', 'Office 365', 'Mail, calendar, rooms'), ('ariba', 'SAP Ariba', 'Hardware orders'),
               ('holmes', 'Script library', 'Approved fixes')]
    y = 72
    for lg, name, sub in systems:
        d.rect(996, y, 188, 90, '#fff', '#dce4e7', rx=10)
        if lg == 'holmes':
            d.wordmark('holmes', 1006, y + 10, 80, 26)
        else:
            d.logo(lg, 1006, y + 10, 34)
        d.t(1050 if lg != 'holmes' else 1090, y + 32, name, 14, 600)
        d.lines(1006, y + 64, sub, 170, 12, 400, SECOND)
        y += 104
    d.arrow((950, 430), (980, 430), color=TEAL)
    d.arrow((980, 460), (950, 460), color=TEAL)

    # people
    d.zone(1230, 20, 250, 840, 'People', 'agent', 'About 10% of cases')
    y = 76
    for avatar, title, sub in [('agent1', 'Live agent', 'Takes over with the full handoff card'), ('agent2', 'Experts', 'Join the same case, no escalation'),
                               ('agent3', 'Approvers', 'Managers and owners decide in Teams'), ('agent4', 'Security team', 'Lost laptops with client data, scams'),
                               (None, 'Engineers', 'Approve the scripts the fix agent drafts')]:
        d.rect(1246, y, 218, 120, '#fff', Z['agent'][1], rx=10)
        if avatar:
            d.image(avatar, 1258, y + 14, 50, round_=True, ring=Z['agent'][1])
        else:
            d.image('tools', 1262, y + 18, 42)
        d.t(1320, y + 38, title, 15, 600)
        d.lines(1260, y + 86, sub, 194, 12, 400, SECOND)
        y += 138
    d.arrow((950, 836), (1230, 836), color=Z['agent'][1], label='Handoff to a person', at=(1000, 828))
    return d


# C. Scenarios ------------------------------------------------------------------------------
# title, our agent, systems, enterprise agents, solved without the help desk, when live support joins
SCEN = [
    ('Meeting room', 'workplace', [('office', 'Office 365'), ('now', 'ServiceNow')], [], 'Rebooks an identical room, files a facilities request', 'The room needs a repair visit'),
    ('VPN offsite', 'fix', [('nexthink', 'Nexthink'), (None, 'Intune')], [], 'Finds the cause, fixes the client or guides the employee', 'The problem is on the network side'),
    ('Password reset', 'identity', [('azure', 'Entra ID')], [], 'Resets after a code or an approval in the authenticator', 'The sign-in looks like an attack'),
    ('Teams channel access', 'access', [('azure', 'Entra ID'), ('office', 'Office 365')], [], 'Asks the channel owner in Teams, adds the employee', None),
    ('Lost laptop', 'devices', [(None, 'Intune'), ('now', 'ServiceNow'), ('ariba', 'SAP Ariba')], [], 'Locks and wipes, new password, forms, replacement', 'Client data was on it: the security team joins'),
    ('Client files in SharePoint', 'access', [('azure', 'Entra ID'), ('nexthink', 'Nexthink')], [], 'Checks the engagement, asks the owner, fixes app errors', 'The app itself is down'),
    ('Outlook access for an assistant', 'access', [('office', 'Office 365')], [], 'Sets the delegation once the mailbox owner confirms', None),
    ('Ordering a peripheral', 'devices', [('ariba', 'SAP Ariba'), ('workday', 'Workday')], [], 'Compatible, in stock, locker; bundles approve automatically', None),
    ('Email scam', 'identity', [('office', 'Office 365'), ('azure', 'Entra ID')], ['Microsoft Defender'], 'Defender removes it for everyone; the identity agent resets the password if it was entered', 'A real attack: the security team joins'),
    ('Failed software install', 'fix', [('nexthink', 'Nexthink'), (None, 'Intune')], [], 'Finds the cause, fixes, installs again, drafts a new fix', 'Two fixes failed, or the employee is frustrated'),
]

# How each scenario starts: the input channel and what the employee does there
START = [
    (['teams'], 'Writes in Teams: the room screen is not working'),
    (['teams'], 'Writes in Teams: the VPN does not connect'),
    (['iphone'], 'Locked out: opens the Digital Hub website on his phone'),
    (['teams'], 'Writes in Teams: needs access to a channel'),
    (['iphone', 'teams'], 'Writes in Teams on his phone: the laptop is gone'),
    (['teams'], 'Writes in Teams: cannot open the client folder in SharePoint'),
    (['teams'], 'Writes in Teams: the new assistant needs his Outlook'),
    (['teams'], 'Writes in Teams: needs a second monitor'),
    (['outlook'], 'Taps Report in Outlook'),
    (['teams'], 'Writes in Teams: needs Visio for a client call'),
]


def scenario_card(i, title, agent, systems, enterprise, done, person):
    d = Rich(f'sc{i}', 560, 330, f'Scenario: {title}')
    d.rect(1, 1, 558, 328, '#fff', '#dce4e7', rx=12)
    d.t(20, 34, f'{i + 1}. {title}', 17, 600)
    # chain: employee, intake agent, our agent
    d.image('cust1', 20, 56, 44, round_=True, ring='#b7c1c5')
    d.arrow((66, 78), (82, 78), color=G)
    d.rect(84, 58, 128, 40, TINT, TEAL, rx=20, sw=1.5)
    d.image('chat', 94, 67, 22)
    d.t(122, 83, 'Intake agent', 13, 600)
    d.arrow((214, 78), (230, 78), color=TEAL)
    agent_badge(d, agent, 232, 50, 210)
    # input channel
    logos, text = START[i]
    d.t(20, 128, 'Starts', 12, 600, fill=SECOND)
    x = 60
    for lg in logos:
        d.logo(lg, x, 113, 20)
        x += 24
    d.t(x + 4, 128, text, 13, 600)
    # systems and enterprise agents
    x = 20
    y = 158
    d.t(x, y, 'Uses', 12, 600, fill=SECOND)
    x = 60
    for lg, name in systems:
        if lg:
            d.logo(lg, x, y - 15, 20)
        else:
            d.el.append(f'<circle cx="{x + 10}" cy="{y - 5}" r="10" fill="#eceff0"/>')
            d.t(x + 10, y, name[0], 10, 700, 'middle')
        d.t(x + 26, y, name, 12, 600, fill=SECOND)
        x += 26 + len(name) * 7 + 16
    for name in enterprise:
        w = len(name) * 7 + 138
        d.rect(x - 4, y - 17, w, 24, '#fff', '#9aa5aa', rx=12)
        d.image('alert', x + 4, y - 13, 16)
        d.t(x + 26, y, name + ' (enterprise agent)', 12, 600, fill=SECOND)
        x += w + 8
    # solved
    d.mark('ok', 20, 182, 26)
    d.lines(56, 200, done, 480, 14, 600, fill=OK)
    # live support
    d.el.append(f'<line x1="20" y1="254" x2="540" y2="254" stroke="#e4e8ea"/>')
    if person:
        d.rect(20, 266, 520, 48, Z['agent'][0], Z['agent'][1], dashed=True, rx=10)
        d.image('agent1', 30, 272, 36, round_=True, ring=Z['agent'][1])
        d.t(76, 286, 'Live support', 13, 600)
        d.t(76, 304, person, 13, 400, fill=SECOND)
    else:
        d.rect(20, 266, 520, 48, TINT, TINT, rx=10)
        d.t(280, 295, 'No live support needed: the help desk never sees this case', 13, 600, 'middle', fill=TEAL)
    return d


# D. Handoff, guardrails, metrics ----------------------------------------------------------------
def handoff():
    d = Rich('ho', 1120, 450, 'Handoff card, confirmation before risky actions, and the target split')
    # handoff card
    d.t(20, 30, 'What the live agent sees', 17, 600)
    d.rect(20, 46, 460, 360, '#fff', Z['agent'][1], rx=14, sw=2)
    d.image('cust7', 40, 66, 56, round_=True, ring='#b7c1c5')
    d.t(110, 88, 'Peter, senior auditor, Manchester', 15, 600)
    d.t(110, 108, 'Visio install failed twice · frustrated', 13, 400, SECOND)
    y = 140
    for lg, t in [('nexthink', 'Device: the disk is almost full'), ('nexthink', 'Tried: disk clean-up and a reinstall, through Nexthink and Intune'),
                  ('chat', 'From the chat: in a hurry, client call in 20 minutes'), ('now', 'Ticket open with all of the above')]:
        if lg == 'holmes':
            d.wordmark('holmes', 40, y - 4, 60, 22)
        else:
            d.logo(lg, 40, y - 6, 30)
        d.lines(110, y + 14, t, 350, 14)
        y += 50
    d.rect(40, 350, 420, 40, TINT, TINT, rx=8)
    d.t(250, 376, 'The agent does not ask anything again', 14, 600, 'middle', fill=TEAL)
    # guardrail
    d.t(520, 30, 'Asks first', 17, 600)
    d.rect(520, 46, 280, 230, '#fff', '#dce4e7', rx=14)
    d.image('iphone', 540, 66, 60)
    d.lines(610, 86, 'Laptop stolen: confirm it is you', 170, 15, 600)
    d.lines(610, 130, 'Approve the request in Authenticator. Then the laptop is locked and wiped.', 170, 13, 400, SECOND)
    d.rect(540, 216, 140, 40, TEAL, TEAL, rx=8)
    d.t(610, 241, 'I approved it', 14, 600, 'middle', fill='#fff')
    d.lines(520, 306, 'A lost laptop is wiped as soon as the employee confirms it is them. Giving access to client data or spending beyond the policy always waits for a person to approve.', 280, 13, 400, SECOND)
    # metric
    d.t(840, 30, 'Target', 17, 600)
    d.rect(840, 46, 260, 384, '#fff', '#dce4e7', rx=14)
    d.el.append(f'<rect x="870" y="80" width="60" height="290" rx="8" fill="{TEAL}"/>')
    d.el.append(f'<rect x="870" y="80" width="60" height="29" rx="8" fill="{Z["agent"][1]}"/>')
    d.t(950, 100, '10%', 24, 600, fill=Z['agent'][1])
    d.t(950, 122, 'people', 13, 400, SECOND)
    d.t(950, 250, '90%', 36, 600, fill=TEAL)
    d.lines(950, 276, 'solved without the help desk', 130, 13, 400, SECOND)
    d.lines(860, 396, 'Counted only if the case does not come back', 230, 12, 400, SECOND)
    return d


def page():
    sc = ''.join(f'<div>{scenario_card(i, *s).svg()}</div>' for i, s in enumerate(SCEN))
    css = (pathlib.Path(__file__).parent / 'page.css').read_text() + '''
.pano{overflow-x:auto}.pano .case-diagram{width:auto;max-width:none;height:auto}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}.grid .case-diagram{width:100%;height:auto}
@media (max-width:900px){.grid{grid-template-columns:1fr}}
.lede{max-width:70ch;font-size:18px;margin:0 0 32px}'''
    figs = [
        ('what-changes', 'What changes', 'The same service, the same journeys and the same data. Agents take the work that had to be written in advance.', what_changes().svg(), False),
        ('architecture', 'Architecture', 'Every channel reaches one team of agents; the systems from 2019 become their tools; people get the cases that need judgment.', architecture().svg(), True),
    ]
    body = ''.join(f'<figure class="figure-panel" id="{i}"><figcaption class="figure-caption"><div><div class="figure-title">{escape(t)}</div><span>{escape(s)}</span></div></figcaption>'
                   f'<div class="{"pano" if p else ""}">{svg}</div></figure>' for i, t, s, svg, p in figs)
    body += ('<figure class="figure-panel" id="scenarios"><figcaption class="figure-caption"><div><div class="figure-title">The 10 scenarios</div>'
             '<span>From the 2019 slide. Who does the work now, and when a person steps in.</span></div></figcaption>'
             f'<div class="grid">{sc}</div></figure>')
    body += ('<figure class="figure-panel" id="handoff"><figcaption class="figure-caption"><div><div class="figure-title">Handoff, confirmation and the target</div>'
             '<span>A person gets the whole story, risky actions wait for a yes, and success counts only when the case stays solved.</span></div></figcaption>'
             f'{handoff().svg()}</figure>')
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Digital Hub 2019 to 2026 · Sandy Tayts</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600&amp;family=Inter:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet"/>
<style>{css}</style></head><body><main style="max-width:1600px">
<h1>Digital Hub: from 2019 to 2026</h1>
<p class="sub">The 2019 service diagrams are the brief. In 2026 agents do the work.</p>
{body}</main></body></html>'''
    out = pathlib.Path(__file__).parent.parent / 'case' / 'transition.html'
    out.write_text(html)
    print('ok', len(html) // 1024, 'KB')


if __name__ == '__main__':
    page()

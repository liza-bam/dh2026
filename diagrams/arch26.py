"""D26-2. Architecture 2026: nine layers. Intake sorts every request into a fixed flow, a domain agent or a team ticket; team agents work for the second line."""
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


AGENTS = [
    ('Security agent', 'lock', 'Stolen devices, scams, locked accounts', 'Wipes only once the employee is verified', 'Small model', [('azure', 'Entra ID'), (None, 'Intune')]),
    ('Devices agent', 'hardware', 'Orders and replaces devices, hardware faults', 'Never wipes a device', 'Small model', [('ariba', 'SAP Ariba'), (None, 'Intune')]),
    ('Software agent', 'tools', 'Installs and repairs apps, VPN, tries fixes', 'Never runs a new fix before an engineer approves', 'Small model', [('nexthink', 'Nexthink'), (None, 'Intune')]),
    ('Mail, calendar and Teams', 'outlook', 'Delegation, mailboxes, channels', 'Never reads the content of mail', 'Small model', [('office', 'Office 365'), ('azure', 'Entra ID')]),
    ('Workplace agent', 'room', 'Rooms, desks, facilities requests', 'Never sees meeting content', 'Small model', [('office', 'Office 365'), ('now', 'ServiceNow')]),
    ('Watcher agent', 'software', 'Reads telemetry, opens cases before people notice', 'Never changes a device', 'Small model', [('nexthink', 'Nexthink'), ('now', 'ServiceNow')]),
]


def build():
    d = Rich('a26', 1500, 1440, 'Digital Hub 2026 architecture in nine layers: channels; an intake agent that sends every request to a fixed flow, a domain agent or a team; '
             'domain agents with limited access; team agents for the second line; enterprise agents; knowledge; systems through MCP; governance; people')
    S = 150  # the team agents band pushes the lower layers down

    # 1 channels ---------------------------------------------------------------------------
    band(d, 20, 120, 1, 'Channels', 'The employee asks anywhere; it is one conversation')
    for i in range(4):
        d.image(f'cust{i + 1}', 70 + i * 50, 62, 44, round_=True, ring='#b7c1c5')
    x = 300
    for icon, name in [('teams', 'Teams'), (None, 'Digital Hub website'), ('email', 'Email'), ('voice', 'Voice')]:
        d.rect(x, 62, 190, 56, '#fff', '#dce4e7', rx=10)
        if icon:
            d.image(icon, x + 12, 74, 32)
        else:
            d.rect(x + 12, 78, 32, 24, '#f5c000', '#f5c000', rx=6)
        d.t(x + 56, 96, name, 14, 600)
        x += 208

    # 2 intake agent and the three paths -------------------------------------------------------
    band(d, 160, 130, 2, 'Intake agent', 'One way in. Sorts every request; changes nothing in a system itself', TINT, TEAL)
    d.rect(40, 202, 400, 80, '#fff', TEAL, rx=12, sw=1.5)
    d.t(54, 226, 'Intake agent', 15, 600)
    cx = 440 - 14 - sum(len(t) * 12 * 0.58 + 24 for t in ('Small model', 'Read only')) + 6
    for t in ('Small model', 'Read only'):
        cx = chip(d, cx, 210, t, '#fff', TEAL, TEAL)
    d.lines(54, 250, 'Understands the request in the employee’s own words and loads the context.', 372, 13, 400, SECOND, lh=17)
    for k, (t, sub) in enumerate([('Fixed flow', 'A simple action: no decisions'), ('Domain agent', 'A problem: decisions needed'), ('Team ticket', 'Nothing fits: a team and its agent')]):
        x = 474 + k * 224
        d.rect(x, 202, 210, 80, '#fff', TEAL, rx=12, sw=1.5)
        d.t(x + 14, 230, t, 15, 600)
        d.lines(x + 14, 254, sub, 186, 13, 400, SECOND, lh=17)
    d.arrow((440, 242), (474, 242), color=TEAL)

    # 3 specialized agents ----------------------------------------------------------------------
    band(d, 310, 300, 3, 'Domain agents', 'Simple actions run as fixed flows; problems the agent solves within its limits', TINT, TEAL)
    for i, (name, icon, can, cannot, model, tools) in enumerate(AGENTS):
        x = 40 + (i % 3) * 368
        y = 356 + (i // 3) * 124
        d.rect(x, y, 352, 112, '#fff', TEAL, rx=12, sw=1.5)
        d.el.append(f'<circle cx="{x + 26}" cy="{y + 26}" r="16" fill="{TINT}"/>')
        d.image(icon, x + 15, y + 15, 22)
        d.t(x + 52, y + 31, name, 15, 600)
        chip(d, x + 352 - (len(model) * 12 * 0.58 + 18) - 10, y + 12, model, TEAL if model == 'Large model' else '#fff', TEAL, '#fff' if model == 'Large model' else TEAL, 11)
        d.mark('ok', x + 14, y + 48, 18)
        d.t(x + 40, y + 62, can, 13, 400)
        d.el.append(f'<circle cx="{x + 23}" cy="{y + 79}" r="8" fill="none" stroke="#bb3446" stroke-width="1.6"/><line x1="{x + 17}" y1="{y + 85}" x2="{x + 29}" y2="{y + 73}" stroke="#bb3446" stroke-width="1.6"/>')
        d.t(x + 40, y + 84, cannot, 13, 400, fill=SECOND)
        tx = x + 40
        for k, n in tools:
            if k:
                d.logo(k, tx, y + 92, 16)
                tx += 20
            d.t(tx, y + 105, n, 11, 600, fill=SECOND)
            tx += len(n) * 6.4 + 14

    # 4 team agents ------------------------------------------------------------------------------
    band(d, 630, 130, 4, 'Team agents', 'The second line: one agent for each team, working for its engineers', TINT, TEAL)
    d.rect(40, 672, 1090, 78, '#fff', TEAL, rx=12, sw=1.5)
    d.lines(54, 696, 'Reads the ticket and the history, suggests what to do from the team’s experience and prepares the actions. An engineer decides. '
            'What the team solves goes back to the first line as knowledge or a new fix.', 700, 13, 400, SECOND, lh=17)
    chip(d, 1130 - 14 - (len('Large model') * 12 * 0.58 + 18), 680, 'Large model', TEAL, TEAL, '#fff')
    cx = 780
    for t in ('Network', 'Messaging', 'End-user computing'):
        cx = chip(d, cx, 716, t, '#fff', '#c9d1d4', None, 11)

    # 4 enterprise agents ------------------------------------------------------------------------
    band(d, 630 + S, 140, 5, 'Enterprise agents', 'Run inside their own platforms, with their own data and audit; connected through A2A')
    ents = [(None, 'Microsoft Defender', 'Phishing triage: decides whether a reported email is a threat'),
            ('now', 'ServiceNow', 'Ticket workflows, approvals, service levels'),
            ('genesys', 'Genesys', 'Routes a case to the right live agent with the whole story')]
    for i, (k, n, s) in enumerate(ents):
        x = 40 + i * 368
        d.rect(x, 676 + S, 352, 80, '#fff', '#c9d1d4', rx=12)
        if k == 'genesys':
            d.wordmark('genesys', x + 12, 682 + S, 130, 36)
        elif k:
            d.logo(k, x + 12, 684 + S, 30)
            d.t(x + 52, 704 + S, n, 14, 600)
        else:
            system(d, x + 12, 685 + S, None, n)
        d.lines(x + 12, 734 + S, s, 330, 13, 400, SECOND)

    # 5 knowledge -----------------------------------------------------------------------------
    band(d, 790 + S, 120, 6, 'Knowledge', 'A library for each domain and each team; answers only from approved EY sources')
    x = 70
    for k, n in [('now', 'ServiceNow Knowledge'), ('sharepoint', 'Policies in SharePoint'), (None, 'How-to videos'), (None, 'Client data rules')]:
        d.rect(x, 836 + S, 252, 52, '#fff', '#dce4e7', rx=10)
        system(d, x + 12, 848 + S, k, n)
        x += 268
    d.t(70, 902 + S, 'Each agent searches only its own library.', 12, 400, fill=SECOND)

    # 6 systems -------------------------------------------------------------------------------
    band(d, 930 + S, 150, 7, 'Systems', 'Reached through their MCP servers, within the rights of the agent and the employee')
    sysl = [('now', 'ServiceNow'), ('workday', 'Workday'), ('azure', 'Entra ID'), (None, 'Intune'), ('nexthink', 'Nexthink'),
            ('office', 'Office 365'), ('ariba', 'SAP Ariba'), ('genesys', 'Genesys')]
    for i, (k, n) in enumerate(sysl):
        x = 70 + (i % 4) * 268
        y = 976 + S + (i // 4) * 50
        d.rect(x, y, 252, 42, '#fff', '#dce4e7', rx=10)
        if k == 'genesys':
            d.wordmark('genesys', x + 12, y + 4, 110, 34)
        else:
            system(d, x + 12, y + 7, k, n)

    # arrows between layers
    for y1, y2 in [(140, 160), (290, 310), (610, 630), (760, 780), (770 + S, 790 + S), (910 + S, 930 + S)]:
        d.arrow((585, y1), (585, y2), color=TEAL)

    # 7 governance ------------------------------------------------------------------------------
    d.rect(1170, 20, 310, 640, '#fff', '#223640', rx=14, sw=1.5)
    d.el.append(f'<circle cx="1196" cy="50" r="14" fill="{TEAL}"/>')
    d.t(1196, 55, '8', 13, 700, 'middle', fill='#fff')
    d.t(1220, 56, 'Governance', 17, 600)
    gov = [('Agent identities', 'Every agent has its own account in Entra ID, like a new employee'),
           ('Agent registry', 'One list of all agents, their owners and their rights'),
           ('Audit', 'Every action of every agent is logged'),
           ('Checks before release', 'Each agent is tested on real scenarios before it goes live'),
           ('Spend limits', 'Each agent has a budget; cost is measured per solved case'),
           ('Independence, one action at a time', 'An agent first proposes, then acts alone; each action moves up after it works on real cases'),
           ('Models in EY’s cloud', 'Client data never leaves EY')]
    y = 80
    for t, s in gov:
        d.t(1190, y + 18, t, 14, 600)
        y = d.lines(1190, y + 38, s, 270, 13, 400, SECOND) + 14
    # 8 people ---------------------------------------------------------------------------------
    P = 80
    d.rect(1170, 600 + P, 310, 550, Z['agent'][0], Z['agent'][1], dashed=True, rx=14)
    d.el.append(f'<circle cx="1196" cy="{630 + P}" r="14" fill="{TEAL}"/>')
    d.t(1196, 635 + P, '9', 13, 700, 'middle', fill='#fff')
    d.t(1220, 636 + P, 'People', 17, 600)
    d.t(1220, 656 + P, 'At every level', 12, 400, fill=SECOND)
    y = 690 + P
    for av, t, s in [('agent1', 'Live agent and experts', 'Take over with the whole story; no escalation'),
                     ('agent2', 'Approvers', 'Managers and owners decide in Teams'),
                     ('agent3', 'Security team', 'Client data at risk, real phishing'),
                     ('agent4', 'Engineers', 'Second line, with their team agent; approve every new fix')]:
        d.image(av, 1186, y, 44, round_=True, ring=Z['agent'][1])
        d.t(1242, y + 18, t, 14, 600)
        d.lines(1242, y + 38, s, 220, 12, 400, SECOND)
        y += 110
    d.arrow((1150, 470), (1170, 470), color=G)
    d.arrow((1150, 715), (1170, 715), color=Z['agent'][1])
    d.H = 1250
    return d

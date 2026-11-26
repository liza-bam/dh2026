"""D26-2. Architecture 2026: eight layers, scoped agents, enterprise agents, knowledge, systems, governance, people."""
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
    ('Identity agent', 'lock', 'Resets passwords, unlocks accounts', 'Never reads mail or files', 'Small model', [('azure', 'Entra ID')]),
    ('Workplace agent', 'room', 'Rebooks rooms, files facilities requests', 'Never sees meeting content', 'Small model', [('office', 'Office 365')]),
    ('Access agent', 'approve', 'Asks owners, grants access once they say yes', 'Never approves its own request', 'Large model', [('azure', 'Entra ID'), ('workday', 'Workday')]),
    ('Devices agent', 'hardware', 'Locks, orders, starts the data transfer', 'Wipes only after the employee confirms', 'Small model', [(None, 'Intune'), ('ariba', 'SAP Ariba')]),
    ('Fix agent', 'tools', 'Runs approved fixes, drafts new ones', 'A new fix waits for an engineer', 'Large model', [('nexthink', 'Nexthink'), (None, 'Intune')]),
    ('Watcher agent', 'software', 'Reads telemetry, opens cases itself', 'Never changes a device', 'Small model', [('nexthink', 'Nexthink'), ('now', 'ServiceNow')]),
]


def build():
    d = Rich('a26', 1500, 1290, 'Digital Hub 2026 architecture in eight layers: channels, front door agent, specialized agents with limited access, '
             'enterprise agents, knowledge, systems through MCP, governance, people')

    # 1 channels ---------------------------------------------------------------------------
    band(d, 20, 120, 1, 'Channels', 'The employee asks anywhere; it is one conversation')
    for i in range(4):
        d.image(f'cust{i + 1}', 70 + i * 50, 62, 44, round_=True, ring='#b7c1c5')
    x = 300
    for icon, name in [('teams', 'Teams'), (None, 'Digital Hub app'), ('email', 'Email'), ('voice', 'Voice')]:
        d.rect(x, 62, 190, 56, '#fff', '#dce4e7', rx=10)
        if icon:
            d.image(icon, x + 12, 74, 32)
        else:
            d.rect(x + 12, 78, 32, 24, '#f5c000', '#f5c000', rx=6)
        d.t(x + 56, 96, name, 14, 600)
        x += 208

    # 2 front door ---------------------------------------------------------------------------
    band(d, 160, 130, 2, 'Front door agent', 'Reads only. Changes nothing in any system', TINT, TEAL)
    d.el.append(f'<circle cx="94" cy="236" r="22" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
    d.image('chat', 80, 222, 28)
    d.lines(132, 228, 'Loads the employee’s context, understands the request, picks the agent, keeps the conversation and tells the employee what is happening.', 560, 14)
    cx = 720
    for t, f, c in [('Large model', TEAL, '#fff'), ('Read only', '#fff', TEAL), ('Own agent identity', '#fff', TEAL)]:
        cx = chip(d, cx, 214, t, f, TEAL, c)
    for k, n in [('workday', 'Profile'), ('office', 'Calendar'), ('nexthink', 'Device'), ('now', 'Tickets')]:
        pass
    d.lines(720, 262, 'Context: profile (Workday), calendar (Office 365), device (Nexthink), tickets (ServiceNow)', 410, 12, 400, SECOND)

    # 3 specialized agents ----------------------------------------------------------------------
    band(d, 310, 300, 3, 'Specialized agents', 'Each has its own identity and only the rights its role needs', TINT, TEAL)
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

    # 4 enterprise agents ------------------------------------------------------------------------
    band(d, 630, 140, 4, 'Enterprise agents', 'Run inside their own platforms, with their own data and audit; connected through A2A')
    ents = [(None, 'Microsoft Defender', 'Phishing triage: decides whether a reported email is a threat'),
            ('now', 'ServiceNow', 'Ticket workflows, approvals, service levels'),
            ('genesys', 'Genesys', 'Routes a case to the right live agent with the whole story')]
    for i, (k, n, s) in enumerate(ents):
        x = 40 + i * 368
        d.rect(x, 676, 352, 80, '#fff', '#c9d1d4', rx=12)
        if k == 'genesys':
            d.wordmark('genesys', x + 12, 682, 130, 36)
        elif k:
            d.logo(k, x + 12, 684, 30)
            d.t(x + 52, 704, n, 14, 600)
        else:
            system(d, x + 12, 685, None, n)
        d.lines(x + 12, 734, s, 330, 13, 400, SECOND)

    # 5 knowledge -----------------------------------------------------------------------------
    band(d, 790, 120, 5, 'Knowledge', 'Agents answer only from approved EY sources, with a link to the source')
    x = 70
    for k, n in [('now', 'ServiceNow Knowledge'), ('sharepoint', 'Policies in SharePoint'), (None, 'How-to videos'), (None, 'Client data rules')]:
        d.rect(x, 836, 252, 52, '#fff', '#dce4e7', rx=10)
        system(d, x + 12, 848, k, n)
        x += 268
    d.t(70, 902, 'Each agent searches only its own topics.', 12, 400, fill=SECOND)

    # 6 systems -------------------------------------------------------------------------------
    band(d, 930, 150, 6, 'Systems', 'Reached through their MCP servers, within the rights of the agent and the employee')
    sysl = [('now', 'ServiceNow'), ('workday', 'Workday'), ('azure', 'Entra ID'), (None, 'Intune'), ('nexthink', 'Nexthink'),
            ('office', 'Office 365'), ('ariba', 'SAP Ariba'), ('genesys', 'Genesys')]
    for i, (k, n) in enumerate(sysl):
        x = 70 + (i % 4) * 268
        y = 976 + (i // 4) * 50
        d.rect(x, y, 252, 42, '#fff', '#dce4e7', rx=10)
        if k == 'genesys':
            d.wordmark('genesys', x + 12, y + 4, 110, 34)
        else:
            system(d, x + 12, y + 7, k, n)

    # arrows between layers
    for y1, y2 in [(140, 160), (290, 310), (610, 630), (770, 790), (910, 930)]:
        d.arrow((585, y1), (585, y2), color=TEAL)

    # 7 governance ------------------------------------------------------------------------------
    d.rect(1170, 20, 310, 560, '#fff', '#223640', rx=14, sw=1.5)
    d.el.append(f'<circle cx="1196" cy="50" r="14" fill="{TEAL}"/>')
    d.t(1196, 55, '7', 13, 700, 'middle', fill='#fff')
    d.t(1220, 56, 'Governance', 17, 600)
    gov = [('Agent identities', 'Every agent has its own account in Entra ID, like a new employee'),
           ('Agent registry', 'One list of all agents, their owners and their rights'),
           ('Audit', 'Every action of every agent is logged'),
           ('Checks before release', 'Each agent is tested on real scenarios before it goes live'),
           ('Spend limits', 'Each agent has a budget; cost is measured per solved case'),
           ('Models in EY’s cloud', 'Client data never leaves EY')]
    y = 80
    for t, s in gov:
        d.t(1190, y + 18, t, 14, 600)
        y = d.lines(1190, y + 38, s, 270, 13, 400, SECOND) + 14
    # 8 people ---------------------------------------------------------------------------------
    d.rect(1170, 600, 310, 480, Z['agent'][0], Z['agent'][1], dashed=True, rx=14)
    d.el.append(f'<circle cx="1196" cy="630" r="14" fill="{TEAL}"/>')
    d.t(1196, 635, '8', 13, 700, 'middle', fill='#fff')
    d.t(1220, 636, 'People', 17, 600)
    d.t(1220, 656, 'About 10% of cases', 13, 400, fill=SECOND)
    y = 680
    for av, t, s in [('agent1', 'Live agent and experts', 'Take over with the whole story; no escalation'),
                     ('agent2', 'Approvers', 'Managers and owners decide in Teams'),
                     ('agent3', 'Security team', 'Client data at risk, real phishing'),
                     ('agent4', 'Engineers', 'Approve every new fix before it joins the library')]:
        d.image(av, 1186, y, 44, round_=True, ring=Z['agent'][1])
        d.t(1242, y + 18, t, 14, 600)
        d.lines(1242, y + 38, s, 220, 12, 400, SECOND)
        y += 96
    d.arrow((1150, 470), (1170, 470), color=G)
    d.arrow((1150, 700), (1170, 700), color=Z['agent'][1])
    d.t(1100, 1120 + 40, '', 12)
    d.H = 1100
    return d

"""D26-6 Stack scorecard: each 2019 platform against the six questions of rule 3. Checked against vendor documentation, November 2026."""
from rich import Rich, Z
from svg import SECOND, wrap
from transition import TEAL, TINT

LIVE = Z['agent'][1]
Q = ['Agents can act through it', 'Agent identity, within the employee’s rights', 'Data no one else has',
     'Extra cost for agents', 'Every agent action on record', 'Change the model or vendor']
# name, logo key (None: letter), marks for questions 1, 2, 3, 5, 6 (y yes, p partly, n no or not found), cost text, verdict
ROWS = [
    ('ServiceNow', 'now', 'ypyyy', 'In Now Assist plans', 'Keep: tickets, approvals, catalogue through its MCP server'),
    ('Workday', 'workday', 'yyyyy', 'Licence', 'Keep: people and approvals; agents inherit its policies'),
    ('Entra ID', 'azure', 'pyyyy', 'Agent 365 or E7', 'Keep: every agent gets its own identity here'),
    ('Intune', None, 'ppyyy', 'Existing licence', 'Keep: device actions through Microsoft Graph'),
    ('Nexthink', 'nexthink', 'ynyny', 'Licence', 'Keep: device telemetry no one else has'),
    ('Microsoft Defender', None, 'yyyyn', 'Security Compute Units', 'Use its phishing triage agent; do not rebuild it'),
    ('Genesys', 'genesys', 'ypyyy', 'Licence', 'Keep: live support, talks to ServiceNow agent to agent'),
    ('SAP Ariba', 'ariba', 'ppynp', 'Joule Base', 'Keep through its APIs; check again for MCP'),
    ('Avaamo', 'avaamo', 'nnnnn', 'Expensive in 2019', 'Drop: the intake agent does its job'),
    ('AI scripts (2019)', None, 'pnnnn', 'Services contract', 'Drop: fixes run through Nexthink and Intune'),
]


def mark(d, cx, cy, m):
    if m == 'y':
        d.el.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{TEAL}"/>')
    elif m == 'p':
        d.el.append(f'<circle cx="{cx}" cy="{cy}" r="8.5" fill="#fff" stroke="{TEAL}" stroke-width="1.6"/>'
                    f'<path d="M{cx} {cy - 8.5} A8.5 8.5 0 0 1 {cx} {cy + 8.5} Z" fill="{TEAL}"/>')
    else:
        d.el.append(f'<circle cx="{cx}" cy="{cy}" r="8.5" fill="#fff" stroke="#9aa5aa" stroke-width="1.6"/>')


def build():
    d = Rich('sc26', 1120, 800, 'Stack scorecard: each platform from 2019 checked against six questions, with a verdict')
    x0, wn, wq, wv = 20, 200, 96, 324
    xs = [x0 + wn + i * wq for i in range(6)]
    xv = x0 + wn + 6 * wq
    # header
    for i, q in enumerate(Q):
        for j, ln in enumerate(wrap(q, wq - 12, 12)):
            d.t(xs[i] + wq / 2, 30 + j * 15, ln, 12, 600, 'middle', fill=SECOND)
    d.t(xv + 12, 30, 'Verdict', 12, 600, fill=SECOND)
    y = 104
    for n, (name, logo, marks, cost, verdict) in enumerate(ROWS):
        drop = verdict.startswith('Drop')
        if n == 8:
            y += 16
        d.rect(x0, y, 1080, 54, '#fff' if not drop else '#fbf3ee', '#dce4e7', rx=10)
        if logo == 'genesys':
            d.wordmark('genesys', x0 + 12, y + 11, 110, 32)
        else:
            if logo:
                d.logo(logo, x0 + 12, y + 13, 28)
            else:
                d.el.append(f'<circle cx="{x0 + 26}" cy="{y + 27}" r="14" fill="#eceff0"/>')
                d.t(x0 + 26, y + 32, name[0], 13, 700, 'middle')
            d.t(x0 + 50, y + 32, name, 14, 600)
        k = 0
        for i in range(6):
            cx = xs[i] + wq / 2
            if i == 3:
                cl = wrap(cost, wq - 10, 11)
                for j, ln in enumerate(cl):
                    d.t(cx, y + 31 - (len(cl) - 1) * 7 + j * 14, ln, 11, 400, 'middle', fill=SECOND)
            else:
                mark(d, cx, y + 27, marks[k])
                k += 1
        vl = wrap(verdict, wv - 24, 13)
        for j, ln in enumerate(vl):
            d.t(xv + 12, y + 32 - (len(vl) - 1) * 8 + j * 16, ln, 13, 600 if j == 0 else 400, fill=LIVE if drop else '#223640')
        y += 62
    # legend
    y += 14
    lx = x0
    for m, t in [('y', 'Yes'), ('p', 'Partly, or with conditions'), ('n', 'No, or not found in public documentation')]:
        mark(d, lx + 9, y, m)
        d.t(lx + 26, y + 5, t, 13, 400, fill=SECOND)
        lx += 60 + len(t) * 7
    d.t(x0, y + 34, 'Checked against vendor documentation, November 2026.', 12, 400, fill=SECOND)
    return d

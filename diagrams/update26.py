"""D19-12b / D26-17. The bad update as a blueprint in Sandy's 2019 style: people on top, systems below,
the data written on the arrows between them. Same seven steps in 2019 and 2026."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import symbol
import base64
from pathlib import Path

VEC = Path(__file__).parent / 'assets' / 'vector'


def vec(name):
    return 'data:image/svg+xml;base64,' + base64.b64encode((VEC / f'{name}.svg').read_bytes()).decode()


def mark(d, key, x, y, r):
    """A platform logo in a disc, drawn from vector files so it stays sharp."""
    if key == 'now':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#293e40"/>')
        d.el.append(f'<image href="{vec("servicenow")}" x="{x - r}" y="{y - r}" width="{2 * r}" height="{2 * r}"/>')
    elif key == 'nexthink':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#0044ac"/>')
        d.t(x, y + 5, 'nexthink', round(r * 0.4), 600, 'middle', fill='#fff')
    else:
        name = {'cloud': 'office', 'intune': 'intune'}[key]
        s = r * 1.15
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="#dce4e7" stroke-width="1.5"/>')
        d.el.append(f'<image href="{vec(name)}" x="{x - s / 2}" y="{y - s / 2}" width="{s}" height="{s}"/>')

W = 1340
X0, COL = 140, 160            # first column centre, column width
TOP, BOT = 96, 470            # top of the people band, top of the systems band
PY, R = 250, 44               # people circles
SY1, SYB, SY3, SR = 556, 690, 830, 34   # actors, the ServiceNow record, integrations
SY2 = SYB
H = 1000
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
        glyph(d, 'laptop_outline', x, PY, 50)
    elif kind == 'everyone':
        d.el.append(f'<circle cx="{x}" cy="{PY}" r="{R}" fill="{TINT}"/>')
        glyph(d, 'groups', x, PY, 50)
    else:
        d.el.append(f'<circle cx="{x}" cy="{PY}" r="{R}" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
        glyph(d, 'support_agent', x, PY, 50)
    d.t(x, PY + R + 22, {'peter': 'Peter', 'engineer': 'Engineer', 'everyone': 'Everyone else'}[kind], 15, 700, 'middle', fill=INK)
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
    if key == 'hub':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{SR}" fill="#f5c000"/>')
        glyph(d, 'hub', x, y, 40, '#fff')
    else:
        mark(d, key, x, y, SR)
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
    for dx, y1, y2 in [(-10, SY1 - SR - 6, PY + R + 32), (10, PY + R + 32, SY1 - SR - 6)]:
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
    d.t(108, y + 5, 'Words on an arrow: the data that moves', 15, 400, fill=SECOND)
    d.el.append(f'<path d="M420 {y}h34" stroke="{LINE}" stroke-width="1.8" marker-start="url(#m{d.uid})" marker-end="url(#m{d.uid})"/>')
    d.t(464, y + 5, 'Reads and writes the record', 15, 400, fill=SECOND)
    if agents:
        d.el.append(f'<circle cx="712" cy="{y}" r="13" fill="{TINT}" stroke="{TEAL}" stroke-width="1.5"/>')
        glyph(d, 'smart_toy', 712, y - 1, 16)
        d.t(734, y + 5, 'An agent: a system with its own account', 15, 400, fill=SECOND)
    d.t(W - 20, y + 5, label, 15, 700, 'end', fill=INK)


STEPS = [
    ('Crash', 'Visio won’t start after the update'),
    ('Ticket', 'A ticket opens, and Peter is told'),
    ('Workaround', 'Peter keeps working'),
    ('Cause', 'The engineer finds out why'),
    ('Hold', 'The update stops for everyone else'),
    ('Fix', 'The fix is written and approved'),
    ('Fixed', 'Peter hears back and rates it'),
    ('Everyone', 'Everyone else gets the fix and notices nothing'),
]


def base(uid, label, year):
    d = Rich(uid, W, H, label)
    frame(d, year, agents=year != '2019')
    for i, (t, s) in enumerate(STEPS):
        head(d, i, i + 1, t, s)
    return d


def record(d, i, caption, first=False):
    """The ServiceNow record: the one thread every step reads and writes."""
    x = cx(i)
    mark(d, 'now', x, SYB, 28)
    d.t(x, SYB + 48, caption, 15, 600, 'middle', fill=SECOND)
    if not first:
        d.el.append(f'<path d="M{cx(i - 1) + 32:.0f} {SYB}H{x - 34:.0f}" fill="none" stroke="{LINE}" stroke-width="1.8" marker-end="url(#m{d.uid})"/>')


def both(d, x, y1, y2):
    """A two-way line: the actor reads and writes the record."""
    d.el.append(f'<path d="M{x:.0f} {y1:.0f}V{y2:.0f}" fill="none" stroke="{LINE}" stroke-width="1.8" '
                f'marker-start="url(#m{d.uid})" marker-end="url(#m{d.uid})"/>')


def under(d, i, key, name, label, up=True, left=False):
    """An integration below the record, and what it gives or takes."""
    x = cx(i)
    system(d, x, SY3, key, name)
    a, b = (SY3 - SR - 6, SYB + 58) if up else (SYB + 58, SY3 - SR - 6)
    d.el.append(f'<path d="M{x:.0f} {a:.0f}V{b:.0f}" fill="none" stroke="{LINE}" stroke-width="1.8" marker-end="url(#m{d.uid})"/>')
    d.t(x - 8 if left else x + 8, (SYB + 58 + SY3 - SR) / 2 + 5, label, 14, 600, 'end' if left else 'start', fill=SECOND)


def everyone(d, i):
    """Step 8: the fix reaches everyone else; they see nothing, so no arrow."""
    person(d, i, 'everyone')
    d.t(cx(i), 400, 'Sees nothing:', 15, 600, 'middle', fill=SECOND)
    d.t(cx(i), 420, 'Visio just works', 15, 600, 'middle', fill=SECOND)


def build19():
    d = base('bu19', 'A bad Visio update in 2019: Peter is told at each step and everyone else gets the fix without noticing, the engineer searches for the cause and writes the fix, Digital Hub scripts do the rest; every step reads and writes the ServiceNow ticket', '2019')
    # 1 Peter's Visio crashes; Nexthink records it
    person(d, 0, 'peter', 'alert'); system(d, cx(0), SY1, 'nexthink', 'Nexthink')
    vline(d, cx(0), PY + R + 32, SY1 - SR - 6, 'Crash\nand version', 410)
    # 2 Digital Hub opens a ticket and tells Peter
    person(d, 1, 'peter', 'message'); system(d, cx(1), SY1, 'hub'); record(d, 1, 'Ticket', first=True)
    vline(d, cx(1), SY1 - SR - 6, PY + R + 32, 'We opened\na ticket', 410)
    hline(d, cx(0) + SR + 6, cx(1) - SR - 8, SY1)
    d.t((cx(0) + cx(1)) / 2, SY1 - 10, 'Crash', 15, 600, 'middle', fill=SECOND)
    both(d, cx(1), SY1 + SR + 6, SYB - 34)
    # 3 Digital Hub offers the workaround
    person(d, 2, 'peter', 'message'); system(d, cx(2), SY1, 'hub'); record(d, 2, 'Workaround')
    vline(d, cx(2), SY1 - SR - 6, PY + R + 32, 'Virtual\nmachine', 410)
    both(d, cx(2), SY1 + SR + 6, SYB - 34)
    # 4 the engineer searches Nexthink; the ticket shows three similar ones
    person(d, 3, 'engineer'); system(d, cx(3), SY1, 'nexthink'); record(d, 3, '3 similar tickets')
    pair(d, cx(3), 'The cause:\nthe update', 'She searches', ly=410, down_first=True)
    both(d, cx(3), SY1 + SR + 6, SYB - 34)
    # 5 Digital Hub holds the update and tells Peter
    person(d, 4, 'peter', 'message'); system(d, cx(4), SY1, 'hub'); record(d, 4, 'Update held')
    vline(d, cx(4), SY1 - SR - 6, PY + R + 32, 'Update held,\nfix underway', 410)
    both(d, cx(4), SY1 + SR + 6, SYB - 34)
    # 6 the engineer writes the steps; Digital Hub runs them
    person(d, 5, 'engineer'); system(d, cx(5), SY1, 'hub'); record(d, 5, 'Fix')
    vline(d, cx(5), PY + R + 32, SY1 - SR - 6, 'Steps she\nwrote', 410)
    both(d, cx(5), SY1 + SR + 6, SYB - 34)
    # 7 Peter hears back and rates it; the ticket closes
    person(d, 6, 'peter', 'done'); system(d, cx(6), SY1, 'hub'); record(d, 6, 'Ticket closed')
    pair(d, cx(6), '\u201cWe fixed it\u201d', 'Rating', ly=410)
    both(d, cx(6), SY1 + SR + 6, SYB - 34)
    # 8 Digital Hub runs the same steps for everyone else; nobody notices
    everyone(d, 7); system(d, cx(7), SY1, 'hub'); record(d, 7, 'All closed')
    both(d, cx(7), SY1 + SR + 6, SYB - 34)
    return d


def build26():
    d = base('bu26', 'A bad Visio update in 2026: Peter sees the same steps and everyone else gets the fix without noticing; agents and flows do the work; the engineer only says yes; every step reads and writes the ServiceNow record', '2026')
    # 1 Peter's Visio crashes; Nexthink records it
    person(d, 0, 'peter', 'alert'); system(d, cx(0), SY1, 'nexthink', 'Nexthink')
    vline(d, cx(0), PY + R + 32, SY1 - SR - 6, 'Crash\nand version', 410)
    # 2 a webhook opens the incident; the Software agent tells Peter
    record(d, 1, 'Incident', first=True)
    mid = cx(0) + 80
    path(d, (cx(0) + SR + 6, SY1), (mid, SY1), (mid, SYB), (cx(1) - 34, SYB), label='Webhook', at=(mid + 40, (SY1 + SYB) / 2 + 5))
    person(d, 1, 'peter', 'message'); robot(d, cx(1), SY1, 'Digital Hub')
    vline(d, cx(1), SY1 - SR - 6, PY + R + 32, 'We opened\na ticket', 410)
    both(d, cx(1), SY1 + SR + 14, SYB - 34)
    # 3 the Software agent gives the workaround from the knowledge base
    person(d, 2, 'peter', 'message'); robot(d, cx(2), SY1, 'Digital Hub'); record(d, 2, 'Workaround')
    vline(d, cx(2), SY1 - SR - 6, PY + R + 32, 'Visio in\nthe browser', 410)
    both(d, cx(2), SY1 + SR + 14, SYB - 34)
    under(d, 2, 'now', 'Knowledge base', 'Workaround')
    # 4 the incidents become one problem; the problem agent prepares the analysis; the engineer says yes
    person(d, 3, 'engineer'); robot(d, cx(3), SY1, 'ServiceNow'); record(d, 3, 'Problem')
    pair(d, cx(3), 'Analysis,\nready', 'Yes', ly=410)
    both(d, cx(3), SY1 + SR + 14, SYB - 34)
    under(d, 3, 'nexthink', 'Nexthink', 'By version')
    # 5 a change pauses the update; the Software agent tells Peter
    person(d, 4, 'peter', 'message'); robot(d, cx(4), SY1, 'Digital Hub'); record(d, 4, 'Change: pause')
    vline(d, cx(4), SY1 - SR - 6, PY + R + 32, 'Update held,\nfix underway', 410)
    both(d, cx(4), SY1 + SR + 14, SYB - 34)
    under(d, 4, 'cloud', 'Cloud Update', 'Pause', up=False)
    # 6 the problem agent prepares the steps; the engineer says yes; Intune changes the settings
    person(d, 5, 'engineer'); robot(d, cx(5), SY1, 'ServiceNow'); record(d, 5, 'Change: fix')
    pair(d, cx(5), 'Steps,\nready', 'Yes', ly=410)
    both(d, cx(5), SY1 + SR + 14, SYB - 34)
    under(d, 5, 'intune', 'Intune', 'Settings', up=False)
    # 7 the Software agent tells Peter; his incident closes
    person(d, 6, 'peter', 'done'); robot(d, cx(6), SY1, 'Digital Hub'); record(d, 6, 'Incident closed')
    pair(d, cx(6), '\u201cWe fixed it\u201d', 'Rating', ly=410)
    both(d, cx(6), SY1 + SR + 14, SYB - 34)
    # 8 Cloud Update rolls the update out to everyone else in waves; nobody notices; everything closes
    everyone(d, 7); record(d, 7, 'All closed')
    under(d, 7, 'cloud', 'Cloud Update', 'In waves', up=False, left=True)
    return d

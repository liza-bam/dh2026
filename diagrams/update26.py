"""D19-12b / D26-17. The bad update as a blueprint in Sandy's 2019 style: people on top, systems below,
the data written on the arrows between them. Same seven steps in 2019 and 2026."""
from rich import Rich
from svg import SECOND, INK, wrap
from transition import TEAL, TINT
from cards26 import symbol
import base64
from pathlib import Path

VEC = Path(__file__).parent / 'assets' / 'vector'


def vec(name):
    return 'data:image/svg+xml;base64,' + base64.b64encode((VEC / f'{name}.svg').read_bytes()).decode()


def mark(d, key, x, y, r):
    """A platform logo in a disc, drawn from vector files so it stays sharp."""
    if key == 'hub':
        d.el.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f5c000"/>')
        glyph(d, 'hub', x, y, r * 1.15, '#fff')
    elif key == 'now':
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

W = 1180
X0, COL = 140, 160            # first column centre, column width
TOP, BOT = 96, 470            # top of the people band, top of the systems band
PY, R = 250, 44               # people circles
SY1, SYB, SY3, SR = 556, 690, 830, 34   # actors, the ServiceNow record, integrations
SY2 = SYB
END = 930                     # bottom of the systems band
H = 1130
GREY = '#f4f7f8'
LINE = '#5d6b72'
RED = '#c0392b'


def cx(i):
    return X0 + i * COL


def glyph(d, name, x, y, s, fill=TEAL):
    k = s / 960
    d.el.append(f'<path d="{symbol(name)}" fill="{fill}" transform="translate({x - s / 2:.1f} {y + s / 2:.1f}) scale({k:.4f})"/>')


def person(d, i, kind, badge=None, x=None):
    """kind: peter (a laptop) or engineer (a person at work). badge: alert, message or done."""
    x = cx(i) if x is None else x
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


def pair(d, x, up, down, ly=400, down_first=False, bottom=None, spread=0):
    """Two arrows between a person and a system, each with its own label beside it:
    the up arrow (left) brings data to the person, the down arrow (right) takes their answer back."""
    b = SY1 - SR - 6 if bottom is None else bottom
    xu, xd = x - 12, x + 12
    d.el.append(f'<path d="M{xu:.0f} {b:.0f}V{PY + R + 32:.0f}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    d.el.append(f'<path d="M{xd:.0f} {PY + R + 32:.0f}V{b:.0f}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    for text, tx, anchor, yy in [(up, xu - 10, 'end', ly - spread), (down, xd + 10, 'start', ly + spread)]:
        ls = text.split('\n')
        y0 = yy - (len(ls) - 1) * 11 + 5
        for k, t in enumerate(ls):
            d.t(tx, y0 + k * 22, t, 15, 700, anchor, fill=TEAL)


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
    d.rect(60, BOT, W - 80, END - BOT, GREY, GREY, rx=0, sw=0)
    for y0, y1, s in [(TOP - 36, BOT - 10, 'PEOPLE'), (BOT, END, 'SYSTEMS')]:
        cy = (y0 + y1) / 2
        d.el.append(f'<text x="36" y="{cy:.0f}" transform="rotate(-90 36 {cy:.0f})" font-family="\'Inter\', sans-serif" font-size="14" '
                    f'font-weight="600" letter-spacing="3" fill="{SECOND}" text-anchor="middle">{s}</text>')
    legend(d, label, agents)


def legend(d, label, agents):
    """Every picture in the diagram, with what it means."""
    d.t(64, END + 34, 'Legend', 15, 700, fill=INK)
    d.t(W - 20, END + 34, label, 15, 700, 'end', fill=INK)
    items = [('peter', 'Peter, whose Visio crashed'), ('engineer', 'The support engineer'),
             ('everyone', 'Everyone else due the update')] + ([] if agents else [('alert', 'Something went wrong')]) + [
             ('message', 'A message to Peter'), ('done', 'Fixed'),
             ('hub', 'Digital Hub'),
             ('now', 'ServiceNow: the case record'), ('nexthink', 'Nexthink: watches every laptop')]
    if agents:
        items += [('cloud', 'Microsoft 365 Cloud Update'), ('intune', 'Microsoft Intune')]
    items += [('arrow', 'Words on an arrow: the data that moves')]
    items += [] if agents else [('both', 'Reads and writes the record')]
    cw, rh = (W - 84) / 5, 50
    for k, (key, text) in enumerate(items):
        x, y = 64 + (k % 5) * cw, END + 70 + (k // 5) * rh
        ix = x + 18
        if key in ('peter', 'everyone'):
            d.el.append(f'<circle cx="{ix}" cy="{y}" r="18" fill="{TINT}"/>')
            glyph(d, 'laptop_outline' if key == 'peter' else 'groups', ix, y, 22)
        elif key == 'engineer':
            d.el.append(f'<circle cx="{ix}" cy="{y}" r="17" fill="#fff" stroke="{TEAL}" stroke-width="1.5"/>')
            glyph(d, 'support_agent', ix, y, 22)
        elif key in ('alert', 'message', 'done'):
            d.el.append(f'<circle cx="{ix}" cy="{y}" r="13" fill="{RED if key == "alert" else TEAL}"/>')
            glyph(d, {'alert': 'notifications', 'message': 'chat_bubble', 'done': 'check_circle'}[key], ix, y, 16, '#fff')
        elif key == 'hub':
            d.el.append(f'<circle cx="{ix}" cy="{y}" r="18" fill="#f5c000"/>')
            glyph(d, 'hub', ix, y, 22, '#fff')
        elif key == 'agent':
            d.el.append(f'<circle cx="{ix}" cy="{y}" r="18" fill="{TINT}" stroke="{TEAL}" stroke-width="1.5"/>')
            glyph(d, 'smart_toy', ix, y, 22)
        elif key == 'arrow':
            d.el.append(f'<path d="M{x} {y}h32" stroke="{LINE}" stroke-width="1.8" marker-end="url(#m{d.uid})"/>')
        elif key == 'auto':
            d.el.append(f'<rect x="{x}" y="{y - 12}" width="36" height="24" fill="#fff" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="5 4"/>')
        elif key == 'both':
            d.el.append(f'<path d="M{x + 2} {y}h32" stroke="{LINE}" stroke-width="1.8" marker-start="url(#m{d.uid})" marker-end="url(#m{d.uid})"/>')
        else:
            mark(d, key, ix, y, 18)
        n = len(wrap(text, cw - 54, 15))
        d.lines(x + 46, y + 5 - (n - 1) * 9.5, text, cw - 54, 15, 400, SECOND, lh=19)


STEPS = [
    ('Crash', 'Visio won’t start after the update'),
    ('Ticket', 'A ticket opens; Peter is told and keeps working'),
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


def everyone(d, i, x=None, y=400):
    """The fix reaches everyone else; they see nothing, so no arrow."""
    x = cx(i) if x is None else x
    person(d, i, 'everyone', x=x)
    d.t(x, y, 'Sees nothing:', 15, 600, 'middle', fill=SECOND)
    d.t(x, y + 20, 'Visio just works', 15, 600, 'middle', fill=SECOND)


FIXED = '\u201cWe fixed\nthe problem\u201d'


def build19():
    d = base('bu19', 'A bad Visio update in 2019: Peter gets two messages, the ticket with a workaround and the fix; the engineer searches for the cause and writes the fix; Digital Hub runs it for everyone else, who notice nothing; every step reads and writes the ServiceNow ticket', '2019')
    # 1 Peter's Visio crashes; Nexthink records it
    person(d, 0, 'peter', 'alert'); system(d, cx(0), SY1, 'nexthink', 'Nexthink')
    vline(d, cx(0), PY + R + 32, SY1 - SR - 6, 'Crash\nand version', 410)
    # 2 Digital Hub opens a ticket and gives Peter the virtual machine, in one message
    person(d, 1, 'peter', 'message'); system(d, cx(1), SY1, 'hub'); record(d, 1, 'Ticket', first=True)
    hline(d, cx(0) + SR + 6, cx(1) - SR - 8, SY1)
    d.t((cx(0) + cx(1)) / 2, SY1 - 10, 'Crash', 15, 600, 'middle', fill=SECOND)
    vline(d, cx(1), SY1 - SR - 6, PY + R + 32, 'Ticket +\nvirtual machine', 410)
    both(d, cx(1), SY1 + SR + 6, SYB - 34)
    # 3 the engineer searches Nexthink; the ticket shows three similar ones
    person(d, 2, 'engineer'); system(d, cx(2), SY1, 'nexthink'); record(d, 2, '3 similar tickets')
    pair(d, cx(2), 'The cause:\nthe update', 'She searches', ly=410, down_first=True, spread=40)
    both(d, cx(2), SY1 + SR + 6, SYB - 34)
    # 4 Digital Hub holds the update and tells Peter
    person(d, 3, 'peter', 'message'); system(d, cx(3), SY1, 'hub'); record(d, 3, 'Update held')
    vline(d, cx(3), SY1 - SR - 6, PY + R + 32, 'Update held,\nfix underway', 410)
    both(d, cx(3), SY1 + SR + 6, SYB - 34)
    # 5 the engineer writes the steps; Digital Hub runs them
    person(d, 4, 'engineer'); system(d, cx(4), SY1, 'hub'); record(d, 4, 'Fix')
    vline(d, cx(4), PY + R + 32, SY1 - SR - 6, 'Steps she\nwrote', 410)
    both(d, cx(4), SY1 + SR + 6, SYB - 34)
    # 6 Peter hears back and rates it; his ticket closes
    person(d, 5, 'peter', 'done'); system(d, cx(5), SY1, 'hub'); record(d, 5, 'Ticket closed')
    pair(d, cx(5), FIXED, 'Rating', ly=410, spread=40)
    both(d, cx(5), SY1 + SR + 6, SYB - 34)
    # 7 Digital Hub runs the same steps for everyone else; nobody notices
    everyone(d, 6); system(d, cx(6), SY1, 'hub'); record(d, 6, 'All closed')
    both(d, cx(6), SY1 + SR + 6, SYB - 34)
    return d


STEPS26 = [
    ('Crash', 'Peter\u2019s Visio crashes. Within a minute, Digital Hub\u2019s agent tells him how to keep working.', '2019: steps 1\u20132'),
    ('Fix', 'ServiceNow\u2019s agent finds the cause and writes the fix by itself. The engineer only says yes, once.', '2019: steps 3\u20135'),
    ('Done', 'Digital Hub\u2019s agent tells Peter it\u2019s fixed. Everyone else gets the update and notices nothing.', '2019: steps 6\u20137'),
]
# the systems, in the order they act: (logo, x, what it does)
NODES26 = [
    ('nexthink', 140, 'Nexthink sees the crash'),
    ('now', 270, 'ServiceNow opens a ticket'),
    ('hub', 400, 'Digital Hub\u2019s agent messages Peter'),
    ('now', 620, 'ServiceNow\u2019s agent finds the cause and writes the fix'),
    ('cloud', 760, 'Cloud Update pauses the update'),
    ('intune', 890, 'Intune changes the settings'),
    ('hub', 1010, 'Digital Hub\u2019s agent tells Peter'),
    ('cloud', 1160, 'Cloud Update gives everyone else the update'),
    ('now', 1290, 'ServiceNow closes the ticket'),
]


def label(d, x, y, text, w, anchor):
    ls = wrap(text, w, 16)
    y0 = y - (len(ls) - 1) * 10 + 5
    for k, t in enumerate(ls):
        d.t(x, y0 + k * 20, t, 15, 600, anchor, fill=TEAL)


def arrow(d, *pts):
    p = 'M' + ' L'.join(f'{a:.0f} {b:.0f}' for a, b in pts)
    d.el.append(f'<path d="{p}" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linejoin="round" marker-end="url(#m{d.uid})"/>')


def build26():
    """2026: three steps. Every system is a node in one chain; each person is linked to the node that talks to them."""
    global W, X0, COL, PY, BOT, END, H
    keep = W, X0, COL, PY, BOT, END, H
    W, X0, COL, PY, BOT, END, H = 1360, 280, 420, 300, 600, 900, 1100
    d = Rich('bu26', W, H, 'A bad Visio update in 2026, in three steps: Digital Hub\u2019s agent tells Peter, ServiceNow\u2019s agent finds the cause and writes the fix, the engineer says yes once, and the systems do the rest by themselves; everyone else notices nothing')
    frame(d, '2026')
    for i, (t, s_, was) in enumerate(STEPS26):
        head(d, i, i + 1, t, s_)
        d.t(cx(i) - COL / 2 + 10, TOP + 112, was, 15, 400, 'start', fill=SECOND)
    ny, top, ly = BOT + 120, PY + R + 32, 490
    # the chain of systems
    for k, (key, x, text) in enumerate(NODES26):
        mark(d, key, x, ny, 24)
        d.lines(x, ny + 46, text, 118, 15, 400, INK, lh=19, anchor='middle')
        if k:
            hline(d, NODES26[k - 1][1] + 30, x - 32, ny)
    d.t(W / 2, END - 26, 'AUTOMATIC: NOBODY TOUCHES IT', 24, 700, 'middle', fill=TEAL)
    # step 1: Peter. His laptop reports the crash to Nexthink; Digital Hub's agent writes to him
    person(d, 0, 'peter', 'message', x=270)
    arrow(d, (258, top), (258, BOT + 40), (140, BOT + 40), (140, ny - 30))
    label(d, 248, ly, 'His laptop reports the crash', 150, 'end')
    arrow(d, (400, ny - 30), (400, BOT + 56), (282, BOT + 56), (282, top))
    label(d, 292, ly, 'Digital Hub\u2019s agent: \u201cWe created a ticket. Use Visio in the browser.\u201d', 160, 'start')
    # step 2: the engineer and ServiceNow's agent
    person(d, 1, 'engineer', x=620)
    arrow(d, (632, ny - 30), (632, top))
    label(d, 642, ly, 'ServiceNow\u2019s agent: \u201cThe new update crashes Visio. Pause it and change the settings?\u201d', 170, 'start')
    arrow(d, (608, top), (608, ny - 30))
    label(d, 598, ly, 'She says yes', 80, 'end')
    # step 3: Peter hears back; everyone else just gets the update
    person(d, 2, 'peter', 'done', x=1010)
    arrow(d, (1022, ny - 30), (1022, top))
    label(d, 1032, ly, 'Digital Hub\u2019s agent: \u201cWe fixed the problem.\u201d', 100, 'start')
    arrow(d, (998, top), (998, ny - 30))
    label(d, 988, ly, 'Peter rates it', 70, 'end')
    person(d, 2, 'everyone', x=1210)
    arrow(d, (1172, ny - 30), (1172, top + 30))
    label(d, 1182, ly + 40, 'The update. They notice nothing', 130, 'start')
    W, X0, COL, PY, BOT, END, H = keep
    return d

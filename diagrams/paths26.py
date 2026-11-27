"""D26-14..16. One request on each of the three paths: a swimlane flowchart, one column for each actor, steps from top to bottom."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import symbol

LINE = '#8fa3ab'
PANEL = '#f4f7f8'
HAIR = '#dce4e7'
W, X0 = 1180, 20
HEAD = 64        # lane header
GAP = 60         # space between rows
FS = 17          # step text
NOTE = 17        # side notes and branch labels

LANES = {
    'employee': ('Employee', 'person'),
    'intake': ('Intake agent', 'smart_toy'),
    'software': ('Software agent', 'smart_toy'),
    'team': ('Network team agent', 'smart_toy'),
    'flow': ('Fixed flow', 'account_tree'),
    'engineer': ('Engineer', 'engineering'),
}


def glyph(d, name, x, y, s, fill=TEAL):
    k = s / 960
    d.el.append(f'<path d="{symbol(name)}" fill="{fill}" transform="translate({x:.1f} {y + s:.1f}) scale({k:.4f})"/>')


def eyebrow(d, x, y, s):
    d.el.append(f'<text x="{x}" y="{y}" font-family="\'Inter\', sans-serif" font-size="11" font-weight="600" '
                f'letter-spacing="1.1" fill="{TEAL}">{s.upper()}</text>')


def tag(d, x, y, s, anchor='start'):
    d.t(x, y, s, NOTE, 700, anchor=anchor, fill=TEAL)


class Lanes:
    def __init__(self, uid, label, lanes):
        self.lanes = lanes
        self.lw = (W - 2 * X0) / len(lanes)
        self.d = Rich(uid, W, 2000, label)
        self.rows = []       # (lane, kind, text, branch, other, y, h)

    def cx(self, lane):
        return X0 + self.lanes.index(lane) * self.lw + self.lw / 2

    def add(self, lane, kind, text, taken=None, other=None):
        """kind: say (the employee's words), box (an action), dia (a choice). taken labels the way down; other is the branch not taken."""
        self.rows.append([lane, kind, text, taken, other])

    def height(self, kind, text):
        w = self.lw - 40
        from svg import wrap
        if kind == 'dia':
            return max(110, 80 + len(wrap(text, w * 0.68, FS)) * 23)
        return 30 + len(wrap(text, w - 20, FS)) * 23

    def draw(self, footnote):
        d = self.d
        y = HEAD + 28
        for r in self.rows:
            r.append(y)
            r.append(self.height(r[1], r[2]))
            y += r[-1] + GAP
        bottom = y - GAP + 28
        # lanes and headers
        for i, lane in enumerate(self.lanes):
            x = X0 + i * self.lw
            d.rect(x, X0, self.lw, bottom - X0, PANEL if i % 2 == 0 else '#fff', 'none', rx=0, sw=0)
            name, ic = LANES[lane]
            glyph(d, ic, x + 20, X0 + 20, 22)
            d.t(x + 52, X0 + 39, name, 18, 600)
        d.el.append(f'<line x1="{X0}" y1="{X0 + HEAD}" x2="{W - X0}" y2="{X0 + HEAD}" stroke="{HAIR}" stroke-width="1"/>')
        d.rect(X0, X0, W - 2 * X0, bottom - X0, 'none', HAIR, rx=0, sw=1)
        # edges first, so the steps sit on top of them
        for a, b in zip(self.rows, self.rows[1:]):
            ax, bx = self.cx(a[0]), self.cx(b[0])
            ay, by = a[5] + a[6], b[5]
            if ax == bx:
                d.arrow((ax, ay), (bx, by - 3))
            else:
                my = ay + GAP / 2
                d.arrow((ax, ay), (ax, my), (bx, my), (bx, by - 3))
            if a[3]:
                tag(d, ax + 10, ay + 20, a[3])
        for lane, kind, text, taken, other, y, h in self.rows:
            cx, w = self.cx(lane), self.lw - 40
            x = cx - w / 2
            if kind == 'dia':
                d.el.append(f'<polygon points="{cx},{y} {cx + w / 2},{y + h / 2} {cx},{y + h} {cx - w / 2},{y + h / 2}" '
                            f'fill="#fff" stroke="{TEAL}" stroke-width="1.8"/>')
                from svg import wrap
                ls = wrap(text, w * 0.68, FS)
                ty = y + h / 2 - (len(ls) - 1) * 11.5 + 6
                for i, ln in enumerate(ls):
                    d.t(cx, ty + i * 23, ln, FS, 600, anchor='middle')
            elif kind == 'say':
                d.rect(x, y, w, h, '#fff', TEAL, rx=0, sw=1.5)
                d.lines(x + 16, y + 28, text, w - 20, FS, 600, INK, lh=23)
            else:
                d.rect(x, y, w, h, '#fff', HAIR, rx=0, sw=1)
                d.lines(x + 16, y + 28, text, w - 20, FS, 400, INK, lh=23)
            if other:
                self.side(cx, y + h / 2, w, other)
        d.lines(X0, bottom + 40, footnote, W - 2 * X0, 18, 400, INK, lh=26)
        d.H = bottom + 76
        return d

    def side(self, cx, cy, w, other):
        """The branch not taken: a dashed arrow into the next lane and a short note."""
        d = self.d
        right = cx + self.lw < W - X0
        x1 = cx + w / 2 if right else cx - w / 2
        x2 = x1 + 34 if right else x1 - 34
        d.el.append(f'<path d="M{x1} {cy}H{x2}" fill="none" stroke="{LINE}" stroke-width="1.6" stroke-dasharray="5 4"/>')
        nw = self.lw - 50
        nx = x2 + 6 if right else x2 - 6 - nw
        label, text = other
        tag(d, nx, cy - 6, label)
        d.lines(nx, cy + 16, text, nw, NOTE, 400, SECOND, lh=21)


def fixed():
    L = Lanes('pa1', 'Path 1, a fixed flow: an employee asks for a second monitor; the intake agent sees no decision is needed and starts the ordering flow; no model decides anything after that',
              ['employee', 'intake', 'flow'])
    L.add('employee', 'say', '“I need a second monitor.”')
    L.add('intake', 'dia', 'Needs a decision?', taken='No: an order', other=('Yes', 'A domain agent takes it.'))
    L.add('flow', 'box', 'Shows a shop card: three monitors for the employee’s role.')
    L.add('employee', 'box', 'Picks one, and where to deliver it.')
    L.add('flow', 'box', 'Orders it in SAP Ariba and opens a ServiceNow request.')
    L.add('employee', 'box', 'Gets the number, then “shipped” and “delivered”.')
    return L.draw('After the intake, no model decides anything. The same request goes the same way every time.')


def domain():
    L = Lanes('pa2', 'Path 2, a domain agent: Visio will not install before a client call; the Software agent checks its fence, solves the call first and hands the repair to a fixed flow',
              ['employee', 'intake', 'software', 'flow'])
    L.add('employee', 'say', '“Visio won’t install. Client call in 20 minutes.”')
    L.add('intake', 'dia', 'Needs a decision?', taken='Yes')
    L.add('software', 'dia', 'Fails for many people?', taken='No', other=('Yes', 'A ticket for the Nexthink agent.'))
    L.add('software', 'dia', 'A license?', taken='Yes', other=('No', 'A request to the manager.'))
    L.add('software', 'box', 'Reads the laptop: the installer cache is broken. A repair takes longer than 20 minutes.')
    L.add('employee', 'box', 'Gets Visio in the browser with the diagram, and joins the call.')
    L.add('flow', 'box', 'After the call: reinstalls Visio from the catalog through Intune.')
    L.add('software', 'dia', 'Works?', taken='Yes', other=('No, twice', 'A person, with the whole story.'))
    L.add('employee', 'box', '“Visio is fixed.”')
    return L.draw('The agent decides inside its fence. Every action it takes runs as a fixed flow.')


def team():
    L = Lanes('pa3', 'Path 3, a team agent: the office Wi-Fi keeps dropping; a ticket goes to the Network team, its agent finds the cause and prepares the fix, an engineer decides',
              ['employee', 'intake', 'team', 'engineer'])
    L.add('employee', 'say', '“The Wi-Fi in the London office keeps dropping.”')
    L.add('intake', 'dia', 'A domain agent takes it?', taken='No', other=('Yes', 'Path 2.'))
    L.add('intake', 'box', 'Opens a ticket for the Network team and gives the employee the number.')
    L.add('team', 'box', 'Finds six similar tickets from the same floor: one access point.')
    L.add('team', 'box', 'Prepares the fix: restart the access point, with the evidence.')
    L.add('engineer', 'dia', 'Approve?', taken='Yes', other=('No', 'The engineer takes over.'))
    L.add('employee', 'box', '“The Wi-Fi is fixed.”')
    L.add('team', 'box', 'Turns the fix into a known fix. Next time, no ticket.')
    return L.draw('Tickets also come from domain agents that gave up, with the whole story. An engineer always decides.')

"""D26-14..16. One request on each of the three paths, step by step, in the portfolio style."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import symbol

LINE = '#b8c6cc'
PANEL = '#f4f7f8'
HAIR = '#dce4e7'

# Who acts at a step: label, icon, fill, border
ACTORS = {
    'employee': ('Employee', 'person', '#fff', HAIR),
    'intake': ('Intake agent', 'smart_toy', TINT, TINT),
    'agent': (None, 'smart_toy', TINT, TINT),
    'flow': ('Fixed flow', 'account_tree', PANEL, PANEL),
    'engineer': ('Engineer', 'engineering', '#fff', HAIR),
}

W, X0, GAP, TOP, TH = 1180, 20, 26, 20, 210


def glyph(d, name, x, y, s, fill=TEAL):
    k = s / 960
    d.el.append(f'<path d="{symbol(name)}" fill="{fill}" transform="translate({x:.1f} {y + s:.1f}) scale({k:.4f})"/>')


def eyebrow(d, x, y, s):
    d.el.append(f'<text x="{x}" y="{y}" font-family="\'Inter\', sans-serif" font-size="11" font-weight="600" '
                f'letter-spacing="1.1" fill="{TEAL}">{s.upper()}</text>')


def flow(uid, label, steps, note, agent_name=None):
    n = len(steps)
    w = (W - 2 * X0 - GAP * (n - 1)) / n
    d = Rich(uid, W, TOP + TH + 84, label)
    for i, (who, title, text) in enumerate(steps):
        name, ic, fill, stroke = ACTORS[who]
        name = name or agent_name
        x = X0 + i * (w + GAP)
        d.rect(x, TOP, w, TH, fill, stroke, rx=0, sw=1)
        glyph(d, ic, x + 16, TOP + 16, 16)
        eyebrow(d, x + 38, TOP + 29, name)
        y = d.lines(x + 16, TOP + 62, title, w - 32, 16, 600, INK, lh=21)
        if isinstance(text, list):
            y += 6
            for ln in text:
                y = d.lines(x + 16, y + 8, ln, w - 32, 13, 400, SECOND, lh=18)
        else:
            d.lines(x + 16, y + 8, text, w - 32, 13, 400, SECOND, lh=18)
        if i < n - 1:
            ax, ay = x + w + 6, TOP + TH / 2
            d.el.append(f'<path d="M{ax:.0f} {ay - 6:.0f}l7 6l-7 6" fill="none" stroke="{TEAL}" stroke-width="1.6" '
                        f'stroke-linecap="round" stroke-linejoin="round"/>')
    y = TOP + TH + 24
    d.el.append(f'<line x1="{X0}" y1="{y}" x2="{W - X0}" y2="{y}" stroke="{HAIR}" stroke-width="1"/>')
    d.lines(X0, y + 30, note, W - 2 * X0, 15, 400, INK, lh=21)
    d.H = TOP + TH + 84
    return d


def fixed():
    return flow('pa1', 'A fixed flow: an employee orders a second monitor, the intake agent starts the ordering flow, and no model decides anything after that', [
        ('employee', '“I need a second monitor.”', 'In Teams, in their own words.'),
        ('intake', 'An order', 'Starts the ordering flow. Its only decision.'),
        ('flow', 'A shop card', 'Three monitors from the catalog for the employee’s role.'),
        ('employee', 'Picks one', 'And where to deliver it.'),
        ('flow', 'Orders it', 'SAP Ariba order, a ServiceNow request, the number in the chat.'),
        ('flow', 'Keeps them posted', 'Shipped, delivered. The same way every time.'),
    ], 'After the intake, no model decides anything. Cheap, predictable, easy to audit.')


def domain():
    return flow('pa2', 'A domain agent: Visio will not install before a client call; the Software agent checks its fence, puts the call first and hands the repair to a fixed flow', [
        ('employee', '“Visio won’t install. Client call in 20 minutes.”', 'The diagram for the call is in Visio.'),
        ('intake', 'A software problem', 'Hands the case to the Software agent.'),
        ('agent', 'Checks its fence', ['Fails for many people? No.', 'A license? Yes.', 'The laptop: a broken installer cache.']),
        ('agent', 'Decides: the call first', 'A repair takes longer than 20 minutes. Visio in the browser now, with the diagram.'),
        ('flow', 'Repairs after the call', 'Reinstalls Visio from the catalog through Intune.'),
        ('agent', 'Checks and closes', 'Visio works. Two failed fixes would bring in a person.'),
    ], 'The agent decides inside its fence. Every action it takes runs as a fixed flow.', agent_name='Software agent')


def team():
    return flow('pa3', 'A team agent: the office Wi-Fi keeps dropping; a ticket goes to the Network team, its agent finds the cause and prepares the fix, an engineer decides', [
        ('employee', '“The Wi-Fi in the London office keeps dropping.”', 'No domain agent takes office networks.'),
        ('intake', 'A ticket', 'For the Network team in ServiceNow. The employee gets the number.'),
        ('agent', 'Finds the pattern', 'Six similar tickets from the same floor, one access point.'),
        ('agent', 'Prepares the fix', 'Restart the access point, with the evidence attached.'),
        ('engineer', 'Decides', 'Approves. The fix runs, the employee hears back.'),
        ('agent', 'Teaches the first line', 'The fix becomes a known fix. Next time, no ticket.'),
    ], 'Tickets also come from domain agents that gave up, with the whole story. An engineer always decides.', agent_name='Team agent')

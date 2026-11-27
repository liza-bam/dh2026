"""D19-11. Support paths as designed for EY Digital Hub in 2019: a flowchart with its choices, the platforms and what the employee sees."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import icon
from paths26 import glyph, HAIR, PANEL

W, H = 1180, 1080
CX = 330          # centre of the flow
BW, BH = 360, 76  # step boxes
EX = 740          # employee column


def zone(d, y, h, label, fill):
    d.rect(20, y, 640, h, fill, fill, rx=0, sw=0)
    d.el.append(f'<text x="40" y="{y + 30}" font-family="\'Inter\', sans-serif" font-size="12" font-weight="600" '
                f'letter-spacing="1.2" fill="{INK}">{label.upper()}</text>')


def step(d, y, ic, title, sub, logos=()):
    x = CX - BW / 2
    d.rect(x, y, BW, BH, '#fff', HAIR, rx=0, sw=1)
    icon(d, ic, x + 38, y + BH / 2, 22)
    d.t(x + 74, y + 33, title, 15, 600)
    d.t(x + 74, y + 54, sub, 13, 400, fill=SECOND)
    for k, lg in enumerate(logos):
        d.logo(lg, x + BW - 30 - k * 26, y + 8, 20)


def diamond(d, cy, lines, w=250, h=120):
    d.el.append(f'<polygon points="{CX},{cy - h / 2} {CX + w / 2},{cy} {CX},{cy + h / 2} {CX - w / 2},{cy}" '
                f'fill="#fff" stroke="{TEAL}" stroke-width="1.8"/>')
    y0 = cy - (len(lines) - 1) * 9 + 5
    for i, ln in enumerate(lines):
        d.t(CX, y0 + i * 18, ln, 14, 600, anchor='middle')


def tag(d, x, y, s, anchor='start'):
    d.t(x, y, s, 13, 700, anchor=anchor, fill=TEAL)


def sees(d, y_from, x_from, msg):
    """A dashed line to what the employee sees: a laptop with the message on its screen."""
    x = EX
    d.el.append(f'<path d="M{x_from} {y_from}H{x - 8}" fill="none" stroke="{TEAL}" stroke-width="1.4" stroke-dasharray="4 4"/>')
    sy = y_from - 34
    d.rect(x, sy, 300, 62, '#fff', '#9fb3ba', rx=0, sw=1.2)               # screen
    d.rect(x + 12, sy + 12, 276, 38, TINT, TINT, rx=0, sw=0)              # notification
    glyph(d, 'chat_bubble', x + 22, sy + 22, 18)
    d.t(x + 50, sy + 36, msg, 13, 600)
    d.el.append(f'<path d="M{x - 14} {sy + 62}h328l-14 10h-300z" fill="#dce4e7"/>')   # laptop base


def build():
    d = Rich('su19', W, H, 'Support paths, 2019: monitoring and AI scripts fix problems first; when they fail, a person works a ticket, and a manual fix that can be automated becomes a new script')
    zone(d, 20, 600, 'Automated preventive support', TINT)
    zone(d, 640, 420, 'Manual preventive support', PANEL)

    d.el.append(f'<text x="{EX}" y="50" font-family="\'Inter\', sans-serif" font-size="12" font-weight="600" '
                f'letter-spacing="1.2" fill="{INK}">WHAT THE EMPLOYEE SEES</text>')

    # Automated
    step(d, 64, 'monitor_heart', 'Monitor laptops and servers', 'System, software, hardware', ('nexthink',))
    d.arrow((CX, 140), (CX, 168))
    diamond(d, 228, ['A failure,', 'or a risk of one?'])
    d.arrow((CX - 125, 228), (70, 228), (70, 102), (CX - BW / 2 - 4, 102))
    tag(d, 82, 220, 'No: keep watching')
    d.arrow((CX, 288), (CX, 316))
    tag(d, CX + 10, 308, 'Yes')
    step(d, 318, 'smart_toy', 'AI scripts fix it', 'Self-healing, on the laptop')
    sees(d, 356, CX + BW / 2, 'A problem found. We are fixing it.')
    d.arrow((CX, 394), (CX, 422))
    step(d, 424, 'manage_search', 'Check the status', 'Did the fix work?', ('nexthink',))
    d.arrow((CX, 500), (CX, 518))
    diamond(d, 572, ['Fixed?'], w=180, h=100)
    d.el.append(f'<path d="M{CX + 90} 572H{CX + BW / 2}" fill="none" stroke="{TEAL}" stroke-width="1.4" stroke-dasharray="4 4"/>')
    sees(d, 572, CX + BW / 2, 'Fixed. You can carry on.')
    tag(d, CX + 100, 564, 'Yes')
    d.arrow((CX, 622), (CX, 686))
    tag(d, CX + 10, 666, 'No')

    # Manual
    step(d, 688, 'confirmation_number', 'A person analyses', 'A ticket opens, with the laptop data', ('now', 'nexthink'))
    sees(d, 726, CX + BW / 2, 'We are on it. Ticket INC12334.')
    d.arrow((CX, 764), (CX, 792))
    step(d, 794, 'check_circle', 'Ticket resolved', 'Status updates along the way', ('now',))
    sees(d, 832, CX + BW / 2, 'Fixed. Thanks for waiting.')
    d.arrow((CX, 870), (CX, 898))
    diamond(d, 960, ['Can the fix', 'be automated?'])
    d.arrow((CX - 125, 960), (45, 960), (45, 356), (CX - BW / 2 - 4, 356))
    tag(d, 56, 952, 'Yes: a new script')
    d.arrow((CX + 125, 960), (560, 960))
    tag(d, CX + 135, 952, 'No')
    d.rect(564, 944, 86, 32, '#fff', HAIR, rx=0, sw=1)
    d.t(607, 965, 'Manual', 13, 600, anchor='middle', fill=SECOND)

    # How messages reach people
    y = 900
    d.logo('nexthink', EX, y, 26)
    d.logo('avaamo', EX + 32, y, 26)
    d.lines(EX, y + 52, 'Messages reach the desktop and the phone. Some fixes ask first: a new version, a disk clean-up.', 400, 14, 400, INK, lh=20)
    d.H = H
    return d

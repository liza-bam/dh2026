"""D19-11. Support paths as designed for EY Digital Hub in 2019: a flowchart with its choices, the platforms and what the employee sees."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from cards26 import icon
from paths26 import glyph, HAIR, PANEL

W, H = 1180, 1290
CX = 370          # centre of the flow
BW, BH = 460, 96  # step boxes
EX = 760          # employee column
FS = 19


def zone(d, y, h, label, fill):
    d.rect(20, y, 700, h, fill, fill, rx=0, sw=0)
    d.el.append(f'<text x="40" y="{y + 32}" font-family="\'Inter\', sans-serif" font-size="15" font-weight="600" '
                f'letter-spacing="1.2" fill="{INK}">{label.upper()}</text>')


def step(d, y, ic, title, sub, logos=()):
    x = CX - BW / 2
    d.rect(x, y, BW, BH, '#fff', HAIR, rx=0, sw=1)
    icon(d, ic, x + 46, y + BH / 2, 28)
    d.t(x + 92, y + 42, title, FS, 600)
    d.t(x + 92, y + 68, sub, 16, 400, fill=SECOND)
    for k, lg in enumerate(logos):
        d.logo(lg, x + BW - 40 - k * 34, y + 10, 28)


def diamond(d, cy, lines, w=270, h=130):
    d.el.append(f'<polygon points="{CX},{cy - h / 2} {CX + w / 2},{cy} {CX},{cy + h / 2} {CX - w / 2},{cy}" '
                f'fill="#fff" stroke="{TEAL}" stroke-width="1.8"/>')
    y0 = cy - (len(lines) - 1) * 11 + 6
    for i, ln in enumerate(lines):
        d.t(CX, y0 + i * 22, ln, 17, 600, anchor='middle')


def tag(d, x, y, s, anchor='start'):
    d.t(x, y, s, 16, 700, anchor=anchor, fill=TEAL)


def sees(d, y_from, x_from, msg):
    """A dashed line to what the employee sees: a Digital Hub notification."""
    d.el.append(f'<path d="M{x_from} {y_from}H{EX - 8}" fill="none" stroke="{TEAL}" stroke-width="1.4" stroke-dasharray="4 4"/>')
    y = y_from - 38
    d.rect(EX, y, 400, 76, '#fff', HAIR, rx=0, sw=1)
    d.rect(EX, y, 4, 76, TEAL, TEAL, rx=0, sw=0)
    glyph(d, 'chat_bubble', EX + 20, y + 13, 16)
    d.el.append(f'<text x="{EX + 44}" y="{y + 27}" font-family="\'Inter\', sans-serif" font-size="15" font-weight="600" '
                f'letter-spacing="1.1" fill="{TEAL}">DIGITAL HUB</text>')
    d.t(EX + 20, y + 56, msg, 16, 600)


def build():
    d = Rich('su19', W, H, 'Support paths, 2019: monitoring and AI scripts fix problems first; when they fail, a person works a ticket, and a manual fix that can be automated becomes a new script')
    zone(d, 20, 730, 'Automated preventive support', TINT)
    zone(d, 770, 500, 'Manual preventive support', PANEL)
    d.el.append(f'<text x="{EX}" y="52" font-family="\'Inter\', sans-serif" font-size="15" font-weight="600" '
                f'letter-spacing="1.2" fill="{INK}">WHAT THE EMPLOYEE SEES</text>')

    # Automated
    step(d, 70, 'monitor_heart', 'Monitor laptops and servers', 'System, software, hardware', ('nexthink',))
    d.arrow((CX, 166), (CX, 189))
    diamond(d, 256, ['A failure,', 'or a risk of one?'])
    d.arrow((CX - 135, 256), (60, 256), (60, 118), (CX - BW / 2 - 4, 118))
    tag(d, 72, 246, 'No: keep watching')
    d.arrow((CX, 321), (CX, 357))
    tag(d, CX + 12, 344, 'Yes')
    step(d, 360, 'smart_toy', 'AI scripts fix it', 'Self-healing, on the laptop')
    sees(d, 408, CX + BW / 2, 'A problem found. We are fixing it.')
    d.arrow((CX, 456), (CX, 487))
    step(d, 490, 'manage_search', 'Check the status', 'Did the fix work?', ('nexthink',))
    d.arrow((CX, 586), (CX, 603))
    diamond(d, 660, ['Fixed?'], w=200, h=110)
    d.el.append(f'<path d="M{CX + 100} 660H{CX + BW / 2}" fill="none" stroke="{TEAL}" stroke-width="1.4" stroke-dasharray="4 4"/>')
    sees(d, 660, CX + BW / 2, 'Fixed. You can carry on.')
    tag(d, CX + 112, 648, 'Yes')
    d.arrow((CX, 715), (CX, 817))
    tag(d, CX + 12, 742, 'No')

    # Manual
    step(d, 820, 'confirmation_number', 'A person analyses', 'A ticket opens, with the laptop data', ('now', 'nexthink'))
    sees(d, 868, CX + BW / 2, 'We are on it. Ticket INC12334.')
    d.arrow((CX, 916), (CX, 947))
    step(d, 950, 'check_circle', 'Ticket resolved', 'Status updates along the way', ('now',))
    sees(d, 998, CX + BW / 2, 'Fixed. Thanks for waiting.')
    d.arrow((CX, 1046), (CX, 1073))
    diamond(d, 1140, ['Can the fix', 'be automated?'])
    d.arrow((CX - 135, 1140), (36, 1140), (36, 408), (CX - BW / 2 - 4, 408))
    tag(d, 48, 1130, 'Yes: a new script')
    d.arrow((CX + 135, 1140), (586, 1140))
    tag(d, CX + 147, 1130, 'No')
    d.rect(590, 1118, 110, 44, '#fff', HAIR, rx=0, sw=1)
    d.t(645, 1146, 'Manual', 17, 600, anchor='middle', fill=SECOND)

    # How messages reach people
    y = 1100
    d.logo('nexthink', EX, y, 32)
    d.logo('avaamo', EX + 40, y, 32)
    d.lines(EX, y + 64, 'Messages reach the desktop and the phone. Some fixes ask first, like a new version or a disk clean-up.', 410, 16, 400, INK, lh=23)
    d.H = H
    return d

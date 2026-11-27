"""D19-11. Support paths as designed for EY Digital Hub in 2019, redrawn in the portfolio style."""
from rich import Rich
from svg import SECOND, INK
from transition import TEAL, TINT
from paths26 import glyph, eyebrow, HAIR, PANEL

W, X0, GAP, TW, TH = 1180, 45, 30, 250, 190
ROW_A, ROW_M = 58, 330
LINE = '#8fa3ab'


def col(i):
    return X0 + i * (TW + GAP)


def tile(d, i, y, who, title, text, sees=None, kind='auto'):
    x = col(i)
    fill, stroke = (TINT, TINT) if kind == 'auto' else ('#fff', HAIR)
    d.rect(x, y, TW, TH, fill, stroke, rx=0, sw=1)
    logo, name = who
    if logo in ('nexthink', 'now'):
        d.logo(logo, x + 16, y + 13, 20)
    else:
        glyph(d, logo, x + 17, y + 15, 17)
    eyebrow(d, x + 44, y + 28, name)
    yy = d.lines(x + 16, y + 62, title, TW - 32, 16, 600, INK, lh=21)
    d.lines(x + 16, yy + 6, text, TW - 32, 13, 400, SECOND, lh=18)
    if sees:
        sy = y + TH - 36
        d.rect(x, sy, TW, 36, '#fff' if kind == 'auto' else PANEL, 'none', rx=0, sw=0)
        glyph(d, 'notifications', x + 16, sy + 10, 16)
        d.t(x + 40, sy + 23, sees, 12.5, 600, fill=TEAL)


def chevron(d, x, y, left=False):
    s = -1 if left else 1
    d.el.append(f'<path d="M{x - 3 * s:.0f} {y - 6:.0f}l{7 * s} 6l{-7 * s} 6" fill="none" stroke="{TEAL}" stroke-width="1.6" '
                f'stroke-linecap="round" stroke-linejoin="round"/>')


def band(d, y, s):
    d.el.append(f'<text x="{X0}" y="{y}" font-family="\'Inter\', sans-serif" font-size="12" font-weight="600" '
                f'letter-spacing="1.2" fill="{INK}">{s.upper()}</text>')


def build():
    d = Rich('su19', W, 620, 'Support paths, 2019: monitoring and AI scripts fix problems first; when they fail, a person works a ticket, and every manual fix is checked for automation')
    band(d, ROW_A - 16, 'Automated preventive support')
    tile(d, 0, ROW_A, ('nexthink', 'Nexthink'), 'Monitors', 'Laptops and servers: system, software, hardware. Finds anomalies.')
    tile(d, 1, ROW_A, ('help', 'Check'), 'A failure, or a risk of one?', 'No: keep monitoring. Yes: fix it.')
    tile(d, 2, ROW_A, ('smart_toy', 'AI scripts'), 'Fix it on their own', 'Self-healing scripts run on the laptop.', 'Employee sees: a possible failure')
    tile(d, 3, ROW_A, ('nexthink', 'Nexthink'), 'Fixed?', 'Checks the status of the issue.', 'Employee sees: problem fixed')
    for i in range(3):
        chevron(d, col(i) + TW + GAP / 2, ROW_A + TH / 2)

    band(d, ROW_M - 16, 'Manual preventive support')
    tile(d, 3, ROW_M, ('now', 'ServiceNow'), 'A person analyses', 'A ticket opens, with the Nexthink data.', 'Employee sees: work in progress', kind='manual')
    tile(d, 2, ROW_M, ('now', 'ServiceNow'), 'Ticket resolved', 'The status updates along the way.', 'Employee sees: problem fixed', kind='manual')
    tile(d, 1, ROW_M, ('now', 'ServiceNow'), 'Can the fix be automated?', 'Yes: it goes into the database as a new script.', kind='manual')
    for i in (2, 3):
        chevron(d, col(i) - GAP / 2, ROW_M + TH / 2, left=True)

    # Not fixed: down to a person
    x = col(3) + TW / 2
    d.el.append(f'<line x1="{x}" y1="{ROW_A + TH}" x2="{x}" y2="{ROW_M - 4}" stroke="{LINE}" stroke-width="1.5"/>')
    d.el.append(f'<path d="M{x - 6} {ROW_M - 11}l6 7l6 -7" fill="none" stroke="{LINE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
    d.t(x + 10, ROW_A + TH + 34, 'Not fixed', 13, 600, fill=SECOND)
    # A new script: back up to the AI scripts
    x1, x2, ym = col(1) + TW / 2, col(2) + TW / 2, ROW_A + TH + 40
    d.el.append(f'<path d="M{x1} {ROW_M}V{ym}H{x2}V{ROW_A + TH + 8}" fill="none" stroke="{TEAL}" stroke-width="1.5" stroke-linejoin="round"/>')
    d.el.append(f'<path d="M{x2 - 6} {ROW_A + TH + 15}l6 -7l6 7" fill="none" stroke="{TEAL}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
    d.t((x1 + x2) / 2, ym - 8, 'A new script', 13, 600, anchor='middle', fill=TEAL)

    y = ROW_M + TH + 30
    d.el.append(f'<line x1="{X0}" y1="{y}" x2="{W - X0}" y2="{y}" stroke="{HAIR}" stroke-width="1"/>')
    d.logo('nexthink', X0, y + 18, 22)
    d.logo('avaamo', X0 + 28, y + 18, 22)
    d.lines(X0 + 64, y + 34, 'Notifications reach the desktop and the phone. Some fixes ask the employee first: a new version, a disk clean-up.',
            W - 2 * X0 - 64, 15, 400, INK, lh=21)
    d.H = 620
    return d

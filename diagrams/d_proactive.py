"""5. Preventive and proactive support (slide 'DXT Proactive Approach')."""
from rich import Rich, Z
from svg import SECOND

G = '#9aa5aa'
Y = '#f5c000'


def diamond(d, cx, cy, text, w=170, h=110):
    d.el.append(f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" fill="{Y}"/>')
    d.lines(cx, cy - 10, text, w * 0.55, 13, 600, anchor='middle')


def step(d, x, y, w, text, logos=(), h=None):
    from rich import wrap
    n = len(wrap(text, w - 24, 14))
    h = h or 22 + n * 19 + (40 if logos else 0)
    d.rect(x, y, w, h, '#eceff0', '#eceff0', rx=8)
    d.lines(x + 12, y + 24, text, w - 24, 14, 600)
    lx = x + 12
    for lg in logos:
        if lg == 'holmes':
            d.wordmark('holmes', lx, y + h - 36, 80, 26)
            lx += 88
        else:
            d.logo(lg, lx, y + h - 42, 34)
            lx += 42
    return y + h


def build():
    d = Rich('pp', 1260, 1210, 'Preventive and proactive support: automated and manual preventive support, push notifications to desktop and mobile')
    d.zone(20, 20, 600, 640, 'Automated preventive support', 'grey')
    d.zone(20, 680, 600, 400, 'Manual preventive support', 'grey')

    # automated -------------------------------------------------------------------
    b = step(d, 200, 62, 300, 'Monitor in real time: client side (OS, software, hardware) and server side. Correlate irregular devices and anomalies')
    diamond(d, 350, 200, 'Any downtime or possible failure?')
    d.arrow((350, b), (350, 145), color=G)
    d.arrow((265, 200), (120, 200), (120, 100), (200, 100), color=G, dashed=True)
    d.t(128, 230, 'No: keep monitoring', 13, 600, fill=SECOND)
    run_b = step(d, 270, 286, 220, 'Run AI scripts to self-heal issues', ['holmes'])
    d.arrow((350, 255), (350, 286), color=G, label='Yes', at=(358, 276))
    add_b = step(d, 50, 286, 180, 'Add the new AI scripts to the library')
    d.arrow((230, 320), (270, 320), color=G, dashed=True)
    chk_b = step(d, 270, run_b + 16, 220, 'Check the status of the issue', ['nexthink'])
    diamond(d, 410, chk_b + 80, 'Issue fixed?', 140, 90)
    d.arrow((380, chk_b), (380, chk_b + 20), (410, chk_b + 20), (410, chk_b + 35), color=G)

    # manual ------------------------------------------------------------------------------
    an_b = step(d, 60, 730, 190, 'Analyze the issue', ['holmes', 'nexthink'])
    tk_b = step(d, 330, 730, 200, 'Ticket created', ['holmes', 'now'])
    d.arrow((410, chk_b + 125), (410, 710), (155, 710), (155, 730), color=G, label='No', at=(418, chk_b + 146))
    d.arrow((410, 710), (430, 710), (430, 730), color=G)
    diamond(d, 155, an_b + 90, 'Can the fix be automated?', 170, 110)
    d.arrow((155, an_b), (155, an_b + 35), color=G)
    d.el.append(f'<rect x="30" y="{an_b + 78}" width="30" height="24" rx="12" fill="#c9cfd2"/>')
    d.arrow((70, an_b + 90), (62, an_b + 90), color=G, dashed=True)
    d.t(64, an_b + 74, 'No', 13, 600, fill=SECOND)
    cr_b = step(d, 60, an_b + 190, 200, 'Create the scripts to automate the issue', ['holmes', 'nexthink'])
    d.arrow((155, an_b + 145), (155, an_b + 190), color=G, label='Yes', at=(163, an_b + 172))
    d.arrow((60, cr_b - 30), (38, cr_b - 30), (38, 320), (50, 320), color=G, dashed=True)
    st_b = step(d, 330, tk_b + 24, 200, 'Ticket status updated', ['holmes', 'now'])
    d.arrow((430, tk_b), (430, tk_b + 24), color=G)
    rs_b = step(d, 330, st_b + 60, 200, 'Ticket resolved', ['now'])
    d.arrow((430, st_b), (430, st_b + 60), color=G)
    db_b = step(d, 220, 1100, 320, 'Database updated and used for better service', ['now'])
    d.arrow((430, rs_b), (430, 1100), color=G)

    # proactive support: notifications ----------------------------------------------------------
    d.zone(660, 20, 300, 1060, 'Proactive support', 'grey', 'Push notifications')
    notes = [('alert', 'About downtime or possible failures', 320), ('ok', 'Problem fixed', chk_b + 80),
             ('tools', 'Work in progress', 790), ('ok', 'Problem fixed', rs_b - 30)]
    for icon, text, cy in notes:
        d.rect(690, cy - 50, 170, 100, '#eceff0', '#eceff0', rx=8)
        d.lines(702, cy - 24, 'Push notification', 150, 14, 600)
        d.lines(702, cy - 4, text, 110, 13, 400, fill=SECOND)
        if icon == 'tools':
            d.image('tools', 810, cy - 2, 40)
        else:
            d.mark(icon, 812, cy, 36)
    d.arrow((490, 320), (690, 320), color=G)
    d.arrow((480, chk_b + 80), (690, chk_b + 80), color=G, label='Yes', at=(500, chk_b + 72))
    d.arrow((530, tk_b - 30), (600, tk_b - 30), (600, 780), (690, 780), color=G)
    d.arrow((530, st_b - 30), (600, st_b - 30), (600, 800), (690, 800), color=G)
    d.arrow((530, rs_b - 30), (690, rs_b - 30), color=G)

    # devices --------------------------------------------------------------------------------------
    m = 520
    d.el.append(f'<path d="M880 60 Q900 60 900 80 L900 {m - 16} Q900 {m} 916 {m} Q900 {m} 900 {m + 16} L900 1040 Q900 1060 880 1060" fill="none" stroke="#223640" stroke-width="2"/>')
    d.arrow((916, 470), (980, 470), color=G)
    d.image('software', 990, 410, 110)
    d.logo('nexthink', 1110, 470, 50)
    d.arrow((916, 590), (980, 590), color=G)
    d.image('iphone', 1010, 550, 80)
    d.logo('nexthink', 1100, 560, 44)
    d.logo('avaamo', 1150, 560, 44)
    d.rect(1100, 612, 92, 30, Y, Y, rx=15)
    d.t(1146, 632, 'DIGITAL HUB', 11, 700, 'middle')
    d.lines(990, 690, 'Push notifications go to desktop and mobile. Some preventive measures need the employee’s consent, such as installing a new version of software or cleaning up the disk.', 240, 14, 400)
    return d

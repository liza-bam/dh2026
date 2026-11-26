"""6. Refresh readiness (slide 'DXT Refresh Readiness Process')."""
from rich import Rich, Z
from svg import SECOND
from d_proactive import diamond

G = '#9aa5aa'
GREEN = '#6aa84f'


def alert_circle(d, cx, cy, text):
    d.el.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="#fff" stroke="#7d9bc2" stroke-width="1.5"/>')
    d.lines(cx, cy - 4, text, 70, 13, 600, anchor='middle')
    d.mark('alert', cx - 15, cy - 74, 30)


def bullets(d, x, y, title, items, w, size=14):
    d.t(x, y, title, size, 600)
    y += size + 8
    for it in items:
        d.el.append(f'<circle cx="{x + 4}" cy="{y - 5}" r="2.5" fill="#223640"/>')
        y = d.lines(x + 14, y, it, w - 14, size) + 2
    return y


def build():
    d = Rich('rr', 1720, 1160, 'Refresh readiness: collect live data, gather existing data, analyze and map, ready for the refresh')
    heads = [(20, 'Collect live data'), (540, 'Gather existing data'), (1010, 'Analyze and map'), (1360, 'Ready for the refresh')]
    for i, (x, t) in enumerate(heads):
        d.t(x, 44, t, 26, 600)
        if i < 3:
            nx = heads[i + 1][0]
            d.el.append(f'<path d="M{x + len(t) * 14 + 10} 36 L{nx - 20} 36" stroke="{GREEN}" stroke-width="2" stroke-dasharray="2 5" fill="none" marker-end="url(#m{d.uid})"/>')

    # Collect live data --------------------------------------------------------------
    for i in range(3):
        d.image(f'cust{i + 1}', 40 + i * 70, 220, 60, round_=True, ring='#b7c1c5')
    d.rect(20, 290, 250, 200, '#eceff0', '#eceff0', rx=8)
    bullets(d, 34, 316, 'Monitor in real time', ['Disk space', 'CPU use', 'RAM use', 'Software used', 'Network speed'], 222)
    d.logo('nexthink', 90, 500, 90)
    diamond(d, 370, 390, 'Hardware challenges?', 150, 100)
    diamond(d, 580, 390, 'Software OK?', 150, 100)
    d.arrow((270, 390), (295, 390), color=G)
    d.arrow((445, 390), (505, 390), color=G, label='Yes', at=(458, 382))
    d.arrow((580, 340), (580, 250), color=G, dashed=True, label='No', at=(588, 300))
    d.rect(495, 186, 170, 64, '#eceff0', '#eceff0', rx=6)
    d.lines(580, 212, 'Automated preventive support', 150, 13, 400, SECOND, anchor='middle')
    d.arrow((370, 440), (370, 950), color=G, label='No', at=(378, 620))
    d.rect(300, 950, 140, 74, '#eceff0', '#eceff0', rx=6)
    d.lines(312, 974, 'Capture the hardware performance data', 120, 13, 600)
    d.arrow((370, 1024), (370, 1050), color=G)
    d.logo('nexthink', 340, 1050, 60)
    d.arrow((370, 1110), (370, 1130), (1200, 1130), (1200, 1000), color=G)

    # Gather existing data ---------------------------------------------------------------
    d.el.append('<path d="M700 200 Q686 200 686 216 L686 376 Q686 390 674 390 Q686 390 686 404 L686 560 Q686 576 700 576" fill="none" stroke="#223640" stroke-width="2"/>')
    d.arrow((655, 390), (672, 390), color=G, label='Yes', at=(640, 380))
    d.rect(710, 196, 240, 50, '#eceff0', '#eceff0', rx=6)
    d.t(724, 227, 'Low network speed', 14, 600)
    d.rect(710, 256, 240, 130, '#eceff0', '#eceff0', rx=6)
    bullets(d, 724, 282, 'Hardware performance challenges', ['CPU?', 'RAM?', 'Disk space?'], 220)
    data = [('ariba', 'Hardware catalogue', ['List of hardware', 'Hardware assignment dates']),
            ('now', 'ServiceNow', ['Hardware issues', 'Software list', 'Software issues']),
            ('office', 'Office 365', ['Mobility: on the way?', 'Urgency: client-facing?', 'Schedule: busy and quiet seasons?']),
            ('workday', 'HR database', ['Band', 'Service tower', 'Base location']),
            ('now', 'ServiceNow', ['Technical capabilities']),
            ('avaamo', 'Avaamo', ['Sentiment'])]
    y = 400
    rows = []
    for logo, title, items in data:
        h = 30 + len(items) * 20 + 10
        d.rect(710, y, 240, h, '#eceff0', '#eceff0', rx=6)
        d.logo(logo, 650, y + h / 2 - 26, 52)
        bullets(d, 724, y + 24, title, items, 220, 13)
        rows.append((y, h))
        y += h + 10
    for (ry, h) in rows[:4]:
        d.arrow((950, ry + h / 2), (1100, ry + h / 2), color=G)
    # flags
    diamond(d, 1010, 320, 'Critical?', 100, 70)
    d.arrow((950, 320), (960, 320), color=G)
    alert_circle(d, 1010, 160, 'Mark for early refresh')
    d.arrow((1010, 285), (1010, 206), color=G, label='Yes', at=(1018, 250))
    d.arrow((1060, 320), (1080, 320), (1080, 400), (1100, 400), color=G)
    alert_circle(d, 860, 120, 'Mark for data-loss risk')
    d.arrow((860, 196), (860, 166), color=G)
    d.el.append(f'<path d="M906 110 L906 90 L1700 90 L1700 1040 L1680 1040" fill="none" stroke="#9aa5aa" stroke-width="1.6" stroke-dasharray="6 5"/>')
    d.el.append(f'<path d="M1056 150 L1060 110 L1600 110 L1600 250" fill="none" stroke="#9aa5aa" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#m{d.uid})"/>')
    vy = rows[4][0] + rows[4][1] / 2 + 20
    diamond(d, 1010, vy, 'Very low?', 100, 70)
    d.arrow((950, rows[4][0] + rows[4][1] / 2), (970, rows[4][0] + rows[4][1] / 2), (970, vy), (960, vy), color=G)
    d.arrow((950, rows[5][0] + rows[5][1] / 2), (970, rows[5][0] + rows[5][1] / 2), (970, vy), color=G)
    alert_circle(d, 1010, vy + 120, 'Mark for extra support')
    d.arrow((1010, vy + 35), (1010, vy + 74), color=G, label='Yes', at=(1018, vy + 58))
    d.arrow((1056, vy + 120), (1560, vy + 120), (1560, 1060), color=G, dashed=True)
    d.arrow((1060, vy), (1100, vy), color=G)

    # Analyze and map -------------------------------------------------------------------------
    d.rect(1100, 380, 210, 620, '#fff', '#c9d1d4', rx=10)
    d.t(1116, 410, 'Analyze the data', 16, 600)
    d.image('analyse', 1116, 426, 130)
    y = d.lines(1116, 590, 'Map employee data to performance and find the trends.', 180, 15)
    d.lines(1116, y + 16, 'Map software needs to hardware and define the minimum configuration and OS.', 180, 15)
    d.logo('nexthink', 1116, 830, 52)
    d.image('ztc', 1176, 830, 52)
    d.logo('avaamo', 1146, 890, 52)
    for i in range(3):
        d.image(f'agent{i + 1}', 1240, 820 + i * 56, 50, round_=True, ring=Z['agent'][1])

    # Ready for the refresh -----------------------------------------------------------------
    d.el.append('<path d="M1356 250 Q1340 250 1340 270 L1340 640 Q1340 660 1326 660 Q1340 660 1340 680 L1340 1060 Q1340 1080 1356 1080" fill="none" stroke="#223640" stroke-width="2"/>')
    d.arrow((1310, 660), (1324, 660), color=G)
    outs = [(250, 'Refresh schedule', ['Early refresh', 'Priority refresh', 'Scheduled refresh', 'Postponed refresh']),
            (560, 'Recommended hardware for user groups', ['OS', 'Configuration', 'Model', 'Peripherals']),
            (850, 'Potential challenges', ['Extra care cases: VIP, low tech adoption, high urgency or priority', 'Cases with potential loss of data'])]
    for y, title, items in outs:
        d.rect(1380, y + 10, 300, 210, '#e4e8ea', '#e4e8ea', rx=8)
        d.rect(1370, y, 300, 210, '#eceff0', '#d5dbde', rx=8)
        bullets(d, 1386, y + 30, title, items, 200, 15)
        d.mark('ok', 1606, y + 76, 54)
    return d

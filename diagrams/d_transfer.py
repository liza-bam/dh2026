"""7. Data transfer to the new laptop."""
from rich import Rich
from svg import SECOND

G = '#7d888d'
YEL = '#fde7a0'
ORA = '#f8c9a4'
BLUE = '#4a72c4'


def note(d, x, y, w, text, fill=YEL, size=13, h=None):
    from rich import wrap
    n = len(wrap(text, w - 20, size))
    h = h or n * (size + 5) + 20
    d.rect(x, y, w, h, fill, fill, rx=8)
    d.lines(x + 10, y + 20, text, w - 20, size)
    return y + h


def bdiamond(d, cx, cy, text, w=110, h=110):
    d.el.append(f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" fill="{BLUE}"/>')
    d.lines(cx, cy - 2, text, w * 0.55, 13, 600, fill='#fff', anchor='middle')


def pc(d, x, y, new, ok=False, s=60):
    d.image('pcgreen' if new else 'pcgrey', x, y, s)
    if ok:
        d.mark('ok', x + s - 18, y - 6, 26)


def build():
    d = Rich('dt', 1860, 640, 'Data transfer from the old laptop to the new one')
    pc(d, 30, 120, True)
    d.lines(60, 206, 'New computer delivered', 110, 13, 600, anchor='middle')
    d.arrow((96, 150), (128, 150), color=G)
    d.rect(124, 112, 120, 76, '#eef2f8', '#9db3d8', rx=6)
    d.lines(184, 134, 'Delivery alert: ServiceNow and Nexthink', 104, 12, 400, anchor='middle')
    pc(d, 30, 290, False)
    d.lines(60, 376, 'Old computer still active', 110, 13, 600, anchor='middle')
    b = note(d, 140, 240, 150, 'Push notification: prepare for the data transfer. Switch on both machines and connect them to the same local network.')
    d.arrow((180, 188), (180, 240), color=G)
    d.arrow((92, 320), (140, 320), color=G)
    d.rect(310, 260, 100, 120, '#eceff0', '#eceff0', rx=8)
    d.lines(360, 296, 'SxL monitors both machines', 80, 13, 600, anchor='middle')
    d.arrow((290, 320), (310, 320), color=G)
    bdiamond(d, 490, 320, 'Both online?')
    d.arrow((410, 320), (435, 320), color=G)
    d.arrow((490, 375), (490, 420), color=G, label='No', at=(498, 400))
    note(d, 430, 420, 120, 'Push notification: put both computers online')
    d.mark('alert', 556, 430, 30)
    d.el.append(f'<path d="M490 530 L490 560 L240 560 L240 {b}" fill="none" stroke="{G}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#m{d.uid})"/>')
    d.arrow((545, 320), (580, 320), color=G, label='Yes', at=(548, 312))
    d.rect(580, 280, 110, 80, '#eceff0', '#eceff0', rx=8)
    d.lines(635, 306, 'Push the transfer agent to both', 90, 13, 600, anchor='middle')
    pc(d, 720, 130, True, True)
    d.lines(750, 112, 'New computer: receive mode', 140, 12, 600, anchor='middle')
    pc(d, 720, 430, False, True)
    d.lines(750, 512, 'Old computer: send mode', 140, 12, 600, anchor='middle')
    d.arrow((635, 280), (635, 160), (718, 160), color=G)
    d.arrow((635, 360), (635, 460), (718, 460), color=G)
    d.rect(820, 270, 110, 100, '#eceff0', '#eceff0', rx=8)
    d.lines(875, 296, 'Run a script to enable a direct connection', 90, 13, 600, anchor='middle')
    d.arrow((782, 160), (875, 160), (875, 270), color=G)
    d.arrow((782, 460), (875, 460), (875, 370), color=G)
    bdiamond(d, 1010, 320, 'Can connect?')
    d.arrow((930, 320), (955, 320), color=G)
    d.arrow((1010, 375), (1010, 420), color=G, label='No', at=(1018, 400))
    note(d, 950, 420, 120, 'Push notification: connect both computers to the same local network')
    d.mark('alert', 1076, 430, 30)
    d.el.append(f'<path d="M1010 564 L1010 600 L200 600 L200 {b}" fill="none" stroke="{G}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#m{d.uid})"/>')
    d.arrow((1065, 320), (1090, 320), color=G, label='Yes', at=(1066, 312))

    # in the local network
    d.rect(1090, 150, 290, 340, '#fff', '#d5dbde', rx=10)
    d.t(1104, 172, 'In the local network', 13, 600, fill=SECOND)
    pc(d, 1104, 190, True, True)
    pc(d, 1104, 390, False, True)
    d.el.append('<path d="M1134 252 L1134 388" stroke="#6aa84f" stroke-width="2"/>')
    d.t(1144, 326, 'Direct connection', 13, 600)
    n_b = note(d, 1214, 190, 156, 'Push notification: log off the new computer and keep it on. Press the button to start the transfer. You can keep working on the old one.')
    bdiamond(d, 1420, 320, 'Ready?', 80, 80)
    d.arrow((1380, 320), (1380, 320), color=G)
    d.el.append(f'<path d="M1420 360 L1420 470 L1290 470 L1290 {n_b}" fill="none" stroke="{G}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#m{d.uid})"/>')

    # data transfer
    d.rect(1460, 150, 160, 340, '#fff', '#d5dbde', rx=10)
    pc(d, 1475, 180, True)
    pc(d, 1475, 390, False)
    d.el.append(f'<path d="M1505 388 L1505 244" stroke="#6aa84f" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    d.lines(1515, 300, 'Agent receives and copies the data', 90, 12, 600)
    d.mark('ok', 1560, 190, 40)
    d.lines(1545, 254, 'All data safely moved', 80, 12, 600)
    d.arrow((1460, 320), (1470, 320), color=G)
    note(d, 1640, 190, 100, 'Push notification: data freeze. Stop working. Final transfer in progress.', ORA, 12)
    d.arrow((1620, 320), (1640, 320), color=G)

    # final
    d.rect(1750, 150, 100, 340, '#fff', '#d5dbde', rx=10)
    pc(d, 1770, 200, True)
    pc(d, 1770, 390, False)
    d.el.append(f'<path d="M1800 388 L1800 264" stroke="#6aa84f" stroke-width="2" marker-end="url(#m{d.uid})"/>')
    d.lines(1758, 300, 'Final transfer of the latest changes', 84, 11, 600)
    d.arrow((1740, 320), (1750, 320), color=G)
    d.mark('ok', 1640, 520, 40)
    d.t(1690, 547, 'Start working on the new computer', 15, 600)
    d.mark('ok', 1640, 580, 40)
    d.t(1690, 607, 'Send back the old laptop', 15, 600)
    return d

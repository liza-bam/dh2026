"""8-10. Scenario storyboards: screens cropped from the 2019 slides, labels, platforms and emotion curve redrawn."""
import base64
import io
from PIL import Image
from rich import Rich, Z
from svg import SECOND

import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
PDF = HERE.parent / 'source' / '2019' / 'DXT0-diagrams.pdf'
CACHE = HERE / '.cache'
# page, crop box at 400 dpi
PAGES = {'pw': (14, 6200, 6550, 9300, 2600), 'mr': (15, 6000, 6600, 6400, 2500), 'vpn': (16, 7300, 6600, 5200, 2900)}
_img = {}


def _src(key):
    CACHE.mkdir(exist_ok=True)
    out = CACHE / f'{key}.png'
    if not out.exists():
        pg, x, y, w, h = PAGES[key]
        subprocess.run(['pdftoppm', '-r', '400', '-f', str(pg), '-l', str(pg), '-x', str(x), '-y', str(y), '-W', str(w), '-H', str(h),
                        '-png', '-singlefile', str(PDF), str(CACHE / key)], check=True)
    return out


def crop(src, box, h):
    if src not in _img:
        _img[src] = Image.open(_src(src)).convert('RGB')
    im = _img[src].crop(box)
    w = round(im.width * h / im.height)
    im = im.resize((w * 2, h * 2), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=82)
    return w, 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def mobile(src, xs, y0, y1, sc):
    return [crop(src, (round(a * sc), round(y0 * sc), round(b * sc), round(y1 * sc)), 300) for a, b in xs]


def header(d, x, w, y, text, logos, h=86):
    d.rect(x, y, w, h, '#fff', '#d5dbde', rx=8)
    yy = y + 16
    lx = x + w / 2 - len(logos) * 19
    for i, lg in enumerate(logos):
        if lg == 'ztc':
            d.image('ztc', lx + i * 38, yy - 6, 34)
        elif lg == 'genesys':
            d.wordmark('genesys', lx + i * 38 - 20, yy - 2, 72, 26)
        else:
            d.logo(lg, lx + i * 38, yy - 6, 32)
    d.lines(x + w / 2, y + (60 if logos else 34), text, w - 16, 13, 600, anchor='middle')


def screens(d, x, y, shots, gap=10):
    xs = []
    for w, data in shots:
        d.el.append(f'<image href="{data}" x="{x}" y="{y}" width="{w}" height="300"/>')
        d.rect(x, y, w, 300, 'none', '#d5dbde', rx=4)
        xs.append((x, w))
        x += w + gap
    return xs


def emotions(d, cols, y, faces):
    """faces: list of (column position as float, level 0..4, emoji)."""
    top, h = y, 170
    for x, w in cols:
        d.rect(x, top, w, h, '#f4f6f7', '#f4f6f7', rx=4)
    d.el.append(f'<line x1="{cols[0][0]}" y1="{top + h - 50}" x2="{cols[-1][0] + cols[-1][1]}" y2="{top + h - 50}" stroke="#c9d1d4" stroke-dasharray="4 4"/>')
    pts = []
    for pos, lvl, em in faces:
        i = min(int(pos), len(cols) - 1)
        x = cols[i][0] + cols[i][1] * (pos - i)
        yy = top + h - 22 - lvl * 32
        pts.append((x, yy))
    d.el.append('<polyline points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts) + '" fill="none" stroke="#a7b0b4" stroke-width="2.5"/>')
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    d.el.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#6aa84f" stroke-width="2.5" stroke-dasharray="8 6"/>')
    for (x, yy), (_, _, em) in zip(pts, faces):
        d.el.append(f'<text x="{x:.0f}" y="{yy + 12:.0f}" font-size="34" text-anchor="middle">{em}</text>')


def above(d, x, w, y_top, text, logo, to_y):
    d.logo(logo, x + w / 2 - 20, y_top, 40)
    d.rect(x + 10, y_top + 46, w - 20, 40, '#fff', '#d5dbde', rx=6)
    d.t(x + w / 2, y_top + 71, text, 13, 600, 'middle')
    d.arrow((x + w / 2, to_y), (x + w / 2, y_top + 88), color='#5d7fbf')


def password():
    d = Rich('pw', 1900, 700, 'Password reset storyboard: mobile app and Windows lock screen')
    s = 5.1667
    mob = mobile('pw', [(15, 98), (103, 183), (188, 268), (273, 353), (360, 441)], 165, 340, s)
    d.t(20, 30, 'Mobile: Digital Hub app', 16, 600, fill=SECOND)
    cols = screens(d, 20, 150, mob)
    x1, x2 = cols[1][0], cols[-1][0] + cols[-1][1]
    d.el.append(f'<path d="M{x1} 140 L{x1} 120 L{x2} 120 L{x2} 140" fill="none" stroke="#9aa5aa" stroke-width="1.5"/>')
    d.logo('azure', (x1 + x2) / 2 - 22, 98, 44)
    emotions(d, cols, 470, [(0.1, 1.5, '\U0001F610'), (1.5, 0.6, '\U0001F62C'), (2.5, 2.4, '\U0001F603'), (3.5, 1.5, '\U0001F610'), (4.6, 3.9, '\U0001F60A')])

    d.t(860, 30, 'Desktop: Windows lock screen', 16, 600, fill=SECOND)
    desk = [(2540, 2370 - 528, 3185, 2370), (3252, 1842, 3957, 2380), (3972, 1850, 4685, 2378), (4708, 1842, 5469, 2380),
            (5483, 1846, 6172, 2380), (6200, 1850, 6825, 2375), (6847, 1850, 7628, 2375)]
    shots = []
    for b in desk:
        im = (b[0], 1842, b[2], 2375)
        w, data = crop('pw', im, 300)
        shots.append((round(w * 0.56), data))
    x = 860
    labels = [('Help at the point of need', []), ('Employee profile', ['azure']), ('Employee profile', ['azure']), ('One-time code data', ['azure']),
              ('Password rules', ['azure']), ('Password reset', ['azure']), ('Feedback collected', ['nexthink'])]
    cx = []
    for (w, data), (lab, logos) in zip(shots, labels):
        d.el.append(f'<image href="{data}" x="{x}" y="300" width="{w}" height="168"/>')
        header(d, x, w, 200, lab, logos, 90)
        cx.append((x, w))
        x += w + 8
    # one-time code to the phone
    w, data = crop('pw', (round(880 * s), round(175 * s), round(955 * s), round(328 * s)), 300)
    px = cx[2][0] + cx[2][1] - 30
    d.el.append(f'<image href="{data}" x="{px}" y="40" width="{round(w * 0.5)}" height="150"/>')
    d.t(px + 120, 70, 'Code sent to the', 13, 600)
    d.t(px + 120, 88, 'employee’s phone', 13, 600)
    d.arrow((cx[2][0] + 40, 200), (px, 140), color='#5d7fbf')
    lx, lw = cx[-1]
    header(d, lx + lw + 10, 120, 200, 'Feedback analyzed', ['ztc'], 90)
    d.arrow((lx + lw - 10, 245), (lx + lw + 10, 245), color='#5d7fbf')
    d.W = lx + lw + 150
    return d


def meeting_room():
    d = Rich('mr', 1900, 790, 'Meeting room storyboard: proactive room change, Avaamo bot, live agent, feedback')
    s = 3.556
    left = mobile('mr', [(28, 143), (148, 262), (271, 386), (393, 507), (515, 630), (638, 752)], 193, 390, s)
    cols = screens(d, 20, 190, left)
    heads = [('Proactive notification: employee calendar', ['office']), ('Urgent room change: employee profile, timing', ['office', 'workday']),
             ('Strong sentiment detected; ticket created', ['avaamo', 'now']), ('Live handoff with all the information', ['genesys', 'avaamo']),
             ('Feedback collected; ticket closed', ['avaamo', 'now']), ('Sentiment and feedback analyzed', ['ztc'])]
    for (x, w), (t, lg) in zip(cols, heads):
        header(d, x, w, 64, t, lg, 116)
    d.t(cols[2][0], 50, 'Help at the point of need', 14, 600, fill=SECOND)
    d.logo('avaamo', cols[1][0] + cols[1][1] - 30, 500, 60)
    d.t(cols[1][0] + cols[1][1], 578, 'Avaamo bot', 13, 600, 'middle')
    d.image('agent1', cols[3][0] + 38, 500, 60, round_=True, ring=Z['agent'][1])
    d.t(cols[3][0] + 68, 578, 'Live agent', 13, 600, 'middle')
    emotions(d, cols, 600, [(0.0, 1.3, '\U0001F610'), (0.7, 2.6, '\U0001F642'), (1.5, 0.5, '\U0001F62E'), (2.6, 3.2, '\U0001F92F'),
                            (3.4, 1.3, '\U0001F610'), (4.6, 2.6, '\U0001F642'), (5.6, 4.0, '\U0001F60E')])

    right = mobile('mr', [(1022, 1137), (1142, 1256), (1266, 1380), (1388, 1502), (1510, 1625), (1633, 1747)], 172, 379, s)
    rx = cols[-1][0] + cols[-1][1] + 70
    rc = screens(d, rx, 190, right)
    header(d, rc[1][0], rc[1][1], 64, 'Room issues', ['now'], 116)
    header(d, rc[2][0], rc[2][1], 44, 'Employee behavior, agent skills, employee and agent sentiment', ['now', 'workday', 'genesys'], 136)
    header(d, rc[3][0], rc[3][1], 64, 'Employee behavior', ['workday'], 116)
    d.W = rc[-1][0] + rc[-1][1] + 20
    return d


def vpn():
    d = Rich('vpn', 1900, 900, 'VPN storyboard: error detected, cause surfaced, micro-learnings, feedback; mobile and desktop')
    d.rect(20, 10, 700, 92, '#f4f6f7', '#f4f6f7', rx=8)
    d.lines(34, 34, 'An employee is at a client site and needs an Excel file on an EY shared drive. The VPN client won’t connect, though the internet works. The file has to be ready for a review with the partner later today.', 670, 13)
    s = 2.889
    mob = mobile('vpn', [(32, 170), (182, 320), (330, 468), (482, 620), (636, 776)], 350, 652, s)
    cols = screens(d, 20, 400, mob)
    heads = [('VPN error detected; notification sent', ['nexthink', 'avaamo']), ('Issue analyzed; likely cause shown', ['nexthink', 'avaamo']),
             ('Relevant micro-learnings', ['avaamo']), ('Feedback collected', ['avaamo']), ('Feedback analyzed', ['ztc'])]
    for (x, w), (t, lg) in zip(cols, heads):
        header(d, x, w, 280, t, lg, 110)
    above(d, cols[1][0], cols[1][1], 160, 'Ticket created', 'now', 290)
    above(d, cols[3][0], cols[3][1], 160, 'Ticket closed', 'now', 290)
    emotions(d, cols, 710, [(0.1, 0.0, '\U0001F62E'), (1.5, 2.0, '\U0001F92F'), (2.5, 1.4, '\U0001F610'), (3.6, 3.0, '\U0001F642'), (4.6, 4.2, '\U0001F60E')])

    d.t(840, 140, 'Desktop', 16, 600, fill=SECOND)
    desk = [(2565, 861, 3785, 1670), (3842, 861, 5056, 1670)]
    x = 840
    dc = []
    for b in desk:
        w, data = crop('vpn', b, 300)
        w2 = round(w * 0.9)
        d.el.append(f'<image href="{data}" x="{x}" y="400" width="{w2}" height="270"/>')
        dc.append((x, w2))
        x += w2 + 20
    header(d, dc[0][0], dc[0][1] * 0.62, 290, 'VPN error detected; notification sent', ['nexthink'], 100)
    above(d, dc[0][0] + dc[0][1] * 0.64, dc[0][1] * 0.36, 160, 'Ticket created', 'now', 290)
    header(d, dc[1][0], dc[1][1] * 0.48, 290, 'Feedback collected', ['nexthink'], 100)
    above(d, dc[1][0], dc[1][1] * 0.48, 160, 'Ticket closed', 'now', 290)
    header(d, dc[1][0] + dc[1][1] * 0.52, dc[1][1] * 0.48, 290, 'Feedback analyzed', ['ztc'], 100)
    d.W = dc[-1][0] + dc[-1][1] + 20
    return d

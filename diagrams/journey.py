"""Scenario flows in swimlanes: who does what, what the employee sees, which module runs, where it branches."""
from rich import Rich, Z
from svg import SECOND, wrap
from transition import TEAL, TINT, AGENTS

G = '#9aa5aa'
OK = '#3d8b2f'
YEL = '#f5c000'
LANE_H = {'employee': 110, 'sees': 210, 'front': 100, 'agent': 120, 'enterprise': 100, 'systems': 100, 'live': 110, 'engineer': 100}
LANE_NAME = {'employee': 'Employee', 'sees': 'What the employee sees', 'front': 'Front door agent', 'agent': 'Our agent',
             'enterprise': 'Enterprise agent', 'systems': 'Systems', 'live': 'Live support', 'engineer': 'Engineer'}
LANE_FILL = {'front': TINT, 'agent': TINT, 'live': Z['agent'][0], 'engineer': Z['agent'][0]}


def card(d, x, y, w, title, lines=(), buttons=(), tone='hub'):
    """A small Digital Hub card as the employee sees it in Teams or on the website."""
    h = 34 + 18 * len(lines) + (40 if buttons else 8) + 20
    d.rect(x, y, w, h, '#fff', '#c9d1d4', rx=8)
    d.el.append(f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="{YEL if tone == "hub" else Z["agent"][1]}"/>')
    d.t(x + 10, y + 26, title, 13, 600)
    yy = y + 44
    for ln in lines:
        d.t(x + 10, yy, ln, 12, 400, fill=SECOND)
        yy += 18
    bx = x + 10
    for i, b in enumerate(buttons):
        bw = len(b) * 7 + 20
        primary = i == 0
        d.rect(bx, yy, bw, 26, TEAL if primary else '#fff', TEAL, rx=6)
        d.t(bx + bw / 2, yy + 17, b, 12, 600, 'middle', fill='#fff' if primary else TEAL)
        bx += bw + 6
    return y + h


def build_flow(uid, label, lanes, steps, edges, cols, colw=210, title_note=None):
    """steps: key -> dict(col, lane, title, sub, module, kind[step|decision|card|done], card=(title, lines, buttons, tone))."""
    left = 170
    W = left + cols * colw + 30
    ys, y = {}, 20
    for ln in lanes:
        ys[ln] = y
        y += LANE_H[ln] + 8
    d = Rich(uid, W, y + 20, label)
    for ln in lanes:
        fill = LANE_FILL.get(ln, '#f7fafb')
        d.rect(10, ys[ln], W - 20, LANE_H[ln], fill, fill, rx=10)
        d.lines(24, ys[ln] + LANE_H[ln] / 2 - 4, LANE_NAME[ln], 130, 13, 600, TEAL if ln in ('front', 'agent') else ('#223640'))
    box = {}
    for key, s in steps.items():
        cx = left + s['col'] * colw + colw / 2
        top = ys[s['lane']]
        lh = LANE_H[s['lane']]
        kind = s.get('kind', 'step')
        if kind == 'card':
            t, lines, buttons, tone = s['card']
            w = colw - 24
            ch = 34 + 18 * len(lines) + (40 if buttons else 8) + 20
            cy = top + (lh - ch) / 2
            card(d, cx - w / 2, cy, w, t, lines, buttons, tone)
            if s.get('module'):
                m = s['module']
                mw = len(m) * 6.6 + 18
                d.rect(cx - w / 2, cy + ch + 6, mw, 20, TEAL, TEAL, rx=10)
                d.t(cx - w / 2 + mw / 2, cy + ch + 20, m, 11, 600, 'middle', fill='#fff')
            box[key] = (cx - w / 2, cy, w, ch)
        elif kind == 'decision':
            w, h = 150, 74
            cy = top + lh / 2
            d.el.append(f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
            for i, ln in enumerate(wrap(s['title'], 90, 12)):
                d.t(cx, cy - 4 + i * 15 - (len(wrap(s['title'], 90, 12)) - 1) * 7, ln, 12, 600, 'middle')
            box[key] = (cx - w / 2, cy - h / 2, w, h)
        else:
            w = colw - 24
            tl = wrap(s['title'], w - 20, 13)
            sl = wrap(s.get('sub', ''), w - 20, 12) if s.get('sub') else []
            h = 16 + 18 * len(tl) + 16 * len(sl) + (26 if s.get('module') else 0) + 8
            by = top + (lh - h) / 2
            fill, stroke = '#fff', '#c9d1d4'
            if s['lane'] in ('front', 'agent'):
                stroke = TEAL
            if s['lane'] in ('live', 'engineer'):
                stroke = Z['agent'][1]
            if kind == 'done':
                fill, stroke = OK, OK
            d.rect(cx - w / 2, by, w, h, fill, stroke, rx=8, sw=1.5)
            yy = by + 20
            for ln in tl:
                d.t(cx - w / 2 + 10, yy, ln, 13, 600, fill='#fff' if kind == 'done' else '#223640')
                yy += 18
            for ln in sl:
                d.t(cx - w / 2 + 10, yy, ln, 12, 400, fill='#fff' if kind == 'done' else SECOND)
                yy += 16
            if s.get('module'):
                m = s['module']
                mw = len(m) * 6.6 + 18
                d.rect(cx - w / 2 + 8, yy - 6, mw, 20, TEAL, TEAL, rx=10)
                d.t(cx - w / 2 + 8 + mw / 2, yy + 8, m, 11, 600, 'middle', fill='#fff')
            if s.get('logos'):
                lx = cx + w / 2 - 6
                for lg in reversed(s['logos']):
                    lx -= 24
                    if lg:
                        d.logo(lg, lx, by - 10, 22)
            box[key] = (cx - w / 2, by, w, h)
    for e in edges:
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else None
        ax, ay, aw, ah = box[a]
        bx, by_, bw, bh = box[b]
        dashed = lab == 'dashed'
        if dashed:
            lab = None
        if abs((ax + aw / 2) - (bx + bw / 2)) < 4:  # same column: vertical
            if by_ > ay:
                d.arrow((ax + aw / 2, ay + ah), (bx + bw / 2, by_), color=G, dashed=dashed, label=lab, at=(ax + aw / 2 + 6, (ay + ah + by_) / 2 + 4))
            else:
                d.arrow((ax + aw / 2, ay), (bx + bw / 2, by_ + bh), color=G, dashed=dashed, label=lab, at=(ax + aw / 2 + 6, (ay + by_ + bh) / 2 + 4))
        else:
            sx, sy = ax + aw, ay + ah / 2
            tx, ty = bx, by_ + bh / 2
            mx = (sx + tx) / 2
            if bx < ax:  # going back
                sx, tx = ax + aw / 2, bx + bw / 2
                yb = max(ay + ah, by_ + bh) + 14
                d.arrow((sx, ay + ah), (sx, yb), (tx, yb), (tx, by_ + bh), color=G, dashed=True, label=lab, at=(tx + 8, yb - 4))
            else:
                d.arrow((sx, sy), (mx, sy), (mx, ty), (tx, ty), color=G, dashed=dashed, label=lab, at=(mx + 6, (sy + ty) / 2 - 4 if sy != ty else sy - 6))
    return d

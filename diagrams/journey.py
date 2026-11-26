"""Scenario flows in swimlanes: who does what, what the employee sees, which module runs, where it branches."""
from rich import Rich, Z
from svg import SECOND, wrap
from transition import TEAL, TINT, AGENTS

G = '#9aa5aa'
OK = '#3d8b2f'
YEL = '#f5c000'
LANE_H = {'employee': 110, 'sees': 210, 'front': 100, 'agent': 120, 'enterprise': 100, 'systems': 100, 'live': 110, 'engineer': 100}
LANE_NAME = {'employee': 'What the employee does and sees', 'sees': 'What the employee sees', 'front': 'Front door agent', 'agent': 'Our agent',
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


def build_flow(uid, label, lanes, steps, edges, cols, colw=210, title_note=None, rows=None):
    """steps: key -> dict(col, lane, title, sub, module, kind[step|decision|card|done], card=(title, lines, buttons, tone)).
    Every employee step is an action in a channel: a verb in the title and the channel logo.
    rows: first column of each row after the first, e.g. [7] stacks columns 7+ under columns 0-6 so the flow fits the page.
    In stacked rows, empty lanes are left out and links between rows use lettered connectors."""
    for key, s in steps.items():
        assert s['lane'] != 'employee' or s.get('kind') == 'card' or s.get('logos'), f'{key}: employee step needs its input channel'
    starts = [0] + list(rows or [])
    bands = [(c0, (starts + [cols])[i + 1]) for i, c0 in enumerate(starts)]
    band_of = {k: max(i for i, (c0, _) in enumerate(bands) if s['col'] >= c0) for k, s in steps.items()}
    left = 170
    W = left + max(c1 - c0 for c0, c1 in bands) * colw + 30
    w = colw - 24

    def size(s):
        kind = s.get('kind', 'step')
        if kind == 'card':
            t, lines, buttons, tone = s['card']
            return 34 + 18 * len(lines) + (40 if buttons else 8) + 20, (26 if s.get('module') else 0)
        if kind == 'decision':
            return 84, 0
        tl = wrap(s['title'], w - 20, 13)
        sl = wrap(s.get('sub', ''), w - 20, 12) if s.get('sub') else []
        return 16 + 18 * len(tl) + 16 * len(sl) + (26 if s.get('module') else 0) + 8, 0

    GAP = 26
    stacks = {}  # steps sharing a lane and a column stack top to bottom in the order they are listed
    for k, s in steps.items():
        stacks.setdefault((band_of[k], s['lane'], s['col']), []).append(k)
    need = {}
    for (b, ln, c), ks in stacks.items():
        tot = sum(sum(size(steps[k])) for k in ks) + GAP * (len(ks) - 1)
        need[b, ln] = max(need.get((b, ln), 0), tot + 36)
    ys, lh_of, y = {}, {}, 20
    for b, (c0, c1) in enumerate(bands):
        used = [ln for ln in lanes if not rows or any(band_of[k] == b and s['lane'] == ln for k, s in steps.items())]
        for ln in used:
            ys[b, ln] = y
            lh_of[b, ln] = max(LANE_H[ln], need.get((b, ln), 0))
            y += lh_of[b, ln] + 8
        y += 40
    d = Rich(uid, W, y - 20, label)
    for (b, ln), top in ys.items():
        fill = LANE_FILL.get(ln, '#f7fafb')
        d.rect(10, top, W - 20, lh_of[b, ln], fill, fill, rx=10)
        d.lines(24, top + lh_of[b, ln] / 2 - 4, LANE_NAME[ln], 130, 13, 600, TEAL if ln in ('front', 'agent') else ('#223640'))
    pos = {}
    for (b, ln, c), ks in stacks.items():
        tot = sum(sum(size(steps[k])) for k in ks) + GAP * (len(ks) - 1)
        yy = ys[b, ln] + (lh_of[b, ln] - tot) / 2
        for k in ks:
            pos[k] = yy
            yy += sum(size(steps[k])) + GAP
    box = {}
    for key, s in steps.items():
        b = band_of[key]
        cx = left + (s['col'] - bands[b][0]) * colw + colw / 2
        kind = s.get('kind', 'step')
        h = size(s)[0]
        by = pos[key]
        if kind == 'card':
            t, lines, buttons, tone = s['card']
            card(d, cx - w / 2, by, w, t, lines, buttons, tone)
            if s.get('module'):
                m = s['module']
                mw = len(m) * 5.9 + 16
                d.rect(cx - w / 2, by + h + 6, mw, 20, TEAL, TEAL, rx=10)
                d.t(cx - w / 2 + mw / 2, by + h + 20, m, 11, 600, 'middle', fill='#fff')
            box[key] = (cx - w / 2, by, w, h)
        elif kind == 'decision':
            dw = 176
            cy = by + h / 2
            d.el.append(f'<polygon points="{cx},{cy - h / 2} {cx + dw / 2},{cy} {cx},{cy + h / 2} {cx - dw / 2},{cy}" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
            tl = wrap(s['title'], 104, 12)
            for i, ln in enumerate(tl):
                d.t(cx, cy + 4 + (i - (len(tl) - 1) / 2) * 15, ln, 12, 600, 'middle')
            box[key] = (cx - dw / 2, by, dw, h)
        else:
            tl = wrap(s['title'], w - 20, 13)
            sl = wrap(s.get('sub', ''), w - 20, 12) if s.get('sub') else []
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
                mw = len(m) * 5.9 + 16
                d.rect(cx - w / 2 + 8, yy - 6, mw, 20, TEAL, TEAL, rx=10)
                d.t(cx - w / 2 + 8 + mw / 2, yy + 8, m, 11, 600, 'middle', fill='#fff')
            if s.get('logos'):
                lx = cx + w / 2 - 6
                for lg in reversed(s['logos']):
                    lx -= 24
                    if lg:
                        d.logo(lg, lx, by - 10, 22)
            box[key] = (cx - w / 2, by, w, h)

    def connector(x, y, letter):
        d.el.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{TEAL}"/>')
        d.t(x, y + 5, letter, 13, 700, 'middle', fill='#fff')

    letters = iter('ABCDEFGH')
    for e in edges:
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else None
        ax, ay, aw, ah = box[a]
        bx, by_, bw, bh = box[b]
        dashed = lab == 'dashed'
        if dashed:
            lab = None
        if steps[a].get('kind') == 'card' and steps[a].get('module') and by_ > ay:
            ah += 26
        if band_of[a] != band_of[b]:  # continues in the next row
            ch = next(letters)
            sy, ty = ay + ah / 2, by_ + bh / 2
            d.arrow((ax + aw, sy), (W - 38, sy), color=G)
            connector(W - 24, sy, ch)
            connector(left - 14, ty, ch)
            d.arrow((left + 1, ty), (bx, ty), color=G)
        elif abs((ax + aw / 2) - (bx + bw / 2)) < 4:  # same column: vertical
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

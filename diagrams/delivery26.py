"""D26-7 Delivery plan: how Digital Hub grows from ten fixed journeys to an orchestrator."""
from rich import Rich, Z
from svg import SECOND, wrap
from transition import TEAL, TINT, G

OK = '#3d8b2f'
LIVE = Z['agent'][1]
ORCH = '#6aa6b5'  # the orchestrator: a lighter teal, white text never sits on it
KIND = {  # fill, stroke, title colour
    'step': ('#fff', '#c9d1d4', '#223640'),
    'agent': (TINT, TEAL, '#223640'),
    'people': ('#fff', LIVE, '#223640'),
    'done': (OK, OK, '#fff'),
}


def box(d, x, y, w, title, sub=None, kind='step', tag=None):
    """A step box; returns its bottom. tag: a small teal chip under the text (model size)."""
    fill, stroke, ink = KIND[kind]
    tl = wrap(title, w - 24, 14)
    sl = wrap(sub, w - 24, 12) if sub else []
    h = 18 + 19 * len(tl) + 16 * len(sl) + (26 if tag else 0) + 8
    d.rect(x, y, w, h, fill, stroke, rx=10, sw=1.5)
    yy = y + 24
    for ln in tl:
        d.t(x + 12, yy, ln, 14, 600, fill=ink)
        yy += 19
    for ln in sl:
        d.t(x + 12, yy, ln, 12, 400, fill='#fff' if kind == 'done' else SECOND)
        yy += 16
    if tag:
        tw = len(tag) * 6.2 + 18
        d.rect(x + 12, yy - 6, tw, 20, TEAL, TEAL, rx=10)
        d.t(x + 12 + tw / 2, yy + 8, tag, 11, 600, 'middle', fill='#fff')
    return y + h


def down(d, x, y1, y2):
    d.arrow((x, y1), (x, y2), color=G)


def split(d, cx, y1, lx, rx, y2, left, right):
    """One box above, two below: a fork with labels."""
    ym = y1 + 18
    d.arrow((cx, y1), (cx, ym), (lx, ym), (lx, y2), color=G)
    d.arrow((cx, ym), (rx, ym), (rx, y2), color=G)
    d.t(lx + 6, ym + 18, left, 12, 600, fill=SECOND)
    d.t(rx + 6, ym + 18, right, 12, 600, fill=SECOND)


def stage(d, x, n, title, sub):
    d.rect(x, 20, 350, 590, '#fff', '#dce4e7', rx=14)
    d.el.append(f'<circle cx="{x + 34}" cy="{56}" r="16" fill="{TEAL}"/>')
    d.t(x + 34, 62, str(n), 16, 700, 'middle', fill='#fff')
    d.t(x + 60, 62, title, 18, 600)
    d.lines(x + 20, 98, sub, 310, 13, 400, SECOND)


def build():
    d = Rich('dp', 1120, 900, 'Delivery plan: ten fixed journeys first, more journeys every week, then the orchestrator takes what has no journey')
    W, half = 350, 155

    # 1. Ten journeys from day one ---------------------------------------------------------
    x = 20
    stage(d, x, 1, 'Ten journeys first', 'The ten most common requests run on fixed journeys. The cost per request stays tiny.')
    cx = x + W / 2
    b = box(d, x + 20, 150, W - 40, 'Every request', 'Teams, the website, the phone')
    down(d, cx, b, b + 26)
    b = box(d, x + 20, b + 26, W - 40, 'Intake agent', 'Reads the request, picks the journey', 'agent', 'Small model')
    split(d, cx, b, x + 20 + half / 2, x + W - 20 - half / 2, b + 58, 'Known', 'No journey yet')
    yb = b + 58
    l1 = box(d, x + 20, yb, half, 'Runs the journey', 'Same steps every time', 'agent')
    r1 = box(d, x + W - 20 - half, yb, half, 'Fills a ServiceNow ticket', 'Category, urgency, group, summary, label', 'agent')
    down(d, x + 20 + half / 2, l1, l1 + 26)
    down(d, x + W - 20 - half / 2, r1, r1 + 26)
    box(d, x + 20, l1 + 26, half, 'Solved', 'The request never reaches the large model', 'done')
    box(d, x + W - 20 - half, r1 + 26, half, 'People solve it', 'Nothing is asked again', 'people')

    # 2. More journeys every week ---------------------------------------------------------------
    x = 385
    stage(d, x, 2, 'More journeys', 'The labels show what people ask most. The most frequent requests become new fixed journeys.')
    cx = x + W / 2
    b = box(d, x + 20, 150, W - 40, 'Labels from the tickets', 'Every request without a journey has one')
    down(d, cx, b, b + 26)
    b = box(d, x + 20, b + 26, W - 40, 'Grouped every week', 'What is asked most, and how often', 'agent', 'Small model')
    down(d, cx, b, b + 26)
    b = box(d, x + 20, b + 26, W - 40, 'People design and approve a new journey', 'Like an engineer approves a new fix', 'people')
    down(d, cx, b, b + 26)
    # the journey library grows
    y = b + 26
    d.rect(x + 20, y, W - 40, 150, TINT, TINT, rx=10)
    d.t(x + 36, y + 28, 'The journey library', 14, 600)
    for i, hgt in enumerate([40, 62, 84]):
        d.rect(x + 40 + i * 64, y + 130 - hgt, 48, hgt, TEAL, TEAL, rx=6)
    d.t(x + 64, y + 118, '10', 14, 600, 'middle', fill='#fff')
    d.t(x + 236, y + 100, 'More every', 13, 600, fill=TEAL)
    d.t(x + 236, y + 118, 'month', 13, 600, fill=TEAL)

    # 3. The switch -------------------------------------------------------------------------------
    x = 750
    stage(d, x, 3, 'The switch', 'When fixed journeys cover most requests, the orchestrator takes what is left. People get what it cannot solve.')
    cx = x + W / 2
    b = box(d, x + 20, 150, W - 40, 'Shadow mode first', 'The orchestrator drafts an answer for each ticket without a journey. The help desk marks every draft: good or not.', 'step')
    down(d, cx, b, b + 26)
    b = box(d, x + 20, b + 26, W - 40, 'Request with no journey', 'One office first, then everyone')
    down(d, cx, b, b + 26)
    b = box(d, x + 20, b + 26, W - 40, 'Orchestrator tries first', 'Uses the agents and their tools', 'agent', 'Large model')
    split(d, cx, b, x + 20 + half / 2, x + W - 20 - half / 2, b + 58, 'Solved', 'Cannot solve')
    yb = b + 58
    box(d, x + 20, yb, half, 'Solved', 'Its answer can become a new journey', 'done')
    box(d, x + W - 20 - half, yb, half, 'A person gets it', 'With the whole story', 'people')

    # Who solves the requests: shares by stage (not to scale) ---------------------------------------
    y = 640
    d.t(20, y, 'Who solves the requests', 17, 600)
    d.t(260, y, 'Not to scale: the real shares come from the pilot', 13, 400, SECOND)
    shares = [[(TEAL, .45), (LIVE, .55)], [(TEAL, .75), (LIVE, .25)], [(TEAL, .78), (ORCH, .12), (LIVE, .10)]]
    for i, parts in enumerate(shares):
        bx, bw, xx = 20 + i * 365, 350, 20 + i * 365
        for col, f in parts:
            d.el.append(f'<rect x="{xx:.0f}" y="{y + 16}" width="{bw * f - 2:.0f}" height="26" rx="5" fill="{col}"/>')
            xx += bw * f
    lx = 20
    for col, name in [(TEAL, 'Fixed journeys'), (ORCH, 'Orchestrator'), (LIVE, 'People')]:
        d.el.append(f'<rect x="{lx}" y="{y + 58}" width="16" height="16" rx="4" fill="{col}"/>')
        d.t(lx + 24, y + 71, name, 13, 600, fill=SECOND)
        lx += 50 + len(name) * 8

    # When to switch, and what changes ------------------------------------------------------------
    y = 740
    d.rect(20, y, 540, 140, '#fff', '#dce4e7', rx=14)
    d.t(40, y + 32, 'Switch when all three are true', 16, 600)
    for i, t in enumerate(['Fixed journeys cover most requests', 'The help desk accepts most of the orchestrator’s drafts',
                           'The orchestrator costs less than people on the same requests']):
        d.mark('ok', 40, y + 48 + i * 28, 20)
        d.t(70, y + 63 + i * 28, t, 14)
    d.rect(580, y, 520, 140, '#fff', '#dce4e7', rx=14)
    d.t(600, y + 32, 'What the switch changes', 16, 600)
    d.t(600, y + 66, 'Before', 13, 600, fill=SECOND)
    d.t(680, y + 66, 'No journey: a ticket for people', 14)
    d.t(600, y + 100, 'After', 13, 600, fill=TEAL)
    d.t(680, y + 100, 'No journey: the orchestrator tries,', 14, 600, fill=TEAL)
    d.t(680, y + 120, 'people get what it cannot solve', 14, 600, fill=TEAL)
    return d

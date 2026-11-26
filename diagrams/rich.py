"""Helpers for the faithful Digital Hub diagrams: zones, cards with logos, avatars, markers."""
import base64
import pathlib
from html import escape
from svg import wrap, INK, LINE, SECOND

A = pathlib.Path(__file__).parent / 'assets'
_cache = {}

# Zone colours from the 2019 slides, softened
Z = {
    'hub': ('#fff6d6', '#e8b500'),       # Digital Hub: yellow
    'bot': ('#f1eaf7', '#8a5fb0'),       # Digital assistant (Avaamo): purple
    'now': ('#e3f3e8', '#3f9a5c'),       # ServiceNow: green
    'agent': ('#fcebe0', '#d9773a'),     # Genesys, live agent: orange
    'r2': ('#eaf0f8', '#3d5f9e'),        # Release 2 data: blue
    'cust': ('#eef5ea', '#9cc48a'),      # Employee data (MVP): light green
    'grey': ('#f2f4f5', '#b7c1c5'),
}


def img(key):
    if key not in _cache:
        _cache[key] = 'data:image/png;base64,' + base64.b64encode((A / f'{key}.png').read_bytes()).decode()
    return _cache[key]


class Rich:
    def __init__(self, uid, w, h, label):
        self.uid, self.W, self.H, self.label, self.el = uid, w, h, label, []
        self.clip = 0

    def t(self, x, y, s, size=14, weight=400, anchor='start', fill=INK, italic=False):
        st = ' font-style="italic"' if italic else ''
        self.el.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="\'Inter\', sans-serif" font-size="{size}" '
                       f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}>{escape(s)}</text>')

    def lines(self, x, y, s, width, size=14, weight=400, fill=INK, lh=None, anchor='start'):
        lh = lh or size + 5
        ls = wrap(s, width, size)
        for i, ln in enumerate(ls):
            self.t(x, y + i * lh, ln, size, weight, anchor, fill)
        return y + len(ls) * lh

    def image(self, key, x, y, s, round_=False, ring=None):
        if round_:
            self.clip += 1
            cid = f'c{self.uid}{self.clip}'
            self.el.append(f'<clipPath id="{cid}"><circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s / 2}"/></clipPath>')
            self.el.append(f'<image href="{img(key)}" x="{x}" y="{y}" width="{s}" height="{s}" '
                           f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})"/>')
            if ring:
                self.el.append(f'<circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s / 2}" fill="none" stroke="{ring}" stroke-width="2"/>')
        else:
            self.el.append(f'<image href="{img(key)}" x="{x}" y="{y}" width="{s}" height="{s}" preserveAspectRatio="xMidYMid meet"/>')

    def logo(self, key, x, y, s=26):
        """Platform logo in a small disc; square logos fill the disc."""
        if key in ('now', 'nexthink', 'avaamo'):
            self.image(key, x, y, s, round_=True)
            return
        self.el.append(f'<circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s / 2}" fill="#fff" stroke="#dce4e7"/>')
        p = s * (0.04 if key in ('ariba', 'genesys') else 0.16)
        self.image(key, x + p, y + p, s - 2 * p)

    def wordmark(self, key, x, y, w, h):
        self.el.append(f'<image href="{img(key)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMinYMid meet"/>')

    def rect(self, x, y, w, h, fill, stroke, dashed=False, rx=10, sw=1.5):
        da = ' stroke-dasharray="7 5"' if dashed else ''
        self.el.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')

    def zone(self, x, y, w, h, title, kind, sub=None):
        fill, stroke = Z[kind]
        self.rect(x, y, w, h, fill, stroke, dashed=True, rx=14)
        self.t(x + 16, y + 28, title, 17, 600)
        if sub:
            self.t(x + 16, y + 48, sub, 13, 400, fill=SECOND)

    def card(self, x, y, w, title=None, items=(), kind=None, fill='#fff', stroke='#dce4e7', size=14, pad=12, logo_size=24, gap=6):
        """items: list of (logo_key or None, text). Returns bottom y."""
        if kind:
            fill = '#fff'
            stroke = Z[kind][1]
        start = len(self.el)
        cy = y + pad
        if title:
            cy = self.lines(x + pad, cy + 15, title, w - 2 * pad, 15, 600) - 15 + 8
        for key, text in items:
            tx = x + pad + (logo_size + 8 if key else 0)
            top = cy
            end = self.lines(tx, cy + 15, text, w - (tx - x) - pad, size, 400, SECOND if title else INK)
            if key:
                self.logo(key, x + pad, top + (end - top) / 2 - 6 - logo_size / 2 + 4, logo_size)
            cy = max(end - 15 + 8, top + logo_size + 6) if key else end - 15 + gap
        h = cy - y + pad - 4
        self.el.insert(start, f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        return y + h

    def mark(self, kind, x, y, s=26):
        self.image('check' if kind == 'ok' else 'alert', x, y, s)

    def arrow(self, *pts, color=LINE, dashed=False, label=None, at=None):
        d = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
        da = ' stroke-dasharray="5 4"' if dashed else ''
        self.el.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" '
                       f'stroke-linejoin="round"{da} marker-end="url(#m{self.uid})"/>')
        if label:
            self.t(at[0], at[1], label, 13, 600, fill=SECOND)

    def svg(self, cls='case-diagram'):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" role="img" '
                f'aria-label="{escape(self.label)}" class="{cls}" width="{self.W}" height="{self.H}">\n'
                f'<defs><marker id="m{self.uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{LINE}"/></marker></defs>\n'
                + '\n'.join(self.el) + '\n</svg>')

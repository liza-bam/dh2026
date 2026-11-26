"""Tiny SVG helpers for the Digital Hub diagrams, in the site's case-diagram style."""
from html import escape

INK = '#223640'
LINE = '#5d6b72'
HAIR = '#dce4e7'
TEAL = '#2c6e7e'
TINT = '#e3eef1'
PANEL = '#f7fafb'
SECOND = '#3f5f6b'

FILL = {'emp': '#fff', 'auto': TINT, 'people': '#fff', 'data': PANEL, 'done': TEAL}
STROKE = {'emp': HAIR, 'auto': TINT, 'people': TEAL, 'data': HAIR, 'done': TEAL}


def wrap(s, width, size):
    per = max(8, int(width / (size * 0.53)))
    out, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > per:
            out.append(cur)
            cur = w
        else:
            cur = f'{cur} {w}'.strip()
    if cur:
        out.append(cur)
    return out


class Box:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    @property
    def cx(self): return self.x + self.w / 2

    @property
    def cy(self): return self.y + self.h / 2

    @property
    def r(self): return self.x + self.w

    @property
    def b(self): return self.y + self.h


class Diagram:
    def __init__(self, uid, width, height, label):
        self.uid, self.W, self.H, self.label = uid, width, height, label
        self.el = []

    def text(self, x, y, s, size=14, weight=400, anchor='start', fill=INK, italic=False):
        st = ' font-style="italic"' if italic else ''
        self.el.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="\'Inter\', sans-serif" font-size="{size}" '
                       f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}>{escape(s)}</text>')

    @staticmethod
    def measure(w, title=None, lines=(), size=14):
        tlines = wrap(title, w - 24, 15) if title else []
        blines = []
        for ln in lines:
            blines += wrap(ln, w - 24, size)
        return tlines, blines, 14 + len(tlines) * 20 + (6 if tlines and blines else 0) + len(blines) * 19 + 10

    def box(self, x, y, w, title=None, lines=(), kind='emp', h=None, size=14):
        tlines, blines, need = self.measure(w, title, lines, size)
        h = h or need
        sw = 2 if kind == 'people' else 1.5
        self.el.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="8" fill="{FILL[kind]}" '
                       f'stroke="{STROKE[kind]}" stroke-width="{sw}"/>')
        col = '#fff' if kind == 'done' else INK
        ty = y + 26
        for t in tlines:
            self.text(x + 12, ty, t, 15, 600, fill=col)
            ty += 20
        if tlines and blines:
            ty += 6
        for t in blines:
            self.text(x + 12, ty - 1, t, size, 400, fill=col if kind == 'done' else SECOND)
            ty += 19
        return Box(x, y, w, h)

    def group(self, x, y, w, h, label, right=False):
        self.el.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" '
                       f'stroke="{HAIR}" stroke-width="1.5" stroke-dasharray="6 5"/>')
        if right:
            self.text(x + 14, y + h - 14, label, 13, 600, fill=TEAL)
        else:
            self.text(x + 14, y + 24, label, 13, 600, fill=TEAL)
        return Box(x, y, w, h)

    def diamond(self, cx, cy, s, w=168, h=92):
        pts = f'{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}'
        self.el.append(f'<polygon points="{pts}" fill="#fff" stroke="{TEAL}" stroke-width="2"/>')
        ls = wrap(s, w * 0.62, 14)
        y0 = cy - (len(ls) - 1) * 9 + 5
        for i, t in enumerate(ls):
            self.text(cx, y0 + i * 18, t, 14, 600, 'middle')
        return Box(cx - w / 2, cy - h / 2, w, h)

    def arrow(self, *pts, label=None, at=None, dashed=False):
        d = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
        da = ' stroke-dasharray="5 4"' if dashed else ''
        self.el.append(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.5" stroke-linecap="round" '
                       f'stroke-linejoin="round"{da} marker-end="url(#m{self.uid})"/>')
        if label:
            x, y = at if at else ((pts[0][0] + pts[1][0]) / 2 + 6, (pts[0][1] + pts[1][1]) / 2 - 6)
            self.text(x, y, label, 13, 600, fill=TEAL)

    def svg(self):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" role="img" '
                f'aria-label="{escape(self.label)}" class="case-diagram">\n'
                f'<defs><marker id="m{self.uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{LINE}"/></marker></defs>\n')
        return head + '\n'.join(self.el) + '\n</svg>'

"""Renders the case study (case/case.md) and the technical document (case/technical.md) as readable pages."""
import pathlib
import re
from html import escape
import markdown
import transition as t26
from build_doc import D19, D26

FIGS = {i: (t, sub, f) for i, t, sub, f in D19 + D26}
FIGS['D26-4'] = ('The 10 scenarios', 'Who does the work now, and when a person steps in',
                 lambda: '<div class="grid">' + ''.join(t26.scenario_card(n, *sc).svg() for n, sc in enumerate(t26.SCEN)) + '</div>')


def figure(i):
    t, sub, f = FIGS[i]
    out = f()
    svg = out if isinstance(out, str) else out.svg()
    return (f'<figure class="fig" id="{i}"><figcaption><b><span class="fid">{i}</span>{escape(t)}</b>'
            f'<span>{escape(sub)}</span></figcaption>{svg}</figure>')


def with_figures(html):
    """After every paragraph that names diagrams like [D26-7], show those diagrams."""
    def add(m):
        ids = [i for i in re.findall(r'\[(D\d\d-\d+)\]', m.group(0)) if i in FIGS]
        figs = ''.join(figure(i) for i in ids)
        # A line that only names diagrams ("Visual: [D26-2] ...") is replaced by the diagrams themselves
        return figs if ids and m.group(0).startswith(('<p>Visual:', '<p>Visuals:')) else m.group(0) + figs
    return re.sub(r'<p>.*?</p>', add, html, flags=re.S)


ROOT = pathlib.Path(__file__).parent.parent
for name, title in [('case', 'Digital Hub 2026: case draft'), ('technical', 'Digital Hub 2026: technical document')]:
  md = (ROOT / 'case' / f'{name}.md').read_text()
  body = with_figures(markdown.markdown(md, extensions=['extra', 'sane_lists']))
  html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600&amp;family=Inter:ital,wght@0,400;0,600;1,400&amp;display=swap" rel="stylesheet"/>
<style>
/* VOICE calm working draft; IDEA the case page itself; PICTURE none, text only;
   COLOUR portfolio slate ink and teal on white; TYPE Inter Tight titles, Inter body; LAYOUT one reading column */
:root{{color-scheme:light dark;--bg:light-dark(#fff,#10191e);--ink:light-dark(#223640,#e6eef1);--teal:light-dark(#2c6e7e,#7cc2d2);--rule:light-dark(#dce4e7,#2a3a42);--panel:light-dark(#f7fafb,#16232a)}}
:root[data-theme=light]{{color-scheme:light}}:root[data-theme=dark]{{color-scheme:dark}}
*{{box-sizing:border-box;min-width:0}}
body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 Inter,system-ui,sans-serif;overflow-x:clip}}
main{{max-width:760px;margin:0 auto;padding:clamp(28px,5vw,64px) max(5vw,16px)}}
h1{{font:600 clamp(36px,6vw,52px)/1.05 'Inter Tight',sans-serif;letter-spacing:-.035em;margin:0 0 16px;text-wrap:balance}}
h2{{font:600 30px/1.15 'Inter Tight',sans-serif;letter-spacing:-.025em;margin:56px 0 16px;padding-top:24px;border-top:1px solid var(--rule)}}
h3{{font:600 21px/1.3 'Inter Tight',sans-serif;margin:32px 0 8px}}
p,li{{max-width:70ch}}ul{{padding-left:22px}}li{{margin:4px 0}}
strong{{font-weight:600}}hr{{border:0;border-top:1px solid var(--rule);margin:32px 0}}
code{{font-size:15px;background:var(--panel);padding:2px 6px;border-radius:4px}}
/* Diagrams sit wider than the text column, on white in both themes */
.fig{{width:min(1120px,calc(100vw - 32px));position:relative;left:50%;transform:translateX(-50%);margin:24px 0 40px;padding:16px;background:#fff;border:1px solid var(--rule);border-radius:8px;color:#223640}}
.fig figcaption{{margin:0 0 12px}}.fig figcaption b{{display:block;font:600 20px/1.3 'Inter Tight',sans-serif}}.fig figcaption span{{display:block;font-size:15px;color:#3f5f6b}}
.fig .fid{{display:inline-block;font:600 13px/1 Inter,sans-serif;color:#fff;background:#2c6e7e;border-radius:6px;padding:5px 7px;margin:0 8px 0 0;vertical-align:3px}}
.fig svg{{display:block;width:100%;height:auto}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
@media (max-width:700px){{.grid{{grid-template-columns:1fr}}}}
small{{font-size:13px;color:light-dark(#3f5f6b,#a9bcc3)}}
</style></head><body><main>{body}</main></body></html>'''
  (ROOT / 'case' / f'{name}.html').write_text(html)
print('ok')

"""Renders case/case.md as a readable page: case/case.html."""
import pathlib
import markdown

ROOT = pathlib.Path(__file__).parent.parent
md = (ROOT / 'case' / 'case.md').read_text()
body = markdown.markdown(md, extensions=['extra', 'sane_lists'])
html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Digital Hub 2026: case draft</title>
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
</style></head><body><main>{body}</main></body></html>'''
(ROOT / 'case' / 'case.html').write_text(html)
print('ok')

"""Builds the scenario flows document: case/flows.html. The scenario cards are its table of contents."""
import pathlib
from html import escape
import transition as t26
from build_doc import FLOWS, fig

HERE = pathlib.Path(__file__).parent


def main():
    css = (HERE / 'page.css').read_text() + '''
.pano{overflow-x:auto;overscroll-behavior-x:contain}.pano .case-diagram{width:auto;max-width:none;height:auto}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}.grid .case-diagram{width:100%;height:auto}
@media (max-width:900px){.grid{grid-template-columns:1fr}}
.figure-caption .fid{display:inline-block;font:600 14px/1 Inter,sans-serif;color:#fff;background:#2c6e7e;border-radius:6px;padding:6px 8px;margin:0 8px 0 0;vertical-align:4px}
h2{font:600 34px/1.15 'Inter Tight',sans-serif;letter-spacing:-.025em;margin:56px 0 24px}
.flowlink{margin:6px 0 0;font-size:15px}.flowlink a{color:#2c6e7e;font-weight:600}.flowlink.muted{color:#5f7480}'''

    def link(n):
        if n in FLOWS:
            return f'<p class="flowlink"><a href="#{FLOWS[n][0]}">Open the flow ({FLOWS[n][0]})</a></p>'
        return '<p class="flowlink muted">Flow: to draw</p>'
    cards = ''.join(f'<div>{t26.scenario_card(n, *sc).svg()}{link(n)}</div>' for n, sc in enumerate(t26.SCEN))
    flows = '\n'.join(fig(fid, t, sub, f().svg(), wide=False) for fid, t, sub, f in FLOWS.values())
    # the full one-row version, kept for a later pop-up
    large = HERE.parent / 'case' / 'large'
    large.mkdir(exist_ok=True)
    for fid, t, sub, f in FLOWS.values():
        (large / f'{fid}.svg').write_text(f(rows=None).svg())
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Digital Hub 2026: scenario flows</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600&amp;family=Inter:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet"/>
<style>{css}</style></head><body><main style="max-width:1760px">
<h1>Digital Hub 2026: scenario flows</h1>
<p class="sub">The ten scenarios as cards, and the full flow behind each one.</p>
<h2>The 10 scenarios</h2><div class="grid">{cards}</div>
<h2>Flows</h2>
{flows}
</main></body></html>'''
    (HERE.parent / 'case' / 'flows.html').write_text(html)
    print('ok', len(html) // 1024, 'KB')


if __name__ == '__main__':
    main()

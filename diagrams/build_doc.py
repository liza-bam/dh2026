"""Builds the single diagrams document: case/diagrams.html. Every diagram has a fixed ID the case text refers to."""
import pathlib
from html import escape
import d_first_contact, d_solving, d_requests, d_status, d_proactive, d_refresh, d_transfer, d_scenarios
import transition as t26
import arch26
import modules26

D19 = [
    ('D19-1', 'First contact', 'From any channel to the right person, with the employee’s data all the way', d_first_contact.build),
    ('D19-2', 'Solving issues', 'Prevention, self-help and AI scripts first; a ticket, triage and a live agent for what is left', d_solving.build),
    ('D19-3', 'Handling requests', 'Requests go through the assistant or self-help; approvals follow the structure in Workday', d_requests.build),
    ('D19-4', 'Checking status and gathering feedback', 'Ticket updates reach the employee, and every contact feeds one sentiment picture', d_status.build),
    ('D19-5', 'Preventive and proactive support', 'Problems are fixed before anyone reports them; manual fixes become new scripts', d_proactive.build),
    ('D19-6', 'Refresh readiness', 'Live data and existing records decide who gets a new laptop, when, and who needs extra care', d_refresh.build),
    ('D19-7', 'Data transfer', 'The transfer agent moves the data while the employee keeps working', d_transfer.build),
    ('D19-8', 'Scenario: password reset', 'Help at the point of need, on the phone and on the Windows lock screen', d_scenarios.password),
    ('D19-9', 'Scenario: meeting room', 'The room is changed before the meeting is lost; the bot and a live agent step in when needed', d_scenarios.meeting_room),
    ('D19-10', 'Scenario: VPN access offsite', 'The error is found before the employee calls, with the likely cause and a short lesson', d_scenarios.vpn),
]

D26 = [
    ('D26-1', 'What changes', 'The same service, journeys and data; agents take the work that had to be written in advance', lambda: t26.what_changes()),
    ('D26-2', 'Architecture', 'Eight layers: one front door that changes nothing, specialized agents with limited rights, enterprise agents, approved knowledge, systems, governance and people', arch26.build),
    ('D26-5', 'Module map', 'Shared modules, designed once: every scenario is built from the same parts, so the same task always looks the same', modules26.build),
    ('D26-3', 'Handoff, confirmation and the target', 'A person gets the whole story, risky actions wait for a yes, success counts only when the case stays solved', lambda: t26.handoff()),
]


def fig(i, title, sub, svg, wide=True):
    return (f'<figure class="figure-panel" id="{i}"><figcaption class="figure-caption"><div>'
            f'<div class="figure-title"><span class="fid">{i}</span> {escape(title)}</div><span>{escape(sub)}</span></div></figcaption>'
            f'<div class="{"pano" if wide else ""}" tabindex="0">{svg}</div></figure>')


def main():
    css = (pathlib.Path(__file__).parent / 'page.css').read_text() + '''
.pano{overflow-x:auto;overscroll-behavior-x:contain}.pano .case-diagram{width:auto;max-width:none;height:auto}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}.grid .case-diagram{width:100%;height:auto}
@media (max-width:900px){.grid{grid-template-columns:1fr}}
.figure-caption .fid{display:inline-block;font:600 14px/1 Inter,sans-serif;color:#fff;background:#2c6e7e;border-radius:6px;padding:6px 8px;margin:0 8px 0 0;vertical-align:4px}
h2{font:600 34px/1.15 'Inter Tight',sans-serif;letter-spacing:-.025em;margin:56px 0 24px}
.toc{columns:2}'''
    toc19 = ''.join(f'<li><a href="#{i}">{i} {escape(t)}</a></li>' for i, t, _, _ in D19)
    toc26 = ''.join(f'<li><a href="#{i}">{i} {escape(t)}</a></li>' for i, t, _, _ in D26) + '<li><a href="#D26-4">D26-4 The 10 scenarios</a></li>'
    body19 = '\n'.join(fig(i, t, s, f().svg()) for i, t, s, f in D19)
    body26 = '\n'.join(fig(i, t, s, f().svg(), i != 'D26-3') for i, t, s, f in D26)
    cards = ''.join(f'<div>{t26.scenario_card(n, *sc).svg()}</div>' for n, sc in enumerate(t26.SCEN))
    body26 += ('<figure class="figure-panel" id="D26-4"><figcaption class="figure-caption"><div><div class="figure-title"><span class="fid">D26-4</span> The 10 scenarios</div>'
               '<span>Who does the work now, and when a person steps in</span></div></figcaption>'
               f'<div class="grid">{cards}</div></figure>')
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Digital Hub diagrams · Sandy Tayts</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600&amp;family=Inter:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet"/>
<style>{css}</style></head><body><main style="max-width:1760px">
<h1>Digital Hub: diagrams</h1>
<p class="sub">Every diagram for the case, with the ID the case text uses.</p>
<h2>2019: the brief</h2><ol class="toc" style="list-style:none;padding:0">{toc19}</ol>
<h2>2026: agents</h2><ol class="toc" style="list-style:none;padding:0">{toc26}</ol>
<h2>2019: the brief</h2>
{body19}
<h2>2026: agents</h2>
{body26}
</main></body></html>'''
    out = pathlib.Path(__file__).parent.parent / 'case' / 'diagrams.html'
    out.write_text(html)
    print('ok', len(html) // 1024, 'KB')


if __name__ == '__main__':
    main()

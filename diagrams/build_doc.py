"""Builds the single diagrams document: case/diagrams.html. Every diagram has a fixed ID the case text refers to."""
import pathlib
from html import escape
import d_first_contact, d_solving, d_requests, d_status, d_proactive, d_refresh, d_transfer, d_scenarios
import transition as t26
import arch26
import modules26
import flows26
import delivery26
import scorecard26

# In the artifact viewer, #links need a script to scroll inside the page
LINK_JS = """<script>(function(){function go(id){var t=id&&document.getElementById(decodeURIComponent(id));if(t)t.scrollIntoView();}
window.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;e.preventDefault();var id=a.getAttribute('href').slice(1);go(id);try{history.replaceState(null,'','#'+id)}catch(_){}},true);
window.addEventListener('hashchange',function(){go(location.hash.slice(1))});
window.addEventListener('load',function(){go(location.hash.slice(1))});})();</script>"""
FLOWS_URL = 'https://claude.ai/artifact/X1kuj4G3xAcsWb86NmQACZ'
FLOWS = {9: ('D26-F10', 'Flow: failed software install', 'The full flow behind scenario 10: what the employee sees, which agent acts, the two fixes, the handover to live support, the new fix an engineer approves', flows26.failed_install)}

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
    ('D26-2', 'Architecture', 'Eight layers: an intake agent, an orchestrator after the switch, specialized agents with limited rights, enterprise agents, approved knowledge, systems, governance and people', arch26.build),
    ('D26-7', 'Delivery plan', 'Ten fixed journeys first, more journeys every week from what people ask, then the orchestrator takes what has no journey', delivery26.build),
    ('D26-6', 'Stack scorecard', 'Every platform from 2019 checked against the six questions: eight stay, two go', scorecard26.build),
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
.toc{columns:2}
.flowlink{margin:6px 0 0;font-size:15px}.flowlink a{color:#2c6e7e;font-weight:600}.flowlink.muted{color:#5f7480}'''
    toc19 = ''.join(f'<li><a href="#{i}">{i} {escape(t)}</a></li>' for i, t, _, _ in D19)
    toc26 = ''.join(f'<li><a href="#{i}">{i} {escape(t)}</a></li>' for i, t, _, _ in D26) + '<li><a href="#D26-4">D26-4 The 10 scenarios</a></li>'
    body19 = '\n'.join(fig(i, t, s, f().svg()) for i, t, s, f in D19)
    body26 = '\n'.join(fig(i, t, s, f().svg(), i not in ('D26-3', 'D26-6', 'D26-7')) for i, t, s, f in D26)
    def link(n):
        if n in FLOWS:
            fid = FLOWS[n][0]
            return f'<p class="flowlink"><a href="{FLOWS_URL}#{fid}" target="_blank" rel="noopener">Open the flow ({fid})</a></p>'
        return '<p class="flowlink muted">Flow: to draw</p>'
    cards = ''.join(f'<div>{t26.scenario_card(n, *sc).svg()}{link(n)}</div>' for n, sc in enumerate(t26.SCEN))
    body26 += ('<figure class="figure-panel" id="D26-4"><figcaption class="figure-caption"><div><div class="figure-title"><span class="fid">D26-4</span> The 10 scenarios</div>'
               '<span>Every case starts at the intake agent and goes to one of our agents; enterprise agents help where they hold the data; live support (routed through Genesys) joins only when it is needed</span></div></figcaption>'
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
</main>{LINK_JS}</body></html>'''
    out = pathlib.Path(__file__).parent.parent / 'case' / 'diagrams.html'
    out.write_text(html)
    print('ok', len(html) // 1024, 'KB')


if __name__ == '__main__':
    main()

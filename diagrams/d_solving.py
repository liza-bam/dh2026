"""2. Solving issues, end to end (slide 'Solving Issues End to End')."""
from rich import Rich, Z
from svg import SECOND
from d_common import live_agent, r2_side, legend, decision

G = '#9aa5aa'


def build():
    d = Rich('si', 1800, 930, 'Solving issues end to end: preventive measures, proactive automation, digital assistant, '
             'ServiceNow ticket, AI triage and live agent session')

    # Preventive measures ---------------------------------------------------------
    d.zone(20, 20, 270, 330, 'Preventive measures', 'grey')
    y = d.card(32, 52, 246, 'Monitor in real time', [(None, 'Client side: OS, software, hardware'), (None, 'Server side'),
                                                   (None, 'Correlate irregular devices and anomalies')])
    y = d.card(32, y + 10, 246, 'Run AI scripts to self-heal issues', [(None, 'Script library built in discovery')])
    d.logo('nexthink', 40, y + 10, 44)
    d.wordmark('holmes', 92, y + 16, 110, 30)
    d.mark('ok', 304, 40)
    d.arrow((290, 54), (302, 54), color=G)

    # Existing issues ---------------------------------------------------------------
    d.zone(20, 560, 270, 350, 'Existing issues', 'grey', 'Employees report a problem')
    for i in range(4):
        d.image(f'cust{i + 2}', 40, 620 + i * 66, 50, round_=True, ring='#b7c1c5')
    for i, k in enumerate(['outlook', 'teams']):
        d.image(k, 130, 640 + i * 80, 40)
    d.rect(120, 810, 84, 40, '#f5c000', '#f5c000', rx=20)
    d.t(162, 835, 'DIGITAL HUB', 11, 700, 'middle')

    # First decision ------------------------------------------------------------------
    decision(d, 360, 470, 'If the issue is not solved')
    d.arrow((150, 350), (150, 470), (312, 470), color=G)
    d.arrow((360, 422), (360, 120), (440, 120), color=G)
    d.lines(300, 150, 'Automation-ready issues', 70, 13, 600, fill=SECOND)
    d.mark('alert', 400, 92, 24)
    d.arrow((408, 470), (440, 470), color=G)
    d.lines(300, 380, 'Self-help ready issues', 70, 13, 600, fill=SECOND)
    d.mark('alert', 412, 440, 22)
    d.arrow((360, 518), (360, 830), (870, 830), color=G)
    d.t(860, 822, 'Other cases', 13, 600, 'end', fill=SECOND)
    d.mark('alert', 370, 700, 24)
    d.arrow((290, 860), (870, 860), color=G)
    d.t(860, 852, 'Manually added issues', 13, 600, 'end', fill=SECOND)
    d.arrow((290, 895), (1085, 895), (1085, 800), (1100, 800), color=G)

    # Proactive automation ------------------------------------------------------------
    d.zone(440, 20, 340, 230, 'Proactive automation', 'grey', 'Common issues')
    y = d.card(452, 64, 316, 'Run AI scripts to fix issues', [(None, 'Script library built in discovery. Samples: VPN and files on the EY network offsite, client files in Canvas, failed install, installing a new version, disk clean-up'),
                                                               (None, 'More use cases in release 2')])
    d.logo('nexthink', 722, 206, 38)
    d.image('software', 660, 202, 44)
    d.mark('ok', 796, 40)
    d.arrow((780, 54), (794, 54), color=G)

    # Digital assistant ------------------------------------------------------------------
    d.zone(440, 270, 340, 530, 'Digital assistant (voice and chat)', 'bot', 'Avaamo bot')
    d.rect(452, 330, 316, 116, '#fff', Z['bot'][1], rx=8)
    d.t(464, 352, 'NLP self-help library', 15, 600)
    d.t(464, 370, 'Top incidents and service requests', 13, 400, fill=SECOND)
    for i, (ic, n) in enumerate([('outlook', 'Outlook'), (None, 'Browser'), (None, 'Antivirus'), ('azure', 'OS, AD')]):
        cx = 470 + i * 76
        if ic:
            d.image(ic, cx + 10, 380, 26)
        else:
            d.el.append(f'<circle cx="{cx + 23}" cy="393" r="12" fill="{Z["bot"][0]}" stroke="{Z["bot"][1]}"/>')
        d.t(cx + 23, 422, n, 12, 600, 'middle')
        d.t(cx + 23, 437, '10 cases', 12, 400, 'middle', fill=SECOND)
    y = d.card(452, 458, 316, '10 common scenarios plus the 10 top call drivers', [(None, s) for s in [
        'Working remotely from an office meeting room', 'VPN: files on the EY network offsite', 'Password reset',
        'Access to a Teams channel', 'Reporting a lost laptop', 'Client files in the Canvas app',
        'Outlook access for a new assistant', 'Ordering a peripheral', 'Reporting an email scam', 'Failed software installation']],
        kind='bot', size=13, gap=1)
    d.card(452, y + 10, 316, 'How-to videos for the common scenarios', [], kind='bot')
    d.mark('ok', 796, 276)
    d.arrow((780, 290), (794, 290), color=G)
    decision(d, 822, 560, 'If not solved', r=34)
    d.arrow((856, 560), (870, 560), color=G)

    # ServiceNow ticket -------------------------------------------------------------------
    d.zone(870, 260, 200, 620, 'ServiceNow ticket', 'now')
    y = 304
    for t in ['Automatic issue creation', 'Manual issue creation']:
        d.rect(882, y, 176, 36, Z['now'][1], Z['now'][1], rx=6)
        d.t(970, y + 23, t, 13, 600, 'middle', fill='#fff')
        y += 44
    y = d.card(882, y + 4, 176, 'Initial customer data', [(None, 'Service line, title, location, calendar, environment, hardware and software, issue status and history')], kind='now', size=13)
    y = d.card(882, y + 8, 176, 'Session data', [(None, 'Timing, sentiment')], kind='now', size=13)
    y = d.card(882, y + 8, 176, 'Issue data', [(None, 'Environment, steps taken, results, errors')], kind='now', size=13)
    d.logo('now', 946, y + 10, 48)

    # AI issue triage ---------------------------------------------------------------------
    d.zone(1100, 360, 180, 280, 'AI issue triage', 'bot')
    for i, t in enumerate(['Urgency', 'Strong sentiment', 'Discovery metrics']):
        d.rect(1112, 400 + i * 52, 156, 42, Z['bot'][0], Z['bot'][1], rx=6)
        d.t(1190, 426 + i * 52, t, 13, 600, 'middle')
    d.logo('avaamo', 1166, 564, 48)
    d.arrow((1070, 500), (1100, 500), color=G)

    # Resolution and handoffs ------------------------------------------------------------------
    d.rect(1100, 250, 180, 56, '#fff', Z['agent'][1], dashed=True, rx=8)
    d.t(1190, 284, 'Issue resolution', 15, 600, 'middle')
    d.mark('ok', 1296, 264)
    d.arrow((1190, 360), (1190, 306), color=G)
    d.arrow((1280, 278), (1294, 278), color=G)
    d.rect(1100, 120, 180, 100, Z['agent'][0], Z['agent'][1], dashed=True, rx=8)
    d.image('cust7', 1110, 140, 50, round_=True, ring='#b7c1c5')
    d.lines(1170, 156, 'Live session booked if needed', 100, 14, 600)
    d.logo('office', 1242, 186, 28)
    d.arrow((1190, 250), (1190, 220), color=G)
    d.rect(1100, 670, 180, 64, Z['agent'][0], Z['agent'][1], dashed=True, rx=8)
    d.logo('avaamo', 1110, 684, 36)
    d.lines(1154, 698, 'Automatic agent handoff', 116, 14, 600)
    d.arrow((1190, 640), (1190, 670), color=G)
    d.rect(1100, 760, 180, 60, Z['agent'][0], Z['agent'][1], dashed=True, rx=8)
    d.image('cust8', 1108, 766, 46, round_=True, ring='#b7c1c5')
    d.lines(1162, 784, 'Employee asks for an agent', 110, 14, 600)
    d.arrow((1280, 702), (1300, 702), (1300, 400), (1320, 400), color=G)
    d.arrow((1280, 790), (1300, 790), (1300, 702), color=G)
    

    # Live agent ---------------------------------------------------------------------------------
    live_agent(d, 1320, 60, 200)
    d.mark('ok', 1530, 66)
    r2_side(d, 1570, 80, 210)
    legend(d, 1320, 720)
    return d

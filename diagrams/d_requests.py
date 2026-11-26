"""3. Handling requests, end to end (slide 'Handling Requests End To End')."""
from rich import Rich, Z
from svg import SECOND
from d_common import employees, employee_data, legend

G = '#9aa5aa'
OK = '#3d8b2f'


def build():
    d = Rich('hr', 1400, 1020, 'Handling requests end to end: employees and their data, digital assistant, Digital Hub applications, '
             'ServiceNow with hardware catalogue and approval structure, help desk')
    d.zone(20, 20, 400, 740, 'Employees', 'grey', 'Hardware and software requests')
    employees(d, 36, 78)
    employee_data(d, 112, 78)

    # Digital assistant (release 2) ------------------------------------------------
    d.zone(470, 20, 380, 320, 'Digital assistant (voice and chat)', 'bot', 'Release 2')
    y = 70
    for t in ['Software and hardware requests raised through the AI bot', 'Hardware bundles, proactive order suggestions',
              'How-to videos for the common scenarios', 'Conversational AI assistant for common software and hardware requests']:
        y = d.card(482, y, 356, None, [(None, t)], fill='#fff', stroke=Z['bot'][1]) + 10
    d.arrow((420, 140), (470, 140), color=G)

    # Digital Hub applications ------------------------------------------------------
    d.zone(470, 360, 380, 390, 'Digital Hub applications', 'hub', 'Self-help for the main support drivers')
    rows = [(['ariba', 'digilocker'], 'hardware', 'Hardware request'), ([], 'ticket', 'Ticket status'),
            (['ariba', 'digilocker'], 'mouse', 'Order a peripheral'), (['now'], 'software', 'Software requests')]
    for i, (logos, icon, name) in enumerate(rows):
        ry = 426 + i * 44
        for k, lg in enumerate(reversed(logos)):
            d.logo(lg, 590 - k * 36, ry - 2, 32)
        d.image(icon, 636, ry, 28)
        d.t(676, ry + 19, name, 15)
    d.t(486, 630, 'Additional features', 14, 600, fill=SECOND)
    d.logo('sharepoint', 590, 644, 32)
    d.image('search', 636, 646, 28)
    d.t(676, 665, 'Search in Digital Hub', 15)
    d.logo('workday', 554, 688, 32)
    d.logo('now', 590, 688, 32)
    d.image('approve', 636, 690, 28)
    d.t(676, 709, 'IT request approvals', 15, 600)
    d.arrow((420, 520), (470, 520), color=G)

    # ServiceNow --------------------------------------------------------------------------
    d.el.append(f'<path d="M866 40 Q880 40 880 60 L880 440 Q880 460 894 460 Q880 460 880 480 L880 670 Q880 690 866 690" fill="none" stroke="#223640" stroke-width="2"/>')
    d.zone(920, 300, 260, 500, 'Create a ServiceNow ticket', 'now')
    y = d.card(934, 346, 232, 'Initial customer data: MVP', [(None, 'Service line, title, location, calendar, environment, hardware and software, request status and history')], kind='now', size=13)
    y = d.card(934, y + 12, 232, None, [('ariba', 'Hardware catalogue')], kind='now', logo_size=36)
    y = d.card(934, y + 12, 232, None, [('workday', 'Approval structure')], kind='now', logo_size=36)
    d.logo('now', 950, y + 16, 56)
    d.logo('workday', 1016, y + 16, 56)
    d.arrow((894, 460), (920, 460), color=G)

    # Outcomes -----------------------------------------------------------------------------
    d.arrow((1180, 400), (1206, 400), color=G)
    d.mark('ok', 1210, 386, 30)
    d.lines(1250, 396, 'Automatic approval. Request handled', 140, 15, 600, fill=OK)
    d.arrow((920, 704), (850, 704), color=G)
    d.lines(858, 724, 'Manual approval needed', 60, 13, 600, fill=SECOND)
    d.mark('ok', 600, 770, 30)
    d.arrow((680, 750), (680, 785), (636, 785), color=G)
    d.lines(470, 782, 'Manual approvals. Request handled', 120, 15, 600, fill=OK)

    # Help desk -------------------------------------------------------------------------------
    d.mark('alert', 740, 770, 28)
    d.lines(776, 784, 'Every channel’s information goes to the SME agent', 150, 14, 600)
    d.arrow((760, 750), (760, 768), color=G)
    d.zone(700, 840, 440, 160, 'Help desk', 'agent')
    d.card(714, 876, 190, 'Unified channel', [(None, 'Video chat, screen share, voice, chat')], kind='agent', size=13)
    d.card(914, 876, 212, 'Personalized dashboard', [(None, 'Request, employee, sentiment, session, history and approval data')], kind='agent', size=13)
    d.logo('avaamo', 1150, 870, 40)
    d.wordmark('genesys', 1150, 916, 90, 30)
    for i in range(3):
        d.image(f'agent{i + 1}', 1250 + i * 46, 860, 42, round_=True, ring=Z['agent'][1])
    d.mark('ok', 1250, 914, 28)
    d.lines(1286, 928, 'Approval with an expert. Request handled', 110, 13, 600, fill=OK)
    legend(d, 1200, 620)
    return d

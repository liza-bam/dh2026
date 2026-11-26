"""1. First contact, end to end (slide 'First contact End to End')."""
from rich import Rich, Z
from svg import SECOND, TEAL


def build():
    d = Rich('fc', 1640, 910, 'First contact end to end: employees and their data, Digital Hub channels, '
             'Digital Hub applications, digital assistant, Genesys agent dashboard and live agent session')

    # Employees and their data --------------------------------------------------
    d.zone(20, 20, 400, 720, 'Employees', 'grey', 'Every channel already knows who is asking')
    for i in range(8):
        d.image(f'cust{i + 1}', 36, 78 + i * 74, 60, round_=True, ring='#b7c1c5')
    y = d.card(112, 78, 292, 'Initial customer data: MVP', [
        ('workday', 'Service line, title, location'), ('office', 'Calendar'),
        ('nexthink', 'Environment: OS, connection'), ('now', 'Hardware and software'),
        ('now', 'Issue and request status'), ('now', 'Issue and request history')], kind='cust')
    d.t(112, y + 30, 'Release 2', 14, 600, fill=Z['r2'][1])
    y = d.card(112, y + 42, 292, 'Customer hyper-personalization', [
        ('now', 'Behavior, preferred contact channel, preferred schedule, technical aptitude')], kind='r2')
    y = d.card(112, y + 12, 292, 'Customer sentiment', [(None, 'Sentiment history and analysis')], kind='r2')
    y = d.card(112, y + 12, 292, 'Customer localization', [(None, 'Fully localized support and UI in 5 languages')], kind='r2')

    # Digital Hub: four channels ----------------------------------------------------
    hx, hy, hw = 470, 120, 190
    d.rect(hx, hy, hw, 560, '#223640', '#223640', rx=22)
    d.rect(hx + 10, hy + 14, hw - 20, 40, '#f5c000', '#f5c000', rx=8)
    d.t(hx + hw / 2, hy + 40, 'DIGITAL HUB', 15, 700, 'middle')
    tiles = []
    for i, (icon, name) in enumerate([('email', 'Support email'), (None, 'Applications'), ('chat', 'Support chat'), ('voice', 'Support voice')]):
        ty = hy + 68 + i * 120
        d.rect(hx + 10, ty, hw - 20, 108, '#fff', '#fff', rx=8)
        if icon:
            d.image(icon, hx + hw / 2 - 24, ty + 12, 48)
        else:
            for k in range(3):
                d.el.append(f'<circle cx="{hx + hw / 2 - 30 + k * 30}" cy="{ty + 36}" r="13" fill="#f5c000"/>')
        d.t(hx + hw / 2, ty + 88, name, 15, 600, 'middle')
        tiles.append(ty + 54)
    # entry points outside the app
    for (key, name), ty in zip([('outlook', 'Outlook'), (None, None), ('teams', 'Teams'), ('phone', 'Phone')], tiles):
        if key:
            d.image(key, 430, ty - 44, 28)
    for ty in tiles:
        d.arrow((420, ty), (hx, ty), color='#6aa84f')

    # Email to ServiceNow -------------------------------------------------------------
    d.rect(700, 20, 470, 58, '#e8eef8', '#e8eef8', rx=8)
    d.image('outlook', 712, 33, 30)
    d.lines(752, 44, 'Email goes to the ServiceNow group for the employee’s location, with all their data', 400, 14, 600)
    d.logo('now', 1190, 22, 54)
    d.arrow((hx + hw, tiles[0]), (680, tiles[0]), (680, 49), (700, 49), color='#2f6fc0')
    d.arrow((1170, 49), (1190, 49), color='#2f6fc0')

    # Digital Hub applications ----------------------------------------------------------
    d.zone(700, 100, 470, 360, 'Digital Hub applications', 'hub', 'Self-help for the main support drivers')
    rows = [(['now'], 'ticket', 'Raise an issue'), (['ariba', 'digilocker', 'now'], 'hardware', 'Raise a hardware request'),
            (['azure'], 'lock', 'Reset password'), (['office'], 'room', 'Book or change a room'),
            (['now'], 'software', 'Software request'), (['wvd'], 'vdi', 'VDI catalogue, automated setup')]
    for i, (logos, icon, name) in enumerate(rows):
        ry = 160 + i * 38
        for k, lg in enumerate(reversed(logos)):
            d.logo(lg, 860 - k * 30, ry, 26)
        d.image(icon, 898, ry, 26)
        d.t(936, ry + 18, name, 14, 400)
    d.t(716, 408, 'Additional features', 14, 600, fill=SECOND)
    for i, (logos, icon, name) in enumerate([(['sharepoint'], 'search', 'Search in Digital Hub'), (['workday', 'now'], 'approve', 'IT request approvals')]):
        ry = 418 + i * 0
        x0 = 716 + i * 230
        for k, lg in enumerate(logos):
            d.logo(lg, x0 + k * 30, ry, 26)
        d.image(icon, x0 + len(logos) * 30 + 4, ry, 26)
        d.t(x0 + len(logos) * 30 + 38, ry + 18, name, 14, 400)
    d.arrow((hx + hw, tiles[1]), (680, tiles[1]), (680, 280), (700, 280), color='#c79a00')

    # Digital assistant ----------------------------------------------------------------
    d.zone(700, 480, 470, 410, 'Digital assistant in chat and voice mode', 'bot', 'Avaamo bot')
    d.image('bot', 1110, 494, 44)
    by = 548
    for s in ['AI-driven conversation built on the employee’s data and what they say', 'Raises tickets automatically',
              'Hands off to a live agent based on the employee, the issue and their sentiment', '40+ self-help cases in the NLP library',
              'Runs self-healing scripts', 'Chat support in 5 languages']:
        d.el.append(f'<circle cx="{722}" cy="{by - 5}" r="3" fill="{Z["bot"][1]}"/>')
        by = d.lines(734, by, s, 410, 14) + 6
    cells = [('Personalization: MVP', 'Real-time sentiment analysis', ['avaamo']),
             ('Natural language recognition', 'NLP search; voice and chat channels', []),
             ('Integrations', 'Out of the box and custom', ['now', 'genesys', 'nexthink'])]
    for i, (a, b, logos) in enumerate(cells):
        cx = 716 + i * 150
        d.rect(cx, 730, 140, 144, '#fff', Z['bot'][1], rx=8)
        yy = d.lines(cx + 10, 752, a, 120, 14, 600)
        d.lines(cx + 10, yy + 4, b, 120, 13, 400, SECOND)
        for k, lg in enumerate(logos):
            d.logo(lg, cx + 10 + k * 32, 834, 28)
    d.arrow((hx + hw, tiles[2]), (680, tiles[2]), (680, 640), (700, 640), color='#8a5fb0')
    # voice: IVR
    d.rect(440, 730, 240, 70, '#f1eaf7', '#f1eaf7', rx=8)
    d.lines(452, 756, 'Voice menu by location, with all the employee’s data', 170, 13, 400)
    d.logo('avaamo', 636, 744, 36)
    d.arrow((hx + hw / 2, hy + 560), (hx + hw / 2, 730), color='#8a5fb0')
    d.arrow((680, 765), (690, 765), (690, 760), (700, 760), color='#8a5fb0')

    # Genesys agent dashboard ----------------------------------------------------------
    d.lines(1200, 140, 'Every channel’s information goes to the Genesys agent dashboard', 190, 15, 600, lh=20)
    gy = 230
    for key, avatar, text in [('now', None, 'Ticket information'), (None, 'cust7', 'Employee asks for an agent'),
                              ('office', 'cust8', 'Live session booked if needed')]:
        d.rect(1200, gy, 200, 76, Z['agent'][0], Z['agent'][1], dashed=True, rx=8)
        if avatar:
            d.image(avatar, 1210, gy + 12, 52, round_=True, ring='#b7c1c5')
        if key:
            d.logo(key, 1210 if not avatar else 1358, gy + (12 if not avatar else 40), 52 if not avatar else 30)
        d.lines(1272, gy + 32, text, 116, 14, 600)
        gy += 92
    d.arrow((1170, 49), (1180, 49), (1180, 268), (1200, 268), color='#2f6fc0')
    d.arrow((1170, 280), (1185, 280), (1185, 360), (1200, 360), color='#c79a00')
    d.arrow((1170, 700), (1190, 700), (1190, 452), (1200, 452), color='#8a5fb0')

    # Live agent session ---------------------------------------------------------------
    d.zone(1430, 100, 190, 640, 'Live agent session', 'agent')
    y = d.card(1442, 146, 166, 'Unified channel', [(None, 'Video chat, screen share, voice, chat')], kind='agent')
    d.wordmark('logmein', 1450, y + 8, 120, 30)
    y = d.card(1442, y + 40, 166, 'Personalized dashboard', [(None, 'All issue, employee, sentiment, session and history data')], kind='agent')
    y = d.card(1442, y + 12, 166, 'Swarmed support', [(None, 'No escalation. One point of contact. Experts swarm in')], kind='agent')
    d.logo('avaamo', 1446, y + 14, 44)
    d.wordmark('genesys', 1500, y + 18, 108, 36)
    for i in range(4):
        d.image(f'agent{i + 1}', 1442 + i * 42, y + 78, 38, round_=True, ring=Z['agent'][1])
    d.t(1442, y + 136, 'Agents and experts', 13, 600, fill=SECOND)
    d.arrow((1400, 360), (1430, 360), color='#6aa84f')
    d.arrow((1244, 49), (1520, 49), (1520, 100), color='#2f6fc0')

    # Agent-side data, release 2 ------------------------------------------------------
    d.t(1200, 778, 'Release 2', 14, 600, fill=Z['r2'][1])
    d.card(1200, 790, 200, 'Agent data: issues', [(None, 'Resolution history, feedback analysis')], kind='r2')
    d.card(1420, 790, 200, 'Agent data: sentiment', [], kind='r2')
    return d

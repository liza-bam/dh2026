"""4. Checking status and gathering feedback (slide 'Checking Status / Gathering Feedback')."""
from rich import Rich, Z
from svg import SECOND

G = '#9aa5aa'


def brace(d, x, y1, y2, right=False):
    m = (y1 + y2) / 2
    k = -14 if right else 14
    d.el.append(f'<path d="M{x + k} {y1} Q{x} {y1} {x} {y1 + 20} L{x} {m - 14} Q{x} {m} {x - k} {m} '
                f'Q{x} {m} {x} {m + 14} L{x} {y2 - 20} Q{x} {y2} {x + k} {y2}" fill="none" stroke="#223640" stroke-width="2"/>')


def build():
    d = Rich('ts', 1330, 800, 'Checking status and gathering feedback')
    # Checking status -------------------------------------------------------------
    d.t(20, 34, 'Checking status', 20, 600)
    d.logo('now', 30, 80, 70)
    d.arrow((100, 115), (140, 115), color=G)
    d.mark('alert', 146, 98, 30)
    d.t(161, 148, 'Ticket updates', 12, 600, 'middle', fill=SECOND)
    d.arrow((180, 115), (220, 115), color=G)
    d.image('cust7', 226, 84, 62, round_=True, ring='#b7c1c5')
    d.arrow((292, 115), (330, 115), color=G)
    d.zone(330, 56, 360, 64, 'Digital assistant (chat)', 'bot')
    d.zone(330, 132, 360, 210, 'Digital Hub applications', 'hub')
    d.card(344, 174, 332, 'Ticket status dashboard', [(None, 'Every ticket with the steps taken, expected resolution time and live sessions booked'),
                                                    (None, 'The agent in charge of it')], kind='hub')

    # Gathering feedback ------------------------------------------------------------
    d.t(20, 404, 'Gathering feedback', 20, 600)
    y = d.card(20, 440, 200, None, [(None, 'Continuous feedback all through the support journey')], fill=Z['bot'][0], stroke=Z['bot'][1])
    d.card(20, y + 30, 200, None, [(None, 'Sentiment analysis across all channels')], fill=Z['bot'][0], stroke=Z['bot'][1])
    d.arrow((220, 470), (240, 470), color=G)
    d.arrow((220, y + 60), (240, y + 60), color=G)
    brace(d, 256, 430, 760)
    srcs = [('Proactive automation of common issues', 'grey', 'nexthink'), ('Digital assistant (voice and chat): self-help', 'bot', 'avaamo'),
            ('Ticket resolution', 'agent', None), ('Live agent session', 'agent', None)]
    yy = 424
    ys = []
    for title, kind, logo in srcs:
        h = 96 if logo else 58
        fill, stroke = Z[kind]
        d.rect(280, yy, 230, h, fill, stroke, dashed=True, rx=8)
        d.lines(294, yy + 24, title, 150 if logo else 200, 14, 600)
        if logo:
            d.logo(logo, 452, yy + 30, 48)
        d.arrow((510, yy + h / 2), (530, yy + h / 2), color=G)
        d.mark('ok', 534, yy + h / 2 - 14, 28)
        d.arrow((566, yy + h / 2), (600, yy + h / 2), color=G)
        ys.append(yy + h / 2)
        yy += h + 14
    d.zone(600, 424, 260, 340, 'Feedback session with the assistant', 'bot', 'After the ticket is closed')
    for i, t in enumerate(['Employee feedback', 'Agent feedback']):
        d.rect(616, 494 + i * 92, 228, 76, '#fff', Z['bot'][1], rx=6)
        d.t(730, 538 + i * 92, t, 15, 600, 'middle')
    d.arrow((860, 590), (880, 590), color=G)
    brace(d, 896, 470, 710)
    d.card(920, 486, 190, 'Employee', [(None, 'Sentiment history and analysis')], fill='#f2f4f5', stroke='#f2f4f5')
    d.card(920, 610, 190, 'Agent data: sentiment', [], fill='#f2f4f5', stroke='#f2f4f5')
    brace(d, 1126, 470, 710, right=True)
    d.arrow((1140, 590), (1160, 590), color=G)
    d.rect(1160, 520, 150, 140, Z['agent'][0], Z['agent'][1], dashed=True, rx=10)
    d.lines(1235, 580, 'Productivity office dashboard', 120, 16, 600, anchor='middle')
    return d

"""Blocks that repeat across the Digital Hub slides."""
from rich import Z
from svg import SECOND


def employee_data(d, x, y, w=292, r2=True):
    y = d.card(x, y, w, 'Initial customer data: MVP', [
        ('workday', 'Service line, title, location'), ('office', 'Calendar'),
        ('nexthink', 'Environment: OS, connection'), ('now', 'Hardware and software'),
        ('now', 'Issue and request status'), ('now', 'Issue and request history')], kind='cust')
    if not r2:
        return y
    d.t(x, y + 30, 'Release 2', 14, 600, fill=Z['r2'][1])
    y = d.card(x, y + 42, w, 'Customer hyper-personalization', [
        ('now', 'Behavior, preferred contact channel, preferred schedule, technical aptitude')], kind='r2')
    y = d.card(x, y + 12, w, 'Customer sentiment', [(None, 'Sentiment history and analysis')], kind='r2')
    return d.card(x, y + 12, w, 'Customer localization', [(None, 'Fully localized support and UI in 5 languages')], kind='r2')


def employees(d, x, y, n=8, step=74, size=60):
    for i in range(n):
        d.image(f'cust{i + 1}', x, y + i * step, size, round_=True, ring='#b7c1c5')


def live_agent(d, x, y, w=190, title='Live agent session', dashboard='All issue, employee, sentiment, session and history data'):
    top = y
    inner = w - 24
    yy = d.card(x + 12, y + 46, inner, 'Unified channel', [(None, 'Video chat, screen share, voice, chat')], kind='agent')
    d.wordmark('logmein', x + 20, yy + 8, 120, 30)
    yy = d.card(x + 12, yy + 44, inner, 'Personalized dashboard', [(None, dashboard)], kind='agent')
    yy = d.card(x + 12, yy + 12, inner, 'Swarmed support', [(None, 'No escalation. One point of contact. Experts swarm in')], kind='agent')
    d.logo('avaamo', x + 16, yy + 14, 44)
    d.wordmark('genesys', x + 70, yy + 18, 108, 36)
    for i in range(4):
        d.image(f'agent{i + 1}', x + 12 + i * 42, yy + 76, 38, round_=True, ring=Z['agent'][1])
    d.t(x + 12, yy + 134, 'Agents and experts', 13, 600, fill=SECOND)
    h = yy + 150 - top
    # draw zone underneath
    fill, stroke = Z['agent']
    d.el.insert(0, f'<rect x="{x}" y="{top}" width="{w}" height="{h:.0f}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5" stroke-dasharray="7 5"/>')
    d.t(x + 16, top + 28, title, 17, 600)
    return top + h


def r2_side(d, x, y, w=220):
    d.t(x, y, 'Release 2', 14, 600, fill=Z['r2'][1])
    y = d.card(x, y + 12, w, 'Customer hyper-personalization', [(None, 'Behavior, preferred contact channel, preferred schedule, technical aptitude')], kind='r2')
    y = d.card(x, y + 10, w, 'Customer sentiment', [(None, 'Sentiment history and analysis')], kind='r2')
    y = d.card(x, y + 10, w, 'Customer localization', [(None, 'Fully localized support and UI in 5 languages')], kind='r2')
    y = d.card(x, y + 10, w, 'Agent data: issues', [(None, 'Resolution history, feedback analysis')], kind='r2')
    return d.card(x, y + 10, w, 'Agent data: sentiment', [], kind='r2')


def legend(d, x, y):
    d.rect(x, y, 200, 96, '#f2f4f5', '#f2f4f5', rx=8)
    d.t(x + 14, y + 26, 'Legend', 14, 600)
    d.mark('ok', x + 14, y + 38, 22)
    d.t(x + 46, y + 55, 'Issue solved', 14)
    d.mark('alert', x + 14, y + 66, 22)
    d.t(x + 46, y + 83, 'Notification', 14)


def decision(d, cx, cy, text, r=48):
    d.el.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e2f4f1" stroke="#7fc8bd" stroke-width="1.5"/>')
    d.lines(cx, cy - 8, text, r * 1.5, 13, 600, anchor='middle')

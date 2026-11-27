"""D26-9. Most IT support needs no AI: six journeys run as fixed flows, four go to agents."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT


def column(d, x, title, sub, items, dark):
    d.rect(x, 20, 560, 380, TINT if dark else '#f7fafb', TEAL if dark else '#dce4e7', rx=14, sw=1.5)
    d.t(x + 24, 60, title, 20, 600)
    d.t(x + 24, 86, sub, 14, 400, fill=SECOND)
    y = 108
    for it in items:
        d.rect(x + 24, y, 512, 40, '#fff', '#dce4e7', rx=8)
        d.t(x + 40, y + 26, it, 15, 600)
        y += 46


def build():
    d = Rich('sp26', 1180, 520, 'Six of the ten journeys need no decision and run as fixed flows; four need a decision and go to agents')
    column(d, 20, 'Six: fixed flows, no AI', 'The employee chooses, the systems act', ['A new device', 'Proxy access to mail and calendar', 'A Teams channel',
           'A password reset', 'A stolen laptop', 'A scam email'], False)
    column(d, 600, 'Four: agents', 'Each case needs a decision', ['A meeting room that does not work', 'An app that will not install or crashes',
           'VPN at a hotel', 'Client files that will not open'], True)
    d.rect(20, 420, 1140, 84, '#fff', '#223640', rx=14, sw=1.5)
    d.image('lock', 49, 447, 30)
    d.t(108, 454, 'Security is always a fixed flow', 17, 600)
    d.t(108, 480, 'It must be fast and never wrong. A model never acts on a scam email: the attacker wrote it.', 14, 400, fill=SECOND)
    d.H = 520
    return d

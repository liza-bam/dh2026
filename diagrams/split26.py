"""D26-9. Most IT support needs no AI: six journeys run as fixed flows, four go to agents."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT
from cards26 import icon


def column(d, x, title, sub, items, dark):
    d.rect(x, 20, 560, 460, TINT if dark else '#f7fafb', TEAL if dark else '#dce4e7', rx=0, sw=1.5)
    d.t(x + 24, 64, title, 24, 600)
    d.t(x + 24, 96, sub, 17, 400, fill=SECOND)
    y = 122
    for it in items:
        d.rect(x + 24, y, 512, 48, '#fff', '#dce4e7', rx=0)
        d.t(x + 42, y + 31, it, 18, 600)
        y += 56


def build():
    d = Rich('sp26', 1180, 640, 'Six of the ten journeys need no decision and run as fixed flows; four need a decision and go to agents')
    column(d, 20, 'Six: fixed flows, no AI', 'The employee chooses, the systems act', ['A new device', 'Proxy access to mail and calendar', 'A Teams channel',
           'A password reset', 'A stolen laptop', 'A scam email'], False)
    column(d, 600, 'Four: agents', 'Each case needs a decision', ['A meeting room that does not work', 'An app that will not install or crashes',
           'VPN at a hotel', 'Client files that will not open'], True)
    d.rect(20, 504, 1140, 112, '#fff', '#dce4e7', rx=0, sw=1.5)
    icon(d, 'lock', 72, 560, 30)
    d.t(124, 548, 'Security is always a fixed flow', 20, 600)
    d.t(124, 580, 'It must be fast and never wrong. A model never acts on a scam email: the attacker wrote it.', 17, 400, fill=SECOND)
    d.H = 640
    return d

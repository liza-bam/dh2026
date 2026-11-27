"""Picture cards for the case: small agents, the fence, and the cost."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT

import os
import re

# Material Symbols, rounded, filled (Apache 2.0), copied into diagrams/icons
HERE = os.path.dirname(os.path.abspath(__file__))


def symbol(name):
    svg = open(os.path.join(HERE, 'icons', name + '.svg')).read()
    return re.search(r' d="([^"]+)"', svg).group(1)


def icon(d, name, cx, cy, r=28):
    """A teal Material Symbol on a tint circle. Symbols use a 960 grid with y from -960 to 0."""
    size = r * 1.3
    k = size / 960
    d.el.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{TINT}"/>'
                f'<path d="{symbol(name)}" fill="{TEAL}" transform="translate({cx - size / 2:.1f} {cy + size / 2:.1f}) scale({k:.4f})"/>')


def cards(uid, label, items, h=230):
    W, gap, n = 1180, 20, len(items)
    w = (W - 40 - gap * (n - 1)) / n
    d = Rich(uid, W, h + 40, label)
    for k, (ic, title, text) in enumerate(items):
        x = 20 + k * (w + gap)
        d.rect(x, 20, w, h, '#fff', '#dce4e7', rx=8)
        icon(d, ic, x + 48, 72)
        d.t(x + 20, 136, title, 18, 600)
        d.lines(x + 20, 164, text, w - 40, 14, 400, SECOND, lh=20)
    d.H = h + 40
    return d


def agents():
    return cards('ag4', 'Small agents: one per domain, kept small by a strict system, ready agents where they exist, agents for the second line too', [
        ('smart_toy', 'One agent per domain', 'Devices, Software, Mail and calendar, Workplace. Small, cheap, easy to test.'),
        ('fact_check', 'Kept small', 'Standard laptop images, an approved app list, files in OneDrive, no open internet.'),
        ('verified_user', 'Ready agents stay', 'Microsoft Defender judges threats. Nexthink takes what fails for many people.'),
        ('engineering', 'The second line too', 'Team agents help engineers. What they solve becomes a new fix.')])


def fence():
    return cards('fn4', 'The fence: what an agent does on its own, what waits for a yes, when it gives up, and what it never does', [
        ('check_circle', 'On its own', 'Reads the laptop. Runs approved, harmless fixes.'),
        ('thumb_up', 'After a yes', 'Anything the employee would notice, like a restart.'),
        ('support_agent', 'Gives up in time', 'Two failed fixes, and a person takes over with the whole story.'),
        ('front_hand', 'Never', 'Apps or fixes that are not approved.')], h=200)


def cost():
    d = Rich('cs26', 1180, 300, 'Cost per 10,000 employees a month: about $268,000 for people at the help desk against about $300 for the models')
    d.t(20, 40, 'Per 10,000 employees a month, about 13,000 requests', 16, 600)
    d.t(20, 92, 'People at the help desk', 15, 600)
    d.rect(260, 66, 820, 40, '#9aa5aa', '#9aa5aa', rx=8)
    d.t(1096, 92, '$268,000', 16, 600)
    d.t(20, 152, 'Models', 15, 600)
    d.rect(260, 126, 3, 40, TEAL, TEAL, rx=1)
    d.t(276, 152, '$300', 16, 600, fill=TEAL)
    d.rect(20, 196, 1140, 84, TINT, TINT, rx=12)
    d.t(44, 230, 'The real saving is time', 16, 600)
    d.t(44, 258, "About 20 minutes of the employee's time for every request that never reaches a person. At EY, that is billable time.", 14, 400, fill=SECOND)
    d.H = 300
    return d

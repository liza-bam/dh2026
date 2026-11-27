"""Picture cards for the case: small agents, the fence, and the cost."""
from rich import Rich
from svg import SECOND, INK
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
    return cards('ag4', 'Four small agents, one for each domain: Devices, Software, Mail and calendar, Workplace', [
        ('devices', 'Devices', 'Hardware faults and replacements.'),
        ('apps', 'Software', 'Installs, repairs, VPN, apps.'),
        ('calendar_month', 'Mail and calendar', 'Delegation, mailboxes, Teams channels.'),
        ('meeting_room', 'Workplace', 'Rooms, desks, facilities.')], h=200)


def system():
    return cards('sy4', 'Why a small agent is enough: standard images, an approved catalog, files in OneDrive, no open internet', [
        ('laptop_mac', 'A standard image', 'Every laptop starts from a fixed image for its group.'),
        ('fact_check', 'An approved catalog', 'Software comes only from the list for each image.'),
        ('cloud', 'Files in OneDrive', 'Nothing important lives on the laptop.'),
        ('public_off', 'No open internet', 'Vendor knowledge is checked and loaded in advance.')], h=200)


def fence():
    return cards('fn3', 'The fence of the Software agent: three steps, in order', [
        ('groups', '1. Fails for many people?', 'Nothing to fix on this laptop. The agent files a ticket for the Nexthink agent and gives the employee the number.'),
        ('license', '2. A license?', 'Entitled: the agent renews it. Not entitled: it fills in the request for the manager, then renews.'),
        ('settings_backup_restore', '3. Back to standard', 'Smallest fix first: a known fix, a reinstall, a reset of the laptop (it asks when), then a person.')], h=220)


def cost():
    d = Rich('cs26', 1180, 350, 'Cost per 10,000 employees a month: about $268,000 for people at the help desk against about $300 for the models')
    d.t(20, 44, 'Per 10,000 employees a month, about 13,000 requests', 20, 600)
    d.t(20, 112, 'People at the help desk', 18, 600)
    d.rect(300, 80, 740, 48, '#9aa8ae', '#9aa8ae', rx=0)
    d.t(1056, 112, '$268,000', 20, 600)
    d.t(20, 184, 'Models', 18, 600)
    d.rect(300, 152, 4, 48, TEAL, TEAL, rx=0)
    d.t(318, 184, '$300', 20, 600, fill=TEAL)
    d.rect(20, 228, 1140, 102, TINT, TINT, rx=0)
    d.t(44, 268, 'The real saving is time', 20, 600)
    d.t(44, 302, "About 20 minutes of the employee's time for every request that never reaches a person. At EY, that is billable time.", 17, 400, fill=INK)
    d.H = 350
    return d

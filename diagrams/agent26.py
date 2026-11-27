"""D26-8. How the Software agent works: many people affected, a license, then the laptop back to standard."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT


def tag(d, x, y, text):
    w = len(text) * 7 + 18
    d.rect(x, y, w, 22, TINT, TEAL, rx=11, sw=1)
    d.t(x + w / 2, y + 15, text, 12, 600, 'middle', fill=TEAL)
    return x + w + 6


def box(d, x, y, w, h, title, text, tags=(), dark=False):
    d.rect(x, y, w, h, TINT if dark else '#fff', TEAL if dark else '#dce4e7', rx=12, sw=1.5)
    d.t(x + 14, y + 26, title, 15, 600)
    yy = d.lines(x + 14, y + 48, text, w - 28, 13, 400, SECOND, lh=17) if text else y + 40
    tx = x + 14
    for t in tags:
        tx = tag(d, tx, y + h - 32, t)


def build():
    d = Rich('ag26', 1200, 616, 'How the Software agent works: if the program fails for many people, a ticket for the Nexthink agent; '
             'if the license is missing, renew it or ask the manager; otherwise bring the laptop back to standard, smallest fix first, then a person')

    box(d, 20, 20, 300, 72, 'A program does not work', 'The employee writes to Digital Hub. The Software agent takes it.')
    d.arrow((170, 92), (170, 120), color=TEAL)

    # 1. many people?
    box(d, 20, 120, 300, 110, '1. Does it fail for many people?', 'The agent checks the service status itself.', dark=True)
    d.arrow((320, 175), (380, 175), color=TEAL, label='Yes', at=(336, 167))
    box(d, 380, 120, 790, 110, 'A ticket for the Nexthink agent',
        'Nothing to fix on this laptop. The Software agent files a ticket and gives the employee the number. The Nexthink agent takes it: updates, network, system fixes.', ['Outlook'])
    d.arrow((170, 230), (170, 260), color=TEAL, label='No', at=(178, 250))

    # 2. license?
    box(d, 20, 260, 300, 112, '2. Does the employee have a license?', 'If yes, go to step 3.', dark=True)
    d.arrow((320, 316), (380, 316), color=TEAL, label='No', at=(326, 336))
    d.arrow((350, 316), (350, 250), (1020, 250), (1020, 260), color=TEAL)
    box(d, 380, 260, 470, 112, 'Entitled: the agent renews it', 'Then step 3, if the program still does not work.', ['Acrobat'])
    box(d, 870, 260, 300, 112, 'Not entitled', 'The agent fills in the request and sends it to the manager. Once approved, it renews.')
    d.arrow((170, 372), (170, 402), color=TEAL, label='Yes', at=(178, 392))

    # 3. back to standard
    box(d, 20, 402, 300, 180, '3. Bring the laptop back to standard', 'Every laptop is set up from a standard image. The smallest fix first; the next only if the program still does not work.', dark=True)
    steps = [('A known fix', 'Clear a cache, switch the headset, turn off an add-in (it asks first).', ['Excel', 'Teams sound']),
             ('Reinstall the program', 'Harmless, so the agent does not ask.', ['Visio']),
             ('Reset the laptop', 'About an hour, so it asks: now or tonight? Files are safe in OneDrive.', []),
             ('A person from IT', 'Takes over and already knows everything that was tried.', ['Visio'])]
    d.arrow((320, 492), (380, 492), color=TEAL)
    for k, (t, tx, tg) in enumerate(steps):
        x = 380 + k * 198
        box(d, x, 402, 186, 180, t, tx, tg)
        if k < 3:
            d.arrow((x + 186, 492), (x + 198, 492), color=TEAL)
    d.t(380, 604, 'Between steps: still not working.', 12, 400, fill=SECOND)
    d.H = 616
    return d

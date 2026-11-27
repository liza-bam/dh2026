"""D26-8. How the Software agent decides: three questions, a short ladder back to the standard image, and where the five cases end."""
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
    d = Rich('ag26', 1200, 716, 'How the Software agent decides: is the problem on the employee\u2019s laptop; if so, the smallest fix that brings it '
             'back to standard; a lost file is a different problem; an app that is not on the approved list goes to a larger model and a person')

    box(d, 20, 20, 270, 72, 'An app does not work', 'The employee writes in, or the watcher spots it.')
    d.arrow((155, 92), (155, 116), color=TEAL)
    d.arrow((20, 56), (8, 56), (8, 513), (20, 513), color=TEAL)

    # 1. is the problem on the laptop?
    box(d, 20, 116, 270, 136, '1. Is it the laptop?', 'Or is the problem elsewhere: the service, the license, the account, the network?', dark=True)
    d.arrow((290, 175), (320, 175), color=TEAL, label='No', at=(292, 196))
    d.arrow((305, 175), (305, 104), (750, 104), (750, 116), color=TEAL)
    d.arrow((750, 104), (1042, 104), (1042, 116), color=TEAL)
    box(d, 320, 116, 276, 136, 'The service is down', 'It is down for everyone. Nothing to fix on the laptop: the agent says when it will work again.', ['Outlook'])
    box(d, 612, 116, 276, 136, 'The license has run out', 'If the employee is entitled, the agent renews it. If not, the manager approves.', ['Acrobat'])
    box(d, 904, 116, 276, 136, 'The account or the network', 'The agent checks the account. A network problem goes to the network team.')

    # 2. back to standard
    d.arrow((155, 252), (155, 282), color=TEAL, label='Yes', at=(162, 272))
    box(d, 20, 282, 270, 150, '2. Bring it back to standard', 'Every laptop is set up from a standard image. The agent tries the smallest fix first, and the next only if it did not help.', dark=True)
    steps = [('A known fix', 'Clear a cache, turn off an add-in, switch the headset.', ['Excel', 'Teams sound']),
             ('Reinstall the app', 'Remove it and install it again. Harmless, so the agent does not ask.', ['Visio']),
             ('Reset the laptop', 'Back to standard. Takes about an hour, so it asks: now or tonight? Files are safe in OneDrive.', []),
             ('A person from IT', 'Takes over and already knows everything that was tried.', ['Visio'])]
    d.arrow((290, 357), (320, 357), color=TEAL)
    for k, (t, tx, tg) in enumerate(steps):
        x = 320 + k * 220
        box(d, x, 282, 200, 150, t, tx, tg)
        if k < 3:
            d.arrow((x + 200, 357), (x + 220, 357), color=TEAL)

    # 3. a file
    box(d, 20, 462, 270, 110, '3. Is it about a file?', 'A lost or damaged file is a different problem.', dark=True)
    d.arrow((290, 513), (320, 513), color=TEAL)
    d.arrow((305, 513), (305, 450), (970, 450), (970, 462), color=TEAL)
    box(d, 320, 462, 420, 110, 'Usually simple', 'The file comes back from the OneDrive recycle bin or an earlier version.')
    box(d, 760, 462, 420, 110, 'Sometimes hard', 'Client data, a deleted shared folder, two versions that clash: a stronger agent works on it together with a person.')

    # not on the approved list
    d.rect(20, 602, 1160, 80, '#f7fafb', '#dce4e7', rx=12)
    d.t(40, 632, 'An app that is not on the approved list', 15, 600)
    d.lines(40, 658, 'The agent does not install it. A larger model checks the request and suggests an approved app that does the same; if none fits, a person decides.', 1120, 13, 400, SECOND, lh=17)
    d.H = 716
    return d

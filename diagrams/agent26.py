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
    d = Rich('ag26', 1200, 640, 'How the Software agent decides: is it this laptop; if so, the lightest step back to the standard image; '
             'files are a separate path; software outside the catalog goes to a larger model and a person')

    box(d, 20, 20, 270, 64, 'A software problem', 'From the employee or the watcher')
    d.arrow((155, 84), (155, 110), color=TEAL)

    # 1. is it this laptop?
    box(d, 20, 110, 270, 110, '1. Is it this laptop?', 'Reinstalling helps only if the problem is on this laptop.', dark=True)
    d.arrow((290, 165), (320, 165), color=TEAL, label='No', at=(293, 158))
    box(d, 320, 110, 276, 110, 'Down for everyone', 'Fix nothing. Say when it is back.', ['Outlook'])
    box(d, 612, 110, 276, 110, 'No license', 'Hand it to the approval flow.', ['Acrobat'])
    box(d, 904, 110, 276, 110, 'Account or network', 'Bring in the Security agent or the network team.')

    # 2. the lightest step back to the image
    d.arrow((155, 220), (155, 250), color=TEAL, label='Yes', at=(162, 240))
    box(d, 20, 250, 270, 130, '2. Back to the image', 'The lightest step first; the next only if it did not work.', dark=True)
    steps = [('A known fix', 'Clear a cache, turn off an add-in, switch the headset.', ['Excel', 'Teams sound']),
             ('Reinstall the app', 'Harmless, so no question.', ['Visio']),
             ('Reset to the image', 'Takes an hour: now or tonight? Files stay in OneDrive.', []),
             ('A person', 'Takes over with the whole story.', ['Visio'])]
    d.arrow((290, 315), (320, 315), color=TEAL)
    for k, (t, s, tg) in enumerate(steps):
        x = 320 + k * 220
        box(d, x, 250, 200, 130, t, s, tg)
        if k < 3:
            d.arrow((x + 200, 315), (x + 220, 315), color=TEAL)

    # 3. is it about data?
    box(d, 20, 410, 270, 110, '3. Is it about data?', 'Lost or broken files are a separate path.', dark=True)
    d.arrow((290, 465), (320, 465), color=TEAL)
    box(d, 320, 410, 420, 110, 'Simple: a restore from OneDrive', 'The recycle bin or an earlier version. A fixed flow.')
    box(d, 760, 410, 420, 110, 'Hard: client data, a shared folder, a sync conflict', 'A stronger agent on a large model works on it with a person.')

    # outside the catalog
    d.rect(20, 548, 1160, 72, '#f7fafb', '#dce4e7', rx=12)
    d.t(40, 578, 'Software outside the catalog', 15, 600)
    d.t(40, 602, 'Never the small agent’s call. A larger model checks the request and offers an approved alternative; a person decides.', 13, 400, fill=SECOND)
    d.H = 640
    return d

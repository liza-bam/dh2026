"""D26-8. How an agent works: the same Visio case, a 2019 script against a 2026 agent that acts freely inside a fence."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT

GREY = '#9aa5aa'


def step(d, x, y, w, n, text, color):
    d.el.append(f'<circle cx="{x + 14}" cy="{y + 12}" r="12" fill="{color}"/>')
    d.t(x + 14, y + 17, str(n), 12, 700, 'middle', fill='#fff')
    return d.lines(x + 38, y + 17, text, w - 40, 14, 400, lh=19) + 14


def build():
    d = Rich('ag26', 1200, 640, 'The same case, a script and an agent: a consultant cannot install Visio 20 minutes before a client call. '
             'The 2019 script runs the same steps and opens a ticket; the 2026 agent reads the laptop, sees the call, gives the diagram in the browser now '
             'and fixes the laptop after the call, inside a fence of what it may do')

    # the situation
    d.rect(20, 20, 1160, 70, '#f7fafb', '#dce4e7', rx=12)
    d.t(40, 48, 'The situation', 15, 600)
    d.t(40, 72, 'A consultant writes in Teams: “Visio will not install, and I have a client call in 20 minutes. I need my diagram.”', 14, 400, fill=SECOND)

    # the script, 2019
    d.rect(20, 110, 560, 440, '#fff', '#dce4e7', rx=14)
    d.t(44, 146, 'A script, 2019', 18, 600)
    d.t(44, 168, 'The same steps for everyone', 13, 400, fill=SECOND)
    y = 190
    for n, t in enumerate(['“Restart your laptop.” Five minutes gone.',
                           '“Try installing again.” It fails.',
                           'Cleans up the disk. It fails again.',
                           '“Describe the error”: a form.',
                           'A ticket in the queue. An engineer calls back hours later and asks the same questions.'], 1):
        y = step(d, 44, y, 512, n, t, GREY)
    d.rect(44, 480, 512, 48, '#f4f6f7', '#f4f6f7', rx=8)
    d.t(60, 509, 'The call happens without the diagram.', 14, 600)

    # the agent, 2026, inside its fence
    d.rect(620, 110, 560, 440, TINT, TEAL, rx=14, sw=1.5)
    d.el.append(f'<rect x="632" y="122" width="536" height="416" rx="10" fill="none" stroke="{TEAL}" stroke-width="1.5" stroke-dasharray="7 5"/>')
    d.t(648, 152, 'An agent, 2026', 18, 600)
    d.t(648, 174, 'Decides from the laptop’s data and the person’s situation', 13, 400, fill=SECOND)
    y = 196
    for n, t in enumerate(['Reads the laptop: the install failed twice because the installer cache is broken. The disk is fine, so no restart and no clean-up.',
                           'Sees the call in 20 minutes. Fixing takes longer, so it solves the real problem first: “Visio in the browser works now. Here is your diagram. I will fix the laptop after the call.”',
                           'After the call it repairs the cache and installs Visio. If that fails, a person from IT takes over and already knows everything.'], 1):
        y = step(d, 648, y, 504, n, t, TEAL)
    d.rect(648, 436, 504, 48, '#fff', '#fff', rx=8)
    d.t(664, 465, 'The diagram is on the call. The laptop is fixed after it.', 14, 600, fill=TEAL)
    d.lines(648, 506, 'The dashed line is the fence: what the agent may do on its own, what waits for a yes, when it calls a person.', 500, 12, 400, SECOND, lh=15)

    # the point
    d.t(20, 584, 'The script does what was asked: install Visio.', 15, 600)
    d.t(20, 610, 'The agent solves the real problem: the diagram on the call. Inside the fence, it is free to choose how.', 15, 600, fill=TEAL)
    d.H = 640
    return d

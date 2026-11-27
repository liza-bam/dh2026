"""D26-5. Module map: the 10 scenarios (and proactive refresh) built from shared modules."""
from rich import Rich
from svg import SECOND
from transition import TEAL, TINT

# key, name, icon, has a card on screen
MODULES = [
    ('id', 'Verify identity', 'lock', True),
    ('order', 'Order a device', 'hardware', True),
    ('install', 'Install software', 'software', True),
    ('approve', 'Get approval', 'approve', True),
    ('confirm', 'Confirm a risky action', 'alert', True),
    ('fix', 'Run a fix', 'tools', False),
    ('room', 'Book or change a room', 'room', True),
    ('access', 'Grant access', 'azure', False),
    ('person', 'Hand over to a person', 'agent1', True),
    ('status', 'Status and updates', 'ticket', True),
    ('feedback', 'Feedback', 'chat', True),
    ('channel', 'Continue in another channel', 'teams', False),
]

SCEN = [  # the same modules, in the same scenarios, as the live demo (app/index.html)
    ('Meeting room', ['room', 'status', 'feedback']),
    ('VPN offsite', ['confirm', 'fix', 'person', 'feedback']),
    ('Password reset', ['id', 'feedback']),
    ('Teams channel access', ['approve', 'access', 'feedback']),
    ('Lost laptop', ['id', 'order', 'person', 'status', 'feedback']),
    ('Client files in Canvas', ['approve', 'access', 'feedback']),
    ('Outlook access for an assistant', ['confirm', 'access', 'feedback']),
    ('Ordering a peripheral', ['order', 'status', 'feedback']),
    ('Email scam', ['channel', 'confirm', 'id', 'person', 'feedback']),
    ('Failed software install', ['install', 'confirm', 'fix', 'person', 'channel', 'feedback']),
    ('Laptop refresh (proactive)', ['order', 'install', 'confirm', 'status', 'feedback', 'channel']),
]


def build():
    left, top, cw, rh = 300, 230, 74, 46
    W = left + cw * len(MODULES) + 110
    H = top + rh * len(SCEN) + 120
    d = Rich('mm', W, H, 'Module map: which shared modules each scenario is built from')
    # column heads
    for j, (k, name, icon, card) in enumerate(MODULES):
        cx = left + j * cw + cw / 2
        d.el.append(f'<circle cx="{cx}" cy="40" r="22" fill="{TINT}" stroke="{TEAL}" stroke-width="1.5"/>')
        if icon.startswith('agent'):
            d.image(icon, cx - 16, 24, 32, round_=True)
        elif icon == 'azure':
            d.image(icon, cx - 13, 27, 26)
        else:
            d.image(icon, cx - 13, 27, 26)
        # rotated name
        d.el.append(f'<text transform="translate({cx + 5},{top - 14}) rotate(-55)" font-family="\'Inter\', sans-serif" font-size="13" font-weight="600" fill="#223640">{name}</text>')
        if card:
            d.rect(cx - 15, 70, 30, 20, '#fff', TEAL, rx=4)
            d.el.append(f'<line x1="{cx - 9}" y1="77" x2="{cx + 9}" y2="77" stroke="{TEAL}" stroke-width="1.5"/><line x1="{cx - 9}" y1="83" x2="{cx + 3}" y2="83" stroke="{TEAL}" stroke-width="1.5"/>')
    # rows
    counts = {k: 0 for k, *_ in MODULES}
    for i, (sname, mods) in enumerate(SCEN):
        y = top + i * rh
        if i % 2 == 0:
            d.rect(10, y, W - 20, rh, '#f7fafb', '#f7fafb', rx=6)
        d.t(24, y + 29, sname, 14, 600 if 'proactive' not in sname else 400, fill='#223640' if 'proactive' not in sname else SECOND)
        for j, (k, *_r) in enumerate(MODULES):
            cx = left + j * cw + cw / 2
            if k in mods:
                counts[k] += 1
                d.el.append(f'<circle cx="{cx}" cy="{y + rh / 2}" r="11" fill="{TEAL}"/>')
            else:
                d.el.append(f'<circle cx="{cx}" cy="{y + rh / 2}" r="3" fill="#d5dbde"/>')
    # totals
    y = top + len(SCEN) * rh + 10
    d.el.append(f'<line x1="10" y1="{y}" x2="{W - 10}" y2="{y}" stroke="#223640" stroke-width="1.5"/>')
    d.t(24, y + 32, 'Used in scenarios', 14, 600)
    for j, (k, *_r) in enumerate(MODULES):
        cx = left + j * cw + cw / 2
        d.t(cx, y + 34, str(counts[k]), 20, 600, 'middle', fill=TEAL)
    # legend
    d.rect(24, 60, 30, 20, '#fff', TEAL, rx=4)
    d.el.append(f'<line x1="30" y1="67" x2="48" y2="67" stroke="{TEAL}" stroke-width="1.5"/><line x1="30" y1="73" x2="42" y2="73" stroke="{TEAL}" stroke-width="1.5"/>')
    d.t(64, 75, 'The employee sees a card', 13, 400, fill=SECOND)
    d.t(64, 95, 'Others work out of sight', 13, 400, fill=SECOND)
    d.lines(24, y + 74, 'Each module is designed once and looks the same wherever it appears: in Teams, on the Digital Hub website, after a handover between them.', W - 60, 14, 400, SECOND)
    return d

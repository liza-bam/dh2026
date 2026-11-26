"""Detailed scenario flows (D26-F*). Each is the working diagram behind a scenario card in D26-4."""
from journey import build_flow


def failed_install(rows=(7,)):
    lanes = ['employee', 'front', 'agent', 'systems', 'live', 'engineer']
    S = {
        'e1': dict(col=0, lane='employee', title='Writes in Teams', sub='“I need Visio for a client call today”', logos=['teams']),
        'f1': dict(col=0, lane='front', title='Loads his context', sub='Role, device, open tickets', logos=['workday', 'nexthink', 'now']),
        'f2': dict(col=1, lane='front', title='Routes to the fix agent'),
        'a1': dict(col=1, lane='agent', title='Checks Visio is approved for his role', logos=['now']),
        's1': dict(col=2, lane='employee', kind='card', card=('Visio is approved for you', ['About 5 minutes'], ['Install now', 'Later'], 'hub'), module='Install software'),
        'e2': dict(col=2, lane='employee', title='Taps Install now', sub='On the card in Teams', logos=['teams']),
        'y1': dict(col=3, lane='systems', title='Intune starts the install'),
        'y2': dict(col=4, lane='systems', title='The install fails', sub='Nexthink: the disk is almost full', logos=['nexthink']),
        'a2': dict(col=4, lane='agent', title='Finds the cause', module='Run a fix'),
        's2': dict(col=5, lane='employee', kind='card', card=('Free up space first?', ['Removes temporary files only', 'Your files stay'], ['Free up space', 'Not now'], 'hub'), module='Confirm a risky action'),
        'e3': dict(col=5, lane='employee', title='Taps Free up space', sub='On the card in Teams', logos=['teams']),
        'a3': dict(col=6, lane='agent', title='Fix 1: clears the disk, installs again'),
        'y3': dict(col=6, lane='systems', title='Fails again'),
        'a4': dict(col=7, lane='agent', title='Fix 2: repairs the installer, installs again'),
        'y4': dict(col=7, lane='systems', title='Still fails'),
        'e4': dict(col=7, lane='employee', title='Writes in Teams', sub='“My call is in 20 minutes, can someone help?”', logos=['teams']),
        'd1': dict(col=8, lane='front', kind='decision', title='Two fixes failed or frustrated?'),
        'n1': dict(col=8, lane='agent', title='No: keeps working on it'),
        'l1': dict(col=9, lane='live', title='Live agent gets the handoff card', sub='Who, what happened, what was tried, the logs', module='Hand over to a person'),
        's4': dict(col=10, lane='employee', kind='card', card=('Tracy from IT joined', ['She already knows', 'what happened'], ['Allow remote session'], 'agent')),
        'e5': dict(col=10, lane='employee', title='Taps Allow remote session', sub='In the same Teams chat', logos=['teams']),
        'l2': dict(col=11, lane='live', title='Fixes it in a remote session', sub='No questions asked again'),
        'e6': dict(col=12, lane='employee', title='Opens Teams on his phone', sub='On the train: the same conversation', module='Continue in another channel', logos=['iphone', 'teams']),
        's5': dict(col=12, lane='employee', kind='card', card=('Visio is installed', ['How did we do?'], ['Rate'], 'hub'), module='Feedback'),
        'e7': dict(col=13, lane='employee', title='Taps Rate', sub='On his phone', logos=['iphone', 'teams']),
        'a5': dict(col=12, lane='agent', title='Drafts a new fix', sub='Check the disk and clear the installer cache before installing'),
        'g1': dict(col=12, lane='engineer', title='Approves the new fix'),
        'g2': dict(col=13, lane='engineer', kind='done', title='Next time it runs automatically'),
    }
    E = [('e1', 'f1'), ('f1', 'f2'), ('f2', 'a1'), ('a1', 's1'), ('s1', 'e2'), ('e2', 'y1'), ('y1', 'y2'), ('y2', 'a2'),
         ('a2', 's2'), ('s2', 'e3'), ('e3', 'a3'), ('a3', 'y3'), ('y3', 'a4'), ('a4', 'y4'), ('y4', 'd1'), ('e4', 'd1'),
         ('d1', 'n1', 'No'), ('d1', 'l1', 'Yes'), ('l1', 's4'), ('s4', 'e5'), ('e5', 'l2'), ('l2', 's5'), ('e6', 's5'), ('s5', 'e7'), ('l2', 'a5'), ('a5', 'g1'), ('g1', 'g2')]
    return build_flow('f10', 'Failed software install: the full flow across the employee, what he sees, our agents, systems, live support and an engineer',
                      lanes, S, E, cols=14, colw=220, rows=rows)

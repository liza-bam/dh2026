# Digital Hub, 2026

**IT support with AI agents. The first decision was where not to use them.**

**Role:** UX, product and service designer. Service design, agent architecture.

**Year:** 2026, my own project.

## Seven years later

In 2019 I designed how EY's IT support would stop a bad software update before it reached everyone. Seven years later I went back and asked: how would I build it today? The journey held up. Only the tools behind it changed.

## Where it started

Digital Hub was the IT support service I designed for EY (https://sandy.tayts.com/dh.html). Its support paths already used AI: monitoring, self-healing scripts, and a check on every manual fix: can it be automated?

Visual: [D19-11] Support paths, 2019.

A bad Visio update takes both halves of this diagram. Monitoring catches the crash, but no script can fix a bad update, so it goes to a person. Her fix becomes a script that runs for everyone else, before they hit the bug.

## A bad update, 2019

Peter opens Visio after an update, and it won't start. Digital Hub files a ticket and gives him a workaround, Visio on a virtual machine, so he keeps working. Behind the scenes it finds similar tickets and calls in support. An engineer finds the cause: the new update. Digital Hub holds the update back from everyone else, runs the engineer's fix and tells the people affected: "We fixed the problem with your Visio update." Everyone else never sees the bug.

Visual: [V19-1] Ticket Trends, Crash bugs and Automated Solutions, 2019.

Visual: [D19-12] SW update issue and resolution, 2019.

Visual: [D19-13] A bad update, 2019.

## Why it was hard

- Four teams and four vendors, and every agreement negotiated again and again.
- Every integration written by hand.
- Every new case a new script.

It cost so much that manual support was cheaper.

## What changed

- **Platforms ship their own agents.** ServiceNow, Nexthink, SAP Ariba and Microsoft Defender: connected, not built.
- **Standard connectors.** Agents reach the systems without hand-written integrations.
- **Agents get identities, like employees.** Microsoft Entra Agent ID: access is agreed once.
- **Small models are cheap.** About $300 a month for 10,000 employees.

The 2019 journey works now, with one change: AI only where a step needs a decision.

## The same journey, 2026

Peter sees the same thing as in 2019. Behind the scenes, the platforms now do what we had to script.

Visual: [D26-17] A bad update, 2026.

## What I designed

The platforms are the parts. The journey is the design, and its first rule is that people do as little as possible. Peter only reads messages and keeps working. The engineer only says yes or no.

What that takes:

- who owns the case at each stage, so nothing is lost between teams;
- what goes into the record at each step, so nobody asks Peter twice;
- where a rule decides, where an agent decides and where an engineer decides;
- what Peter sees, and when.

## Where AI helps

Only where a step needs a decision. In this journey that is two places: the Software agent, which talks to Peter and links the incidents, and ServiceNow's problem agent, which prepares the analysis for the engineer. Everything that changes a system waits for the engineer's yes and runs as a fixed flow.

Across the ten journeys, six run as fixed flows and four need agents.

Visual: [D26-9] Six and four.

Visual: [D26-2] Architecture.

Technical document, with every step, system and source: https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY

<small>Model costs measured in the demo or assumed. Logic checked against ServiceNow, Nexthink, Microsoft, Moveworks and Salesforce in November 2026. Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 and warns about "agent washing". Digital Hub uses an agent only where a flow cannot do the job.</small>

# Digital Hub, 2026

**IT support with AI agents. The first decision was where not to use them.**

**Role:** UX, product and service designer. Service design, agent architecture.

**Year:** 2026, my own project.

## Seven years later

In 2019 I designed how EY's IT support would stop a bad software update before it reached everyone. Seven years later I went back and asked: how would I build it today? The journey held up. Only the tools behind it changed.

## Where it started

In 2019 I designed Digital Hub for EY (https://sandy.tayts.com/dh.html). Its support paths already used AI: monitoring, self-healing scripts, and a check on every manual fix: can it be automated?

Visual: [D19-11] Support paths, 2019.

One scenario showed these paths at work.

## A bad update, 2019

Peter opens Visio after an update, and it won't start. Digital Hub files a ticket and gives him a workaround, Visio on a virtual machine, so he keeps working. Behind the scenes it finds similar tickets and calls in support. An engineer finds the cause: the new update. Digital Hub holds the update back from everyone else, runs the engineer's fix and tells the people affected: "We fixed the problem with your Visio update." Everyone else never sees the bug.

Visual: the 2019 video, "Ticket Trends, Crash bugs and Automated Solutions" (to add).

Visual: the 2019 blueprint, "SW update issue and resolution": Submit, Confirm, Identify, Notify, Resolve, Inform (to add).

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

| Stage | 2019 | 2026 |
|---|---|---|
| Submit | Digital Hub files a ticket and offers a workaround | Nexthink records the crash and files an incident in ServiceNow. The Software agent messages Peter first, with a workaround from the knowledge base |
| Confirm | Digital Hub finds similar tickets. An engineer confirms the cause and blocks the update | Nexthink flags the version that crashes more than others, and ServiceNow finds similar incidents. The Software agent links them to one problem. ServiceNow's problem agent prepares the analysis, and an engineer confirms the cause. A flow pauses the update |
| Identify | Digital Hub lists everyone using the update | Nexthink and Microsoft 365 Cloud Update show who has the new version |
| Notify | The people affected hear that the update is blocked and a fix is underway | A flow messages everyone on the problem in Teams |
| Resolve | The engineer writes the steps, and Digital Hub runs them | ServiceNow's problem agent proposes the steps, and the engineer approves them. A flow changes the settings and rolls the update out in waves |
| Inform | "We fixed the problem", and a sentiment score | A flow closes every linked incident. Each person gets a message and a one-tap rating |

## What I designed

The platforms are the parts. The journey is the design:

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

# Digital Hub, 2026

**IT support with AI agents. The first decision was where not to use them.**

**Role:** UX, product and service designer. Service design, agent architecture.

**Year:** 2026, my own project.

## Where it started

In 2019 I designed Digital Hub for EY (https://sandy.tayts.com/dh.html). Its support paths already used AI: monitoring, self-healing scripts, and a check on every manual fix: can it be automated?

Visual: [D19-11] Support paths, 2019.

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

The 2019 paths work now, with one change: AI only where a request needs a decision.

## Where AI helps

Only where solving a request needs a decision. Of the ten journeys, six need none and four do.

Visual: [D26-9] Six and four.

## One way in, three paths

An intake agent on a small model reads the request and picks the path: a fixed flow, a domain agent, or a ticket to a team and its agent.

Visual: [D26-2] Architecture.

## One request on each path

Visual: [D26-14] Path 1: a fixed flow.

Visual: [D26-15] Path 2: a domain agent.

Visual: [D26-16] Path 3: a team agent.

## What it costs

Visual: [D26-12] What it costs.

Technical document, with every agent, rule and number: https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY

<small>Costs: MetricNet benchmarks ($20.61 per contact, 1.3 tickets per user a month, 20 minutes saved per avoided ticket); model costs measured in the demo or assumed. Logic checked against ServiceNow, Moveworks, Salesforce and Microsoft in November 2026. Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 and warns about "agent washing". Digital Hub uses an agent only where a flow cannot do the job.</small>

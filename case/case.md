# What I would change today

**Most IT support needs no AI.**

Of the ten journeys EY's research named, six need no decision: a new device, proxy access to mail and calendar, a Teams channel, a password reset, a stolen laptop, a scam email. They run as fixed flows: the employee chooses, the systems act. Security above all: it must always be fast and never wrong, so its steps are fixed and people make the real calls.

Four need a decision: a meeting room that does not work, a failed install, VPN at a hotel, client files that will not open. Only these go to agents.

## Small agents, each with a fence

Every request comes in through one intake agent on a small model. Simple actions go to fixed flows. Problems go to an agent for their domain: Devices, Software, Mail and calendar, Workplace. Each has its own tools and a fence: what it does on its own, what waits for a yes, when it calls a person. Anything that fits nowhere goes to the right team as a ticket, and that team has its own agent to help its engineers.

Visual: [D26-2] Architecture.

## Inside the fence, the agent decides

A script does what was asked. An agent solves the real problem. Visio will not install twenty minutes before a client call: the script restarts, reinstalls, cleans the disk and opens a ticket. The agent reads the laptop, sees the call, opens the diagram in the browser now and fixes the laptop after the call.

Visual: [D26-8] A script and an agent.

Technical document: https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY

<small>Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

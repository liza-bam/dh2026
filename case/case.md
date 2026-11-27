# What I would change today

**Most IT support needs no AI.**

Of the ten journeys EY's research named, I asked one question of each: does solving it need a decision?

- **Six do not:** a new device, proxy access to mail and calendar, a Teams channel, a password reset, a stolen laptop, a scam email. They run as fixed flows: the employee chooses, the systems act, and the same request goes the same way every time.
- **Four do:** a meeting room that does not work, a failed install, VPN at a hotel, client files that will not open. Only these go to agents.

**Security is always a fixed flow.** It must be fast and never wrong. A stolen laptop is locked and wiped as soon as the employee confirms it is them. A scam email is judged by Microsoft Defender, and the real calls belong to the security team. A model never acts on a scam email: the email is written by the attacker. When in doubt, the intake agent sends a case to security; a false alarm is cheap.

## Small agents, each with a fence

Every request comes in through one intake agent on a small model. It reads what the employee writes and picks the path: a fixed flow, a domain agent, or a ticket for the right team.

- **One agent per domain:** Devices, Software, Mail and calendar, Workplace. Not one big agent: small ones are cheaper, can touch only their own systems, and can be tested before release.
- **What keeps them small:** every laptop starts from a standard image for its group, software comes from an approved list, files live in OneDrive, and agents have no open internet. Vendor knowledge goes into each agent's library in advance.
- **Ready agents stay where they are:** Microsoft Defender judges threats; the Nexthink agent takes problems that hit many people at once. We decide what to give them; we do not rebuild them.
- **The second line has agents too.** A ticket goes to the right team, and that team's agent helps its engineers. What they solve comes back to the first line as a new fix, once an engineer approves it.

Visual: [D26-2] Architecture.

## The fence

Each agent is defined the way ServiceNow defines its first-line AI specialist: a role, the problems it takes, its tools and clear limits.

- **Does on its own:** reads the laptop, runs approved harmless fixes, reinstalls an approved app.
- **Waits for a yes:** anything the employee would notice, like a restart or resetting the laptop. For a reset it also asks when.
- **Gives up in time:** after two fixes that did not work, a person from IT takes over with the whole story. Nobody asks the employee again.
- **Never:** installs software outside the approved list, runs a fix that is not in its library, or touches another laptop.

Independence grows one action at a time: first the agent proposes and an engineer approves, then it acts alone on harmless fixes, then within its full limits. Each agent is measured by two numbers: how many cases it is allowed to take, and how many of those it solves without the case coming back.

## Inside the fence, the agent decides

A script does what was asked. An agent solves the real problem. Visio will not install twenty minutes before a client call: the script restarts, reinstalls, cleans the disk and opens a ticket. The agent reads the laptop, sees a broken installer cache and the call, opens the diagram in the browser now and fixes the laptop after the call.

Visual: [D26-8] A script and an agent.

## What the employee sees

- **Real choices, not forms:** a short catalog of monitors; three levels of proxy access, from seeing the calendar to sending email.
- **No nagging:** tap Later, and the agent offers one reminder in 15 minutes, then starts the install itself; the employee can still cancel.
- **A record of everything:** every request gets a number, even when agents do all the work.

Technical document, with every agent, tool and rule: https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY

<small>Checked against the market in November 2026: ServiceNow's AI front door and AI specialists, Moveworks, Salesforce, Microsoft Agent 365, and Anthropic's and IBM's guidance on workflows and agents. Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

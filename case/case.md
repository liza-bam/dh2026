# Digital Hub, 2026

**IT support for EY, rebuilt with AI agents. The first decision was where not to use them.**

**Role:** UX, product and service designer. Service design, agent architecture, prototype.

**Year:** 2026, my own project.

**Links:** live demo (https://digital-hub-demo.alexandra-tayts.workers.dev), technical document (https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY).

## Most IT support needs no AI

Research named the ten most common IT requests at EY. I asked one question of each: does solving it need a decision?

- **No:** a new monitor, proxy access to mail and calendar, a Teams channel, a password reset, a stolen laptop, a scam email.
- **Yes:** a meeting room that does not work, a failed install, VPN at a hotel, client files that will not open.

The first six run as fixed flows. Security above all: a stolen laptop or a scam email must always be handled fast and never wrong, so the steps are fixed, Microsoft Defender judges the email, and the security team makes the real calls. When in doubt, the intake agent sends a case to security: a false alarm is cheap. Agents get only the other four.

And not one big agent: small ones, one per domain. They stay small because the system around them is strict: standard laptops, apps that install themselves, files in OneDrive. A software problem has a short ladder, from a known fix to a reset; the agent picks the step and the moment. Anything else goes up to people.

## What I designed

- **One way in.** A small, cheap model reads what the employee writes and picks the path.
- **An agent for each domain.** Devices, Software, Mail and calendar, Workplace. Each has its own tools, its own knowledge and clear limits: what it does alone, what waits for a yes, when it calls a person. One agent leads each case.
- **Agents for the people behind the help desk, too.** When nothing fits, the ticket goes to the right team, and that team's agent helps its engineers. What they solve becomes a fix for next time.
- **Help before anyone asks.** A watcher agent finds the full disk before Visio fails.

Visual: [D26-2] Architecture.

## How an agent works

A fence, and freedom inside it.

Every laptop starts from a standard image for its group, and software comes from an approved list. That gives the Software agent its fence:
- If a program fails for many people, it files a ticket for the Nexthink agent and tells the employee.
- If the license is missing, it renews it, or sends the manager a ready request.
- On the laptop it uses only approved fixes. Anything the employee would notice waits for a yes. After two fixes that did not work, a person from IT takes over with the whole story.

Inside the fence, it decides for itself, from the laptop's data and the person's situation. A script does what was asked. The agent solves the real problem.

Visual: [D26-8] A script and an agent.

## What the employee sees

- **Real choices.** A short catalog of monitors. Three levels of proxy access, from seeing the calendar to sending email.
- **No nagging.** Tap Later, and the agent offers one reminder in 15 minutes. Then it starts the install itself, and you can still cancel.
- **Never explain twice.** When a person takes over, they already know everything that was tried.
- **A record of everything.** Every request gets a number, even when agents do all the work.

## Try it

Three journeys on a phone: a monitor, proxy access, and a Visio install that fails until a person takes over. A real agent reads what you write; next to the phone you see which agent works, on which model, and what it costs.

https://digital-hub-demo.alexandra-tayts.workers.dev

## Lessons learned

To write at the end.

<small>Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

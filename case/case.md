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

Every laptop starts from a standard image for its group: auditors, consultants, designers. Software comes from an approved catalog. So the agent knows what each laptop should look like, and asks three questions:

1. **Is the problem on the employee's laptop?** Or is it the service, the license, the account, the network? If Microsoft 365 is down for everyone or a license has run out, reinstalling helps nobody. The case goes another way.
2. **If it is, what is the lightest step back to the standard?** A known fix, then reinstalling the app, then resetting the laptop to its image. Files stay in OneDrive.
3. **Is it about data?** Most "where is my file" cases are a restore from OneDrive. Client data, a deleted shared folder or a sync conflict is hard: a stronger agent works on it with a person.

Like ServiceNow's first-line AI specialist, each agent has a role, the kinds of problems it takes, its tools, clear limits and a rule for when to hand over: two fixes that did not work, and a person takes over with the whole story.

Software outside the catalog is never the small agent's call. A larger model checks the request and offers an approved alternative; a person decides.

Visual: [D26-8] How the Software agent decides.

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

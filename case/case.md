# Digital Hub, 2026

**IT support for EY, rebuilt with AI agents. The first decision was where not to use them.**

**Role:** UX, product and service designer. Service design, agent architecture, prototype.

**Year:** 2026, my own project.

**Links:** live demo (https://digital-hub-demo.alexandra-tayts.workers.dev), technical document (https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY).

---

## Half of IT support needs no AI

Research named the ten most common IT requests at EY. I asked one question of each: does solving it need a decision?

- **No:** a new monitor, an assistant's access to Outlook, a Teams channel, a password reset, a meeting room. Same steps every time; the only choices are the employee's.
- **Yes:** a failed install, VPN at a hotel, client files that will not open, a scam email, a stolen laptop. The next step depends on what turns up.

So the simple half runs as fixed flows: fast, cheap, predictable. Agents get only the five problems that need judgment.

And not one big agent. Small ones, each an expert in one domain: cheaper, safer, easier to test. They stay small because the system around them is strict: standard laptops, apps that install themselves, files in OneDrive. A software problem has a short ladder, from a known fix to a reset, and the agent only picks the step and the moment. Anything outside its library goes up to people.

---

## What I designed

- **One way in.** A small, cheap model reads what the employee writes and picks the path.
- **An agent for each domain.** Security, Devices, Software, Mail and calendar, Workplace. Each has its own tools, its own knowledge and clear limits: what it does alone, what waits for a yes, when it calls a person. One agent leads each case.
- **Agents for the people behind the help desk, too.** When nothing fits, the ticket goes to the right team, and that team's agent helps its engineers. What they solve becomes a fix for next time.
- **Help before anyone asks.** A watcher agent finds the full disk before Visio fails.

Visual: [D26-2] Architecture.

---

## What the employee sees

The agents are the means. This is the point.

- **Real choices.** A short catalog of monitors. Three levels of access for an assistant, from seeing the calendar to sending email.
- **No nagging.** Tap Later, and the agent offers one reminder in 15 minutes. Then it starts the install itself, and you can still cancel.
- **Never explain twice.** When a person takes over, they already know everything that was tried.
- **A record of everything.** Every request gets a number, even when agents do all the work. You never have to look at it.

---

## Try it

Three journeys on a phone: a monitor, an assistant's access, and a Visio install that fails until a person takes over. A real agent reads what you write; next to the phone you see which agent works, on which model, and what it costs.

https://digital-hub-demo.alexandra-tayts.workers.dev

---

## Lessons learned

To write at the end.

<small>Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

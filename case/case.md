# Digital Hub, 2026

Working draft of the portfolio case study. The full system is in the technical document.

---

## Header

**Title:** Digital Hub, 2026

**Subtitle:** In 2019 I designed IT support for EY that fixes problems before people notice them. In 2026 I rebuilt it with AI agents, on my own.

**Role:** UX, product and service designer. Service design, agent architecture, prototype.

**Timeline:** 2019–2020 proposal for EY at Wipro; 2026 rebuild.

**Links:** live demo (https://digital-hub-demo.alexandra-tayts.workers.dev), 2019 case study, technical document (https://claude.ai/artifact/CS5DidDxcR4oQ1qnekNmPY).

---

## TL;DR

**Problem.** One IT issue at EY meant three or more support channels, cases lost between teams and the same questions again and again. My 2019 Digital Hub fixed the experience, but its bot could only handle what someone had written in advance.

**What I did.** Looked at the ten most common requests again and saw that only five need a decision. Simple actions became fixed flows; problems went to small agents, one per domain, each with its own tools, knowledge and limits. Then I designed what the employee sees and built a live demo.


---

## Where it started

In 2019, on Wipro's proposal for EY, I designed Digital Hub: one place for every IT issue, live status on every request, and support that acts before people notice a problem. The client called it the strongest part of the bid. Its limit was the bot: anything nobody had scripted became a ticket. That limit is where 2026 starts.

---

## Five need a decision, five do not

I started from the same ten requests and asked one question: does solving it need a decision?

Ordering a monitor does not. The steps are always the same, and the only choices are the employee's. A failed Visio install does: the next step depends on what the agent finds on the laptop.

- **No decision:** ordering a device, an assistant's access to Outlook, a Teams channel, a password reset, a meeting room.
- **Decisions needed:** a failed install, VPN at a hotel, client files that will not open, a scam email, a stolen laptop.

That leaves five problems for agents, not ten. Everything else stays a cheap, predictable flow.

---

## What I designed

- **Simple actions run as fixed flows.** The intake agent understands the request in the employee's words. From there no model decides anything.
- **Problems go to an agent for their domain.** Security, Devices, Software, Mail, calendar and Teams, Workplace. Each has its own tools, its own library and its limits: what it does alone, what waits for a yes, when it brings in a person. One agent leads each case and brings in the others.
- **Anything else goes to the right team, and the team has an agent too.** It works for the engineers. What they solve comes back to the first line as a new fix.
- **Before anyone asks.** A watcher agent finds the full disk or the outdated VPN app and fixes it before the employee notices.

Visual: [D26-2] Architecture.

---

## What the employee sees

The agents are a means to an end. What matters is how it feels to the person with the problem.

- **The flow decides, the agent speaks.** Tap Later on Visio, and the agent offers one reminder in 15 minutes. Then it starts the install itself; the employee can still cancel. It never asks twice.
- **Real choices, not yes or no.** A short catalog of monitors and where to deliver. Three levels of access for an assistant, from seeing the calendar to sending email.
- **Every request leaves a record**, even when agents do all the work, so the employee always has a number. They never need to look at it.
- **Nobody asks again.** When a person takes over, they get the whole story. A stolen laptop is wiped as soon as the employee confirms it is them.

---

## The live demo

Three journeys on a phone, each showing something different: a small shop for a monitor, a choice of control for an assistant, and a failed install that a person takes over. A real intake agent reads what you write; next to the phone you see which agent works, on which model, and what it costs.

https://digital-hub-demo.alexandra-tayts.workers.dev

---

## Lessons learned

To write at the end.

<small>Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

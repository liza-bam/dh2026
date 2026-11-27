# Digital Hub, 2026

Working draft. Diagram IDs refer to `diagrams.html`. Sections marked "to write" are the plan, not copy.

---

## Header

**Title:** Digital Hub, 2026

**Subtitle:** In 2019 I designed IT support for EY that fixes problems before people notice them. In 2026 I rebuilt it with AI agents, on my own.

**Role:** UX, product and service designer. Service design, agent architecture, prototype.

**Timeline:** 2019–2020 proposal for EY at Wipro; 2026 rebuild.

**Links:** live demo (when built), 2019 case study, diagrams.

---

## TL;DR

**Problem.** EY employees work on tight client deadlines, but one IT issue meant 3+ support channels, 30%+ of cases lost between teams, and the same checks again and again. In 2019 I designed Digital Hub to solve problems before people noticed them, but every case the bot could handle had to be written in advance.

**What I did.** Took the 2019 service as the brief and rebuilt it with specialized AI agents: the same journeys, the same employee data, the same systems, with agents doing the work people had to script. Re-evaluated the stack, gave agents access the way people get it, and built a live demo.

**Result.** To write once the demo runs: share of cases solved without the help desk, repeat contacts, cost per solved case. No numbers until they are measured.

---

## Where it started: 2019

In 2019, on Wipro's proposal for EY, I designed Digital Hub: one app for every IT issue, live status on every request, and support that acts before people notice a problem. I led a team of 7 through the ten journeys EY's discovery named, from password resets to lost laptops, and built them from shared modules so the same task always looked the same.

The delivery plan followed the same idea. The first journey, the laptop refresh, was the MVP. Every next journey reused its modules and added only what was unique to it, about two sprints each. The rollout went in waves: 500 people in the UK first, then 17,500; in the US and India, 20,000 first; in other countries, 500, then 2,000, then everyone, each in its own language. And the platform sat on top of EY's systems through APIs, so EY could change a system without changing what employees saw.

Digital Hub reached the final round of the bid. The client called it the strongest part of the proposal, and more than 50 later Wipro bids were built on it.

It had one limit. The AI bot could only handle cases someone had written in advance, and every proactive behavior was a separate script. Anything new became a ticket. That limit is where 2026 starts.

Visuals: [D19-1] First contact, [D19-2] Solving issues, [D19-5] Proactive support. The rest of D19 behind "see more diagrams".

---

## Three rules before any agent

### 1. It costs less than the help desk it replaces
Every solved case has a price: model calls, licences, the engineer who approves a new fix. Fixed journeys run on small, cheap models. The large model only gets requests that have no journey, and only after the switch. Cost is measured per solved case, against the cost of the same case at the help desk.

### 2. Agents get access the way people do
Each agent has its own identity, its own role and only the rights that role needs. The password agent resets passwords and nothing else. Risky actions wait for a person.

### 3. A new year means a new look at the stack
Some platforms I had to design around in 2019 are gone. Others became stronger. I checked each one against six questions:
- Can agents act through it, not just read from it?
- Does it give agents their own identity and keep them within the employee's rights?
- Does it hold data no one else has?
- What does one solved case cost?
- Is every agent action on record?
- Can we change the model or the vendor without rebuilding?

Eight platforms stay, and each now has a way for agents to act through it. Two go: the Avaamo bot, because the intake agent does its job, and Wipro Holmes, because fixes now run through Nexthink and Intune.

Visual: [D26-6] Stack scorecard.

---

## The logic: how Digital Hub grows

An orchestrator that talks to every employee from day one makes the best demo and the worst plan. EY is a very large company, and every conversation on a large model costs money. So Digital Hub starts cheap and earns the right to use the large model.

The plan grows out of 2019: start with one set of journeys, reuse modules for the next ones, roll out in waves. What changes is where new journeys come from. In 2019 each one cost about two sprints of design and build. In 2026 the requests themselves show which journey to build next.

### Stage 1. Ten fixed journeys from day one
The ten most common requests from 2019 become fixed journeys: the same steps every time, built from shared modules. An intake agent on a small model reads every request and picks the journey.

When a request has no journey, the intake agent does not stop. It opens a ServiceNow ticket and fills it in: category, urgency, the right support group, a summary of the conversation, the employee's device. It labels the ticket and tells the employee what happens next. People solve these cases, and nobody asks the employee anything again.

Requests never reach the large model at this stage. Tickets drop from the first day. The large model works only off to the side: when people solve a new kind of problem, it drafts a fix from the case, and an engineer approves it before it runs anywhere.

### Stage 2. More journeys every week
Every ticket without a journey carries a label. Once a week the intake agent groups them: what people ask most, and how often. The most frequent requests become new fixed journeys. People design and approve each one, the same way an engineer approves a new fix. The library grows, and the share that reaches the help desk falls.

### Stage 3. The switch
When fixed journeys cover most requests, what is left is small enough to give to the large model. It starts in shadow mode: for every ticket without a journey, the orchestrator drafts an answer, and the help desk marks each draft as good or not. Nothing reaches the employee. Then one office, then everyone.

We switch when three things are true:
- Fixed journeys cover most requests.
- The help desk accepts most of the orchestrator's drafts.
- The orchestrator costs less than people on the same requests.

The switch changes the default path. Before: no journey means a ticket for people. After: no journey means the orchestrator tries first, and people get what it cannot solve. When the orchestrator solves something often enough, it becomes a new fixed journey.

### Why this order
Cheap work runs on fixed journeys and a small model, so the first rule holds from day one. The large model gets only what is left, and only after the help desk has seen it work. Each stage pays for the next one.

Visual: [D26-7] Delivery plan.

---

## Architecture

Eight layers, each with one job.

1. **Channels.** Teams, the Digital Hub website, email and voice. It is one conversation, wherever it starts.
2. **Intake agent and orchestrator.** The intake agent reads every request, picks the journey or fills a ticket. After the switch, the orchestrator takes what has no journey. Neither changes anything in a system itself.
3. **Specialized agents.** Identity, workplace, access, devices, fix and watcher. Each has its own identity, only the rights its role needs, and a list of what it never does. All run on small models.
4. **Enterprise agents.** Microsoft Defender, ServiceNow and Genesys bring their own agents, data and audit. Ours ask them; we do not rebuild them.
5. **Knowledge.** Agents answer only from approved EY sources, with a link to the source.
6. **Systems.** ServiceNow, Workday, Entra ID, Intune, Nexthink, Office 365 and SAP Ariba, reached through their MCP servers and only within the rights of the agent and the employee.
7. **Governance.** Every agent is registered, tested on real scenarios before release, has a budget, and every action is logged.
8. **People.** Live agents, approvers, the security team and engineers: the cases that need judgment.

Visuals: [D26-1] What changes, [D26-2] Architecture.

## Ten scenarios

The ten scenarios are the ten journeys from 2019, now run by agents. Each card shows how a scenario starts, which agent does the work, which systems it uses, what solved looks like, and when a person steps in. Three of the ten never reach the help desk at all: channel access, Outlook access for an assistant and ordering a peripheral.

Visual: [D26-4] The 10 scenarios.

## Modules

In 2019 I split the ten journeys into modules where functionality repeated: fewer screens to build, and employees learn the app once. The 2026 version keeps that idea and makes it stricter. Twelve modules, from verifying identity to handing over to a person, and every scenario is built only from them.

Two channels, one system. Digital Hub lives in Teams for every day. The Digital Hub website does everything too, and it is the way in when Teams is out of reach, for example with a locked password. A conversation started in one continues in the other, and nothing is asked again.

Every step the employee takes has a channel: they write in Teams, tap a button on a card, or open the website on their phone. Nothing happens in their head.

Visual: [D26-5] Module map.

## Handoff to people

Three rules decide when a person steps in.

- **A person gets the whole story.** Who the employee is, what happened, what was tried, the logs. Nobody asks the employee anything again.
- **Risky actions wait for a yes.** Wiping a device, giving access to client data or spending beyond the policy always waits for a person to confirm.
- **Solved means it stays solved.** The target is that nine cases in ten never reach the help desk, and a case counts only if it does not come back.

Visual: [D26-3] Handoff, confirmation and the target.

## The live demo

All ten scenarios run in a live demo, built from the same twelve modules as the diagrams. Next to the chat, a "Behind the scenes" panel shows which agent acts and which system it uses at every step.

Today the agents' answers are scripted. Next, a real intake agent reads what the employee writes and routes it, so the logic above can be tried live. Mobile first, then desktop.

## Result

To write once measured.

## Lessons learned

To write at the end.

# What we decided

Everything we agreed on, so nothing gets lost. Newest decisions win. Last update: 26 November 2026.

## Two documents

- **The case study** (case/case.md) is short: the story and Sandy's decisions, for hiring managers. 2019 gets two or three sentences and a link to the 2019 case study.
- **The technical document** (case/technical.md) holds the full system: rules, stack, architecture, agents, scenarios, modules, handoff, rollout. One link to it from the case.
- Every change goes into both at once: short in the case, in full in the technical document.

## The logic

- The starting point is still the ten most common requests from EY's discovery in 2019.
- They are sorted by one question: does solving it need a decision?
  - **No decision (5):** ordering a device, an assistant's access to Outlook, a Teams channel, a password reset, a meeting room.
  - **Decisions needed (5):** a failed software install, VPN at a hotel, client files in Canvas, a scam email, a stolen laptop.
- Every request takes one of three paths after the intake agent:
  1. **Simple action: a fixed flow.** No model decides anything. The employee chooses, the systems act.
  2. **Problem: a domain agent.** It has a goal, its own tools, its own library and its limits, and leads the case itself.
  3. **Nothing fits: a ticket to the right team.** The intake agent fills it and routes it to the ServiceNow group. The team has its own agent that works for its engineers.
- A ticket is not where agents stop. Every second-line team has an agent: it reads the ticket and the history, suggests what to do, prepares actions. An engineer decides.
- What the second line solves goes back to the first line as knowledge or a new fix, after an engineer approves it.
- The old plan (fixed journeys first, then a switch to one large orchestrator) is dropped. It was a bot with a router.
- **Before anyone asks:** the watcher agent reads telemetry, opens the case itself and gives it to the domain agent. Proactive support was the heart of 2019; it stays at the center.
- Checked against the market in November 2026 (ServiceNow EmployeeWorks and AI specialists, Moveworks, Salesforce, Microsoft Agent 365 and Entra Agent ID, Anthropic and IBM guidance on workflows and agents). The logic matches current practice. Three gaps were closed: one lead agent per case, proactive support as its own path, two numbers per agent.

## Agents

- Many small agents, one per domain, not one big agent:
  - **Security:** passwords, stolen devices, scams, locked accounts. Wipes only once the employee is verified.
  - **Devices:** ordering and replacing devices, hardware faults. Never wipes.
  - **Software:** installs and repairs, VPN, apps. Never runs a new fix before an engineer approves.
  - **Mail, calendar and Teams:** delegation, mailboxes, channels. Never reads the content of mail.
  - **Workplace:** rooms, desks, facilities.
  - **Watcher:** reads telemetry and opens cases before people notice. Never changes a device.
- Each agent runs the fixed flows of its domain and solves its problems within its limits.
- Every case has one lead agent. It brings in other agents when the problem crosses domains (VPN: Software leads, asks Security about the account; stolen laptop: Security leads, Devices orders the replacement). The employee talks to one agent the whole time.
- Each agent has its own library of how its domain works, and searches only that library.
- Limits for each agent: what it does alone, what waits for the employee's yes, how many tries before it brings in a person, what it never does.
- Independence grows one action at a time: first the agent proposes and a person decides, then it acts alone in simple cases, then within its full limits. An action moves up only after it has worked on real cases.
- Cost: flows and domain agents run on small models. The large model works only where cases are few and hard: team agents and drafting new fixes.
- Two numbers per agent: how many cases it is allowed to take, and how many of those it solves (ServiceNow's own first-line agent: 15% of incidents eligible, 46% of them solved). A case counts only if it does not come back.
- The case cites Gartner in small print: over 40% of agentic AI projects canceled by the end of 2027, and "agent washing". Digital Hub uses an agent only where a flow cannot do the job.
- New things come from ticket labels: a frequent simple request becomes a new fixed flow, a frequent problem becomes a new skill for its domain agent.

## Rules for the employee's experience

- The agents are a means to an end. The demo shows the employee's experience. The agent side only explains it.
- Every request leaves a record, even when agents do all the work: REQ for requests, INC for incidents. The employee never has to look at it.
- The journey decides, the agent speaks. An agent may come back once, by itself.
- Visio "Later": "Shall I remind you in 15 minutes?" After 15 minutes the agent starts the install itself, and the employee can cancel. Cancel: no more reminders, the request stays open for the service desk.
- Declining a fix: "Is it urgent?" Yes: straight to a person, no more questions. No: "Shall I file a ticket?" Yes: file it and give the number. Never mind: cancelled.
- A stolen laptop: the employee confirms it is them in Authenticator, then the laptop is locked and wiped at once, without asking.
- Confirmation means "it is me", not "yes, wipe it".
- Never ask again what the employee already said.
- Give real choices: a catalog of monitors and where to deliver, a level of access for an assistant (see the calendar, manage the calendar, calendar and email).
- Clearing temporary files is not risky: the agent just does it and says so.
- Tracy (live support) is played by a large model with a face and the support playbook. She gives real next steps right away; she never says "I am looking into it" and stops.

## The demo

- Phone only. No laptop view.
- Three journeys switched on, each showing something different:
  - **New device:** a small shop.
  - **Assistant's Outlook:** a choice of the level of control.
  - **Software install (Visio):** the agent fails twice and a person takes over with the whole story.
- "Something else" shows how a ticket is filed. The other seven journeys stay in the code, switched off (`ON` list in `app/index.html`). A request for one of them files a ticket.
- The right panel: "Version 1: fixed journeys", big buttons, then "You can describe these problems in your own words. The agent understands them too." Version 2 is not mentioned until it exists, and then it is a link.
- A button types the sentence into the input, quickly, then sends it. The model still picks the journey.
- Messages arrive one at a time: a short pause with "typing" before every card.
- Time passes with a clock on the right, not a button.
- Start again: a circular-arrow icon at the top right.
- No placeholder text in the input.
- No Microsoft logos; purple is allowed. No dark text on dark fills. No arrows in links or buttons.

## Next

- Rebuild the demo on the new logic: real domain agents with tools and limits, starting with the Software agent for Visio.
- Decide how each of the five problem cases is solved by its agent.
- Redraw D26-1 (what changes) and D26-7 (delivery plan) for the new logic. D26-2 (architecture) is redrawn.
- Later: the "how is my Visio?" status demo from saved requests; a user test with 5 people; Result and Lessons in the case; rotate the API key.

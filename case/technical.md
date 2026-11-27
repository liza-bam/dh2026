# Digital Hub, 2026: how it works

The technical document behind the case study: the full logic, architecture, agents, scenarios and rules. Diagram IDs refer to `diagrams.html`.

## Header

**Title:** Digital Hub, 2026

**Subtitle:** In 2019 I designed IT support for EY that fixes problems before people notice them. In 2026 I rebuilt it with AI agents, on my own.

**Role:** UX, product and service designer. Service design, agent architecture, prototype.

**Timeline:** 2019–2020 proposal for EY at Wipro; 2026 rebuild.

**Links:** live demo (when built), 2019 case study, diagrams.

## TL;DR

**Problem.** EY employees work on tight client deadlines, but one IT issue meant 3+ support channels, 30%+ of cases lost between teams, and the same checks again and again. In 2019 I designed Digital Hub to solve problems before people noticed them, but every case the bot could handle had to be written in advance.

**What I did.** Took the 2019 service as the brief and rebuilt it with specialized AI agents: the same journeys, the same employee data, the same systems, with agents doing the work people had to script. Re-evaluated the stack, gave agents access the way people get it, and built a live demo.

## Where it started: 2019

In 2019, on Wipro's proposal for EY, I designed Digital Hub: one app for every IT issue, live status on every request, and support that acts before people notice a problem. I led a team of 7 through the ten journeys EY's discovery named, from password resets to lost laptops, and built them from shared modules so the same task always looked the same.

The delivery plan followed the same idea. The first journey, the laptop refresh, was the MVP. Every next journey reused its modules and added only what was unique to it, about two sprints each. The rollout went in waves: 500 people in the UK first, then 17,500; in the US and India, 20,000 first; in other countries, 500, then 2,000, then everyone, each in its own language. And the platform sat on top of EY's systems through APIs, so EY could change a system without changing what employees saw.

Digital Hub reached the final round of the bid. The client called it the strongest part of the proposal, and more than 50 later Wipro bids were built on it.

It had one limit. The AI bot could only handle cases someone had written in advance, and every proactive behavior was a separate script. Anything new became a ticket. That limit is where 2026 starts.

The support paths already followed the logic 2026 uses: monitoring finds a problem, AI scripts try to fix it, a person works the ticket when they fail, and every manual fix is checked for automation. Building it was the hard part: four teams (Digital Hub, Automation, ServiceNow, Genesys) and their vendors, agreements negotiated again and again, integrations written by hand, and a new script for every new case. It cost so much that manual support was cheaper.

What changed by 2026: the platforms ship their own agents (ServiceNow, Nexthink, SAP Ariba, Microsoft Defender), so they are connected rather than built; agents reach systems through standard connectors; an agent gets its own identity, like an employee (Microsoft Entra Agent ID), so access is agreed once; and small models cost little, about $300 a month for 10,000 employees. The 2019 paths can work now, with one change: AI only where a request needs a decision.

Visual: [D19-11] Support paths, 2019.

Visuals: [D19-1] First contact, [D19-2] Solving issues, [D19-5] Proactive support. The rest of D19 behind "see more diagrams".

## Three rules before any agent

### 1. It costs less than the help desk it replaces
Every solved case has a price: model calls, licences, the engineer who approves a new fix. Fixed flows and domain agents run on small, cheap models. The large model works only where cases are few and hard. Cost is measured per solved case, against the cost of the same case at the help desk.

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

## The logic: does it need a decision?

**Most IT support needs no AI.** The whole design follows from three decisions: what gets no AI at all, what goes to agents, and which agents.

The starting point is research: the ten most common IT requests at EY. I sort them by one question: does solving it need a decision?

Ordering a monitor does not. The steps are always the same, and the only choices are the employee's: which monitor, where to deliver it. A failed Visio install does. The next step depends on what the agent finds on the laptop, and the plan changes as it goes.

Of the ten, six need no decision: ordering a device, proxy access to mail and calendar, a Teams channel, a password reset, a stolen laptop, a scam email. Four do: a meeting room that does not work, a failed install, VPN at a hotel, client files that will not open. That leaves four problems for agents to think about, not ten.

A stolen laptop and a scam email look serious, but there is nothing for an agent to decide. The steps are always the same: confirm it is you, lock and wipe, sign out everywhere, a new password, a replacement. Microsoft Defender judges whether an email is a threat, and the real calls (was client data exposed, must the client be told) belong to the security team. Security must always be fast and never wrong, so it runs as fixed flows with a clean audit trail, not on a model's judgment.

Two more reasons keep models out of security actions. A scam email is text written by the attacker: a model that reads it and acts on it gives the attacker a way to instruct the agent. And models do help in security, but in a narrow role: Microsoft Defender uses them to triage reported email and to brief analysts, while the flows act and people decide.

The intake agent only recognizes that a message is about security. When in doubt, it sends the case to the security flow: a false alarm costs a minute, a missed attack costs far more.

So every request takes one of three paths.

### 1. Simple actions: fixed flows
Ordering a device, proxy access to mail and calendar, joining a Teams channel, resetting a password, a stolen laptop, a scam email, booking a room. The intake agent understands the request in the employee's own words and starts the flow. From there no model decides anything: the employee chooses, the systems act, and the same request goes the same way every time. Cheap, predictable, easy to audit.

Digital Hub adds no AI after the intake, but the platforms it calls may bring their own. An order goes to SAP Ariba, where Joule fills in the requisition with the contract supplier and routes the approval; the employee never searches Ariba.

Visual: [D26-14] Path 1: a fixed flow.

### 2. Problems: small agents, one for each domain
Not one big agent that knows everything. Small agents, each an expert in one domain, on small models: cheaper to run, safer because each can touch only its own systems, and easier to test before release.

Visual: [D26-15] Path 2: a domain agent.

A meeting room that does not work, a failed install, VPN at a hotel, client files that will not open. Each domain has its own agent: Devices; Software; Mail and calendar; Workplace. Security has no agent of its own: Microsoft Defender judges threats, the security team decides, and the rest runs as fixed flows. An agent gets a goal, its own tools, its own library of how things work in its domain, and its limits:
- what it does on its own, like clearing temporary files;
- what waits for the employee's yes;
- how many tries it gets before it brings in a person;

**Why a small agent is enough.** The system around it is strict:
- Every laptop starts from a standard image for its group: auditors, consultants, designers and a few others. The groups differ, but each image is fixed.
- Software comes from an approved catalog for each image, and installs centrally.
- Files live in OneDrive, not on the laptop.
- Agents have no open internet. Vendor knowledge (Microsoft, Adobe) goes into their libraries in advance, checked and kept up to date. An agent that searches forums can find a wrong fix or a page with hidden instructions, and nobody can test it in advance.

So the agent knows what each laptop should look like. A diagnosis is the difference between the laptop and its image, and fixing it means bringing the laptop back to the image.

Those rules make the fence. For the Software agent it has three steps:

1. **Does the program fail for many people?** The agent checks the service status itself. If yes, there is nothing to fix on this laptop, but the employee is never left stuck: the agent files a ticket, gives the number, and the Nexthink agent takes it (updates, network, system fixes). Nexthink brings its own agent, like Microsoft Defender does; we decide what to give it, not rebuild it.
2. **Does the employee have a license?** If not but they are entitled, the agent renews it. If they are not entitled, it fills in the request and sends it to the manager; once approved, it renews.
3. **Bring the laptop back to standard.** The smallest fix first: a known fix (clear a cache, switch the headset, turn off an add-in after a yes); then reinstall the program; then reset the laptop, which takes about an hour, so the agent asks when; then a person from IT with the whole story.

**Inside the fence the agent decides for itself.** The steps are its limits, not a script. It reads the laptop's data and skips what will not help. It weighs the person's situation. Take Visio twenty minutes before a client call: the data shows a broken installer cache and a fine disk, so no restart and no clean-up; fixing takes longer than twenty minutes, so the agent first solves the real problem ("Visio in the browser works now, here is your diagram"), and fixes the laptop after the call. A script does what was asked. The agent solves the problem.

**Other starts, other paths.** A lost or damaged file is not a software problem: most come back from the OneDrive recycle bin or an earlier version as a fixed flow, and the hard ones (client data, a deleted shared folder, two versions that clash) go to a stronger agent with a person. A program that is not on the approved list is never the small agent's call: a larger model checks the request and offers an approved alternative; if none fits, a person decides.

The agent does not need to understand everything. Anything outside its library goes to the second-line team.

Within those limits the agent leads the case itself: it checks, tries, changes the plan and tells the employee what is happening. Simple actions in its domain still run as fixed flows: the Devices agent does not improvise an order.

Many problems cross domains. A VPN that will not connect can be the app, the account or the hotel network. So every case has one lead agent, and it brings in the others when it needs them. For the VPN, the Software agent leads, checks the account and brings in the network team if the hotel network is the problem. For a meeting room, the Workplace agent leads and asks the Devices agent about the screen. The employee talks to one agent the whole time.

**The agents**
- **Devices:** ordering and replacing devices, hardware faults.
- **Software:** installs, repairs, VPN, apps.
- **Mail and calendar:** delegation, mailboxes, Teams channels.
- **Workplace:** rooms, desks, facilities.
- **Watcher:** reads telemetry and opens cases before people notice.

One rule for all of them: every agent has its own identity, touches only its own systems, answers only from approved knowledge, and every action is logged. Risky actions wait for a yes, and a new fix runs only after an engineer approves it.

**The Software agent: five cases, one ladder** (diagram [D26-8])
- **Visio will not install, with a client call in 20 minutes.** The data shows a broken installer cache, so no restart or clean-up. The call comes first: Visio in the browser now, the laptop fixed after the call. If the repair fails, a person takes over in a remote session.
- **Excel crashes on the client model.** The crash log points to an add-in: the agent offers to turn it off, and waits for a yes. A very large file: it opens in safe mode and recovers the autosave. Office itself is broken: the agent repairs it.
- **Outlook will not connect.** First the agent checks whether Microsoft 365 is down for everyone. If it is, there is nothing to fix on the laptop: it files a ticket for the Nexthink agent and gives the employee the number. If it is only this employee, it clears the cached sign-in and the Outlook profile.
- **No sound in a Teams call that starts in 10 minutes.** The device: switch the headset, update the driver. The network: say so, and suggest joining from the phone. The fastest fix first; the cause after the call.
- **Acrobat says the license has expired.** Entitled: the agent reactivates it. Not entitled: it fills in the request and sends it to the manager; once approved, it renews.

#### The Software agent in full

Defined the way ServiceNow defines its first-line AI specialist: a role, the kinds of problems it takes (its skills), the actions it can use (its tools), clear limits, and a rule for when to hand over.

**Role.** Brings a laptop's software back to its standard image, with as little of the employee's time as possible.

**Takes.** Software problems on one managed laptop: an app that will not install, crashes, will not connect, has no sound, or asks for a license. Anything else goes back to the intake agent, which picks another path.

**Tools.** Each one reaches a single system, within the agent's own rights.
- Read the laptop (Nexthink): disk, crashes, app versions, recent errors.
- Check the service (Microsoft 365 status, the vendor's status): does it fail for many people?
- File a ticket for the Nexthink agent (ServiceNow).
- Send the manager a request (Teams), filled in by the agent.
- Check the license (ServiceNow): is the employee entitled?
- Read the image and the catalog: what should be on the employee's laptop.
- Run a known fix (Intune): only fixes from the approved library.
- Reinstall an app (Intune): only apps from the catalog.
- Reset the laptop to its image (Intune).
- Show the employee a choice: a card with options, never a form.
- Hand over (ServiceNow): a ticket with the whole story, for a person or a team.

**Steps.** The fence: does it fail for many people; does the employee have a license; bring the laptop back to standard. Inside it, the agent chooses from the data and the person's situation.

**Limits.**
- **Does on its own:** reads anything on the laptop it was given; runs fixes marked harmless (clear a cache or temporary files, restart an app); reinstalls an app from the catalog.
- **Waits for a yes:** anything the employee would notice: turning off an add-in, restarting the laptop, resetting it to the image. For a reset it also asks when.
- **Acts only when the data points to one cause.** Two possible causes: one question to the employee. No clear cause: a person.
- **Gives up in time:** two fixes that did not work, or two questions without an answer, and a person takes over.
- **Never:** installs software outside the catalog, runs a fix that is not in the library, touches another laptop, or changes an account.

**Hands over with the whole story:** what the employee said, what the laptop showed, what was tried and what happened. Nobody asks again.

**Independence, step by step.** First supervised: the agent proposes each action and an engineer approves it. Then it acts on its own for harmless fixes. Then within its full limits. The same switch exists for ServiceNow's specialists, so a team can watch the agent before trusting it.

**Measured by:** how many cases it was allowed to take, how many it solved, how many came back, and why it handed over.

### 3. Everything else: a ticket to the right team, and that team's agent
When nothing fits, the intake agent fills a ServiceNow ticket and sends it to the right team: category, urgency, a summary, the device, a label. The ticket is not where agents stop. Every second-line team has its own agent, working for its engineers. It reads the ticket and the history, suggests what to do from the team's experience and prepares the actions. An engineer decides.

What a team solves goes back down. Its agent turns the solution into knowledge or a new fix for the first line, an engineer approves it, and next time the same case never becomes a ticket.

Visual: [D26-16] Path 3: a team agent.

### Before anyone asks
In 2019 the heart of Digital Hub was support that acts before people notice a problem. In 2026 that is the watcher agent. It reads device telemetry, finds the disk that is almost full or the VPN app that is out of date, opens the case itself and gives it to the right domain agent. The agent fixes it quietly, or tells the employee in one message what it did. The best request is the one nobody has to make.

### How it grows
- **New flows and new skills.** Ticket labels show what people ask most. A frequent simple request becomes a new fixed flow. A frequent problem becomes a new skill for its domain agent.
- **More independence, one action at a time.** An agent starts by proposing while a person decides. Then it acts on its own in simple cases, then within its full limits. Each action moves up only after it has worked on real cases.
- **The rollout of 2019 stays.** The same waves, the same reuse of modules: the first ten requests, then whatever the labels show next.

### What we measure
One number hides too much, so agents get two. How many cases an agent is allowed to take, and how many of those it solves. ServiceNow's own first-line agent shows why: 15% of incidents are eligible for it, and it solves 46% of those. Digital Hub grows both numbers, one action at a time. A case counts as solved only if it does not come back.

### What it costs

An estimate, not a measurement, per 10,000 employees a month.

**Volume.** MetricNet's benchmarks put the average at about 1.3 first-line tickets per user a month: about 13,000 requests.

**Today, with people.** MetricNet's 2023 North American average is $20.61 per contact (fully loaded). 13,000 × $20.61 ≈ $268,000 a month. Desktop support costs more per ticket (about $62 to $70), and an escalated ticket costs the sum of every level it passes.

**With Digital Hub, the models:**
- Intake agent: about $0.0001 a request, measured in the demo on a small model ($0.10 per million tokens in, $0.50 out). 13,000 requests ≈ $1.30.
- Fixed flows: no model decides anything, so no model cost beyond the intake.
- Domain agents: assume 40% of requests (5,200) at about $0.01 each on a small model, a few tool calls per case ≈ $52.
- Team agents: assume 10% (1,300) at about $0.20 each on a large model ($2 per million tokens in, $10 out), with long histories ≈ $260.
- Total ≈ $315 a month.

**Where the money really is.** The models are a rounding error next to people. The saving comes from requests that never reach a person, and from the employee's time: MetricNet estimates that an avoided first-line ticket saves the user about 20 minutes. 13,000 requests × 20 minutes ≈ 4,300 hours a month. At a firm that bills its people's time to clients, that is the bigger number.

**Not counted.** ServiceNow, Nexthink and Microsoft licenses (EY already pays for them), the engineers' time approving new fixes, building and testing the agents, and the people who still handle what agents cannot. The 40% and 10% shares are assumptions; the demo would measure the real ones.

Sources: MetricNet benchmarks via HDI (2020: tickets per user, cost per level, time saved; 2023: cost per contact).

### Why this works
Most requests are simple, and simple requests run on flows and small models, so the first rule holds from day one. The large model works where cases are few and hard: for the teams' agents and for drafting new fixes. People are at every level, and the higher the level, the more people decide.

Agents go only where a decision is needed. Everything else stays a cheap, predictable flow.

The logic was checked against the market in November 2026: ServiceNow's AI front door and AI specialists, Moveworks, Salesforce, Microsoft Agent 365 with Entra Agent ID, and Anthropic's and IBM's guidance on workflows and agents. It matches current practice: one way in, narrow agents with the rights of the role, fixed workflows where logic is fixed, and independence that grows step by step.

<small>Gartner expects over 40% of agentic AI projects to be canceled by the end of 2027 because of cost, unclear value or weak risk controls, and warns about "agent washing": chatbots and RPA renamed as agents. Digital Hub uses an agent only where a flow cannot do the job.</small>

Visual: [D26-7] Delivery plan (to redraw).

## Architecture

Nine layers, each with one job.

1. **Channels.** Teams, the Digital Hub website, email and voice. It is one conversation, wherever it starts.
2. **Intake agent.** Reads every request and sends it down one of the three paths: a fixed flow, a domain agent or a team. Small model. Changes nothing in any system itself.
3. **Domain agents.** Devices; Software; Mail and calendar; Workplace. Each runs the fixed flows of its domain and solves its problems within its limits. Every case has one lead agent, which brings in the others. The watcher agent reads device telemetry and opens cases before people notice. All run on small models, each with its own identity and only the rights its domain needs.
4. **Team agents.** One for each second-line team, working for the engineers, not the employees. Large model: few cases, hard ones.
5. **Enterprise agents.** Microsoft Defender, ServiceNow and Genesys bring their own agents, data and audit. Ours ask them; we do not rebuild them.
6. **Knowledge.** A library for each domain and each team. Agents answer only from approved EY sources, with a link to the source.
7. **Systems.** ServiceNow, Workday, Entra ID, Intune, Nexthink, Office 365 and SAP Ariba, reached through their MCP servers and only within the rights of the agent and the employee.
8. **Governance.** Every agent is registered, tested on real scenarios before release, has a budget and a level of independence for each action, and every action is logged.
9. **People.** Employees who approve, live support, engineers and the security team: the cases that need judgment.

Visual: [D26-2] Architecture, the simple version. The nine layers above are the detail behind it.

## Ten scenarios

The ten scenarios are the ten journeys from 2019, now run by agents. Each card shows how a scenario starts, which agent does the work, which systems it uses, what solved looks like, and when a person steps in. Three of the ten never reach the help desk at all: channel access, Outlook access for an assistant and ordering a peripheral.

Visual: [D26-4] The 10 scenarios.

## Modules

In 2019 I split the ten journeys into modules where functionality repeated: fewer screens to build, and employees learn the app once. The 2026 version keeps that idea and makes it stricter. Twelve modules, from verifying identity to handing over to a person, and every scenario is built only from them.

Two channels, one system. Digital Hub lives in Teams for every day. The Digital Hub website does everything too, and it is the way in when Teams is out of reach, for example with a locked password. A conversation started in one continues in the other, and nothing is asked again.

Every step the employee takes has a channel: they write in Teams, tap a button on a card, or open the website on their phone. Nothing happens in their head.

Visual: [D26-5] Module map.

## The flow decides, the agent speaks

Digital Hub combines fixed flows with AI agents, and each does what it is good at. The flow decides what happens and when: which system acts, which record is filed, when to come back. The agent decides how to say it and finds the right moment within those rules.

Take Visio. The employee taps Later. The flow files a request in ServiceNow, and the agent offers one reminder in 15 minutes. Then it comes back by itself and starts the install. If the employee cancels, the agent does not ask again, and the request stays open.

Two rules follow from this.

- **Every request leaves a record**, even when agents do all the work. The employee always has a number in My requests, but never has to look at it: the agent comes back. The records are also the data that new flows and agent skills grow from.
- **An agent comes back once.** More than that is nagging.

If the agent decided on its own whether to come back, the same request could go differently each time, and nobody could test it before release.

## Rules for the employee's experience

- **Never ask twice.** If the employee has already said what happened, nobody asks again: not the agent, not a person.
- **Real choices, not yes or no.** A catalog of monitors and where to deliver. A level of proxy access: see the calendar, manage the calendar, calendar and email.
- **Harmless steps need no question.** Clearing temporary files is not risky: the agent does it and says so.
- **Declining is a choice, not a dead end.** Not now: "Is it urgent?" Yes: straight to a person, no more questions. No: "Shall I file a ticket?" Yes: it is filed and the number given. Never mind: cancelled.
- **Confirmation means "it is me".** A stolen laptop: the employee confirms who they are in Authenticator, and the laptop is locked and wiped at once, without a second question.
- **A person who joins gives real help at once.** Live support works from the same approved playbook as the agents and starts with next steps, not "I am looking into it".

## Handoff to people

Three rules decide when a person steps in.

- **A person gets the whole story.** Who the employee is, what happened, what was tried, the logs. Nobody asks the employee anything again.
- **Risky actions wait for a yes.** A lost laptop is wiped as soon as the employee confirms it is them. Giving access to client data or spending beyond the policy always waits for a person to approve.
- **Solved means it stays solved.** The target is that nine cases in ten never reach the help desk, and a case counts only if it does not come back.

Visual: [D26-3] Handoff, confirmation and the target.

## The live demo

The live demo runs on a phone, inside a Teams-like frame: https://digital-hub-demo.alexandra-tayts.workers.dev

- A real intake agent on a small model reads what the visitor writes and picks the path. Its cost is shown for every request.
- Three journeys are switched on, each showing something different: a new monitor (a small shop), proxy access to mail and calendar (a choice of the level of control), and a failed Visio install (the agent fails twice and a person takes over with the whole story). The other seven stay in the code, switched off; a request for one of them files a ticket.
- Tracy, the live support person, is played by a larger model with a face and the support playbook.
- Next to the phone, "How it runs" shows every agent and system as it acts: its model, memory, tools and cost.
- Next: the domain agents become real agents with tools and limits, starting with the Software agent for Visio.

## Lessons learned

To write at the end.

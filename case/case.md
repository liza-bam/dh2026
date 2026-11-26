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

To write, short. The 2019 proposal: ten journeys, one front door, proactive support, a team of 7, final round of the bid, 50+ later Wipro bids built on it. What it could not do: every case had to be written in advance, so anything new became a ticket.

Visuals: [D19-1] First contact, [D19-2] Solving issues, [D19-5] Proactive support. The rest of D19 behind "see more diagrams".

---

## Three rules before any agent

### 1. It costs less than the help desk it replaces
Every solved case has a price: model calls, licences, the engineer who approves a new fix. Simple cases run on small, cheap models. The large model only decides and hands over. Cost is measured per solved case, against the cost of the same case at the help desk.

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

Visual: stack scorecard (to draw: D26-6).

---

## Architecture

To write after the redraw. Eight layers: channels; front door agent with no write access; specialized agents with limited access; enterprise agents from the vendors; knowledge layer (answers only from approved EY sources); systems through MCP; governance and audit; people.

Visuals: [D26-1] What changes, [D26-2] Architecture (to redraw).

## Ten scenarios

To write. Visual: [D26-4] The 10 scenarios.

## Modules

To write. Two channels, one system: Digital Hub in Teams every day, the Digital Hub website for everything too, and for the moments Teams is out of reach (a locked password). A conversation started in one continues in the other. Every scenario is built from the same modules, so the same task always looks the same. Visual: [D26-5] Module map.

## Handoff to people

To write. Visual: [D26-3] Handoff, confirmation and the target.

## The live demo

To write once built. Mobile first, then desktop.

## Result

To write once measured.

## Lessons learned

To write at the end.

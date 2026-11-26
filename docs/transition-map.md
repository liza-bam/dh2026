# Digital Hub 2019 → 2026: transition map

The 2019 diagrams are the brief. The service, the journeys, the employee data and the platforms stay the same. What changes is who does the work: in 2019 every case the bot could solve had to be written in advance; in 2026 agents act on the same systems, and people get only the cases that need judgment.

## 1. Component map

| 2019 diagram | What it did | 2026 |
|---|---|---|
| Digital Hub app, chat, voice, email | One front door for every channel | Same front door. Every channel talks to one agent team |
| Initial customer data (Workday, Office, Nexthink, ServiceNow) | Every channel knew who was asking | Context the agents load at the start of every conversation |
| Avaamo bot + NLP library (40+ cases) | Answered cases written in advance | Front door agent: understands any request and routes it to the right agent |
| AI scripts library (Wipro Holmes), built in discovery | Fixed known issues | Fix agent runs the library and drafts new scripts; an engineer approves them before they join the library |
| Preventive measures (Nexthink monitoring) | Found problems before people reported them | Watcher agent reads the same telemetry and opens cases on its own |
| AI issue triage: urgency, sentiment | Decided when to call a person | Handoff rules (section 4), the same signals |
| ServiceNow ticket | Record of every case | Same. Agents create and update tickets themselves |
| Approval structure (Workday) | Automatic, manual, expert approval | Same structure. Agents ask the approver in Teams; the approver decides |
| Genesys agent dashboard, live agent, swarming | A person takes over with all the data | Same. The handoff card carries what the agents already did |
| Push notifications (desktop and mobile) | Kept the employee informed | Same, sent by the agents |
| Feedback and sentiment analysis (ZTC) | Measured the service | Metrics: share of cases solved without the help desk, repeat contacts, sentiment |

## 2. Agents

| Agent | Scenarios | Systems (tools) |
|---|---|---|
| Front door | All: understands the request, loads the employee's data, routes, keeps the conversation | Workday, ServiceNow, Office 365 |
| Identity | Password reset | Azure AD |
| Workplace | Meeting room problems | Office 365 rooms and calendar, room devices |
| Access | Teams channel access, client files in Canvas, Outlook access for a new assistant, software requests | Azure AD, Office 365, ServiceNow catalogue, Workday approvals |
| Devices | Lost laptop, ordering a peripheral, laptop refresh, data transfer | ServiceNow CMDB, SAP Ariba, DigiLocker, Nexthink |
| Fix | VPN offsite, failed software installation, other troubleshooting | Nexthink diagnostics, script library |
| Security | Email scam | Mail, Azure AD |
| Watcher | Proactive: downtime, failures, refresh readiness | Nexthink, ServiceNow |

## 3. The 10 scenarios

| Scenario (2019 slide) | Agent | Solved without the help desk | A person steps in when |
|---|---|---|---|
| Collaborating remotely from an office meeting room | Workplace | Rebooks an identical room, files a facilities request | The room equipment needs a repair visit |
| VPN access: files on the EY network offsite | Fix | Finds the likely cause, fixes the client or guides the employee | The problem is on the network side |
| Password reset | Identity | Always, through the one-time code | Sign-in risk looks like an attack |
| Access to a Teams channel | Access | The channel owner approves in Teams | Never the help desk |
| Reporting a lost laptop | Devices | Locks and wipes, changes the password, fills the forms, orders a replacement | Client data was on the laptop: the security team |
| Client files in the Canvas app | Access + Fix | Checks the engagement, asks the owner, fixes app errors on the device | The error is in the app itself |
| Outlook access for a new assistant | Access | Sets the delegation after the mailbox owner confirms | Never the help desk |
| Ordering a peripheral | Devices | Compatible, in stock, locker or vending machine; bundles approve automatically | Outside the bundle: the manager approves |
| Reporting an email scam | Security | Removes similar messages for everyone | The employee entered their password: reset plus the security team |
| Failed software installation | Fix | Finds the cause, fixes, installs again, drafts a script | Two fixes failed, or the employee is frustrated |

Proactive (Watcher): downtime and possible failures, refresh readiness, data transfer to the new laptop.

## 4. Handoff to a person

The agent hands the case over when:
- two fixes did not work;
- the employee is frustrated (sentiment), or the case is urgent;
- it needs a physical repair;
- it is an exception to policy;
- it is a security incident;
- the employee asks for a person.

The handoff card carries the employee's data, what happened, what the agents tried and the logs. The person does not ask again.

## 5. What agents never do without confirmation

Wipe a device, give access to client data, spend money beyond the policy. Every action is logged.

## 6. Metrics

- Share of cases solved without the help desk, per scenario. Target: 90%.
- Repeat contacts: a case that comes back within a few days does not count as solved.
- Sentiment before and after, as in the 2019 feedback flow.

## 7. What we build

1. Case study: the story, the 2019 diagrams, the 2026 architecture, results.
2. Application: Digital Hub 2026 with live agents on mock systems. Mobile web app first (from the 2020 mobile wireframes), then desktop.
3. Live demo limits: about 10 messages per visitor, a limit per address, a monthly spend limit.

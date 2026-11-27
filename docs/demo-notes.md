# Demo notes

Working notes for building the live demo. The logic, architecture, agents and rules of the experience live in the technical document (case/technical.md), not here.

## How we work

- Two documents: the short case study (case/case.md) and the technical document (case/technical.md). Every change goes into both at once: short in the case, in full in the technical document.
- No Result section and no numbers: this is Sandy's own project, made to show she can do this kind of work.
- The ten requests come from research; the year does not matter.

## What is in the demo now

- Phone only, in a Teams-like frame. No laptop view.
- Three journeys switched on: New device (a small shop), Proxy access (a level of control), Software install (Visio: the agent fails twice and a person takes over). "Something else" files a ticket.
- The other seven journeys stay in the code, switched off (`ON` list in `app/index.html`). A request for one of them files a ticket.
- Right panel: "Version 1: fixed journeys", large buttons, then "You can describe these problems in your own words. The agent understands them too." Version 2 is not mentioned until it exists, and then it is a link.
- A button types the sentence into the input quickly, then sends it. The real intake model still picks the journey.
- Messages arrive one at a time: a short pause with "typing" before every card.
- Time passes with a clock on the right, not a button.
- Visio "Later": "Shall I remind you in 15 minutes?" After the clock, the agent starts the install itself, with Cancel. Cancel: no more reminders, the request stays open.
- Every request gets a REQ or INC number in My requests, saved in the browser for a later "how is my Visio?" demo.
- Tracy (live support) is a larger model with a face and the support playbook.
- Start again: a circular-arrow icon at the top right. No placeholder text in the input.
- No Microsoft logos; purple is allowed. No dark text on dark fills. No arrows in links or buttons.

## Next

1. Study how ServiceNow builds its agents and write what we take into the technical document.
2. Design the five problem cases in detail.
3. Build the Software agent as a real agent with tools and limits: Visio, Excel, Outlook, Teams sound, Acrobat. Only tools everyone knows. The fictional client is Halden; client files live in SharePoint.
4. Test it with 20 to 30 runs.
5. Draw the main visual of the case: five and five, and the three paths. Redraw or drop D26-1 and D26-7.
6. Lessons learned, screenshots or a short video of the demo.
7. Move it all to https://sandy.tayts.com when Sandy says so. The case lives in Experiments and shows under a new "Agent design" pill (a filter, with Loomik, Pleasant Street Pipeline and the site maker); a one-line link from the EY case, and a link back to it.
   After this case: when any pill is selected, projects and work show in one grid, not split into sections.
8. Rotate the API key.

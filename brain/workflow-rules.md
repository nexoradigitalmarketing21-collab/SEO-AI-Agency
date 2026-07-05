# Workflow Rules - Nexora AI SEO Agency

## Purpose

This document defines the standard workflows, procedures, and coordination rules that all agents must follow. It ensures consistent, efficient, and high-quality delivery across all client projects.

---

## Complete Agency Workflow

### End-to-End Client Journey

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. LEAD ACQUISITION                                              │
│    - Client inquiry via platform (Upwork, Fiverr, etc.)          │
│    - Sales Agent qualifies lead                                  │
│    - Initial consultation call                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. PROPOSAL & CONTRACT                                           │
│    - Sales Agent creates custom proposal                         │
│    - Uses sales/[platform]-proposal-template.md                 │
│    - Client reviews and negotiates                               │
│    - Contract signed, deposit received                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. PROJECT KICKOFF                                               │
│    - Project Manager creates project plan                        │
│    - Client onboarding completed                                 │
│    - Access credentials collected                                │
│    - Kickoff meeting scheduled                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. STRATEGY DEVELOPMENT                                          │
│    - SEO Strategist conducts discovery                           │
│    - Creates comprehensive SEO strategy                          │
│    - Client reviews and approves strategy                        │
│    - CEO Agent reviews for alignment                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. EXECUTION (Parallel Agents)                                   │
│    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│    │ Technical SEO │  │   Keyword    │  │    Content   │        │
│    │    Agent      │  │ Research Agent│  │  Writer Agent│        │
│    └──────────────┘  └──────────────┘  └──────────────┘        │
│    ┌──────────────┐  ┌──────────────┐                            │
│    │  On-Page SEO │  │    Local     │                            │
│    │    Agent     │  │     SEO      │                            │
│    └──────────────┘  └──────────────┘                            │
│    ┌──────────────┐                                             │
│    │ Link Building│                                             │
│    │    Agent     │                                             │
│    └──────────────┘                                             │
│    All agents consult brain/ for standards                        │
│    All deliverables follow templates                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. QUALITY ASSURANCE                                             │
│    - QA Agent reviews all deliverables                           │
│    - Checks against brain/quality-standards.md                  │
│    - Provides feedback and approval                              │
│    - Revisions made if needed                                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. REPORTING & DELIVERY                                          │
│    - Reporting Agent compiles deliverables                       │
│    - Creates client-ready reports                                │
│    - Uses deliverables/ templates                                │
│    - Final QA check                                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. CLIENT DELIVERY & FOLLOW-UP                                   │
│    - Client Success Agent presents to client                     │
│    - Walkthrough call scheduled                                  │
│    - Implementation support provided                             │
│    - Feedback collected                                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 9. ONGOING OPTIMIZATION                                          │
│    - Monthly reporting cycle                                     │
│    - Continuous optimization                                     │
│    - Client success monitoring                                   │
│    - Upsell opportunities identified                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Coordination Rules

### Sequential Workflows

**Definition:** Tasks that must be completed in order, where each step depends on the previous one.

**Examples:**
- Strategy → Execution → QA → Reporting
- Audit → Recommendations → Implementation → Verification

**Rules:**
1. Previous step must be approved before next begins
2. Clear handoff criteria defined
3. All outputs documented in project file
4. Timeline includes buffer for reviews

**Handoff Process:**
1. Completing agent marks task as "ready for review"
2. Next agent notified via project management tool
3. Receiving agent reviews and accepts or requests changes
4. Handoff documented with timestamp and notes

### Parallel Workflows

**Definition:** Tasks that can be executed simultaneously by different agents.

**Examples:**
- Technical SEO + Keyword Research + Content Strategy (during discovery)
- Multiple page optimizations (during on-page SEO)
- Multiple platform optimizations (during local SEO)

**Rules:**
1. All parallel tasks must have clear boundaries
2. No dependencies between parallel tasks
3. Integration point defined where outputs combine
4. QA reviews all parallel outputs together

**Coordination:**
- Daily sync between parallel agents
- Shared project timeline
- Centralized documentation
- Clear ownership of each component

### Feedback Loops

**Definition:** Iterative cycles where output is reviewed, feedback is provided, and improvements are made.

**Examples:**
- Draft → Review → Revision → Final
- Strategy → Client Feedback → Refinement → Approval

**Rules:**
1. Maximum 3 revision rounds (per agency-rules.md)
2. Feedback must be specific and actionable
3. 48-hour turnaround for revisions
4. Escalate if consensus cannot be reached

**Feedback Format:**
```
- What: Specific element needing change
- Why: Reason for change
- How: Suggested improvement
- Priority: High/Medium/Low
```

---

## Quality Gates

### Gate 1: Strategy Approval

**When:** After SEO Strategist completes strategy document

**Who Reviews:**
- SEO Strategist (self-review)
- CEO Agent (strategic alignment)
- Client (approval to proceed)

**Criteria:**
- [ ] Strategy aligns with client goals
- [ ] Data supports recommendations
- [ ] Timeline is realistic
- [ ] Budget is appropriate
- [ ] Risks identified and mitigated
- [ ] Success metrics defined

**Cannot Proceed Until:**
- Client written approval received
- All questions answered
- Budget confirmed

### Gate 2: Execution Review

**When:** After all execution agents complete their work

**Who Reviews:**
- QA Agent (quality check)
- SEO Strategist (strategic alignment)
- Client (major deliverables)

**Criteria:**
- [ ] All deliverables meet quality-standards.md
- [ ] All templates completed
- [ ] No placeholder text
- [ ] Data verified and sourced
- [ ] Recommendations actionable
- [ ] Implementation guidance clear

**Cannot Proceed Until:**
- QA approval received
- All revisions completed
- Client approval for major items

### Gate 3: Final Delivery

**When:** Before delivering final package to client

**Who Reviews:**
- QA Agent (final quality check)
- Reporting Agent (completeness)
- CEO/PM (strategic review for large projects)

**Criteria:**
- [ ] All deliverables compiled
- [ ] Professional presentation
- [ ] Branding applied
- [ ] Executive summary included
- [ ] Next steps clearly defined
- [ ] All files organized

**Cannot Proceed Until:**
- Final QA approval
- All files ready for delivery
- Client communication planned

---

## Agent Handoff Procedures

### Standard Handoff Process

**Step 1: Preparation (Completing Agent)**
- Complete all work per requirements
- Run self-quality check
- Document all decisions and assumptions
- Prepare handoff notes
- Mark task as "ready for handoff" in project management tool

**Step 2: Notification**
- Notify receiving agent via project management tool
- Include: project name, deliverables, timeline, special notes
- Tag relevant stakeholders

**Step 3: Review (Receiving Agent)**
- Review all deliverables
- Check against requirements
- Verify quality standards met
- Ask questions if unclear

**Step 4: Acceptance or Revision Request**
- Accept: Mark as "in progress" and begin work
- Request revisions: Provide specific feedback, return to completing agent

**Step 5: Documentation**
- Document handoff in project file
- Include: timestamp, agents involved, deliverables, notes
- Update project timeline

### Handoff Criteria

**Must Have:**
- All required deliverables completed
- Quality standards met
- Clear documentation
- No blocking issues

**Nice to Have:**
- Recommendations for next steps
- Lessons learned
- Additional context
- Suggested improvements

---

## Timeline Standards

### Project Timeline Templates

**SEO Audit Project:**
- Week 1: Discovery and data collection
- Week 2: Technical audit
- Week 3: Analysis and recommendations
- Week 4: Report writing and QA
- Week 5: Client delivery and presentation

**Keyword Research Project:**
- Week 1: Discovery and seed keywords
- Week 2: Research and analysis
- Week 3: Clustering and prioritization
- Week 4: Report and delivery

**Content Strategy Project:**
- Week 1: Discovery and research
- Week 2: Strategy development
- Week 3: Content calendar creation
- Week 4: Documentation and delivery

**Ongoing SEO (Monthly):**
- Week 1: Reporting (previous month)
- Week 2: Strategy adjustments
- Week 3: Implementation
- Week 4: Planning (next month)

### Timeline Rules

**Buffer Time:**
- Always include 20% buffer for unexpected issues
- Build in time for client feedback
- Account for QA and revision cycles

**Critical Path:**
- Identify tasks that cannot be delayed
- Focus resources on critical path
- Communicate delays immediately

**Milestones:**
- Define clear milestones
- Track progress against milestones
- Alert stakeholders if milestone at risk
- Celebrate milestone achievements

---

## Reporting Cadence

### Client Reporting Schedule

**Weekly (Active Projects):**
- Status update email
- Progress against milestones
- Upcoming tasks
- Any issues or blockers
- Next steps

**Monthly (Ongoing Clients):**
- Comprehensive performance report
- KPI dashboard
- Wins and challenges
- Recommendations for next month
- Strategy adjustments

**Quarterly (All Clients):**
- Strategic review
- ROI analysis
- Goal setting for next quarter
- Relationship building
- Upsell opportunities

**Annually:**
- Year in review
- Growth metrics
- Case study development
- Strategy refresh
- Contract renewal discussion

### Internal Reporting

**Daily:**
- Agent standup (15 minutes)
- Progress updates
- Blocker identification
- Resource needs

**Weekly:**
- Agency-wide status meeting
- Project reviews
- Quality metrics review
- Client feedback discussion
- Knowledge sharing

**Monthly:**
- Financial review
- Capacity planning
- Agent performance review
- Process improvements
- Strategic initiatives

**Quarterly:**
- Business review
- Market analysis
- Competitive review
- Technology assessment
- Annual planning

---

## Escalation Procedures

### When to Escalate

**Escalate Immediately:**
- Client threatens to leave
- Website down or critical issue
- Budget exceeds $10,000
- Ethical concern
- Security breach
- Agent conflict cannot be resolved

**Escalate Within 24 Hours:**
- Timeline at risk
- Major blocker identified
- Quality standard cannot be met
- Client complaint received
- Resource constraint

**Escalate Within 3 Days:**
- Strategy change needed
- Scope creep identified
- Agent needs support
- Process improvement identified

### Escalation Path

**Level 1: Peer Resolution**
- Agents attempt to resolve directly
- 24-hour timeout if unresolved
- Document all attempts

**Level 2: Project Manager**
- PM reviews and decides
- Consults brain/ files
- Communicates decision
- Updates project plan

**Level 3: CEO Agent**
- CEO reviews complex issues
- Makes final decision
- Updates brain/ if needed
- Communicates to all stakeholders

**Level 4: Human Owner**
- For existential agency issues
- Final authority
- Strategic decisions

### Escalation Documentation

**Required Information:**
- Issue description
- Impact assessment
- Attempted solutions
- Recommended action
- Timeline sensitivity
- Stakeholders affected

**Format:**
```
ESCALATION REQUEST
==================
Date: [date]
From: [agent name]
To: [escalation target]
Priority: [Critical/High/Medium/Low]

ISSUE:
[Clear description]

IMPACT:
[What's affected]

ATTEMPTED SOLUTIONS:
[What was tried]

RECOMMENDATION:
[Suggested action]

TIMELINE:
[Urgency level]
```

---

## Project Management Standards

### Project File Structure

Every client project must have:

```
clients/[client-name]/
├── project-brief.md
├── contract.pdf
├── kickoff-notes.md
├── strategy/
│   └── seo-strategy.md
├── execution/
│   ├── technical-seo/
│   ├── keyword-research/
│   ├── content/
│   ├── on-page-seo/
│   ├── local-seo/
│   └── link-building/
├── deliverables/
│   ├── reports/
│   ├── presentations/
│   └── data/
├── communication/
│   ├── meeting-notes/
│   └── email-archive/
└── status/
    └── project-timeline.md
```

### Project Management Tools

**Required:**
- Project management platform (Asana, Monday.com, etc.)
- Document storage (Google Drive, Dropbox, etc.)
- Communication tool (Slack, Teams, etc.)
- Time tracking (if billable hours)

**Usage Rules:**
- Update project status daily
- Log all client communications
- Store all deliverables in project folder
- Track time against tasks
- Archive completed projects

### Status Reporting

**Project Status Levels:**
- 🟢 Green: On track, no issues
- 🟡 Yellow: At risk, mitigation plan in place
- 🔴 Red: Off track, immediate action required

**Status Update Must Include:**
- Current status (Green/Yellow/Red)
- Progress against milestones
- Completed tasks
- In-progress tasks
- Upcoming tasks
- Blockers and risks
- Next steps

---

## Communication Protocols

### Internal Communication

**Daily Standup:**
- Time: 9:00 AM
- Duration: 15 minutes max
- Format: What did I do? What will I do? Any blockers?
- All agents attend

**Project Updates:**
- Post in project channel
- Tag relevant agents
- Include status and next steps
- Update project management tool

**Decision Documentation:**
- Document all strategic decisions
- Include rationale
- Tag stakeholders
- Store in project file

### Client Communication

**Proactive Communication:**
- Weekly status updates (even if no news)
- Immediate notification of issues
- Celebrate wins together
- Be transparent about challenges

**Communication Templates:**
- Weekly status email template
- Issue notification template
- Milestone completion template
- Request for feedback template

**Response Times:**
- Critical: 2 hours (per agency-rules.md)
- Urgent: 4 business hours
- Standard: 1 business day
- Non-urgent: 2 business days

---

## Documentation Standards

### Required Documentation

**Project Level:**
- Project brief
- Strategy document
- Timeline and milestones
- Status reports
- Meeting notes
- Final deliverables

**Agent Level:**
- System prompts (in agents/)
- Workflows followed
- Decisions made
- Issues encountered
- Lessons learned

**Agency Level:**
- brain/ files
- knowledge-base/ files
- SOPs
- Templates
- Process documentation

### Documentation Rules

**When to Document:**
- All client interactions
- All strategic decisions
- All process changes
- All issues and resolutions
- All lessons learned

**Documentation Format:**
- Markdown for text documents
- PDF for final deliverables
- Excel for data
- PowerPoint for presentations

**Storage:**
- Centralized project folders
- Version control enabled
- Backed up regularly
- Accessible to all agents

---

## Continuous Improvement

### Process Review Cycle

**Monthly:**
- Review workflow effectiveness
- Identify bottlenecks
- Gather agent feedback
- Implement quick fixes

**Quarterly:**
- Comprehensive workflow review
- Benchmark against industry
- Update brain/workflow-rules.md
- Train agents on improvements

**Annually:**
- Complete workflow audit
- Strategic workflow planning
- Technology assessment
- Major process overhauls

### Improvement Process

**1. Identify:**
- Agent feedback
- Client feedback
- Performance metrics
- Bottlenecks identified

**2. Analyze:**
- Root cause analysis
- Impact assessment
- Solution options
- Cost-benefit analysis

**3. Implement:**
- Update brain/workflow-rules.md
- Update templates
- Train agents
- Communicate changes

**4. Monitor:**
- Track metrics
- Gather feedback
- Adjust as needed
- Document results

---

## Exception Handling

### When Workflows Cannot Be Followed

**Process:**
1. Document the exception
2. Explain why standard workflow cannot be used
3. Propose alternative approach
4. Get approval from Project Manager
5. Document exception with justification
6. Implement alternative
7. Follow up and document results

**Approval Levels:**
- Minor exception: Project Manager
- Major exception: CEO Agent
- Client-impacting: Client approval

**Documentation:**
- Record all exceptions
- Track patterns
- Use to improve workflows
- Share learnings

---

## Success Metrics

### Workflow Effectiveness

**Efficiency:**
- Project completion time vs. estimate
- Revision rounds per deliverable
- Agent utilization rate
- Handoff time

**Quality:**
- QA first-pass approval rate
- Client satisfaction score
- Error rate
- Rework percentage

**Client Satisfaction:**
- On-time delivery rate
- Communication satisfaction
- Process transparency
- Overall experience

**Agent Satisfaction:**
- Process clarity
- Tool effectiveness
- Support availability
- Workload balance

---

## Notes

- Workflows are guidelines, not rigid rules
- Common sense and client needs come first
- Document all deviations
- Continuously improve based on learnings
- brain/workflow-rules.md is living document
- CEO Agent has final say on workflow interpretation
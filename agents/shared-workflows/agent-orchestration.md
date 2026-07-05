# Agent Orchestration Workflow

## Purpose

This document defines how agents in the Nexora AI SEO Agency work together to complete SEO projects. It establishes the communication protocols, decision trees, and workflows that enable seamless collaboration between agents.

**Every agent must understand when and how to call other agents** to ensure efficient, coordinated project execution.

---

## Core Principle: No Agent Works in Isolation

Every agent is part of an integrated system. No agent should:
- Work alone on a complete project
- Make decisions outside their expertise
- Deliver directly to clients without QA
- Skip required collaboration steps

Instead, every agent should:
- Know their role in the workflow
- Understand when to call other agents
- Follow the established workflow
- Collaborate through defined handoffs

---

## Agency Workflow Overview

### Complete Client Journey

```
Client Request
     │
     ▼
Sales Agent (qualify & propose)
     │
     ▼
CEO Agent (approve & assign)
     │
     ▼
SEO Strategist (plan & coordinate)
     │
     ├──────────────────┐
     ▼                  ▼                  ▼
Keyword Agent    Technical SEO    Content Writer
     │             Agent              Agent
     │                  │                  │
     └────────┬─────────┘                  │
              │                            │
              ▼                            │
       Reporting Agent ◄───────────────────┘
              │
              ▼
         QA Agent
              │
              ▼
       Client Delivery
```

---

## Agent Roles & Responsibilities

### 1. Sales Agent
**Primary Role:** Client acquisition and relationship management

**Responsibilities:**
- Respond to client inquiries
- Qualify leads
- Create proposals
- Negotiate terms
- Onboard clients
- Manage client expectations

**When to Call Other Agents:**
- **CEO Agent:** For complex proposals, pricing approval, strategic decisions
- **SEO Strategist:** For technical questions, feasibility assessment, timeline estimates
- **QA Agent:** Before sending final proposals (quality check)

**Never:**
- Promise results without SEO Strategist input
- Set pricing without CEO approval
- Deliver technical analysis
- Create final reports

---

### 2. CEO Agent
**Primary Role:** Strategic oversight and decision-making

**Responsibilities:**
- Approve proposals and pricing
- Make strategic decisions
- Allocate resources
- Resolve conflicts
- Ensure quality standards
- Final client approval for major decisions

**When to Call Other Agents:**
- **Sales Agent:** For client updates, negotiation support
- **SEO Strategist:** For strategic planning, resource allocation
- **QA Agent:** For final quality approval before client delivery

**Never:**
- Write client communications (delegate to Sales)
- Perform technical analysis (delegate to specialists)
- Create deliverables (delegate to appropriate agents)

---

### 3. SEO Strategist
**Primary Role:** Strategic planning and coordination

**Responsibilities:**
- Analyze client needs
- Develop SEO strategies
- Create project plans
- Coordinate specialist agents
- Review deliverables for strategic alignment
- Ensure comprehensive coverage

**When to Call Other Agents:**
- **Keyword Research Agent:** For keyword strategy development
- **Technical SEO Agent:** For technical audits and fixes
- **Content Writer Agent:** For content strategy and briefs
- **Reporting Agent:** For performance tracking setup
- **QA Agent:** For quality review of strategies
- **Sales Agent:** For client communication about strategy
- **CEO Agent:** For strategic decisions, resource approval

**Never:**
- Execute technical implementations (delegate to Technical SEO)
- Write content (delegate to Content Writer)
- Perform detailed keyword research (delegate to Keyword Research)
- Create final reports (delegate to Reporting)

---

### 4. Keyword Research Agent
**Primary Role:** Keyword strategy and research

**Responsibilities:**
- Conduct keyword research
- Analyze search intent
- Identify opportunities
- Create keyword databases
- Develop content roadmaps
- Provide keyword recommendations

**When to Call Other Agents:**
- **SEO Strategist:** For strategy alignment, priority setting
- **Content Writer Agent:** For content briefs, keyword targeting
- **Reporting Agent:** For tracking keyword rankings
- **QA Agent:** For quality review of research

**Never:**
- Make strategic decisions (escalate to SEO Strategist)
- Write content (delegate to Content Writer)
- Communicate directly with clients (escalate to Sales/Strategist)

---

### 5. Technical SEO Agent
**Primary Role:** Technical analysis and implementation

**Responsibilities:**
- Conduct technical audits
- Identify technical issues
- Implement technical fixes
- Optimize site performance
- Implement schema markup
- Monitor Core Web Vitals

**When to Call Other Agents:**
- **SEO Strategist:** For strategy, prioritization
- **Reporting Agent:** For tracking technical metrics
- **QA Agent:** For quality review of implementations
- **Content Writer Agent:** For technical content needs

**Never:**
- Create content strategy (escalate to SEO Strategist)
- Write content (delegate to Content Writer)
- Communicate directly with clients (escalate to Sales/Strategist)

---

### 6. Content Writer Agent
**Primary Role:** Content creation and optimization

**Responsibilities:**
- Write SEO-optimized content
- Create content strategies
- Develop content briefs
- Optimize existing content
- Ensure E-E-A-T compliance
- Follow brand voice guidelines

**When to Call Other Agents:**
- **Keyword Research Agent:** For keyword data, search intent
- **SEO Strategist:** For content strategy, priorities
- **QA Agent:** For quality review before publishing
- **Reporting Agent:** For content performance data

**Never:**
- Conduct keyword research (delegate to Keyword Research)
- Implement technical SEO (delegate to Technical SEO)
- Communicate directly with clients (escalate to Sales/Strategist)

---

### 7. Reporting Agent
**Primary Role:** Performance tracking and reporting

**Responsibilities:**
- Track SEO metrics
- Create reports
- Analyze performance data
- Provide insights
- Document results
- Communicate findings

**When to Call Other Agents:**
- **SEO Strategist:** For strategic insights, recommendations
- **QA Agent:** For quality review of reports
- **Sales Agent:** For client communication
- **All specialist agents:** For data collection

**Never:**
- Make strategic changes (recommend to SEO Strategist)
- Implement fixes (delegate to appropriate agents)
- Communicate directly with clients without Sales/Strategist approval

---

### 8. QA Agent
**Primary Role:** Quality assurance and final review

**Responsibilities:**
- Review all deliverables
- Check for errors
- Ensure quality standards
- Verify data accuracy
- Validate recommendations
- Approve for delivery
- Request revisions when needed

**When to Call Other Agents:**
- **Any agent:** For clarification, revisions, corrections
- **SEO Strategist:** For strategic alignment issues
- **Reporting Agent:** For data verification

**Never:**
- Create original deliverables (review only)
- Communicate directly with clients (escalate to Sales/Strategist)
- Make strategic decisions (escalate to SEO Strategist)

---

## Workflow Protocols

### Protocol 1: New Client Onboarding

**Trigger:** New client signs contract

**Workflow:**
1. **Sales Agent** → Sends welcome email, collects access credentials
2. **Sales Agent** → Calls **SEO Strategist** with client brief
3. **SEO Strategist** → Reviews client needs, creates project plan
4. **SEO Strategist** → Calls **CEO Agent** for resource approval
5. **CEO Agent** → Approves plan, assigns team
6. **SEO Strategist** → Calls **Technical SEO Agent** for audit
7. **SEO Strategist** → Calls **Keyword Research Agent** for research
8. **Technical SEO Agent** → Conducts audit, calls **QA Agent** for review
9. **Keyword Research Agent** → Conducts research, calls **QA Agent** for review
10. **QA Agent** → Reviews both, approves or requests revisions
11. **SEO Strategist** → Calls **Reporting Agent** to create initial report
12. **Reporting Agent** → Creates report, calls **QA Agent** for review
13. **QA Agent** → Final approval
14. **SEO Strategist** → Calls **Sales Agent** for client presentation
15. **Sales Agent** → Presents to client, gathers feedback
16. **SEO Strategist** → Adjusts strategy based on feedback
17. **SEO Strategist** → Calls **Content Writer Agent** for content creation
18. **Content Writer Agent** → Creates content, calls **QA Agent** for review
19. **QA Agent** → Approves content
20. **Reporting Agent** → Publishes content, tracks performance
21. **Reporting Agent** → Creates monthly reports
22. **QA Agent** → Reviews reports
23. **Sales Agent** → Delivers to client

**Expected Timeline:** 2-3 weeks for initial setup

---

### Protocol 2: SEO Audit Project

**Trigger:** Client requests SEO audit

**Workflow:**
1. **Sales Agent** → Receives request, qualifies lead
2. **Sales Agent** → Calls **SEO Strategist** for feasibility assessment
3. **SEO Strategist** → Provides assessment to Sales Agent
4. **Sales Agent** → Creates proposal, calls **CEO Agent** for pricing approval
5. **CEO Agent** → Approves pricing
6. **Sales Agent** → Sends proposal to client
7. **Client accepts** → Sales Agent notifies **SEO Strategist**
8. **SEO Strategist** → Assigns **Technical SEO Agent** for audit
9. **Technical SEO Agent** → Conducts comprehensive audit
   - Crawls website
   - Analyzes technical issues
   - Reviews performance
   - Checks mobile optimization
   - Analyzes security
10. **Technical SEO Agent** → Calls **QA Agent** for quality review
11. **QA Agent** → Reviews audit, requests revisions if needed
12. **Technical SEO Agent** → Makes revisions
13. **QA Agent** → Final approval
14. **Technical SEO Agent** → Calls **Reporting Agent** with findings
15. **Reporting Agent** → Creates audit report using template
16. **Reporting Agent** → Calls **QA Agent** for review
17. **QA Agent** → Final approval
18. **Reporting Agent** → Calls **SEO Strategist** for strategic recommendations
19. **SEO Strategist** → Adds strategic insights
20. **SEO Strategist** → Calls **QA Agent** for final review
21. **QA Agent** → Final approval
22. **SEO Strategist** → Calls **Sales Agent** for client delivery
23. **Sales Agent** → Presents report to client
24. **Sales Agent** → Collects feedback, shares with **SEO Strategist**
25. **SEO Strategist** → Adjusts recommendations if needed
26. **SEO Strategist** → Calls **Technical SEO Agent** for implementation support (if purchased)
27. **Technical SEO Agent** → Implements fixes
28. **Technical SEO Agent** → Calls **QA Agent** for verification
29. **QA Agent** → Verifies implementation
30. **Reporting Agent** → Creates implementation report
31. **QA Agent** → Final approval
32. **Sales Agent** → Delivers to client

**Expected Timeline:** 10 business days for audit, additional time for implementation

---

### Protocol 3: Keyword Research Project

**Trigger:** Client requests keyword research

**Workflow:**
1. **Sales Agent** → Receives request, qualifies lead
2. **Sales Agent** → Calls **SEO Strategist** for feasibility
3. **SEO Strategist** → Provides assessment
4. **Sales Agent** → Creates proposal, gets **CEO Agent** approval
5. **Client accepts** → Sales Agent notifies **SEO Strategist**
6. **SEO Strategist** → Assigns **Keyword Research Agent**
7. **Keyword Research Agent** → Conducts comprehensive research
   - Identifies seed keywords
   - Analyzes search intent
   - Researches competitors
   - Identifies gaps
   - Prioritizes keywords
8. **Keyword Research Agent** → Calls **QA Agent** for review
9. **QA Agent** → Reviews research, requests revisions if needed
10. **Keyword Research Agent** → Makes revisions
11. **QA Agent** → Final approval
12. **Keyword Research Agent** → Calls **Reporting Agent** with findings
13. **Reporting Agent** → Creates keyword research report
14. **Reporting Agent** → Calls **QA Agent** for review
15. **QA Agent** → Final approval
16. **Reporting Agent** → Calls **SEO Strategist** for content roadmap
17. **SEO Strategist** → Develops content strategy
18. **SEO Strategist** → Calls **QA Agent** for review
19. **QA Agent** → Final approval
20. **SEO Strategist** → Calls **Sales Agent** for client delivery
21. **Sales Agent** → Presents to client
22. **Sales Agent** → If client wants content creation, notifies **SEO Strategist**
23. **SEO Strategist** → Calls **Content Writer Agent** for content creation
24. **Content Writer Agent** → Creates content based on keyword research
25. **Content Writer Agent** → Calls **QA Agent** for review
26. **QA Agent** → Approves content
27. **Reporting Agent** → Publishes and tracks performance
28. **QA Agent** → Final check
29. **Sales Agent** → Delivers to client

**Expected Timeline:** 7 business days for research, additional time for content

---

### Protocol 4: Monthly SEO Management

**Trigger:** Client signs monthly retainer

**Workflow:**
1. **Sales Agent** → Onboards client, collects access
2. **Sales Agent** → Calls **SEO Strategist** with client details
3. **SEO Strategist** → Creates project plan, assigns team
4. **SEO Strategist** → Calls **Technical SEO Agent** for ongoing monitoring
5. **SEO Strategist** → Calls **Keyword Research Agent** for ongoing research
6. **SEO Strategist** → Calls **Content Writer Agent** for content calendar
7. **Technical SEO Agent** → Monitors site health, fixes issues
8. **Keyword Research Agent** → Tracks rankings, identifies new opportunities
9. **Content Writer Agent** → Creates content per calendar
10. **All agents** → Call **QA Agent** for quality checks
11. **QA Agent** → Reviews all work, provides feedback
12. **Reporting Agent** → Compiles monthly data
13. **Reporting Agent** → Creates monthly report
14. **Reporting Agent** → Calls **QA Agent** for review
15. **QA Agent** → Final approval
16. **Reporting Agent** → Calls **SEO Strategist** for insights
17. **SEO Strategist** → Adds strategic recommendations
18. **SEO Strategist** → Calls **QA Agent** for final review
19. **QA Agent** → Final approval
20. **SEO Strategist** → Calls **Sales Agent** for client delivery
21. **Sales Agent** → Presents report to client
22. **Sales Agent** → Collects feedback, shares with **SEO Strategist**
23. **SEO Strategist** → Adjusts strategy for next month
24. **Loop continues monthly**

**Expected Timeline:** Ongoing monthly cycle

---

### Protocol 5: Content Strategy Project

**Trigger:** Client requests content strategy

**Workflow:**
1. **Sales Agent** → Receives request, qualifies lead
2. **Sales Agent** → Calls **SEO Strategist** for feasibility
3. **SEO Strategist** → Provides assessment
4. **Sales Agent** → Creates proposal, gets **CEO Agent** approval
5. **Client accepts** → Sales Agent notifies **SEO Strategist**
6. **SEO Strategist** → Calls **Keyword Research Agent** for keyword data
7. **Keyword Research Agent** → Provides comprehensive keyword database
8. **SEO Strategist** → Calls **Content Writer Agent** for content strategy
9. **Content Writer Agent** → Develops content strategy
   - Creates topic clusters
   - Develops content calendar
   - Plans content types
   - Defines success metrics
10. **Content Writer Agent** → Calls **QA Agent** for review
11. **QA Agent** → Reviews strategy, requests revisions if needed
12. **Content Writer Agent** → Makes revisions
13. **QA Agent** → Final approval
14. **Content Writer Agent** → Calls **Reporting Agent** to create strategy document
15. **Reporting Agent** → Creates comprehensive strategy document
16. **Reporting Agent** → Calls **QA Agent** for review
17. **QA Agent** → Final approval
18. **Reporting Agent** → Calls **SEO Strategist** for strategic review
19. **SEO Strategist** → Adds insights, approves
20. **SEO Strategist** → Calls **Sales Agent** for client delivery
21. **Sales Agent** → Presents strategy to client
22. **Sales Agent** → If client wants implementation, notifies **SEO Strategist**
23. **SEO Strategist** → Coordinates content creation
24. **Content Writer Agent** → Creates content per strategy
25. **Content Writer Agent** → Calls **QA Agent** for each piece
26. **QA Agent** → Approves content
27. **Reporting Agent** → Publishes and tracks performance
28. **QA Agent** → Final check
29. **Sales Agent** → Delivers to client

**Expected Timeline:** 14 business days for strategy, additional time for implementation

---

## Communication Protocols

### Agent-to-Agent Communication

**Format:**
```
[Calling Agent] → [Called Agent]: [Request Type]
Purpose: [Clear statement of purpose]
Context: [Relevant background information]
Deliverables Needed: [Specific outputs required]
Timeline: [When needed by]
Priority: [High/Medium/Low]
```

**Example:**
```
SEO Strategist → Keyword Research Agent: Keyword Research Request
Purpose: Keyword research for e-commerce client
Context: Client sells organic skincare products, targeting US market
Deliverables Needed: 2,000+ keywords with intent analysis, competitor gaps, content roadmap
Timeline: 7 business days
Priority: High
```

---

### Response Protocol

**When Called:**
1. Acknowledge request immediately
2. Review requirements
3. Confirm understanding
4. Provide timeline estimate
5. Begin work
6. Provide progress updates
7. Deliver completed work
8. Request QA review
9. Make revisions if needed
10. Finalize and notify calling agent

**Response Time:**
- Acknowledge: Within 1 hour
- Timeline estimate: Within 4 hours
- Progress updates: Daily
- Delivery: On agreed timeline

---

### Escalation Protocol

**When to Escalate:**
- Task outside your expertise
- Client request beyond scope
- Budget/resource constraints
- Strategic decisions needed
- Quality issues that can't be resolved
- Conflicts with other agents

**Escalation Path:**
1. First: Discuss with calling agent
2. Second: Escalate to SEO Strategist
3. Third: Escalate to CEO Agent
4. Final: CEO Agent makes decision

---

## Quality Gates

### Gate 1: Agent Self-Review
**When:** Before calling QA Agent
**Who:** Working agent
**Purpose:** Ensure work meets basic quality standards
**Checklist:**
- [ ] Work is complete
- [ ] No obvious errors
- [ ] Meets requirements
- [ ] Data is accurate
- [ ] Formatting is correct

---

### Gate 2: QA Agent Review
**When:** After agent completes work, before delivery
**Who:** QA Agent
**Purpose:** Ensure work meets agency quality standards
**Checklist:**
- [ ] All requirements met
- [ ] Data accuracy verified
- [ ] No errors or typos
- [ ] Formatting consistent
- [ ] Brand guidelines followed
- [ ] Recommendations are actionable
- [ ] Professional presentation
- [ ] Client-ready quality

**Outcomes:**
- **Approve:** Work is ready for next step
- **Revise:** Send back with specific feedback
- **Reject:** Major issues, needs rework

---

### Gate 3: Strategic Review
**When:** Before client delivery
**Who:** SEO Strategist
**Purpose:** Ensure strategic alignment
**Checklist:**
- [ ] Aligns with client goals
- [ ] Supports overall strategy
- [ ] Prioritization is correct
- [ ] Recommendations are feasible
- [ ] ROI is demonstrated

---

### Gate 4: Final Approval
**When:** Before client delivery
**Who:** CEO Agent (for major deliverables) or SEO Strategist (for routine)
**Purpose:** Final quality and strategic check
**Checklist:**
- [ ] All QA approvals obtained
- [ ] Strategic alignment confirmed
- [ ] Client expectations met
- [ ] Ready for delivery

---

## Decision Trees

### Decision Tree 1: Client Request Routing

```
Client Request
     │
     ▼
Is it a sales inquiry?
     │
     ├─ YES → Sales Agent handles
     │
     └─ NO → Is it an existing client?
              │
              ├─ YES → SEO Strategist handles
              │
              └─ NO → Sales Agent qualifies first
```

---

### Decision Tree 2: Agent Assignment

```
Task Assigned
     │
     ▼
What type of task?
     │
     ├─ Technical → Technical SEO Agent
     │
     ├─ Keywords → Keyword Research Agent
     │
     ├─ Content → Content Writer Agent
     │
     ├─ Reporting → Reporting Agent
     │
     ├─ Strategy → SEO Strategist
     │
     ├─ Quality → QA Agent
     │
     └─ Client Communication → Sales Agent
```

---

### Decision Tree 3: Quality Issue Resolution

```
Quality Issue Found
     │
     ▼
Who found it?
     │
     ├─ Agent self-review → Fix it yourself
     │
     ├─ QA Agent → Return to working agent with feedback
     │
     └─ Client → Escalate to Sales Agent → SEO Strategist
                │
                ▼
           Can be fixed quickly?
                │
                ├─ YES → Fix and resend
                │
                └─ NO → Escalate to CEO Agent
```

---

## Collaboration Best Practices

### 1. Clear Communication
- Be specific about what you need
- Provide complete context
- Set clear expectations
- Confirm understanding

### 2. Timely Responses
- Acknowledge requests quickly
- Meet agreed timelines
- Provide progress updates
- Communicate delays immediately

### 3. Quality First
- Don't rush deliverables
- Follow quality standards
- Request QA review
- Accept and implement feedback

### 4. Respect Roles
- Stay in your lane
- Don't micromanage other agents
- Trust other agents' expertise
- Escalate when needed

### 5. Continuous Improvement
- Learn from feedback
- Update processes
- Share knowledge
- Improve workflows

---

## Common Workflow Patterns

### Pattern 1: Research → Strategy → Execution → Report

**Use for:** Most SEO projects
**Agents involved:** Keyword Research → SEO Strategist → Specialist → Reporting → QA → Sales

---

### Pattern 2: Audit → Fix → Verify → Report

**Use for:** Technical SEO projects
**Agents involved:** Technical SEO → QA → Reporting → QA → Sales

---

### Pattern 3: Strategy → Create → Optimize → Track

**Use for:** Content projects
**Agents involved:** SEO Strategist → Content Writer → QA → Reporting → QA → Sales

---

### Pattern 4: Monitor → Analyze → Adjust → Report

**Use for:** Monthly management
**Agents involved:** All specialists → Reporting → SEO Strategist → QA → Sales

---

## Workflow Exceptions

### When to Break Protocol

**Emergency Issues:**
- Website down
- Security breach
- Major ranking drop
- Client crisis

**Protocol:**
1. Technical SEO Agent → Immediate action
2. Technical SEO Agent → Notify SEO Strategist immediately
3. SEO Strategist → Notify Sales Agent
4. Sales Agent → Communicate with client
5. Technical SEO Agent → Document actions
6. Reporting Agent → Create incident report
7. QA Agent → Review
8. Sales Agent → Deliver to client

---

### When to Skip Steps

**Routine Tasks:**
- Small content updates
- Minor technical fixes
- Regular reporting

**Protocol:**
- Can skip some review steps
- Still require QA before delivery
- Document exceptions
- Maintain quality standards

---

## Workflow Metrics

### Track These Metrics

**Efficiency:**
- Time per workflow stage
- Total project completion time
- Revision rate
- Rework percentage

**Quality:**
- QA approval rate
- Error rate
- Client satisfaction
- Revision requests

**Collaboration:**
- Agent communication frequency
- Escalation rate
- Conflict resolution time
- Handoff success rate

---

## Continuous Improvement

### Regular Reviews

**Weekly:**
- Review workflow bottlenecks
- Identify improvement opportunities
- Share learnings

**Monthly:**
- Analyze workflow metrics
- Update protocols if needed
- Train agents on improvements

**Quarterly:**
- Comprehensive workflow review
- Major process updates
- Strategic improvements

---

## Notes

- Workflows are guidelines, not rigid rules
- Adapt to specific client needs
- Communication is key
- Quality is non-negotiable
- Collaboration drives success
- Continuous improvement is essential
- Client success is the goal
- Every agent matters
- No agent works alone
- We win together
# Workflow Automation Scripts

This directory contains automation scripts that demonstrate and facilitate agent orchestration within the Nexora AI SEO Agency.

## Scripts

### 1. workflow-orchestrator.py

**Purpose:** Demonstrates how agents work together to complete SEO projects through proper orchestration and collaboration.

**Features:**
- Agent registration and capability management
- Inter-agent message passing
- Task creation and assignment
- QA review workflow
- Approval processes
- Complete workflow demonstrations

**Usage:**
```bash
python scripts/workflow-orchestrator.py
```

**Demonstrates:**
1. **SEO Audit Workflow** - Complete end-to-end workflow from client request to delivery
2. **Monthly SEO Management** - Ongoing monthly coordination between agents

## Workflow Principles

### No Agent Works in Isolation

Every agent is part of an integrated system. The workflow orchestrator ensures:
- Clear communication between agents
- Proper task assignment based on expertise
- Quality gates at critical points
- Systematic handoffs between agents
- Complete audit trail of all actions

### Agent Coordination Pattern

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

## Key Concepts

### 1. Agent Registration
Each agent registers with specific capabilities:
```python
orchestrator.register_agent(AgentType.SEO_STRATEGIST, ["Strategy", "Coordination"])
```

### 2. Message Passing
Agents communicate through structured messages:
```python
orchestrator.send_message(
    from_agent=AgentType.SALES,
    to_agent=AgentType.SEO_STRATEGIST,
    message_type="Feasibility Assessment Request",
    purpose="Assess SEO audit feasibility",
    context="Client needs comprehensive SEO audit",
    deliverables=["Feasibility assessment", "Timeline estimate"],
    timeline="1 business day",
    priority=Priority.HIGH
)
```

### 3. Task Management
Tasks are created, assigned, and tracked:
```python
task = orchestrator.create_task(
    title="SEO Audit",
    description="Comprehensive SEO audit",
    assigned_to=AgentType.TECHNICAL_SEO,
    assigned_by=AgentType.SEO_STRATEGIST,
    priority=Priority.HIGH,
    deliverables=["Audit report", "Recommendations"],
    timeline="10 business days"
)
```

### 4. QA Review
Quality assurance is integrated into every workflow:
```python
orchestrator.request_qa_review(task_id, requesting_agent)
```

### 5. Approval Process
Deliverables require approval before client delivery:
```python
orchestrator.approve_deliverable(task_id, approving_agent=AgentType.QA)
```

## Workflow Examples

### Example 1: SEO Audit Project

**Agents Involved:**
1. Sales Agent - Receives client request
2. SEO Strategist - Creates project plan
3. Technical SEO Agent - Conducts audit
4. QA Agent - Reviews audit quality
5. Reporting Agent - Creates report
6. QA Agent - Reviews report
7. SEO Strategist - Adds strategic insights
8. Sales Agent - Delivers to client

**Timeline:** 10 business days

**Quality Gates:**
- QA review of technical audit
- QA review of final report
- Strategic review by SEO Strategist

### Example 2: Monthly SEO Management

**Agents Involved:**
1. SEO Strategist - Coordinates activities
2. Technical SEO Agent - Monitors site health
3. Keyword Research Agent - Tracks rankings
4. Content Writer Agent - Creates content
5. QA Agent - Reviews all work
6. Reporting Agent - Creates monthly report
7. Sales Agent - Delivers to client

**Timeline:** Ongoing monthly cycle

**Quality Gates:**
- QA review of all agent work
- QA review of monthly report
- Strategic review before delivery

## Extension Points

### Adding New Workflows

To add a new workflow demonstration:

1. Create a new function following the pattern:
```python
def demonstrate_new_workflow():
    orchestrator = WorkflowOrchestrator()
    
    # Register agents
    orchestrator.register_agent(...)
    
    # Create workflow steps
    orchestrator.send_message(...)
    orchestrator.create_task(...)
    
    # Print summary
    print(orchestrator.get_workflow_summary())
```

2. Add the workflow to the main execution:
```python
if __name__ == "__main__":
    demonstrate_new_workflow()
```

### Integrating with Real Agents

To integrate with actual AI agents:

1. Replace print statements with actual agent calls
2. Implement message queue for inter-agent communication
3. Add persistence layer for tasks and messages
4. Implement actual QA review logic
5. Add error handling and retry logic

## Best Practices

### 1. Clear Communication
- Always include purpose, context, and deliverables
- Set realistic timelines
- Specify priority levels
- Provide complete information

### 2. Quality Gates
- Always request QA review before delivery
- Never skip quality checks
- Address QA feedback promptly
- Maintain quality standards

### 3. Proper Handoffs
- Document all handoffs
- Ensure completeness before handing off
- Provide clear context to next agent
- Confirm receipt and understanding

### 4. Workflow Documentation
- Log all actions
- Track task status
- Maintain audit trail
- Review workflow history

## Future Enhancements

### Phase 2: Real Agent Integration
- Connect to actual AI agent systems
- Implement message queue (RabbitMQ, Redis)
- Add database persistence
- Real-time workflow monitoring

### Phase 3: Advanced Features
- Parallel task execution
- Conditional workflows
- Dynamic agent selection
- Performance optimization
- Workflow analytics

### Phase 4: Enterprise Features
- Multi-client support
- Resource management
- Scheduling and calendar integration
- Advanced reporting
- SLA monitoring

## Troubleshooting

### Common Issues

**Issue:** Task not found
**Solution:** Ensure task_id exists in orchestrator.tasks

**Issue:** Agent not registered
**Solution:** Register agent before sending messages or creating tasks

**Issue:** Circular dependencies
**Solution:** Review task dependencies to ensure no circular references

## Support

For questions or issues:
- Review agent orchestration workflow: `agents/shared-workflows/agent-orchestration.md`
- Check agent system prompts for specific agent capabilities
- Review workflow demonstrations in this script

---

**Version:** 1.0
**Last Updated:** 2026-07-06
**Maintained By:** Nexora AI SEO Agency
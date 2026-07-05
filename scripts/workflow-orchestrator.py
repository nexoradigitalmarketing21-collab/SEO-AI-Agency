#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Workflow Orchestrator
This script demonstrates how agents work together to complete SEO projects.
"""

from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

class AgentType(Enum):
    SALES = "sales"
    CEO = "ceo"
    SEO_STRATEGIST = "seo_strategist"
    KEYWORD_RESEARCH = "keyword_research"
    TECHNICAL_SEO = "technical_seo"
    CONTENT_WRITER = "content_writer"
    REPORTING = "reporting"
    QA = "qa"

class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    NEEDS_REVISION = "needs_revision"
    APPROVED = "approved"

@dataclass
class Task:
    """Represents a task in the workflow"""
    id: str
    title: str
    description: str
    assigned_to: AgentType
    assigned_by: AgentType
    priority: Priority
    status: TaskStatus
    deliverables: List[str]
    timeline: str
    dependencies: List[str]
    created_at: datetime
    completed_at: Optional[datetime] = None

@dataclass
class Message:
    """Represents communication between agents"""
    id: str
    from_agent: AgentType
    to_agent: AgentType
    message_type: str
    purpose: str
    context: str
    deliverables_needed: List[str]
    timeline: str
    priority: Priority
    timestamp: datetime

class WorkflowOrchestrator:
    """Orchestrates agent collaboration and workflow execution"""

    def __init__(self):
        self.agents = {agent: [] for agent in AgentType}
        self.tasks: Dict[str, Task] = {}
        self.messages: List[Message] = []
        self.workflow_history: List[str] = []

    def register_agent(self, agent_type: AgentType, capabilities: List[str]):
        """Register an agent with its capabilities"""
        self.agents[agent_type] = capabilities
        print(f"✓ Registered {agent_type.value} agent with capabilities: {', '.join(capabilities)}")

    def send_message(self, from_agent: AgentType, to_agent: AgentType,
                     message_type: str, purpose: str, context: str,
                     deliverables: List[str], timeline: str, priority: Priority) -> Message:
        """Send a message from one agent to another"""

        message = Message(
            id=f"msg_{len(self.messages) + 1}",
            from_agent=from_agent,
            to_agent=to_agent,
            message_type=message_type,
            purpose=purpose,
            context=context,
            deliverables_needed=deliverables,
            timeline=timeline,
            priority=priority,
            timestamp=datetime.now()
        )

        self.messages.append(message)
        self.log_workflow(f"{from_agent.value} → {to_agent.value}: {message_type}")

        return message

    def create_task(self, title: str, description: str, assigned_to: AgentType,
                    assigned_by: AgentType, priority: Priority, deliverables: List[str],
                    timeline: str, dependencies: List[str] = None) -> Task:
        """Create a new task"""

        task = Task(
            id=f"task_{len(self.tasks) + 1}",
            title=title,
            description=description,
            assigned_to=assigned_to,
            assigned_by=assigned_by,
            priority=priority,
            status=TaskStatus.PENDING,
            deliverables=deliverables,
            timeline=timeline,
            dependencies=dependencies or [],
            created_at=datetime.now()
        )

        self.tasks[task.id] = task
        self.log_workflow(f"Task created: {title} → {assigned_to.value}")

        return task

    def complete_task(self, task_id: str, results: str):
        """Mark a task as completed"""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.status = TaskStatus.COMPLETED
            task.completed_at = datetime.now()
            self.log_workflow(f"Task completed: {task.title}")

    def request_qa_review(self, task_id: str, requesting_agent: AgentType) -> Message:
        """Request QA review for a completed task"""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")

        message = self.send_message(
            from_agent=requesting_agent,
            to_agent=AgentType.QA,
            message_type="QA Review Request",
            purpose=f"Review completed {task.title}",
            context=f"Task {task_id} has been completed and needs quality review",
            deliverables=task.deliverables,
            timeline="2 business days",
            priority=Priority.HIGH
        )

        return message

    def approve_deliverable(self, task_id: str, approving_agent: AgentType) -> Message:
        """Approve a deliverable for client delivery"""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")

        task.status = TaskStatus.APPROVED
        self.log_workflow(f"Deliverable approved: {task.title} by {approving_agent.value}")

        # Notify the working agent
        message = self.send_message(
            from_agent=approving_agent,
            to_agent=task.assigned_by,
            message_type="Approval Notification",
            purpose=f"{task.title} approved for delivery",
            context=f"QA has approved the deliverable for client delivery",
            deliverables=["Client delivery"],
            timeline="Immediate",
            priority=Priority.HIGH
        )

        return message

    def log_workflow(self, action: str):
        """Log workflow actions"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.workflow_history.append(f"[{timestamp}] {action}")

    def get_workflow_summary(self) -> str:
        """Get a summary of the workflow"""
        summary = "\n" + "="*80 + "\n"
        summary += "WORKFLOW ORCHESTRATION SUMMARY\n"
        summary += "="*80 + "\n\n"

        summary += "Registered Agents:\n"
        for agent, capabilities in self.agents.items():
            if capabilities:
                summary += f"  • {agent.value}: {', '.join(capabilities)}\n"

        summary += f"\nTotal Tasks: {len(self.tasks)}\n"
        summary += f"Total Messages: {len(self.messages)}\n"

        summary += "\nWorkflow History:\n"
        for action in self.workflow_history:
            summary += f"  {action}\n"

        summary += "\nTask Status:\n"
        for task_id, task in self.tasks.items():
            summary += f"  • {task.title}: {task.status.value} ({task.assigned_to.value})\n"

        summary += "\n" + "="*80 + "\n"

        return summary


def demonstrate_seo_audit_workflow():
    """Demonstrate a complete SEO audit workflow"""

    print("\n" + "="*80)
    print("NEXORA AI SEO AGENCY - WORKFLOW DEMONSTRATION")
    print("="*80)
    print("\nScenario: Client requests SEO audit\n")

    orchestrator = WorkflowOrchestrator()

    # Register agents
    print("Step 1: Registering Agents")
    print("-" * 80)
    orchestrator.register_agent(AgentType.SALES, ["Client communication", "Proposals"])
    orchestrator.register_agent(AgentType.CEO, ["Strategic decisions", "Approvals"])
    orchestrator.register_agent(AgentType.SEO_STRATEGIST, ["Strategy", "Coordination"])
    orchestrator.register_agent(AgentType.TECHNICAL_SEO, ["Technical audits", "Implementation"])
    orchestrator.register_agent(AgentType.KEYWORD_RESEARCH, ["Keyword research", "Analysis"])
    orchestrator.register_agent(AgentType.CONTENT_WRITER, ["Content creation", "SEO writing"])
    orchestrator.register_agent(AgentType.REPORTING, ["Reports", "Analytics"])
    orchestrator.register_agent(AgentType.QA, ["Quality assurance", "Approval"])

    print("\nStep 2: Client Request Received")
    print("-" * 80)
    print("Client: 'I need a comprehensive SEO audit for my website'")

    # Sales Agent receives client request
    print("\n→ Sales Agent receives client inquiry")

    # Sales Agent calls SEO Strategist for feasibility
    print("\nStep 3: Sales Agent → SEO Strategist")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.SALES,
        to_agent=AgentType.SEO_STRATEGIST,
        message_type="Feasibility Assessment Request",
        purpose="Assess SEO audit feasibility for new client",
        context="Client needs comprehensive SEO audit for e-commerce website",
        deliverables=["Feasibility assessment", "Timeline estimate", "Resource requirements"],
        timeline="1 business day",
        priority=Priority.HIGH
    )
    print("Sales Agent requests feasibility assessment from SEO Strategist")

    # SEO Strategist creates project plan
    print("\nStep 4: SEO Strategist Creates Project Plan")
    print("-" * 80)
    seo_audit_task = orchestrator.create_task(
        title="SEO Audit Project",
        description="Comprehensive SEO audit for e-commerce client",
        assigned_to=AgentType.TECHNICAL_SEO,
        assigned_by=AgentType.SEO_STRATEGIST,
        priority=Priority.HIGH,
        deliverables=["Technical audit report", "Prioritized recommendations", "Implementation roadmap"],
        timeline="10 business days",
        dependencies=[]
    )
    print("SEO Strategist creates SEO audit project and assigns to Technical SEO Agent")

    # SEO Strategist calls Technical SEO Agent
    print("\nStep 5: SEO Strategist → Technical SEO Agent")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.SEO_STRATEGIST,
        to_agent=AgentType.TECHNICAL_SEO,
        message_type="SEO Audit Assignment",
        purpose="Conduct comprehensive SEO audit",
        context="E-commerce client needs technical SEO audit with recommendations",
        deliverables=["Technical audit report", "Prioritized issues", "Recommendations"],
        timeline="10 business days",
        priority=Priority.HIGH
    )
    print("SEO Strategist assigns SEO audit to Technical SEO Agent")

    # Technical SEO Agent conducts audit
    print("\nStep 6: Technical SEO Agent Conducts Audit")
    print("-" * 80)
    print("Technical SEO Agent:")
    print("  • Crawls website with Screaming Frog")
    print("  • Analyzes technical issues")
    print("  • Reviews performance metrics")
    print("  • Checks mobile optimization")
    print("  • Analyzes security")
    technical_audit_task = orchestrator.create_task(
        title="Technical SEO Audit",
        description="Conduct comprehensive technical SEO audit",
        assigned_to=AgentType.TECHNICAL_SEO,
        assigned_by=AgentType.SEO_STRATEGIST,
        priority=Priority.HIGH,
        deliverables=["Crawl analysis", "Performance metrics", "Technical issues list"],
        timeline="7 business days",
        dependencies=[seo_audit_task.id]
    )
    orchestrator.complete_task(technical_audit_task.id, "Audit completed")

    # Technical SEO Agent calls QA Agent for review
    print("\nStep 7: Technical SEO Agent → QA Agent")
    print("-" * 80)
    orchestrator.request_qa_review(technical_audit_task.id, AgentType.TECHNICAL_SEO)
    print("Technical SEO Agent requests QA review of audit findings")

    # QA Agent reviews
    print("\nStep 8: QA Agent Reviews Audit")
    print("-" * 80)
    print("QA Agent:")
    print("  • Reviews audit completeness")
    print("  • Verifies data accuracy")
    print("  • Checks recommendations quality")
    print("  • Approves with minor revisions")
    qa_review_task = orchestrator.create_task(
        title="QA Review - Technical Audit",
        description="Review technical SEO audit for quality",
        assigned_to=AgentType.QA,
        assigned_by=AgentType.TECHNICAL_SEO,
        priority=Priority.HIGH,
        deliverables=["Quality approval", "Feedback"],
        timeline="2 business days",
        dependencies=[technical_audit_task.id]
    )
    orchestrator.complete_task(qa_review_task.id, "QA review completed - Approved with minor revisions")

    # Technical SEO Agent makes revisions
    print("\nStep 9: Technical SEO Agent Makes Revisions")
    print("-" * 80)
    print("Technical SEO Agent addresses QA feedback and finalizes audit")

    # Technical SEO Agent calls Reporting Agent
    print("\nStep 10: Technical SEO Agent → Reporting Agent")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.TECHNICAL_SEO,
        to_agent=AgentType.REPORTING,
        message_type="Audit Report Creation Request",
        purpose="Create SEO audit report from technical findings",
        context="Technical audit completed, need professional report created",
        deliverables=["SEO audit report", "Visualizations", "Executive summary"],
        timeline="3 business days",
        priority=Priority.HIGH
    )
    print("Technical SEO Agent provides findings to Reporting Agent for report creation")

    # Reporting Agent creates report
    print("\nStep 11: Reporting Agent Creates Report")
    print("-" * 80)
    report_task = orchestrator.create_task(
        title="SEO Audit Report Creation",
        description="Create comprehensive SEO audit report",
        assigned_to=AgentType.REPORTING,
        assigned_by=AgentType.TECHNICAL_SEO,
        priority=Priority.HIGH,
        deliverables=["SEO audit report", "Executive summary", "Recommendations"],
        timeline="3 business days",
        dependencies=[qa_review_task.id]
    )
    orchestrator.complete_task(report_task.id, "Report created")

    # Reporting Agent calls QA Agent
    print("\nStep 12: Reporting Agent → QA Agent")
    print("-" * 80)
    orchestrator.request_qa_review(report_task.id, AgentType.REPORTING)
    print("Reporting Agent requests QA review of report")

    # QA Agent reviews report
    print("\nStep 13: QA Agent Reviews Report")
    print("-" * 80)
    qa_report_task = orchestrator.create_task(
        title="QA Review - SEO Audit Report",
        description="Review SEO audit report for quality",
        assigned_to=AgentType.QA,
        assigned_by=AgentType.REPORTING,
        priority=Priority.HIGH,
        deliverables=["Quality approval", "Feedback"],
        timeline="2 business days",
        dependencies=[report_task.id]
    )
    orchestrator.complete_task(qa_report_task.id, "QA review completed - Approved")

    # QA Agent approves
    print("\nStep 14: QA Agent Approves Report")
    print("-" * 80)
    orchestrator.approve_deliverable(report_task.id, AgentType.QA)
    print("QA Agent approves report for client delivery")

    # Reporting Agent calls SEO Strategist
    print("\nStep 15: Reporting Agent → SEO Strategist")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.REPORTING,
        to_agent=AgentType.SEO_STRATEGIST,
        message_type="Report Ready for Strategic Review",
        purpose="SEO audit report ready for strategic review",
        context="Report has been QA approved and is ready for strategic review",
        deliverables=["SEO audit report"],
        timeline="1 business day",
        priority=Priority.HIGH
    )
    print("Reporting Agent sends approved report to SEO Strategist for final review")

    # SEO Strategist reviews and adds strategic insights
    print("\nStep 16: SEO Strategist Adds Strategic Insights")
    print("-" * 80)
    print("SEO Strategist:")
    print("  • Reviews report for strategic alignment")
    print("  • Adds implementation priorities")
    print("  • Includes ROI projections")
    print("  • Adds next steps")

    # SEO Strategist calls Sales Agent for delivery
    print("\nStep 17: SEO Strategist → Sales Agent")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.SEO_STRATEGIST,
        to_agent=AgentType.SALES,
        message_type="Deliverable Ready for Client",
        purpose="SEO audit report ready for client delivery",
        context="Report has been QA approved and strategically reviewed",
        deliverables=["SEO audit report", "Executive presentation"],
        timeline="Immediate",
        priority=Priority.HIGH
    )
    print("SEO Strategist sends final report to Sales Agent for client delivery")

    # Sales Agent delivers to client
    print("\nStep 18: Sales Agent Delivers to Client")
    print("-" * 80)
    print("Sales Agent:")
    print("  • Reviews with QA Agent (final check)")
    print("  • Presents report to client")
    print("  • Gathers feedback")
    print("  • Ensures client satisfaction")

    # Print workflow summary
    print(orchestrator.get_workflow_summary())

    print("\n" + "="*80)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("="*80)
    print("\nKey Takeaways:")
    print("✓ No agent worked in isolation")
    print("✓ Clear communication between all agents")
    print("✓ Quality gates at critical points (QA reviews)")
    print("✓ Proper handoffs between agents")
    print("✓ Client receives comprehensive, quality-assured deliverable")
    print("\n")


def demonstrate_monthly_seo_workflow():
    """Demonstrate monthly SEO management workflow"""

    print("\n" + "="*80)
    print("MONTHLY SEO MANAGEMENT WORKFLOW DEMONSTRATION")
    print("="*80)
    print("\nScenario: Ongoing monthly SEO management for existing client\n")

    orchestrator = WorkflowOrchestrator()

    # Register agents
    orchestrator.register_agent(AgentType.SALES, ["Client communication"])
    orchestrator.register_agent(AgentType.SEO_STRATEGIST, ["Strategy", "Coordination"])
    orchestrator.register_agent(AgentType.TECHNICAL_SEO, ["Technical monitoring"])
    orchestrator.register_agent(AgentType.KEYWORD_RESEARCH, ["Ranking tracking"])
    orchestrator.register_agent(AgentType.CONTENT_WRITER, ["Content creation"])
    orchestrator.register_agent(AgentType.REPORTING, ["Monthly reports"])
    orchestrator.register_agent(AgentType.QA, ["Quality review"])

    print("Step 1: SEO Strategist Coordinates Monthly Activities")
    print("-" * 80)

    # SEO Strategist assigns tasks to multiple agents
    tasks = [
        ("Technical monitoring", AgentType.TECHNICAL_SEO, "Monitor site health and fix issues"),
        ("Keyword tracking", AgentType.KEYWORD_RESEARCH, "Track rankings and identify opportunities"),
        ("Content creation", AgentType.CONTENT_WRITER, "Create content per calendar"),
    ]

    for task_title, agent, description in tasks:
        orchestrator.create_task(
            title=task_title,
            description=description,
            assigned_to=agent,
            assigned_by=AgentType.SEO_STRATEGIST,
            priority=Priority.MEDIUM,
            deliverables=[f"{task_title} deliverables"],
            timeline="Ongoing",
            dependencies=[]
        )
        print(f"  ✓ {task_title} assigned to {agent.value}")

    print("\nStep 2: Agents Execute Their Tasks")
    print("-" * 80)
    print("  • Technical SEO: Monitors site, fixes issues")
    print("  • Keyword Research: Tracks rankings, finds opportunities")
    print("  • Content Writer: Creates content per calendar")

    print("\nStep 3: All Agents Call QA for Review")
    print("-" * 80)
    for task_id in list(orchestrator.tasks.keys()):
        orchestrator.request_qa_review(task_id, AgentType.SEO_STRATEGIST)
    print("  ✓ All tasks submitted for QA review")

    print("\nStep 4: QA Agent Reviews All Work")
    print("-" * 80)
    print("  • Reviews technical fixes")
    print("  • Reviews keyword research")
    print("  • Reviews content")
    print("  • Approves all work")

    print("\nStep 5: Reporting Agent Creates Monthly Report")
    print("-" * 80)
    report_task = orchestrator.create_task(
        title="Monthly SEO Report",
        description="Compile monthly performance report",
        assigned_to=AgentType.REPORTING,
        assigned_by=AgentType.SEO_STRATEGIST,
        priority=Priority.MEDIUM,
        deliverables=["Monthly report", "KPI dashboard", "Insights"],
        timeline="5 business days after month end",
        dependencies=[]
    )
    orchestrator.complete_task(report_task.id, "Report created")

    print("\nStep 6: QA Agent Reviews Report")
    print("-" * 80)
    orchestrator.request_qa_review(report_task.id, AgentType.REPORTING)
    orchestrator.complete_task(f"task_{len(orchestrator.tasks)}", "QA review completed")

    print("\nStep 7: SEO Strategist Reviews and Adds Insights")
    print("-" * 80)
    print("  • Reviews report for strategic alignment")
    print("  • Adds insights and recommendations")
    print("  • Approves for delivery")

    print("\nStep 8: Sales Agent Delivers to Client")
    print("-" * 80)
    orchestrator.send_message(
        from_agent=AgentType.SEO_STRATEGIST,
        to_agent=AgentType.SALES,
        message_type="Monthly Report Ready",
        purpose="Monthly SEO report ready for client",
        context="Report compiled, QA approved, and strategically reviewed",
        deliverables=["Monthly SEO report"],
        timeline="Immediate",
        priority=Priority.MEDIUM
    )
    print("  ✓ Sales Agent delivers report to client")

    print(orchestrator.get_workflow_summary())

    print("\n" + "="*80)
    print("MONTHLY WORKFLOW COMPLETED")
    print("="*80)
    print("\n")


if __name__ == "__main__":
    # Demonstrate SEO audit workflow
    demonstrate_seo_audit_workflow()

    # Demonstrate monthly SEO workflow
    demonstrate_monthly_seo_workflow()

    print("✓ All workflow demonstrations completed successfully!")
    print("\nThis demonstrates how agents collaborate to complete SEO projects.")
    print("No agent works in isolation - they coordinate through clear workflows.")
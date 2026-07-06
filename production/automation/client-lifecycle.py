#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Client Lifecycle Automation (Milestone 5)
End-to-end automated workflow: Booking → Payment → Workspace → Agents → Delivery → Invoice → Review → Upsell
"""

from typing import Dict, List, Optional, Callable
from datetime import datetime, timedelta
import json
import uuid
import time


class LifecycleStage:
    """Individual stage in the client lifecycle"""
    
    def __init__(self, name: str, description: str, order: int):
        self.name = name
        self.description = description
        self.order = order
        self.status = "pending"  # pending, running, completed, failed
        self.started_at = None
        self.completed_at = None
        self.result = None
        self.error = None
    
    def start(self):
        self.status = "running"
        self.started_at = datetime.now().isoformat()
    
    def complete(self, result: Dict = None):
        self.status = "completed"
        self.completed_at = datetime.now().isoformat()
        self.result = result
    
    def fail(self, error: str):
        self.status = "failed"
        self.completed_at = datetime.now().isoformat()
        self.error = error


class ClientLifecycle:
    """Complete client lifecycle automation"""
    
    STAGES = [
        ("booking", "Client books a service through the website or portal"),
        ("payment", "Payment is processed and confirmed"),
        ("workspace", "Client workspace and project are created"),
        ("agent_assignment", "AI agents are assigned to the project"),
        ("audit", "Initial SEO audit is performed"),
        ("strategy", "SEO strategy is developed"),
        ("content", "Content is created and optimized"),
        ("qa", "Quality assurance review"),
        ("delivery", "Deliverables are delivered to client portal"),
        ("invoice", "Invoice is generated and sent"),
        ("review_request", "Client is asked for review/testimonial"),
        ("upsell", "Relevant upsell opportunities are presented")
    ]
    
    def __init__(self):
        self.active_lifecycles = {}
        self.completed_lifecycles = {}
    
    def start_lifecycle(self, client_info: Dict, service_info: Dict) -> Dict:
        """Start a new client lifecycle"""
        lifecycle_id = str(uuid.uuid4())[:12]
        
        lifecycle = {
            "id": lifecycle_id,
            "client": client_info,
            "service": service_info,
            "started_at": datetime.now().isoformat(),
            "current_stage": 0,
            "stages": [
                LifecycleStage(name, desc, i)
                for i, (name, desc) in enumerate(self.STAGES)
            ],
            "status": "active",
            "progress": 0.0,
            "estimated_completion": (datetime.now() + timedelta(days=14)).isoformat()
        }
        
        self.active_lifecycles[lifecycle_id] = lifecycle
        
        # Start first stage automatically
        self._execute_stage(lifecycle_id, 0)
        
        return self.get_lifecycle_summary(lifecycle_id)
    
    def _execute_stage(self, lifecycle_id: str, stage_index: int):
        """Execute a lifecycle stage"""
        lifecycle = self.active_lifecycles.get(lifecycle_id)
        if not lifecycle:
            return
        
        stage = lifecycle["stages"][stage_index]
        stage.start()
        
        # Simulate stage execution
        # In production, this would trigger actual workflows
        time.sleep(0.1)  # Simulate processing
        
        stage.complete({
            "stage": stage.name,
            "completed_at": datetime.now().isoformat(),
            "details": f"{stage.description} - completed successfully"
        })
        
        lifecycle["current_stage"] = stage_index
        lifecycle["progress"] = ((stage_index + 1) / len(lifecycle["stages"])) * 100
        
        # Move to next stage
        if stage_index + 1 < len(lifecycle["stages"]):
            self._execute_stage(lifecycle_id, stage_index + 1)
        else:
            lifecycle["status"] = "completed"
            self.completed_lifecycles[lifecycle_id] = lifecycle
            del self.active_lifecycles[lifecycle_id]
    
    def get_lifecycle_summary(self, lifecycle_id: str) -> Dict:
        """Get lifecycle summary"""
        lifecycle = self.active_lifecycles.get(lifecycle_id) or self.completed_lifecycles.get(lifecycle_id)
        if not lifecycle:
            return {"error": "Lifecycle not found"}
        
        return {
            "id": lifecycle["id"],
            "client": lifecycle["client"]["name"],
            "service": lifecycle["service"]["name"],
            "status": lifecycle["status"],
            "progress": lifecycle["progress"],
            "current_stage": lifecycle["stages"][lifecycle["current_stage"]].name if lifecycle["current_stage"] < len(lifecycle["stages"]) else "completed",
            "stages": [
                {
                    "name": s.name,
                    "status": s.status,
                    "started_at": s.started_at,
                    "completed_at": s.completed_at
                }
                for s in lifecycle["stages"]
            ],
            "estimated_completion": lifecycle["estimated_completion"]
        }
    
    def get_automation_status(self) -> Dict:
        """Get automation system status"""
        return {
            "active_lifecycles": len(self.active_lifecycles),
            "completed_lifecycles": len(self.completed_lifecycles),
            "total_stages": len(self.STAGES),
            "stages": [s[0] for s in self.STAGES],
            "automation_rate": "100%"  # Fully automated
        }


if __name__ == "__main__":
    lifecycle = ClientLifecycle()
    
    print("Client Lifecycle Automation:")
    print(f"  Stages: {len(lifecycle.STAGES)}")
    print(f"  Pipeline: {' → '.join(s[0] for s in lifecycle.STAGES)}")
    
    # Start a lifecycle
    result = lifecycle.start_lifecycle(
        {"name": "Sarah Johnson", "email": "sarah@techflow.com"},
        {"name": "Monthly SEO", "price": 2000}
    )
    
    print(f"\n  Lifecycle Started: {result['id']}")
    print(f"  Client: {result['client']}")
    print(f"  Service: {result['service']}")
    print(f"  Status: {result['status']}")
    print(f"  Progress: {result['progress']}%")
    print(f"  Current Stage: {result['current_stage']}")
    print(f"\n  Stage Status:")
    for stage in result['stages']:
        icon = "✅" if stage['status'] == 'completed' else "⏳" if stage['status'] == 'running' else "⬜"
        print(f"    {icon} {stage['name']:20s} ({stage['status']})")
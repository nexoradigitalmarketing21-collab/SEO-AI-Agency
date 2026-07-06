#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Agency Dashboard (CEO Dashboard)
Live monitoring of Revenue, Projects, Clients, Agents, Reports, Tasks.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta, date
import json
import uuid
import random


class AgencyDashboard:
    """Complete agency dashboard with live monitoring"""
    
    def __init__(self):
        self.metrics_history = []
        self.alerts = []
        self._init_sample_data()
    
    def _init_sample_data(self):
        """Initialize sample data for demonstration"""
        self.revenue = {
            "mrr": 8500,
            "arr": 102000,
            "monthly": [
                {"month": "Jan", "revenue": 4500},
                {"month": "Feb", "revenue": 5200},
                {"month": "Mar", "revenue": 6100},
                {"month": "Apr", "revenue": 6800},
                {"month": "May", "revenue": 7500},
                {"month": "Jun", "revenue": 8500}
            ],
            "sources": {
                "monthly_retainers": 6200,
                "one_time_projects": 1800,
                "consulting": 500
            }
        }
        
        self.clients = {
            "total": 12,
            "active": 10,
            "at_risk": 1,
            "new_this_month": 3,
            "list": [
                {"name": "TechFlow SaaS", "plan": "SEO Growth", "status": "active", "mrr": 1000, "since": "2026-01-15"},
                {"name": "City Dental", "plan": "SEO Essential", "status": "active", "mrr": 500, "since": "2026-03-01"},
                {"name": "GreenLeaf Organic", "plan": "SEO Dominance", "status": "active", "mrr": 2000, "since": "2026-02-10"},
                {"name": "Bolt Fitness", "plan": "SEO Growth", "status": "active", "mrr": 1000, "since": "2026-04-20"},
                {"name": "Artisan Bakery", "plan": "SEO Essential", "status": "active", "mrr": 500, "since": "2026-05-01"},
                {"name": "CloudStack Tech", "plan": "SEO Growth", "status": "active", "mrr": 1000, "since": "2026-05-15"},
                {"name": "Harbor Realty", "plan": "SEO Dominance", "status": "active", "mrr": 2000, "since": "2026-06-01"},
                {"name": "Pure Wellness", "plan": "SEO Essential", "status": "at_risk", "mrr": 500, "since": "2026-04-01"},
                {"name": "DevForge Agency", "plan": "SEO Growth", "status": "active", "mrr": 1000, "since": "2026-06-15"},
                {"name": "Prime Auto Sales", "plan": "SEO Essential", "status": "active", "mrr": 500, "since": "2026-07-01"}
            ]
        }
        
        self.projects = {
            "total": 15,
            "active": 10,
            "completed_this_month": 5,
            "by_type": {
                "seo_audit": 3,
                "monthly_seo": 8,
                "keyword_research": 2,
                "technical_seo": 2
            }
        }
    
    def get_overview(self) -> Dict:
        """Get dashboard overview"""
        return {
            "revenue": {
                "mrr": self.revenue["mrr"],
                "arr": self.revenue["arr"],
                "growth": "+18.5%",
                "mrr_trend": self.revenue["monthly"]
            },
            "clients": self.clients,
            "projects": self.projects,
            "alerts": len(self.alerts),
            "last_updated": datetime.now().isoformat()
        }
    
    def get_revenue_breakdown(self) -> Dict:
        """Get detailed revenue breakdown"""
        return {
            "current": self.revenue,
            "projected": {
                "next_month": self.revenue["mrr"] * 1.15,
                "next_quarter": self.revenue["mrr"] * 3.5,
                "next_year": self.revenue["arr"] * 1.3
            },
            "metrics": {
                "arpu": round(self.revenue["mrr"] / max(self.clients["active"], 1), 2),
                "lifetime_value": self.revenue["mrr"] * 12 * 0.7,
                "churn_rate": "5.2%",
                "acquisition_cost": "$350"
            }
        }
    
    def get_client_health(self) -> Dict:
        """Get client health overview"""
        healthy = sum(1 for c in self.clients["list"] if c["status"] == "active")
        at_risk = sum(1 for c in self.clients["list"] if c["status"] == "at_risk")
        
        return {
            "healthy_clients": healthy,
            "at_risk_clients": at_risk,
            "health_score": round((healthy / max(self.clients["total"], 1)) * 100, 1),
            "client_list": self.clients["list"]
        }
    
    def get_agent_performance(self) -> Dict:
        """Get AI agent performance metrics"""
        return {
            "agents": [
                {"name": "SEO Auditor", "tasks_completed": 47, "avg_quality": 94.5, "status": "active"},
                {"name": "Content Writer", "tasks_completed": 82, "avg_quality": 92.0, "status": "active"},
                {"name": "Keyword Researcher", "tasks_completed": 35, "avg_quality": 96.0, "status": "active"},
                {"name": "Technical SEO", "tasks_completed": 28, "avg_quality": 91.5, "status": "active"},
                {"name": "Outreach Agent", "tasks_completed": 120, "avg_quality": 88.0, "status": "active"},
                {"name": "QA Reviewer", "tasks_completed": 65, "avg_quality": 97.0, "status": "active"},
                {"name": "Report Generator", "tasks_completed": 40, "avg_quality": 95.0, "status": "active"}
            ],
            "total_tasks": 417,
            "avg_quality_score": 93.4,
            "uptime": "99.9%"
        }
    
    def get_tasks(self) -> Dict:
        """Get pending and in-progress tasks"""
        return {
            "pending": [
                {"id": "TASK-001", "title": "SEO Audit - Prime Auto Sales", "priority": "high", "due": "2026-07-08"},
                {"id": "TASK-002", "title": "Content Strategy - TechFlow", "priority": "medium", "due": "2026-07-10"},
                {"id": "TASK-003", "title": "Technical Fixes - City Dental", "priority": "high", "due": "2026-07-07"}
            ],
            "in_progress": [
                {"id": "TASK-004", "title": "Monthly Report - GreenLeaf", "priority": "medium", "progress": 65},
                {"id": "TASK-005", "title": "Keyword Research - Bolt Fitness", "priority": "low", "progress": 30}
            ],
            "completed_today": 4,
            "total_pending": 3
        }
    
    def get_dashboard_status(self) -> Dict:
        """Get complete dashboard status"""
        return {
            "overview": self.get_overview(),
            "revenue": self.get_revenue_breakdown(),
            "clients": self.get_client_health(),
            "agents": self.get_agent_performance(),
            "tasks": self.get_tasks()
        }


if __name__ == "__main__":
    dashboard = AgencyDashboard()
    print("=" * 60)
    print("AGENCY DASHBOARD - LIVE MONITORING")
    print("=" * 60)
    
    overview = dashboard.get_overview()
    print(f"\n📊 OVERVIEW")
    print(f"  MRR: ${overview['revenue']['mrr']:,}")
    print(f"  ARR: ${overview['revenue']['arr']:,}")
    print(f"  Active Clients: {overview['clients']['active']}")
    print(f"  Active Projects: {overview['projects']['active']}")
    
    revenue = dashboard.get_revenue_breakdown()
    print(f"\n💰 REVENUE")
    print(f"  ARPU: ${revenue['metrics']['arpu']:,.2f}")
    print(f"  Churn Rate: {revenue['metrics']['churn_rate']}")
    print(f"  Next Month Projected: ${revenue['projected']['next_month']:,.0f}")
    
    agents = dashboard.get_agent_performance()
    print(f"\n🤖 AI AGENTS")
    print(f"  Total Tasks: {agents['total_tasks']}")
    print(f"  Avg Quality: {agents['avg_quality_score']}%")
    for agent in agents['agents']:
        print(f"  • {agent['name']:20s} | {agent['tasks_completed']:3d} tasks | {agent['avg_quality']}% quality")
    
    tasks = dashboard.get_tasks()
    print(f"\n📋 TASKS")
    print(f"  Pending: {tasks['total_pending']}")
    print(f"  Completed Today: {tasks['completed_today']}")
    for task in tasks['pending'][:2]:
        print(f"  • [{task['priority']:6s}] {task['title']}")
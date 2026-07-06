#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Cost Tracker
Milestone 1: Track AI usage costs across providers, projects, and clients with budget alerts.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta, date
import json
import uuid


class CostEntry:
    """Individual cost entry"""
    
    def __init__(self, provider: str, model: str, task_type: str,
                 input_tokens: int, output_tokens: int, cost: float,
                 project_id: str = None, client_id: str = None, agent: str = None):
        self.id = str(uuid.uuid4())[:12]
        self.provider = provider
        self.model = model
        self.task_type = task_type
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = input_tokens + output_tokens
        self.cost = cost
        self.project_id = project_id
        self.client_id = client_id
        self.agent = agent
        self.timestamp = datetime.now().isoformat()
        self.date = date.today().isoformat()


class CostTracker:
    """Track and analyze AI usage costs"""
    
    PROVIDER_COSTS = {
        "openai": {"gpt-4o": {"input": 0.01, "output": 0.03}},
        "anthropic": {"claude-3-5-sonnet": {"input": 0.003, "output": 0.015}},
        "gemini": {"gemini-1.5-pro": {"input": 0.0035, "output": 0.0105}},
        "groq": {"llama3-70b-8192": {"input": 0.00059, "output": 0.00079}},
        "openrouter": {"openrouter/auto": {"input": 0.001, "output": 0.003}}
    }
    
    def __init__(self):
        self.entries = []
        self.budgets = {}
        self.daily_costs = {}
        self.monthly_costs = {}
        self.project_budgets = {}
    
    def record_cost(self, provider: str, model: str, task_type: str,
                    input_tokens: int, output_tokens: int,
                    project_id: str = None, client_id: str = None, 
                    agent: str = None) -> CostEntry:
        """Record an AI usage cost"""
        cost = self._calculate_cost(provider, model, input_tokens, output_tokens)
        
        entry = CostEntry(provider, model, task_type, input_tokens, 
                         output_tokens, cost, project_id, client_id, agent)
        self.entries.append(entry)
        
        # Update daily costs
        today = date.today().isoformat()
        if today not in self.daily_costs:
            self.daily_costs[today] = 0.0
        self.daily_costs[today] += cost
        
        # Update monthly costs
        month = today[:7]  # YYYY-MM
        if month not in self.monthly_costs:
            self.monthly_costs[month] = {"cost": 0.0, "calls": 0, "tokens": 0}
        self.monthly_costs[month]["cost"] += cost
        self.monthly_costs[month]["calls"] += 1
        self.monthly_costs[month]["tokens"] += input_tokens + output_tokens
        
        # Check budget alerts
        self._check_budget_alerts(project_id, client_id)
        
        return entry
    
    def _calculate_cost(self, provider: str, model: str, 
                        input_tokens: int, output_tokens: int) -> float:
        """Calculate cost based on provider pricing"""
        provider_models = self.PROVIDER_COSTS.get(provider, {})
        pricing = provider_models.get(model, {"input": 0.001, "output": 0.003})
        
        input_cost = (input_tokens / 1000) * pricing["input"]
        output_cost = (output_tokens / 1000) * pricing["output"]
        
        return round(input_cost + output_cost, 6)
    
    def set_budget(self, project_id: str, monthly_limit: float, 
                   alert_threshold: float = 0.8) -> Dict:
        """Set a budget for a project"""
        budget = {
            "project_id": project_id,
            "monthly_limit": monthly_limit,
            "alert_threshold": alert_threshold,
            "current_spend": 0.0,
            "alerts_sent": []
        }
        self.project_budgets[project_id] = budget
        return budget
    
    def _check_budget_alerts(self, project_id: str, client_id: str):
        """Check if any budgets have been exceeded"""
        if project_id and project_id in self.project_budgets:
            budget = self.project_budgets[project_id]
            month = date.today().isoformat()[:7]
            
            # Calculate current month spend for this project
            monthly_spend = sum(
                e.cost for e in self.entries 
                if e.project_id == project_id and e.timestamp.startswith(month)
            )
            
            budget["current_spend"] = monthly_spend
            usage_ratio = monthly_spend / budget["monthly_limit"] if budget["monthly_limit"] > 0 else 0
            
            if usage_ratio >= budget["alert_threshold"]:
                # Send alert
                budget["alerts_sent"].append({
                    "date": datetime.now().isoformat(),
                    "usage_ratio": usage_ratio,
                    "current_spend": monthly_spend,
                    "limit": budget["monthly_limit"]
                })
    
    def get_daily_cost(self, days: int = 30) -> List[Dict]:
        """Get daily cost breakdown"""
        today = date.today()
        result = []
        
        for i in range(days - 1, -1, -1):
            d = (today - timedelta(days=i)).isoformat()
            result.append({
                "date": d,
                "cost": round(self.daily_costs.get(d, 0.0), 4),
                "calls": sum(1 for e in self.entries if e.timestamp.startswith(d))
            })
        
        return result
    
    def get_monthly_cost(self, months: int = 6) -> List[Dict]:
        """Get monthly cost breakdown"""
        today = date.today()
        result = []
        
        for i in range(months - 1, -1, -1):
            first = today.replace(day=1) - timedelta(days=i * 30)
            month = first.isoformat()[:7]
            data = self.monthly_costs.get(month, {"cost": 0.0, "calls": 0, "tokens": 0})
            result.append({
                "month": month,
                "cost": round(data["cost"], 2),
                "calls": data["calls"],
                "tokens": data["tokens"]
            })
        
        return result
    
    def get_cost_by_provider(self) -> Dict:
        """Get cost breakdown by provider"""
        providers = {}
        for entry in self.entries:
            if entry.provider not in providers:
                providers[entry.provider] = {"cost": 0.0, "calls": 0, "tokens": 0}
            providers[entry.provider]["cost"] += entry.cost
            providers[entry.provider]["calls"] += 1
            providers[entry.provider]["tokens"] += entry.total_tokens
        
        return {k: {**v, "cost": round(v["cost"], 2)} for k, v in providers.items()}
    
    def get_cost_by_project(self) -> Dict:
        """Get cost breakdown by project"""
        projects = {}
        for entry in self.entries:
            pid = entry.project_id or "uncategorized"
            if pid not in projects:
                projects[pid] = {"cost": 0.0, "calls": 0, "tokens": 0}
            projects[pid]["cost"] += entry.cost
            projects[pid]["calls"] += 1
            projects[pid]["tokens"] += entry.total_tokens
        
        return {k: {**v, "cost": round(v["cost"], 2)} for k, v in projects.items()}
    
    def get_cost_by_task(self) -> Dict:
        """Get cost breakdown by task type"""
        tasks = {}
        for entry in self.entries:
            task = entry.task_type
            if task not in tasks:
                tasks[task] = {"cost": 0.0, "calls": 0, "tokens": 0}
            tasks[task]["cost"] += entry.cost
            tasks[task]["calls"] += 1
            tasks[task]["tokens"] += entry.total_tokens
        
        return {k: {**v, "cost": round(v["cost"], 2)} for k, v in tasks.items()}
    
    def get_tracker_status(self) -> Dict:
        """Get cost tracker status"""
        total_cost = sum(e.cost for e in self.entries)
        total_calls = len(self.entries)
        total_tokens = sum(e.total_tokens for e in self.entries)
        
        return {
            "total_cost": round(total_cost, 2),
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "avg_cost_per_call": round(total_cost / max(total_calls, 1), 4),
            "avg_tokens_per_call": round(total_tokens / max(total_calls, 1)),
            "by_provider": self.get_cost_by_provider(),
            "by_project": self.get_cost_by_project(),
            "daily_trend": self.get_daily_cost(7),
            "active_budgets": len(self.project_budgets),
            "budget_alerts": sum(
                1 for b in self.project_budgets.values() if b["alerts_sent"]
            )
        }


if __name__ == "__main__":
    tracker = CostTracker()
    
    # Record some costs
    tracker.record_cost("openai", "gpt-4o", "content_creation", 1500, 3000, "proj-001")
    tracker.record_cost("anthropic", "claude-3-haiku", "outreach", 500, 800, "proj-001")
    tracker.record_cost("gemini", "gemini-1.5-pro", "research", 2000, 1000, "proj-002")
    tracker.record_cost("groq", "llama3-70b-8192", "data_extraction", 1000, 500, "proj-002")
    
    # Set budget
    tracker.set_budget("proj-001", 50.0)
    
    print("Cost Tracker Status:")
    status = tracker.get_tracker_status()
    print(f"  Total Cost: ${status['total_cost']}")
    print(f"  Total Calls: {status['total_calls']}")
    print(f"  Total Tokens: {status['total_tokens']:,}")
    print(f"  Avg Cost/Call: ${status['avg_cost_per_call']}")
    print(f"\n  By Provider:")
    for provider, data in status['by_provider'].items():
        print(f"    {provider:12s}: ${data['cost']:.2f} ({data['calls']} calls, {data['tokens']:,} tokens)")
    print(f"\n  By Project:")
    for project, data in status['by_project'].items():
        print(f"    {project:12s}: ${data['cost']:.2f} ({data['calls']} calls)")
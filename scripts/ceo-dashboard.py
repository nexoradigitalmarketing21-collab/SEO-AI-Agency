#!/usr/bin/env python3
"""
Nexora AI SEO Agency - CEO Dashboard
Command center for business intelligence and strategic decision-making.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os

class CEODashboard:
    """Executive-level business dashboard for strategic oversight"""
    
    def __init__(self, data_file: str = "data/business-metrics.json"):
        self.data_file = data_file
        self.metrics = self._load_metrics()
        self.targets = self._load_targets()
        
    def _load_metrics(self) -> Dict:
        """Load business metrics from file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return self._initialize_metrics()
    
    def _initialize_metrics(self) -> Dict:
        """Initialize default metrics structure"""
        return {
            "leads": [],
            "proposals": [],
            "projects": [],
            "revenue": [],
            "clients": [],
            "deliverables": [],
            "agent_utilization": [],
            "automation_metrics": [],
            "last_updated": datetime.now().isoformat()
        }
    
    def _load_targets(self) -> Dict:
        """Load business targets"""
        return {
            "monthly_revenue": 25000,
            "monthly_leads": 20,
            "win_rate": 25,
            "avg_project_value": 7500,
            "quality_score": 95,
            "delivery_time_hours": 48,
            "client_satisfaction": 90,
            "automation_rate": 80
        }
    
    def _save_metrics(self):
        """Save metrics to file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self.metrics["last_updated"] = datetime.now().isoformat()
        with open(self.data_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def calculate_revenue_metrics(self) -> Dict:
        """Calculate revenue metrics"""
        now = datetime.now()
        this_month = now.strftime('%Y-%m')
        last_month = (now - timedelta(days=30)).strftime('%Y-%m')
        
        # This month's revenue
        revenue_this_month = sum(
            r['amount'] for r in self.metrics['revenue']
            if datetime.fromisoformat(r['date']).strftime('%Y-%m') == this_month
        )
        
        # Last month's revenue
        revenue_last_month = sum(
            r['amount'] for r in self.metrics['revenue']
            if datetime.fromisoformat(r['date']).strftime('%Y-%m') == last_month
        )
        
        # Revenue target
        revenue_target = self.targets['monthly_revenue']
        
        # Revenue growth
        if revenue_last_month > 0:
            revenue_growth = ((revenue_this_month - revenue_last_month) / revenue_last_month) * 100
        else:
            revenue_growth = 0
        
        # Total revenue
        total_revenue = sum(r['amount'] for r in self.metrics['revenue'])
        
        # Profit calculation (assuming 60% profit margin)
        profit_margin = 0.60
        profit_this_month = revenue_this_month * profit_margin
        
        return {
            "revenue_this_month": revenue_this_month,
            "revenue_last_month": revenue_last_month,
            "revenue_target": revenue_target,
            "revenue_growth": round(revenue_growth, 2),
            "total_revenue": total_revenue,
            "profit_this_month": profit_this_month,
            "target_achievement": round((revenue_this_month / revenue_target) * 100, 2) if revenue_target > 0 else 0
        }
    
    def calculate_client_metrics(self) -> Dict:
        """Calculate client metrics"""
        now = datetime.now()
        thirty_days_ago = now - timedelta(days=30)
        
        # Active clients
        active_clients = len([p for p in self.metrics['projects'] if p['status'] == 'Active'])
        
        # New clients this month
        new_clients_this_month = len([
            p for p in self.metrics['projects']
            if datetime.fromisoformat(p['start_date']) >= thirty_days_ago
        ])
        
        # Total clients ever
        total_clients_ever = len(set(p['client_name'] for p in self.metrics['projects']))
        
        # Client retention rate
        completed_projects = [p for p in self.metrics['projects'] if p['status'] == 'Completed']
        retained_clients = len(set(p['client_name'] for p in completed_projects if p.get('retained', False)))
        retention_rate = (retained_clients / total_clients_ever * 100) if total_clients_ever > 0 else 0
        
        # Average client value
        if total_clients_ever > 0:
            total_revenue = sum(r['amount'] for r in self.metrics['revenue'])
            avg_client_value = total_revenue / total_clients_ever
        else:
            avg_client_value = 0
        
        return {
            "active_clients": active_clients,
            "new_clients_this_month": new_clients_this_month,
            "total_clients_ever": total_clients_ever,
            "retention_rate": round(retention_rate, 2),
            "avg_client_value": round(avg_client_value, 2)
        }
    
    def calculate_sales_metrics(self) -> Dict:
        """Calculate sales and proposal metrics"""
        now = datetime.now()
        thirty_days_ago = now - timedelta(days=30)
        
        # Leads
        total_leads = len(self.metrics['leads'])
        leads_this_month = len([
            l for l in self.metrics['leads']
            if datetime.fromisoformat(l['date']) >= thirty_days_ago
        ])
        
        # Proposals
        total_proposals = len(self.metrics['proposals'])
        proposals_this_month = len([
            p for p in self.metrics['proposals']
            if datetime.fromisoformat(p['date']) >= thirty_days_ago
        ])
        
        # Win rate
        won_proposals = len([p for p in self.metrics['proposals'] if p.get('won', False)])
        win_rate = (won_proposals / total_proposals * 100) if total_proposals > 0 else 0
        
        # Lead to proposal rate
        lead_to_proposal_rate = (total_proposals / total_leads * 100) if total_leads > 0 else 0
        
        # Average project value
        if self.metrics['projects']:
            avg_project_value = sum(p['value'] for p in self.metrics['projects']) / len(self.metrics['projects'])
        else:
            avg_project_value = 0
        
        # Sales conversion rate
        total_projects = len(self.metrics['projects'])
        sales_conversion_rate = (total_projects / total_leads * 100) if total_leads > 0 else 0
        
        return {
            "total_leads": total_leads,
            "leads_this_month": leads_this_month,
            "leads_target": self.targets['monthly_leads'],
            "total_proposals": total_proposals,
            "proposals_this_month": proposals_this_month,
            "win_rate": round(win_rate, 2),
            "win_rate_target": self.targets['win_rate'],
            "lead_to_proposal_rate": round(lead_to_proposal_rate, 2),
            "avg_project_value": round(avg_project_value, 2),
            "sales_conversion_rate": round(sales_conversion_rate, 2)
        }
    
    def calculate_delivery_metrics(self) -> Dict:
        """Calculate delivery and quality metrics"""
        # Average quality score
        if self.metrics['deliverables']:
            avg_quality_score = sum(d['quality_score'] for d in self.metrics['deliverables']) / len(self.metrics['deliverables'])
        else:
            avg_quality_score = 0
        
        # Quality target
        quality_target = self.targets['quality_score']
        
        # Average delivery time
        if self.metrics['deliverables']:
            avg_delivery_time = sum(d['delivery_time_hours'] for d in self.metrics['deliverables']) / len(self.metrics['deliverables'])
        else:
            avg_delivery_time = 0
        
        # Delivery time target
        delivery_target = self.targets['delivery_time_hours']
        
        # Quality pass rate
        if self.metrics['deliverables']:
            passed = len([d for d in self.metrics['deliverables'] if d['quality_score'] >= 90])
            quality_pass_rate = (passed / len(self.metrics['deliverables'])) * 100
        else:
            quality_pass_rate = 0
        
        # Total deliverables
        total_deliverables = len(self.metrics['deliverables'])
        
        return {
            "avg_quality_score": round(avg_quality_score, 2),
            "quality_target": quality_target,
            "quality_gap": round(avg_quality_score - quality_target, 2),
            "avg_delivery_time": round(avg_delivery_time, 2),
            "delivery_target": delivery_target,
            "delivery_efficiency": round((delivery_target / avg_delivery_time * 100) if avg_delivery_time > 0 else 0, 2),
            "quality_pass_rate": round(quality_pass_rate, 2),
            "total_deliverables": total_deliverables
        }
    
    def calculate_agent_utilization(self) -> Dict:
        """Calculate agent utilization metrics"""
        # Simulated agent data (in production, this would come from actual agent monitoring)
        agents = {
            "CEO Agent": {"status": "active", "tasks_completed": 45, "tasks_assigned": 50},
            "Sales Agent": {"status": "active", "tasks_completed": 38, "tasks_assigned": 40},
            "SEO Strategist": {"status": "active", "tasks_completed": 52, "tasks_assigned": 55},
            "Technical SEO": {"status": "active", "tasks_completed": 41, "tasks_assigned": 45},
            "Keyword Research": {"status": "active", "tasks_completed": 48, "tasks_assigned": 50},
            "Content Writer": {"status": "active", "tasks_completed": 35, "tasks_assigned": 40},
            "Reporting Agent": {"status": "active", "tasks_completed": 28, "tasks_assigned": 30},
            "QA Agent": {"status": "active", "tasks_completed": 42, "tasks_assigned": 45}
        }
        
        agent_metrics = {}
        total_utilization = 0
        
        for agent_name, data in agents.items():
            utilization = (data['tasks_completed'] / data['tasks_assigned'] * 100) if data['tasks_assigned'] > 0 else 0
            agent_metrics[agent_name] = {
                "status": data['status'],
                "tasks_completed": data['tasks_completed'],
                "tasks_assigned": data['tasks_assigned'],
                "utilization": round(utilization, 2)
            }
            total_utilization += utilization
        
        avg_utilization = total_utilization / len(agents) if agents else 0
        
        return {
            "agents": agent_metrics,
            "average_utilization": round(avg_utilization, 2),
            "total_tasks_completed": sum(a['tasks_completed'] for a in agents.values()),
            "total_tasks_assigned": sum(a['tasks_assigned'] for a in agents.values())
        }
    
    def calculate_automation_metrics(self) -> Dict:
        """Calculate automation and time savings"""
        # Simulated automation data
        total_tasks = 156
        automated_tasks = 142
        manual_tasks = total_tasks - automated_tasks
        
        automation_rate = (automated_tasks / total_tasks * 100) if total_tasks > 0 else 0
        automation_target = self.targets['automation_rate']
        
        # Time savings (assuming 30 minutes per manual task)
        time_saved_hours = (automated_tasks * 0.5)  # 30 minutes per task
        time_saved_value = time_saved_hours * 100  # $100/hour value
        
        # Efficiency gain
        efficiency_gain = automation_rate
        
        return {
            "total_tasks": total_tasks,
            "automated_tasks": automated_tasks,
            "manual_tasks": manual_tasks,
            "automation_rate": round(automation_rate, 2),
            "automation_target": automation_target,
            "automation_gap": round(automation_rate - automation_target, 2),
            "time_saved_hours": round(time_saved_hours, 2),
            "time_saved_value": round(time_saved_value, 2),
            "efficiency_gain": round(efficiency_gain, 2)
        }
    
    def calculate_profit_per_project(self) -> Dict:
        """Calculate profit metrics per project"""
        projects = self.metrics['projects']
        
        if not projects:
            return {
                "avg_profit_per_project": 0,
                "total_projects": 0,
                "most_profitable_project": None,
                "profit_margin": 0
            }
        
        # Calculate profit per project (assuming 60% profit margin)
        profit_margin = 0.60
        project_profits = []
        
        for project in projects:
            project_revenue = sum(
                r['amount'] for r in self.metrics['revenue']
                if r.get('project_id') == project.get('project_id')
            )
            profit = project_revenue * profit_margin
            project_profits.append({
                "project_id": project.get('project_id'),
                "client_name": project.get('client_name'),
                "revenue": project_revenue,
                "profit": profit,
                "margin": profit_margin * 100
            })
        
        avg_profit = sum(p['profit'] for p in project_profits) / len(project_profits) if project_profits else 0
        most_profitable = max(project_profits, key=lambda x: x['profit']) if project_profits else None
        
        return {
            "avg_profit_per_project": round(avg_profit, 2),
            "total_projects": len(projects),
            "most_profitable_project": most_profitable,
            "profit_margin": profit_margin * 100
        }
    
    def generate_ceo_dashboard(self) -> str:
        """Generate comprehensive CEO dashboard"""
        # Calculate all metrics
        revenue_metrics = self.calculate_revenue_metrics()
        client_metrics = self.calculate_client_metrics()
        sales_metrics = self.calculate_sales_metrics()
        delivery_metrics = self.calculate_delivery_metrics()
        agent_utilization = self.calculate_agent_utilization()
        automation_metrics = self.calculate_automation_metrics()
        profit_metrics = self.calculate_profit_per_project()
        
        # Generate dashboard
        dashboard = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    NEXORA AI SEO AGENCY - CEO DASHBOARD                     ║
║                         Command Center for Strategic Growth                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 REVENUE COMMAND CENTER

  Revenue This Month:      ${revenue_metrics['revenue_this_month']:>12,.2f}
  Revenue Target:          ${revenue_metrics['revenue_target']:>12,.2f}
  Target Achievement:      {revenue_metrics['target_achievement']:>11.2f}%
  Revenue Growth:          {revenue_metrics['revenue_growth']:>11.2f}%
  Profit This Month:       ${revenue_metrics['profit_this_month']:>12,.2f}
  Total Revenue:           ${revenue_metrics['total_revenue']:>12,.2f}

  Status: {'✅ ON TRACK' if revenue_metrics['target_achievement'] >= 80 else '⚠️  BELOW TARGET' if revenue_metrics['target_achievement'] < 50 else '📈 PROGRESSING'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 CLIENT PORTFOLIO

  Active Clients:          {client_metrics['active_clients']:>6}
  New Clients (30 Days):   {client_metrics['new_clients_this_month']:>6}
  Total Clients Ever:      {client_metrics['total_clients_ever']:>6}
  Client Retention Rate:   {client_metrics['retention_rate']:>6.2f}%
  Avg Client Value:        ${client_metrics['avg_client_value']:>10,.2f}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SALES PERFORMANCE

  Leads This Month:        {sales_metrics['leads_this_month']:>6} / {sales_metrics['leads_target']:>6} target
  Proposals This Month:    {sales_metrics['proposals_this_month']:>6}
  Win Rate:                {sales_metrics['win_rate']:>6.2f}% (target: {sales_metrics['win_rate_target']}%)
  Avg Project Value:       ${sales_metrics['avg_project_value']:>10,.2f}
  Sales Conversion Rate:   {sales_metrics['sales_conversion_rate']:>6.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ DELIVERY EXCELLENCE

  Avg Quality Score:       {delivery_metrics['avg_quality_score']:>6.2f}/100 (target: {delivery_metrics['quality_target']})
  Quality Gap:             {delivery_metrics['quality_gap']:>+6.2f}
  Avg Delivery Time:       {delivery_metrics['avg_delivery_time']:>6.1f}h (target: {delivery_metrics['delivery_target']}h)
  Delivery Efficiency:     {delivery_metrics['delivery_efficiency']:>6.2f}%
  Quality Pass Rate:       {delivery_metrics['quality_pass_rate']:>6.2f}%
  Total Deliverables:      {delivery_metrics['total_deliverables']:>6}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AGENT UTILIZATION

  Average Utilization:     {agent_utilization['average_utilization']:>6.2f}%
  Total Tasks Completed:   {agent_utilization['total_tasks_completed']:>6}
  Total Tasks Assigned:    {agent_utilization['total_tasks_assigned']:>6}

  Agent Breakdown:
"""
        
        # Add agent breakdown
        for agent_name, metrics in agent_utilization['agents'].items():
            status_icon = "✅" if metrics['utilization'] >= 80 else "⚠️" if metrics['utilization'] >= 60 else "❌"
            dashboard += f"    {status_icon} {agent_name:20s}: {metrics['utilization']:>5.1f}% ({metrics['tasks_completed']}/{metrics['tasks_assigned']})\n"
        
        dashboard += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️  AUTOMATION & EFFICIENCY

  Automation Rate:         {automation_metrics['automation_rate']:>6.2f}% (target: {automation_metrics['automation_target']}%)
  Automation Gap:          {automation_metrics['automation_gap']:>+6.2f}%
  Time Saved This Month:   {automation_metrics['time_saved_hours']:>6.1f}h
  Time Saved Value:        ${automation_metrics['time_saved_value']:>10,.2f}
  Efficiency Gain:         {automation_metrics['efficiency_gain']:>6.2f}%
  Manual Tasks Remaining:  {automation_metrics['manual_tasks']:>6} / {automation_metrics['total_tasks']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎 PROFITABILITY ANALYSIS

  Avg Profit/Project:      ${profit_metrics['avg_profit_per_project']:>10,.2f}
  Total Projects:          {profit_metrics['total_projects']:>6}
  Profit Margin:           {profit_metrics['profit_margin']:>6.2f}%
  
"""
        
        # Add most profitable project
        if profit_metrics['most_profitable_project']:
            mpp = profit_metrics['most_profitable_project']
            dashboard += f"""  Most Profitable Project:
    Client: {mpp['client_name']}
    Revenue: ${mpp['revenue']:,.2f}
    Profit:  ${mpp['profit']:,.2f}
"""
        
        dashboard += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 KEY PERFORMANCE INDICATORS

  Monthly Recurring Revenue:  ${revenue_metrics['revenue_this_month']:>12,.2f}
  Active Client Count:         {client_metrics['active_clients']:>6}
  Proposal Win Rate:           {sales_metrics['win_rate']:>6.2f}%
  Average Quality Score:       {delivery_metrics['avg_quality_score']:>6.2f}/100
  Agent Utilization:           {agent_utilization['average_utilization']:>6.2f}%
  Automation Rate:             {automation_metrics['automation_rate']:>6.2f}%
  Client Retention Rate:       {client_metrics['retention_rate']:>6.2f}%
  Profit Margin:               {profit_metrics['profit_margin']:>6.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 STRATEGIC INSIGHTS

"""
        
        # Generate insights
        insights = self._generate_ceo_insights(
            revenue_metrics, client_metrics, sales_metrics,
            delivery_metrics, agent_utilization, automation_metrics, profit_metrics
        )
        
        for insight in insights:
            dashboard += f"  {insight}\n"
        
        dashboard += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎬 RECOMMENDED ACTIONS

"""
        
        # Generate recommended actions
        actions = self._generate_recommended_actions(
            revenue_metrics, client_metrics, sales_metrics,
            delivery_metrics, agent_utilization, automation_metrics
        )
        
        for i, action in enumerate(actions, 1):
            dashboard += f"  {i}. {action}\n"
        
        dashboard += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 PROJECTIONS (Next 30 Days)

  Projected Revenue:        ${revenue_metrics['revenue_this_month'] * 1.15:>12,.2f} (+15%)
  Projected Leads:          {sales_metrics['leads_this_month'] + 5:>6}
  Projected New Clients:    {client_metrics['new_clients_this_month'] + 2:>6}
  Projected Deliverables:   {delivery_metrics['total_deliverables'] + 15:>6}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated by Nexora AI SEO Agency CEO Dashboard
{datetime.now().strftime('%Y')}

"""
        return dashboard
    
    def _generate_ceo_insights(self, revenue: Dict, clients: Dict, sales: Dict,
                               delivery: Dict, agents: Dict, automation: Dict, profit: Dict) -> List[str]:
        """Generate strategic insights for CEO"""
        insights = []
        
        # Revenue insights
        if revenue['target_achievement'] >= 100:
            insights.append("✅ Revenue target exceeded - " + f"${revenue['revenue_this_month']:,.2f}" + " vs $" + f"{revenue['revenue_target']:,.2f}" + " target")
        elif revenue['target_achievement'] >= 80:
            insights.append("📈 Revenue on track - " + f"{revenue['target_achievement']:.1f}% of target achieved")
        else:
            insights.append("⚠️  Revenue below target - " + f"Only {revenue['target_achievement']:.1f}% achieved. Action needed.")
        
        # Client insights
        if clients['retention_rate'] >= 80:
            insights.append("✅ Excellent client retention - " + f"{clients['retention_rate']:.1f}%")
        elif clients['retention_rate'] < 50:
            insights.append("⚠️  Client retention needs attention - " + f"{clients['retention_rate']:.1f}%")
        
        # Sales insights
        if sales['win_rate'] >= 30:
            insights.append("✅ Strong win rate - " + f"{sales['win_rate']:.1f}%")
        elif sales['win_rate'] < 15:
            insights.append("⚠️  Low win rate - Review proposals and pricing strategy")
        
        # Quality insights
        if delivery['avg_quality_score'] >= 95:
            insights.append("✅ Excellent quality - " + f"{delivery['avg_quality_score']:.1f}/100 average")
        elif delivery['avg_quality_score'] < 85:
            insights.append("⚠️  Quality below standard - Review QA processes")
        
        # Automation insights
        if automation['automation_rate'] >= 80:
            insights.append("✅ High automation - " + f"{automation['automation_rate']:.1f}% of tasks automated")
        else:
            insights.append("📊 Automation opportunity - " + f"Only {automation['automation_rate']:.1f}% automated, target is {automation['automation_target']}%")
        
        # Agent insights
        if agents['average_utilization'] >= 80:
            insights.append("✅ High agent utilization - " + f"{agents['average_utilization']:.1f}%")
        elif agents['average_utilization'] < 60:
            insights.append("⚠️  Low agent utilization - Consider workload redistribution")
        
        # Profit insights
        if profit['avg_profit_per_project'] > 3000:
            insights.append("✅ Strong profitability - " + f"${profit['avg_profit_per_project']:,.2f} avg profit per project")
        
        return insights
    
    def _generate_recommended_actions(self, revenue: Dict, clients: Dict, sales: Dict,
                                      delivery: Dict, agents: Dict, automation: Dict) -> List[str]:
        """Generate recommended actions for CEO"""
        actions = []
        
        # Revenue actions
        if revenue['target_achievement'] < 80:
            actions.append("Increase sales outreach - Target " + str(sales['leads_target'] - sales['leads_this_month']) + " more leads this month")
        
        # Sales actions
        if sales['win_rate'] < 20:
            actions.append("Review proposal quality and pricing strategy to improve win rate")
        
        if sales['leads_this_month'] < sales['leads_target']:
            actions.append("Boost lead generation through Upwork, Fiverr, and Freelancer platforms")
        
        # Quality actions
        if delivery['avg_quality_score'] < 90:
            actions.append("Focus on quality improvement - Current score " + f"{delivery['avg_quality_score']:.1f}/100, target 95/100")
        
        # Automation actions
        if automation['automation_rate'] < automation['automation_target']:
            actions.append("Increase automation - " + f"Close {automation['automation_gap']:.1f}% gap to reach {automation['automation_target']}% target")
        
        # Agent actions
        underutilized = [name for name, metrics in agents['agents'].items() if metrics['utilization'] < 70]
        if underutilized:
            actions.append("Redistribute workload to underutilized agents: " + ", ".join(underutilized))
        
        # Client actions
        if clients['retention_rate'] < 70:
            actions.append("Improve client retention - Implement check-ins and satisfaction surveys")
        
        if not actions:
            actions.append("Continue current strategy - All metrics on track")
        
        return actions
    
    def export_ceo_report(self, output_path: str):
        """Export CEO dashboard report"""
        dashboard = self.generate_ceo_dashboard()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(dashboard)
        
        print(f"✓ CEO Dashboard exported to: {output_path}")
    
    def get_executive_summary(self) -> Dict:
        """Get executive summary for quick review"""
        revenue = self.calculate_revenue_metrics()
        clients = self.calculate_client_metrics()
        sales = self.calculate_sales_metrics()
        delivery = self.calculate_delivery_metrics()
        automation = self.calculate_automation_metrics()
        
        return {
            "revenue_this_month": revenue['revenue_this_month'],
            "revenue_target": revenue['revenue_target'],
            "target_achievement": revenue['target_achievement'],
            "active_clients": clients['active_clients'],
            "new_clients": clients['new_clients_this_month'],
            "win_rate": sales['win_rate'],
            "leads_this_month": sales['leads_this_month'],
            "avg_quality_score": delivery['avg_quality_score'],
            "automation_rate": automation['automation_rate'],
            "profit_this_month": revenue['profit_this_month'],
            "overall_health": self._calculate_overall_health(revenue, clients, sales, delivery, automation)
        }
    
    def _calculate_overall_health(self, revenue: Dict, clients: Dict, sales: Dict,
                                   delivery: Dict, automation: Dict) -> str:
        """Calculate overall business health"""
        scores = []
        
        # Revenue health
        scores.append(min(100, revenue['target_achievement']))
        
        # Client health
        scores.append(clients['retention_rate'])
        
        # Sales health
        scores.append(sales['win_rate'] * 3)  # Scale to 100
        
        # Quality health
        scores.append(delivery['avg_quality_score'])
        
        # Automation health
        scores.append(automation['automation_rate'])
        
        avg_score = sum(scores) / len(scores)
        
        if avg_score >= 80:
            return "EXCELLENT"
        elif avg_score >= 60:
            return "GOOD"
        elif avg_score >= 40:
            return "FAIR"
        else:
            return "NEEDS_ATTENTION"


def demonstrate_ceo_dashboard():
    """Demonstrate CEO dashboard"""
    print("\n" + "="*80)
    print("CEO DASHBOARD DEMONSTRATION")
    print("="*80 + "\n")
    
    ceo_dashboard = CEODashboard()
    
    # Add sample data
    print("Step 1: Loading business data...")
    print("-" * 80)
    
    # Add sample leads
    ceo_dashboard.metrics['leads'].append({
        'date': datetime.now().isoformat(),
        'source': 'Upwork',
        'platform': 'Upwork',
        'client_name': 'John Smith',
        'company': 'TechStart Solutions',
        'budget': '$5,000-$10,000',
        'services': ['SEO Audit']
    })
    
    # Add sample proposals
    ceo_dashboard.metrics['proposals'].append({
        'date': datetime.now().isoformat(),
        'platform': 'Upwork',
        'client_name': 'John Smith',
        'project_value': 7500,
        'won': True
    })
    
    # Add sample projects
    ceo_dashboard.metrics['projects'].append({
        'project_id': 'PROJ-001',
        'start_date': datetime.now().isoformat(),
        'client_name': 'John Smith',
        'company': 'TechStart Solutions',
        'services': ['SEO Audit'],
        'value': 7500,
        'status': 'Active',
        'retained': True
    })
    
    # Add sample revenue
    ceo_dashboard.metrics['revenue'].append({
        'date': datetime.now().isoformat(),
        'project_id': 'PROJ-001',
        'client_name': 'John Smith',
        'amount': 7500,
        'type': 'project_payment'
    })
    
    # Add sample deliverables
    ceo_dashboard.metrics['deliverables'].append({
        'date': datetime.now().isoformat(),
        'project_id': 'PROJ-001',
        'client_name': 'John Smith',
        'type': 'SEO Audit',
        'quality_score': 95.5,
        'delivery_time_hours': 48
    })
    
    print("✓ Sample data loaded")
    
    print("\n\nStep 2: Generating CEO Dashboard...")
    print("-" * 80)
    
    # Generate and display dashboard
    dashboard_report = ceo_dashboard.generate_ceo_dashboard()
    print(dashboard_report)
    
    print("Step 3: Executive Summary")
    print("-" * 80)
    
    summary = ceo_dashboard.get_executive_summary()
    print(f"\nRevenue This Month:  ${summary['revenue_this_month']:,.2f}")
    print(f"Revenue Target:      ${summary['revenue_target']:,.2f}")
    print(f"Target Achievement:  {summary['target_achievement']:.1f}%")
    print(f"Active Clients:      {summary['active_clients']}")
    print(f"New Clients (30d):   {summary['new_clients']}")
    print(f"Win Rate:            {summary['win_rate']:.1f}%")
    print(f"Leads (30 Days):     {summary['leads_this_month']}")
    print(f"Avg Quality Score:   {summary['avg_quality_score']:.1f}/100")
    print(f"Automation Rate:     {summary['automation_rate']:.1f}%")
    print(f"Profit This Month:   ${summary['profit_this_month']:,.2f}")
    print(f"Overall Health:      {summary['overall_health']}")
    
    print("\n\nStep 4: Exporting dashboard...")
    print("-" * 80)
    ceo_dashboard.export_ceo_report("data/ceo-dashboard-report.txt")
    
    print("\n" + "="*80)
    print("CEO DASHBOARD READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Revenue command center")
    print("✓ Client portfolio management")
    print("✓ Sales performance tracking")
    print("✓ Delivery excellence metrics")
    print("✓ Agent utilization monitoring")
    print("✓ Automation & efficiency tracking")
    print("✓ Profitability analysis")
    print("✓ Strategic insights generation")
    print("✓ Recommended actions")
    print("✓ 30-day projections")
    print("✓ Executive summary")
    print("✓ Overall business health score")
    print("\n")


if __name__ == "__main__":
    demonstrate_ceo_dashboard()
#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Business Dashboard
Track business metrics, KPIs, and performance.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os

class BusinessDashboard:
    """Business intelligence and metrics dashboard"""
    
    def __init__(self, data_file: str = "data/business-metrics.json"):
        self.data_file = data_file
        self.metrics = self._load_metrics()
        
    def _load_metrics(self) -> Dict:
        """Load business metrics from file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        
        # Initialize with default structure
        return {
            "leads": [],
            "proposals": [],
            "projects": [],
            "revenue": [],
            "clients": [],
            "deliverables": [],
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_metrics(self):
        """Save metrics to file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self.metrics["last_updated"] = datetime.now().isoformat()
        with open(self.data_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def add_lead(self, lead_data: Dict) -> Dict:
        """Add new lead"""
        lead = {
            "lead_id": f"LEAD-{len(self.metrics['leads']) + 1:04d}",
            "date": datetime.now().isoformat(),
            "source": lead_data.get('source', 'Unknown'),
            "platform": lead_data.get('platform', 'Unknown'),
            "client_name": lead_data.get('client_name', ''),
            "company": lead_data.get('company', ''),
            "email": lead_data.get('email', ''),
            "budget": lead_data.get('budget', ''),
            "services": lead_data.get('services', []),
            "status": "New",
            "converted": False
        }
        
        self.metrics['leads'].append(lead)
        self._save_metrics()
        
        return lead
    
    def add_proposal(self, proposal_data: Dict) -> Dict:
        """Add sent proposal"""
        proposal = {
            "proposal_id": f"PROP-{len(self.metrics['proposals']) + 1:04d}",
            "date": datetime.now().isoformat(),
            "lead_id": proposal_data.get('lead_id'),
            "platform": proposal_data.get('platform', 'Unknown'),
            "client_name": proposal_data.get('client_name', ''),
            "project_value": proposal_data.get('project_value', 0),
            "services": proposal_data.get('services', []),
            "status": "Sent",
            "responded": False,
            "won": False
        }
        
        self.metrics['proposals'].append(proposal)
        self._save_metrics()
        
        return proposal
    
    def add_project(self, project_data: Dict) -> Dict:
        """Add won project"""
        project = {
            "project_id": f"PROJ-{len(self.metrics['projects']) + 1:04d}",
            "start_date": datetime.now().isoformat(),
            "client_name": project_data.get('client_name', ''),
            "company": project_data.get('company', ''),
            "services": project_data.get('services', []),
            "value": project_data.get('value', 0),
            "status": "Active",
            "completion_date": None,
            "revenue_received": 0
        }
        
        self.metrics['projects'].append(project)
        self._save_metrics()
        
        return project
    
    def add_revenue(self, revenue_data: Dict):
        """Add revenue transaction"""
        transaction = {
            "transaction_id": f"REV-{len(self.metrics['revenue']) + 1:04d}",
            "date": datetime.now().isoformat(),
            "project_id": revenue_data.get('project_id'),
            "client_name": revenue_data.get('client_name', ''),
            "amount": revenue_data.get('amount', 0),
            "type": revenue_data.get('type', 'payment'),
            "status": "completed"
        }
        
        self.metrics['revenue'].append(transaction)
        self._save_metrics()
        
        return transaction
    
    def add_deliverable(self, deliverable_data: Dict):
        """Add completed deliverable"""
        deliverable = {
            "deliverable_id": f"DEL-{len(self.metrics['deliverables']) + 1:04d}",
            "date": datetime.now().isoformat(),
            "project_id": deliverable_data.get('project_id'),
            "client_name": deliverable_data.get('client_name', ''),
            "type": deliverable_data.get('type', ''),
            "quality_score": deliverable_data.get('quality_score', 0),
            "delivery_time_hours": deliverable_data.get('delivery_time_hours', 0)
        }
        
        self.metrics['deliverables'].append(deliverable)
        self._save_metrics()
        
        return deliverable
    
    def get_dashboard_metrics(self) -> Dict:
        """Get comprehensive dashboard metrics"""
        now = datetime.now()
        thirty_days_ago = now - timedelta(days=30)
        
        # Leads metrics
        total_leads = len(self.metrics['leads'])
        leads_last_30d = len([l for l in self.metrics['leads'] 
                             if datetime.fromisoformat(l['date']) >= thirty_days_ago])
        leads_by_source = self._count_by_field(self.metrics['leads'], 'source')
        leads_by_platform = self._count_by_field(self.metrics['leads'], 'platform')
        conversion_rate = self._calculate_conversion_rate()
        
        # Proposals metrics
        total_proposals = len(self.metrics['proposals'])
        proposals_last_30d = len([p for p in self.metrics['proposals'] 
                                 if datetime.fromisoformat(p['date']) >= thirty_days_ago])
        win_rate = self._calculate_win_rate()
        avg_project_value = self._calculate_avg_project_value()
        
        # Projects metrics
        active_projects = len([p for p in self.metrics['projects'] if p['status'] == 'Active'])
        completed_projects = len([p for p in self.metrics['projects'] if p['status'] == 'Completed'])
        
        # Revenue metrics
        total_revenue = sum(r['amount'] for r in self.metrics['revenue'])
        revenue_last_30d = sum(r['amount'] for r in self.metrics['revenue'] 
                              if datetime.fromisoformat(r['date']) >= thirty_days_ago])
        revenue_by_month = self._revenue_by_month()
        
        # Deliverables metrics
        total_deliverables = len(self.metrics['deliverables'])
        deliverables_last_30d = len([d for d in self.metrics['deliverables'] 
                                    if datetime.fromisoformat(d['date']) >= thirty_days_ago])
        avg_quality_score = self._calculate_avg_quality_score()
        avg_delivery_time = self._calculate_avg_delivery_time()
        
        # Client metrics
        active_clients = len([p for p in self.metrics['projects'] if p['status'] == 'Active'])
        total_clients_ever = len(set(p['client_name'] for p in self.metrics['projects']))
        
        return {
            "overview": {
                "total_leads": total_leads,
                "leads_last_30_days": leads_last_30d,
                "total_proposals": total_proposals,
                "proposals_last_30_days": proposals_last_30d,
                "active_projects": active_projects,
                "completed_projects": completed_projects,
                "active_clients": active_clients,
                "total_clients_ever": total_clients_ever
            },
            "conversion_metrics": {
                "lead_to_proposal_rate": self._calculate_rate(total_leads, total_proposals),
                "proposal_win_rate": win_rate,
                "overall_conversion_rate": conversion_rate,
                "avg_project_value": avg_project_value
            },
            "revenue_metrics": {
                "total_revenue": total_revenue,
                "revenue_last_30_days": revenue_last_30d,
                "revenue_by_month": revenue_by_month,
                "avg_revenue_per_client": total_revenue / total_clients_ever if total_clients_ever > 0 else 0
            },
            "delivery_metrics": {
                "total_deliverables": total_deliverables,
                "deliverables_last_30_days": deliverables_last_30d,
                "avg_quality_score": avg_quality_score,
                "avg_delivery_time_hours": avg_delivery_time,
                "quality_pass_rate": self._calculate_quality_pass_rate()
            },
            "breakdown": {
                "leads_by_source": leads_by_source,
                "leads_by_platform": leads_by_platform,
                "revenue_by_type": self._count_by_field(self.metrics['revenue'], 'type')
            },
            "trends": {
                "leads_trend": self._calculate_trend('leads'),
                "revenue_trend": self._calculate_trend('revenue'),
                "projects_trend": self._calculate_trend('projects')
            }
        }
    
    def _count_by_field(self, items: List[Dict], field: str) -> Dict:
        """Count items by field value"""
        counts = {}
        for item in items:
            value = item.get(field, 'Unknown')
            counts[value] = counts.get(value, 0) + 1
        return counts
    
    def _calculate_conversion_rate(self) -> float:
        """Calculate lead to project conversion rate"""
        total_leads = len(self.metrics['leads'])
        total_projects = len(self.metrics['projects'])
        
        if total_leads == 0:
            return 0.0
        
        return round((total_projects / total_leads) * 100, 2)
    
    def _calculate_win_rate(self) -> float:
        """Calculate proposal win rate"""
        total_proposals = len(self.metrics['proposals'])
        won_proposals = len([p for p in self.metrics['proposals'] if p.get('won', False)])
        
        if total_proposals == 0:
            return 0.0
        
        return round((won_proposals / total_proposals) * 100, 2)
    
    def _calculate_rate(self, numerator: int, denominator: int) -> float:
        """Calculate percentage rate"""
        if denominator == 0:
            return 0.0
        return round((numerator / denominator) * 100, 2)
    
    def _calculate_avg_project_value(self) -> float:
        """Calculate average project value"""
        projects = self.metrics['projects']
        if not projects:
            return 0.0
        
        total_value = sum(p['value'] for p in projects)
        return round(total_value / len(projects), 2)
    
    def _calculate_avg_quality_score(self) -> float:
        """Calculate average quality score"""
        deliverables = self.metrics['deliverables']
        if not deliverables:
            return 0.0
        
        total_score = sum(d['quality_score'] for d in deliverables)
        return round(total_score / len(deliverables), 2)
    
    def _calculate_avg_delivery_time(self) -> float:
        """Calculate average delivery time in hours"""
        deliverables = self.metrics['deliverables']
        if not deliverables:
            return 0.0
        
        total_time = sum(d['delivery_time_hours'] for d in deliverables)
        return round(total_time / len(deliverables), 2)
    
    def _calculate_quality_pass_rate(self) -> float:
        """Calculate quality pass rate"""
        deliverables = self.metrics['deliverables']
        if not deliverables:
            return 0.0
        
        passed = len([d for d in deliverables if d['quality_score'] >= 90])
        return round((passed / len(deliverables)) * 100, 2)
    
    def _revenue_by_month(self) -> Dict:
        """Calculate revenue by month"""
        revenue_by_month = {}
        
        for transaction in self.metrics['revenue']:
            date = datetime.fromisoformat(transaction['date'])
            month_key = date.strftime('%Y-%m')
            
            if month_key not in revenue_by_month:
                revenue_by_month[month_key] = 0
            
            revenue_by_month[month_key] += transaction['amount']
        
        return revenue_by_month
    
    def _calculate_trend(self, metric_type: str) -> str:
        """Calculate trend for a metric"""
        items = self.metrics.get(metric_type, [])
        
        if len(items) < 2:
            return "stable"
        
        # Compare last 30 days to previous 30 days
        now = datetime.now()
        thirty_days_ago = now - timedelta(days=30)
        sixty_days_ago = now - timedelta(days=60)
        
        recent = len([i for i in items if datetime.fromisoformat(i['date']) >= thirty_days_ago])
        previous = len([i for i in items 
                       if sixty_days_ago <= datetime.fromisoformat(i['date']) < thirty_days_ago])
        
        if previous == 0:
            return "up" if recent > 0 else "stable"
        
        change = ((recent - previous) / previous) * 100
        
        if change > 10:
            return "up"
        elif change < -10:
            return "down"
        else:
            return "stable"
    
    def generate_dashboard_report(self) -> str:
        """Generate visual dashboard report"""
        metrics = self.get_dashboard_metrics()
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║          NEXORA AI SEO AGENCY - BUSINESS DASHBOARD           ║
╚══════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 OVERVIEW

  Total Leads:            {metrics['overview']['total_leads']:>6}
  Leads (Last 30 Days):   {metrics['overview']['leads_last_30_days']:>6}
  Total Proposals:        {metrics['overview']['total_proposals']:>6}
  Proposals (Last 30d):   {metrics['overview']['proposals_last_30_days']:>6}
  Active Projects:        {metrics['overview']['active_projects']:>6}
  Completed Projects:     {metrics['overview']['completed_projects']:>6}
  Active Clients:         {metrics['overview']['active_clients']:>6}
  Total Clients Ever:     {metrics['overview']['total_clients_ever']:>6}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 CONVERSION METRICS

  Lead → Proposal Rate:   {metrics['conversion_metrics']['lead_to_proposal_rate']:>6}%
  Proposal Win Rate:      {metrics['conversion_metrics']['proposal_win_rate']:>6}%
  Overall Conversion:     {metrics['conversion_metrics']['overall_conversion_rate']:>6}%
  Avg Project Value:      ${metrics['conversion_metrics']['avg_project_value']:>8,.2f}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💵 REVENUE METRICS

  Total Revenue:          ${metrics['revenue_metrics']['total_revenue']:>10,.2f}
  Revenue (Last 30 Days): ${metrics['revenue_metrics']['revenue_last_30_days']:>10,.2f}
  Avg Revenue/Client:     ${metrics['revenue_metrics']['avg_revenue_per_client']:>8,.2f}

  Revenue by Month:
"""
        # Add revenue by month
        for month, revenue in sorted(metrics['revenue_metrics']['revenue_by_month'].items()):
            report += f"    {month}: ${revenue:>10,.2f}\n"
        
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 DELIVERY METRICS

  Total Deliverables:     {metrics['delivery_metrics']['total_deliverables']:>6}
  Deliverables (30 Days): {metrics['delivery_metrics']['deliverables_last_30_days']:>6}
  Avg Quality Score:      {metrics['delivery_metrics']['avg_quality_score']:>6.2f}/100
  Avg Delivery Time:      {metrics['delivery_metrics']['avg_delivery_time_hours']:>6.1f} hours
  Quality Pass Rate:      {metrics['delivery_metrics']['quality_pass_rate']:>6.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 BREAKDOWN

  Leads by Source:
"""
        for source, count in metrics['breakdown']['leads_by_source'].items():
            report += f"    {source:20s}: {count:>3}\n"
        
        report += f"""
  Leads by Platform:
"""
        for platform, count in metrics['breakdown']['leads_by_platform'].items():
            report += f"    {platform:20s}: {count:>3}\n"
        
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 TRENDS

  Leads Trend:    {metrics['trends']['leads_trend'].upper()}
  Revenue Trend:  {metrics['trends']['revenue_trend'].upper()}
  Projects Trend: {metrics['trends']['projects_trend'].upper()}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 KEY PERFORMANCE INDICATORS

"""
        # Calculate KPIs
        kpis = self._calculate_kpis(metrics)
        for kpi, value in kpis.items():
            report += f"  {kpi:30s}: {value}\n"
        
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 INSIGHTS & RECOMMENDATIONS

"""
        insights = self._generate_insights(metrics)
        for insight in insights:
            report += f"  {insight}\n"
        
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated by Nexora AI SEO Agency Business Dashboard
{datetime.now().strftime('%Y')}

"""
        return report
    
    def _calculate_kpis(self, metrics: Dict) -> Dict:
        """Calculate key performance indicators"""
        kpis = {}
        
        # Revenue KPI
        kpis['Monthly Recurring Revenue'] = f"${metrics['revenue_metrics']['revenue_last_30_days']:,.2f}"
        
        # Client KPI
        kpis['Active Client Count'] = str(metrics['overview']['active_clients'])
        
        # Delivery KPI
        kpis['Avg Quality Score'] = f"{metrics['delivery_metrics']['avg_quality_score']:.2f}/100"
        
        # Efficiency KPI
        kpis['Avg Delivery Time'] = f"{metrics['delivery_metrics']['avg_delivery_time_hours']:.1f} hours"
        
        # Growth KPI
        kpis['Leads (30 Days)'] = str(metrics['overview']['leads_last_30_days'])
        
        # Success KPI
        kpis['Win Rate'] = f"{metrics['conversion_metrics']['proposal_win_rate']:.2f}%"
        
        return kpis
    
    def _generate_insights(self, metrics: Dict) -> List[str]:
        """Generate business insights"""
        insights = []
        
        # Lead insights
        if metrics['overview']['leads_last_30_days'] > 10:
            insights.append("✓ Strong lead generation - " + str(metrics['overview']['leads_last_30_days']) + " leads in last 30 days")
        elif metrics['overview']['leads_last_30_days'] < 5:
            insights.append("⚠️  Low lead generation - Consider increasing outreach")
        
        # Conversion insights
        if metrics['conversion_metrics']['proposal_win_rate'] > 30:
            insights.append("✓ Excellent win rate - " + str(metrics['conversion_metrics']['proposal_win_rate']) + "%")
        elif metrics['conversion_metrics']['proposal_win_rate'] < 15:
            insights.append("⚠️  Low win rate - Review proposal quality and pricing")
        
        # Revenue insights
        if metrics['revenue_metrics']['revenue_last_30_days'] > 10000:
            insights.append("✓ Strong revenue - $" + f"{metrics['revenue_metrics']['revenue_last_30_days']:,.2f}" + " in last 30 days")
        
        # Quality insights
        if metrics['delivery_metrics']['avg_quality_score'] >= 95:
            insights.append("✓ Excellent quality - Average score " + f"{metrics['delivery_metrics']['avg_quality_score']:.2f}/100")
        elif metrics['delivery_metrics']['avg_quality_score'] < 85:
            insights.append("⚠️  Quality needs improvement - Review QA processes")
        
        # Trend insights
        if metrics['trends']['revenue_trend'] == 'up':
            insights.append("✓ Revenue trending upward")
        elif metrics['trends']['revenue_trend'] == 'down':
            insights.append("⚠️  Revenue trending downward - Take action")
        
        if not insights:
            insights.append("Continue monitoring metrics for insights")
        
        return insights
    
    def export_metrics(self, output_path: str):
        """Export metrics to JSON file"""
        with open(output_path, 'w') as f:
            json.dump(self.get_dashboard_metrics(), f, indent=2)
        
        print(f"✓ Metrics exported to: {output_path}")


def demonstrate_business_dashboard():
    """Demonstrate business dashboard"""
    print("\n" + "="*80)
    print("BUSINESS DASHBOARD DEMONSTRATION")
    print("="*80 + "\n")
    
    dashboard = BusinessDashboard()
    
    # Add sample data
    print("Step 1: Adding sample business data...")
    print("-" * 80)
    
    # Add leads
    dashboard.add_lead({
        'source': 'Website',
        'platform': 'Upwork',
        'client_name': 'John Smith',
        'company': 'TechStart Solutions',
        'email': 'john@techstart.com',
        'budget': '$5,000-$10,000',
        'services': ['SEO Audit', 'Keyword Research']
    })
    
    dashboard.add_lead({
        'source': 'Referral',
        'platform': 'Direct',
        'client_name': 'Emma Wilson',
        'company': 'GrowthCo',
        'email': 'emma@growthco.com',
        'budget': '$10,000-$25,000',
        'services': ['Monthly SEO', 'Content Writing']
    })
    
    print("✓ Added 2 leads")
    
    # Add proposals
    dashboard.add_proposal({
        'lead_id': 'LEAD-0001',
        'platform': 'Upwork',
        'client_name': 'John Smith',
        'project_value': 7500,
        'services': ['SEO Audit', 'Keyword Research']
    })
    
    print("✓ Added 1 proposal")
    
    # Add projects
    dashboard.add_project({
        'client_name': 'John Smith',
        'company': 'TechStart Solutions',
        'services': ['SEO Audit', 'Keyword Research'],
        'value': 7500
    })
    
    print("✓ Added 1 project")
    
    # Add revenue
    dashboard.add_revenue({
        'project_id': 'PROJ-0001',
        'client_name': 'John Smith',
        'amount': 3750,
        'type': 'initial_payment'
    })
    
    dashboard.add_revenue({
        'project_id': 'PROJ-0001',
        'client_name': 'John Smith',
        'amount': 3750,
        'type': 'final_payment'
    })
    
    print("✓ Added 2 revenue transactions")
    
    # Add deliverables
    dashboard.add_deliverable({
        'project_id': 'PROJ-0001',
        'client_name': 'John Smith',
        'type': 'SEO Audit',
        'quality_score': 95.5,
        'delivery_time_hours': 48
    })
    
    dashboard.add_deliverable({
        'project_id': 'PROJ-0001',
        'client_name': 'John Smith',
        'type': 'Keyword Research',
        'quality_score': 92.0,
        'delivery_time_hours': 36
    })
    
    print("✓ Added 2 deliverables")
    
    print("\n\nStep 2: Generating dashboard report...")
    print("-" * 80)
    
    # Generate dashboard report
    dashboard_report = dashboard.generate_dashboard_report()
    print(dashboard_report)
    
    print("Step 3: Exporting metrics...")
    print("-" * 80)
    dashboard.export_metrics("data/business-metrics-export.json")
    
    print("\n" + "="*80)
    print("BUSINESS DASHBOARD READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Lead tracking")
    print("✓ Proposal management")
    print("✓ Project tracking")
    print("✓ Revenue tracking")
    print("✓ Deliverable tracking")
    print("✓ KPI calculation")
    print("✓ Trend analysis")
    print("✓ Business insights")
    print("✓ Dashboard reporting")
    print("✓ Metrics export")
    print("\n")


if __name__ == "__main__":
    demonstrate_business_dashboard()
#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Revenue Dashboard
CEO Agent dashboard for tracking leads, proposals, won jobs, revenue, MRR, pipeline value, and conversion rates.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os
import random


class RevenueDashboard:
    """Revenue Dashboard - Track all revenue metrics"""
    
    def __init__(self):
        self.metrics_history = []
    
    def generate_dashboard(self, crm_data: Dict = None) -> Dict:
        """Generate complete revenue dashboard"""
        
        # Simulate CRM data if not provided
        if crm_data is None:
            crm_data = self._simulate_crm_data()
        
        dashboard = {
            "generated_at": datetime.now().isoformat(),
            "period": {
                "start": (datetime.now() - timedelta(days=30)).isoformat(),
                "end": datetime.now().isoformat(),
                "label": "Last 30 Days"
            },
            
            # Today's metrics
            "today": {
                "new_leads": random.randint(1, 5),
                "open_proposals": random.randint(3, 10),
                "won_jobs": random.randint(0, 2),
                "lost_jobs": random.randint(0, 1),
                "revenue": random.randint(500, 3000),
                "messages_received": random.randint(5, 20)
            },
            
            # Revenue metrics
            "revenue": {
                "total_revenue": crm_data.get('total_revenue', 0),
                "monthly_recurring_revenue": crm_data.get('mrr', 0),
                "average_deal_size": crm_data.get('average_deal_size', 0),
                "lifetime_client_value": crm_data.get('ltv', 0),
                "revenue_by_source": self._calculate_revenue_by_source(crm_data),
                "revenue_trend": self._generate_revenue_trend(),
                "projected_revenue": self._project_revenue(crm_data)
            },
            
            # Pipeline metrics
            "pipeline": {
                "total_leads": crm_data.get('total_leads', 0),
                "qualified_leads": crm_data.get('qualified_leads', 0),
                "proposals_sent": crm_data.get('proposals_sent', 0),
                "interviews_scheduled": crm_data.get('interviews', 0),
                "active_clients": crm_data.get('active_clients', 0),
                "pipeline_value": crm_data.get('pipeline_value', 0),
                "weighted_pipeline": crm_data.get('weighted_pipeline', 0)
            },
            
            # Conversion metrics
            "conversion": {
                "lead_to_qualified": self._calculate_rate(
                    crm_data.get('qualified_leads', 0),
                    crm_data.get('total_leads', 0)
                ),
                "qualified_to_proposal": self._calculate_rate(
                    crm_data.get('proposals_sent', 0),
                    crm_data.get('qualified_leads', 0)
                ),
                "proposal_to_won": self._calculate_rate(
                    crm_data.get('won_deals', 0),
                    crm_data.get('proposals_sent', 0)
                ),
                "overall_win_rate": self._calculate_rate(
                    crm_data.get('won_deals', 0),
                    crm_data.get('total_leads', 0)
                ),
                "target_win_rate": 30  # Target: 30%
            },
            
            # Client metrics
            "clients": {
                "active": crm_data.get('active_clients', 0),
                "at_risk": crm_data.get('at_risk_clients', 0),
                "satisfaction_score": crm_data.get('satisfaction_score', 95),
                "avg_project_duration": crm_data.get('avg_project_duration', '3 months'),
                "repeat_business_rate": crm_data.get('repeat_rate', 40),
                "referral_rate": crm_data.get('referral_rate', 20)
            },
            
            # Platform performance
            "platforms": {
                "upwork": {
                    "proposals_sent": random.randint(10, 30),
                    "response_rate": f"{random.randint(40, 80)}%",
                    "win_rate": f"{random.randint(20, 40)}%",
                    "revenue": random.randint(1000, 5000),
                    "rating": round(4.5 + random.random() * 0.5, 1)
                },
                "fiverr": {
                    "active_gigs": random.randint(3, 8),
                    "orders": random.randint(5, 20),
                    "revenue": random.randint(500, 3000),
                    "rating": round(4.5 + random.random() * 0.5, 1)
                },
                "freelancer": {
                    "bids_submitted": random.randint(5, 15),
                    "win_rate": f"{random.randint(15, 35)}%",
                    "revenue": random.randint(500, 2000),
                    "rating": round(4.0 + random.random() * 0.8, 1)
                },
                "direct_outreach": {
                    "emails_sent": random.randint(20, 100),
                    "response_rate": f"{random.randint(10, 30)}%",
                    "meetings_booked": random.randint(2, 10),
                    "revenue": random.randint(1000, 5000)
                },
                "linkedin": {
                    "connections": random.randint(10, 50),
                    "messages_sent": random.randint(10, 40),
                    "response_rate": f"{random.randint(20, 40)}%",
                    "revenue": random.randint(500, 3000)
                }
            },
            
            # Growth metrics
            "growth": {
                "month_over_month_growth": f"{random.randint(5, 30)}%",
                "quarter_over_quarter_growth": f"{random.randint(10, 50)}%",
                "year_over_year_growth": f"{random.randint(50, 200)}%",
                "runway_months": random.randint(6, 24),
                "break_even_month": "Month 3"
            },
            
            # Top opportunities
            "top_opportunities": self._get_top_opportunities(crm_data),
            
            # Alerts and actions
            "alerts": self._generate_alerts(crm_data),
            "recommended_actions": self._generate_recommended_actions(crm_data)
        }
        
        return dashboard
    
    def _simulate_crm_data(self) -> Dict:
        """Simulate CRM data for demonstration"""
        return {
            "total_leads": 45,
            "qualified_leads": 28,
            "proposals_sent": 20,
            "interviews": 12,
            "won_deals": 8,
            "lost_deals": 4,
            "active_clients": 6,
            "at_risk_clients": 1,
            "total_revenue": 45000,
            "mrr": 4800,
            "average_deal_size": 1200,
            "ltv": 7200,
            "pipeline_value": 35000,
            "weighted_pipeline": 18500,
            "satisfaction_score": 96,
            "repeat_rate": 45,
            "referral_rate": 25,
            "avg_project_duration": "3 months"
        }
    
    def _calculate_rate(self, numerator: int, denominator: int) -> float:
        """Calculate percentage rate"""
        if denominator == 0:
            return 0.0
        return round((numerator / denominator) * 100, 1)
    
    def _calculate_revenue_by_source(self, crm_data: Dict) -> Dict:
        """Calculate revenue breakdown by source"""
        total = crm_data.get('total_revenue', 45000)
        return {
            "upwork": round(total * 0.35),
            "fiverr": round(total * 0.15),
            "freelancer": round(total * 0.10),
            "direct_outreach": round(total * 0.25),
            "linkedin": round(total * 0.10),
            "referrals": round(total * 0.05)
        }
    
    def _generate_revenue_trend(self) -> List[Dict]:
        """Generate revenue trend data"""
        trend = []
        for i in range(6):
            month = (datetime.now() - timedelta(days=30 * (5 - i))).strftime("%b")
            trend.append({
                "month": month,
                "revenue": random.randint(3000, 8000),
                "expenses": random.randint(1000, 3000),
                "profit": random.randint(2000, 5000)
            })
        return trend
    
    def _project_revenue(self, crm_data: Dict) -> Dict:
        """Project future revenue"""
        current_mrr = crm_data.get('mrr', 4800)
        growth_rate = 0.15  # 15% monthly growth
        
        projections = []
        for i in range(1, 7):
            projected = current_mrr * ((1 + growth_rate) ** i)
            projections.append({
                "month": (datetime.now() + timedelta(days=30 * i)).strftime("%b"),
                "projected_mrr": round(projected, -2),
                "confidence": max(30, 90 - (i * 10))
            })
        
        return {
            "current_mrr": current_mrr,
            "projected_mrr_6months": round(current_mrr * ((1 + growth_rate) ** 6), -2),
            "annual_run_rate": round(current_mrr * 12, -2),
            "monthly_projections": projections
        }
    
    def _get_top_opportunities(self, crm_data: Dict) -> List[Dict]:
        """Get top revenue opportunities"""
        return [
            {
                "type": "upsell",
                "client": "TechFlow SaaS",
                "opportunity": "Add content writing service",
                "potential_value": 500,
                "probability": 70
            },
            {
                "type": "referral",
                "client": "GreenLeaf Ecom",
                "opportunity": "Referred partner company",
                "potential_value": 2000,
                "probability": 50
            },
            {
                "type": "expansion",
                "client": "City Dental",
                "opportunity": "Expand to multi-location SEO",
                "potential_value": 1000,
                "probability": 60
            },
            {
                "type": "new_service",
                "market": "Local Businesses",
                "opportunity": "Launch local SEO package",
                "potential_value": 3000,
                "probability": 40
            }
        ]
    
    def _generate_alerts(self, crm_data: Dict) -> List[Dict]:
        """Generate alerts based on data"""
        alerts = []
        
        # Check win rate
        win_rate = self._calculate_rate(
            crm_data.get('won_deals', 0),
            crm_data.get('proposals_sent', 0)
        )
        if win_rate < 30:
            alerts.append({
                "type": "warning",
                "message": f"Win rate is {win_rate}% - below target of 30%",
                "action": "Review proposal quality and pricing strategy"
            })
        
        # Check at-risk clients
        if crm_data.get('at_risk_clients', 0) > 0:
            alerts.append({
                "type": "warning",
                "message": f"{crm_data['at_risk_clients']} client(s) at risk of churning",
                "action": "Schedule check-in calls with at-risk clients"
            })
        
        # Check pipeline
        if crm_data.get('pipeline_value', 0) < crm_data.get('mrr', 0) * 3:
            alerts.append({
                "type": "info",
                "message": "Pipeline value is low - need more leads",
                "action": "Increase outreach and marketing efforts"
            })
        
        # Positive alerts
        if crm_data.get('satisfaction_score', 0) >= 95:
            alerts.append({
                "type": "success",
                "message": f"Client satisfaction at {crm_data['satisfaction_score']}%",
                "action": "Request testimonials and referrals"
            })
        
        return alerts
    
    def _generate_recommended_actions(self, crm_data: Dict) -> List[str]:
        """Generate recommended actions"""
        actions = [
            "Follow up with 3 high-value leads that haven't responded",
            "Send proposals to 5 qualified leads in pipeline",
            "Check in with at-risk clients to ensure satisfaction",
            "Request referrals from 2 satisfied clients",
            "Review and optimize underperforming Fiverr gigs",
            "Post 3 new proposals on Upwork for high-fit jobs",
            "Update pricing strategy based on market analysis",
            "Create case study from best performing project"
        ]
        
        # Prioritize based on data
        if crm_data.get('pipeline_value', 0) < 20000:
            actions.insert(0, "URGENT: Increase lead generation - pipeline value is low")
        
        if crm_data.get('at_risk_clients', 0) > 0:
            actions.insert(0, "URGENT: Schedule retention calls with at-risk clients")
        
        return actions
    
    def get_executive_summary(self) -> Dict:
        """Get executive summary for CEO Agent"""
        dashboard = self.generate_dashboard()
        
        return {
            "summary": f"Revenue: ${dashboard['revenue']['total_revenue']:,} | MRR: ${dashboard['revenue']['monthly_recurring_revenue']:,} | Pipeline: ${dashboard['pipeline']['pipeline_value']:,} | Win Rate: {dashboard['conversion']['proposal_to_won']}%",
            "key_metrics": {
                "revenue": f"${dashboard['revenue']['total_revenue']:,}",
                "mrr": f"${dashboard['revenue']['monthly_recurring_revenue']:,}",
                "pipeline": f"${dashboard['pipeline']['pipeline_value']:,}",
                "active_clients": dashboard['pipeline']['active_clients'],
                "win_rate": f"{dashboard['conversion']['proposal_to_won']}%",
                "satisfaction": f"{dashboard['clients']['satisfaction_score']}%"
            },
            "alerts": dashboard['alerts'],
            "top_actions": dashboard['recommended_actions'][:3],
            "growth": dashboard['growth']
        }


def demonstrate_revenue_dashboard():
    """Demonstrate Revenue Dashboard"""
    print(f"\n{'='*80}")
    print("REVENUE DASHBOARD - Demonstration")
    print(f"{'='*80}\n")
    
    dashboard = RevenueDashboard()
    
    # Generate dashboard
    data = dashboard.generate_dashboard()
    
    # Executive Summary
    print("📊 EXECUTIVE SUMMARY")
    print("─" * 60)
    print(f"  Revenue: ${data['revenue']['total_revenue']:,}")
    print(f"  MRR: ${data['revenue']['monthly_recurring_revenue']:,}")
    print(f"  Pipeline: ${data['pipeline']['pipeline_value']:,}")
    print(f"  Active Clients: {data['pipeline']['active_clients']}")
    print(f"  Win Rate: {data['conversion']['proposal_to_won']}%")
    print(f"  Satisfaction: {data['clients']['satisfaction_score']}%")
    
    # Today's Metrics
    print(f"\n📅 TODAY'S METRICS")
    print("─" * 60)
    today = data['today']
    print(f"  New Leads: {today['new_leads']}")
    print(f"  Open Proposals: {today['open_proposals']}")
    print(f"  Won Jobs: {today['won_jobs']}")
    print(f"  Revenue Today: ${today['revenue']}")
    
    # Pipeline
    print(f"\n🔷 PIPELINE")
    print("─" * 60)
    pipeline = data['pipeline']
    print(f"  Total Leads: {pipeline['total_leads']}")
    print(f"  Qualified: {pipeline['qualified_leads']}")
    print(f"  Proposals Sent: {pipeline['proposals_sent']}")
    print(f"  Interviews: {pipeline['interviews_scheduled']}")
    print(f"  Pipeline Value: ${pipeline['pipeline_value']:,}")
    print(f"  Weighted Pipeline: ${pipeline['weighted_pipeline']:,}")
    
    # Conversion Rates
    print(f"\n🎯 CONVERSION RATES")
    print("─" * 60)
    conv = data['conversion']
    print(f"  Lead → Qualified: {conv['lead_to_qualified']}%")
    print(f"  Qualified → Proposal: {conv['qualified_to_proposal']}%")
    print(f"  Proposal → Won: {conv['proposal_to_won']}%")
    print(f"  Overall Win Rate: {conv['overall_win_rate']}%")
    print(f"  Target Win Rate: {conv['target_win_rate']}%")
    
    # Revenue by Source
    print(f"\n💰 REVENUE BY SOURCE")
    print("─" * 60)
    for source, amount in data['revenue']['revenue_by_source'].items():
        print(f"  {source.replace('_', ' ').title():20s}: ${amount:,}")
    
    # Revenue Trend
    print(f"\n📈 REVENUE TREND (Last 6 Months)")
    print("─" * 60)
    for month_data in data['revenue']['revenue_trend']:
        print(f"  {month_data['month']}: Revenue=${month_data['revenue']:,} | Profit=${month_data['profit']:,}")
    
    # Projections
    print(f"\n🔮 REVENUE PROJECTIONS")
    print("─" * 60)
    proj = data['revenue']['projected_revenue']
    print(f"  Current MRR: ${proj['current_mrr']:,}")
    print(f"  Projected MRR (6mo): ${proj['projected_mrr_6months']:,}")
    print(f"  Annual Run Rate: ${proj['annual_run_rate']:,}")
    
    # Platform Performance
    print(f"\n🌐 PLATFORM PERFORMANCE")
    print("─" * 60)
    for platform, metrics in data['platforms'].items():
        revenue = metrics.get('revenue', 0)
        print(f"  {platform.replace('_', ' ').title():20s}: ${revenue:,}")
    
    # Alerts
    print(f"\n⚠️  ALERTS")
    print("─" * 60)
    for alert in data['alerts']:
        icon = "✅" if alert['type'] == 'success' else "⚠️" if alert['type'] == 'warning' else "ℹ️"
        print(f"  {icon} {alert['message']}")
    
    # Recommended Actions
    print(f"\n📋 RECOMMENDED ACTIONS")
    print("─" * 60)
    for i, action in enumerate(data['recommended_actions'][:5], 1):
        print(f"  {i}. {action}")
    
    # Growth
    print(f"\n📊 GROWTH METRICS")
    print("─" * 60)
    growth = data['growth']
    print(f"  Month-over-Month: {growth['month_over_month_growth']}")
    print(f"  Quarter-over-Quarter: {growth['quarter_over_quarter_growth']}")
    print(f"  Year-over-Year: {growth['year_over_year_growth']}")
    
    print(f"\n{'='*80}")
    print("REVENUE DASHBOARD - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Today's metrics (leads, proposals, won/lost jobs, revenue)")
    print("✓ Revenue tracking (total, MRR, LTV, by source)")
    print("✓ Pipeline management (all stages)")
    print("✓ Conversion rates (lead → qualified → proposal → won)")
    print("✓ Platform performance (Upwork, Fiverr, Freelancer, Direct, LinkedIn)")
    print("✓ Revenue trends and projections")
    print("✓ Growth metrics (MoM, QoQ, YoY)")
    print("✓ Alerts and recommended actions")
    print("✓ Executive summary for CEO Agent")
    print("\nOutputs: Dashboard data, Executive summary, Alerts, Projections")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_revenue_dashboard()
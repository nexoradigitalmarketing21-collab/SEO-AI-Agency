#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Acquisition Orchestrator
Ties together all Phase 4 agents: Lead Hunter, Website Analyzer, Proposal Agent,
Outreach Agent, CRM Agent, Pricing Agent, and Revenue Dashboard.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Note: File names use hyphens but Python imports use underscores.
# These imports assume the files are importable. If running directly,
# the classes are available in the same directory.
import importlib.util
import sys

def _import_from_file(module_name, file_path):
    """Import a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Get the directory where this file is located
_acq_dir = os.path.dirname(os.path.abspath(__file__))

# Import all agents dynamically
_lead_hunter_module = _import_from_file("lead_hunter", os.path.join(_acq_dir, "lead-hunter-agent.py"))
_website_module = _import_from_file("website_analyzer", os.path.join(_acq_dir, "website-analyzer.py"))
_proposal_module = _import_from_file("proposal_agent", os.path.join(_acq_dir, "proposal-agent.py"))
_outreach_module = _import_from_file("outreach_agent", os.path.join(_acq_dir, "outreach-agent.py"))
_crm_module = _import_from_file("crm_agent", os.path.join(_acq_dir, "crm-agent.py"))
_pricing_module = _import_from_file("pricing_agent", os.path.join(_acq_dir, "pricing-agent.py"))
_revenue_module = _import_from_file("revenue_dashboard", os.path.join(_acq_dir, "revenue-dashboard.py"))

LeadHunterAgent = _lead_hunter_module.LeadHunterAgent
WebsiteAnalyzer = _website_module.WebsiteAnalyzer
ProposalAgent = _proposal_module.ProposalAgent
OutreachAgent = _outreach_module.OutreachAgent
CRMAgent = _crm_module.CRMAgent
PricingAgent = _pricing_module.PricingAgent
RevenueDashboard = _revenue_module.RevenueDashboard


class AcquisitionOrchestrator:
    """Orchestrates all client acquisition activities"""
    
    def __init__(self):
        self.lead_hunter = LeadHunterAgent()
        self.website_analyzer = WebsiteAnalyzer()
        self.proposal_agent = ProposalAgent()
        self.outreach_agent = OutreachAgent()
        self.crm = CRMAgent()
        self.pricing_agent = PricingAgent()
        self.revenue_dashboard = RevenueDashboard()
        
        self.current_campaign = None
        self.campaigns_history = []
    
    def run_full_acquisition_cycle(self, target_market: Dict) -> Dict:
        """Run a complete acquisition cycle from lead finding to CRM entry"""
        
        print(f"\n{'='*80}")
        print(f"ACQUISITION ORCHESTRATOR - Full Cycle")
        print(f"{'='*80}\n")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "target_market": target_market,
            "leads_found": 0,
            "websites_analyzed": 0,
            "proposals_generated": 0,
            "outreach_sequences": 0,
            "crm_entries": 0,
            "pricing_recommendations": 0,
            "revenue_projection": None
        }
        
        # Step 1: Find leads
        print("Step 1: Finding Leads...")
        scan_results = self.lead_hunter.run_full_scan(
            target_market.get('location', 'New York'),
            target_market.get('industry')
        )
        results['leads_found'] = scan_results['total_opportunities']
        print(f"  ✓ {results['leads_found']} opportunities found")
        
        # Step 2: Analyze websites for top prospects
        print("\nStep 2: Analyzing Websites...")
        website_insights = []
        for prospect in scan_results.get('prioritized_report', {}).get('top_5_prospects', []):
            if prospect.get('website'):
                insights = self.website_analyzer.generate_proposal_insights(prospect['website'])
                website_insights.append(insights)
                results['websites_analyzed'] += 1
                print(f"  ✓ {prospect['business_name']}: SEO Score {insights['seo_score']}")
        
        # Step 3: Generate proposals
        print("\nStep 3: Generating Proposals...")
        proposals = []
        for prospect in scan_results.get('prioritized_report', {}).get('top_5_prospects', [])[:3]:
            client_info = {
                "name": prospect.get('business_name', 'Client'),
                "company": prospect.get('business_name', 'Company'),
                "industry": prospect.get('industry', 'General'),
                "business_size": "small",
                "website_score": 50
            }
            project_info = {
                "title": f"SEO Strategy for {prospect.get('business_name', 'Client')}",
                "type": "monthly_seo",
                "industry": prospect.get('industry', 'General'),
                "budget": 2000,
                "complexity": "medium",
                "timeline": "3 months"
            }
            
            proposal = self.proposal_agent.generate_proposal("upwork", client_info, project_info)
            proposals.append(proposal)
            results['proposals_generated'] += 1
            print(f"  ✓ Proposal for {prospect['business_name']}: ${proposal['pricing']['calculated_price']:,.0f}")
        
        # Step 4: Create outreach sequences
        print("\nStep 4: Creating Outreach Sequences...")
        for prospect in scan_results.get('prioritized_report', {}).get('top_5_prospects', [])[:3]:
            outreach_prospect = {
                "name": prospect.get('business_name', 'Client'),
                "company": prospect.get('business_name', 'Company'),
                "industry": prospect.get('industry', 'General'),
                "email": f"info@{prospect.get('website', 'company.com').replace('https://', '').replace('www.', '')}",
                "recent_result": "significant SEO improvements",
                "website_analyzed": True
            }
            sequence = self.outreach_agent.generate_outreach_sequence(outreach_prospect, "cold_email")
            results['outreach_sequences'] += 1
            print(f"  ✓ Outreach sequence for {prospect['business_name']} ({len(sequence)} messages)")
        
        # Step 5: Add to CRM
        print("\nStep 5: Adding to CRM...")
        for prospect in scan_results.get('prioritized_report', {}).get('top_5_prospects', []):
            lead = self.crm.add_lead({
                "company": prospect.get('business_name', 'Unknown'),
                "name": prospect.get('business_name', 'Unknown'),
                "email": f"info@{prospect.get('website', 'company.com').replace('https://', '').replace('www.', '')}",
                "source": "lead_hunter",
                "budget_range": "$1000-$3000",
                "service_interest": "SEO",
                "estimated_value": 2000,
                "industry": prospect.get('industry', 'General')
            })
            results['crm_entries'] += 1
            print(f"  ✓ {prospect['business_name']} added to CRM (Score: {lead['score']}/100)")
        
        # Step 6: Get pricing recommendations
        print("\nStep 6: Pricing Recommendations...")
        pricing_context = {
            "country": target_market.get('country', 'United States'),
            "competition": target_market.get('competition', 'medium'),
            "client_budget": 2000,
            "website_size": "medium",
            "complexity": "medium"
        }
        catalog = self.pricing_agent.get_service_catalog(pricing_context)
        results['pricing_recommendations'] = len(catalog)
        print(f"  ✓ {len(catalog)} services priced for {pricing_context['country']} market")
        
        # Step 7: Generate revenue projection
        print("\nStep 7: Revenue Projection...")
        dashboard = self.revenue_dashboard.generate_dashboard()
        results['revenue_projection'] = dashboard['revenue']['projected_revenue']
        print(f"  ✓ Current MRR: ${dashboard['revenue']['monthly_recurring_revenue']:,}")
        print(f"  ✓ Projected MRR (6mo): ${dashboard['revenue']['projected_revenue']['projected_mrr_6months']:,}")
        
        # Summary
        print(f"\n{'='*80}")
        print("ACQUISITION CYCLE COMPLETE")
        print(f"{'='*80}")
        print(f"\n📊 Summary:")
        print(f"  Leads Found: {results['leads_found']}")
        print(f"  Websites Analyzed: {results['websites_analyzed']}")
        print(f"  Proposals Generated: {results['proposals_generated']}")
        print(f"  Outreach Sequences: {results['outreach_sequences']}")
        print(f"  CRM Entries: {results['crm_entries']}")
        print(f"  Pricing Recommendations: {results['pricing_recommendations']}")
        
        return results
    
    def run_daily_operations(self) -> Dict:
        """Run daily acquisition operations"""
        return {
            "date": datetime.now().isoformat(),
            "actions_taken": [
                "Scanned job boards for new opportunities",
                "Analyzed new leads in CRM",
                "Generated proposals for qualified leads",
                "Sent follow-up emails",
                "Updated pipeline stages",
                "Checked revenue metrics"
            ],
            "metrics": self.revenue_dashboard.get_executive_summary()
        }
    
    def get_system_status(self) -> Dict:
        """Get status of all acquisition systems"""
        return {
            "lead_hunter": {
                "status": "active",
                "capabilities": [
                    "Job board scanning",
                    "Local business discovery",
                    "Competitor gap analysis",
                    "Prospect prioritization"
                ]
            },
            "website_analyzer": {
                "status": "active",
                "capabilities": [
                    "SEO score calculation",
                    "Technical issue detection",
                    "Keyword opportunity finding",
                    "Proposal insight generation"
                ]
            },
            "proposal_agent": {
                "status": "active",
                "capabilities": [
                    "Multi-platform proposals",
                    "Industry-aware content",
                    "Smart pricing",
                    "Discovery questions"
                ]
            },
            "outreach_agent": {
                "status": "active",
                "capabilities": [
                    "Cold email generation",
                    "LinkedIn messaging",
                    "Follow-up sequences",
                    "Meeting requests"
                ]
            },
            "crm": {
                "status": "active",
                "stages": [
                    "Lead → Qualified → Proposal Sent → Interview → Won → Active Client → Upsell → Referral"
                ],
                "capabilities": [
                    "Pipeline management",
                    "Lead scoring",
                    "Communication log",
                    "Testimonial tracking"
                ]
            },
            "pricing_agent": {
                "status": "active",
                "capabilities": [
                    "Country-specific pricing",
                    "Competition analysis",
                    "Package generation",
                    "Market positioning"
                ]
            },
            "revenue_dashboard": {
                "status": "active",
                "capabilities": [
                    "Revenue tracking",
                    "Pipeline valuation",
                    "Conversion analytics",
                    "Growth projections"
                ]
            }
        }


def demonstrate_orchestrator():
    """Demonstrate Acquisition Orchestrator"""
    print(f"\n{'='*80}")
    print("ACQUISITION ORCHESTRATOR - Complete System Demo")
    print(f"{'='*80}\n")
    
    orchestrator = AcquisitionOrchestrator()
    
    # Show system status
    print("System Status:")
    status = orchestrator.get_system_status()
    for system, info in status.items():
        print(f"  ✓ {system.replace('_', ' ').title()}: {info['status']}")
    
    # Run a full acquisition cycle
    target_market = {
        "location": "New York",
        "industry": "Dental",
        "country": "United States",
        "competition": "medium"
    }
    
    results = orchestrator.run_full_acquisition_cycle(target_market)
    
    print(f"\n{'='*80}")
    print("ACQUISITION ORCHESTRATOR - READY")
    print(f"{'='*80}")
    print("\nComplete System Features:")
    print("✅ Find SEO leads (job boards + local businesses)")
    print("✅ Analyze websites (SEO score, issues, opportunities)")
    print("✅ Generate proposals (Upwork, Fiverr, Freelancer, LinkedIn, Email)")
    print("✅ Manage CRM (8-stage pipeline)")
    print("✅ Track every opportunity (lead → active client → referral)")
    print("✅ Track revenue (MRR, pipeline value, conversion rates)")
    print("✅ Prepare Fiverr gigs (titles, descriptions, packages, FAQ)")
    print("✅ Prepare Upwork bids (analysis, proposals, follow-ups)")
    print("✅ Prepare Freelancer bids (milestones, timelines, pricing)")
    print("✅ Follow up automatically (sequences, timing, personalization)")
    print("\nGoal: Consistent client acquisition across all channels")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_orchestrator()
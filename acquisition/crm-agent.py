#!/usr/bin/env python3
"""
Nexora AI SEO Agency - CRM Agent
Complete pipeline management: Lead → Qualified → Proposal Sent → Interview → Won → Active Client → Upsell → Referral
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os
import uuid


class CRMAgent:
    """CRM Agent - Manage complete client pipeline"""
    
    PIPELINE_STAGES = [
        "lead",
        "qualified",
        "proposal_sent",
        "interview",
        "won",
        "active_client",
        "upsell",
        "referral"
    ]
    
    def __init__(self):
        self.leads = []
        self.clients = []
        self.messages = []
        self.projects = []
        self.testimonials = []
        self.referrals = []
    
    def add_lead(self, lead_info: Dict) -> Dict:
        """Add a new lead to the pipeline"""
        lead = {
            "id": str(uuid.uuid4())[:8],
            "company": lead_info.get('company', 'Unknown'),
            "contact_name": lead_info.get('name', 'Unknown'),
            "email": lead_info.get('email', ''),
            "phone": lead_info.get('phone', ''),
            "website": lead_info.get('website', ''),
            "industry": lead_info.get('industry', 'Unknown'),
            "source": lead_info.get('source', 'direct'),
            "budget_range": lead_info.get('budget_range', 'Not specified'),
            "service_interest": lead_info.get('service_interest', 'SEO'),
            "notes": lead_info.get('notes', ''),
            "stage": "lead",
            "score": self._calculate_lead_score(lead_info),
            "created_at": datetime.now().isoformat(),
            "last_contacted": None,
            "next_follow_up": (datetime.now() + timedelta(days=1)).isoformat(),
            "probability": 20,
            "estimated_value": lead_info.get('estimated_value', 0),
            "tags": lead_info.get('tags', []),
            "activities": []
        }
        
        self.leads.append(lead)
        return lead
    
    def _calculate_lead_score(self, lead_info: Dict) -> int:
        """Calculate lead quality score"""
        score = 0
        
        # Contact info completeness
        if lead_info.get('name'): score += 10
        if lead_info.get('email'): score += 10
        if lead_info.get('phone'): score += 10
        if lead_info.get('website'): score += 10
        
        # Budget indicator
        budget = lead_info.get('budget_range', '')
        if '5000' in budget or '10000' in budget:
            score += 20
        elif '2000' in budget:
            score += 15
        elif '1000' in budget:
            score += 10
        
        # Source quality
        source = lead_info.get('source', '')
        if source in ['referral', 'direct']:
            score += 15
        elif source in ['upwork', 'fiverr']:
            score += 10
        
        # Service interest
        if lead_info.get('service_interest'):
            score += 10
        
        return min(100, score)
    
    def qualify_lead(self, lead_id: str, qualification_info: Dict) -> Dict:
        """Qualify a lead - move to qualified stage"""
        lead = self._find_lead(lead_id)
        if not lead:
            return {"error": "Lead not found"}
        
        lead['stage'] = "qualified"
        lead['score'] = min(100, lead['score'] + 10)
        lead['probability'] = 30
        lead['qualification_notes'] = qualification_info.get('notes', '')
        lead['budget_confirmed'] = qualification_info.get('budget_confirmed', False)
        lead['timeline'] = qualification_info.get('timeline', 'Not specified')
        lead['decision_maker'] = qualification_info.get('decision_maker', lead['contact_name'])
        lead['activities'].append({
            "type": "qualified",
            "timestamp": datetime.now().isoformat(),
            "details": "Lead qualified"
        })
        
        return lead
    
    def send_proposal(self, lead_id: str, proposal_info: Dict) -> Dict:
        """Mark proposal as sent"""
        lead = self._find_lead(lead_id)
        if not lead:
            return {"error": "Lead not found"}
        
        lead['stage'] = "proposal_sent"
        lead['probability'] = 50
        lead['proposal_amount'] = proposal_info.get('amount', 0)
        lead['proposal_sent_at'] = datetime.now().isoformat()
        lead['proposal_type'] = proposal_info.get('type', 'standard')
        lead['proposal_content'] = proposal_info.get('content', '')
        lead['activities'].append({
            "type": "proposal_sent",
            "timestamp": datetime.now().isoformat(),
            "details": f"Proposal sent - ${proposal_info.get('amount', 0):,.0f}"
        })
        
        return lead
    
    def schedule_interview(self, lead_id: str, interview_info: Dict) -> Dict:
        """Schedule interview/call with lead"""
        lead = self._find_lead(lead_id)
        if not lead:
            return {"error": "Lead not found"}
        
        lead['stage'] = "interview"
        lead['probability'] = 60
        lead['interview_date'] = interview_info.get('scheduled_at', datetime.now().isoformat())
        lead['interview_type'] = interview_info.get('type', 'video_call')
        lead['interview_notes'] = interview_info.get('notes', '')
        lead['activities'].append({
            "type": "interview_scheduled",
            "timestamp": datetime.now().isoformat(),
            "details": f"Interview scheduled: {interview_info.get('type', 'call')}"
        })
        
        return lead
    
    def win_deal(self, lead_id: str, deal_info: Dict) -> Dict:
        """Move lead to won stage"""
        lead = self._find_lead(lead_id)
        if not lead:
            return {"error": "Lead not found"}
        
        lead['stage'] = "won"
        lead['probability'] = 100
        lead['won_at'] = datetime.now().isoformat()
        lead['deal_value'] = deal_info.get('amount', lead.get('proposal_amount', 0))
        lead['contract_type'] = deal_info.get('contract_type', 'project')
        lead['start_date'] = deal_info.get('start_date', datetime.now().isoformat())
        lead['activities'].append({
            "type": "deal_won",
            "timestamp": datetime.now().isoformat(),
            "details": f"Deal won - ${deal_info.get('amount', 0):,.0f}"
        })
        
        # Move to clients list
        client = self._convert_to_client(lead, deal_info)
        self.clients.append(client)
        
        return {"lead": lead, "client": client}
    
    def _convert_to_client(self, lead: Dict, deal_info: Dict) -> Dict:
        """Convert won lead to client"""
        return {
            "id": str(uuid.uuid4())[:8],
            "lead_id": lead['id'],
            "company": lead['company'],
            "contact_name": lead['contact_name'],
            "email": lead['email'],
            "phone": lead.get('phone', ''),
            "website": lead.get('website', ''),
            "industry": lead['industry'],
            "deal_value": deal_info.get('amount', 0),
            "contract_type": deal_info.get('contract_type', 'project'),
            "start_date": deal_info.get('start_date', datetime.now().isoformat()),
            "status": "active",
            "projects": [],
            "total_revenue": 0,
            "lifetime_value": 0,
            "created_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "satisfaction_score": None,
            "testimonials": [],
            "referrals": []
        }
    
    def start_project(self, client_id: str, project_info: Dict) -> Dict:
        """Start a new project for an active client"""
        client = self._find_client(client_id)
        if not client:
            return {"error": "Client not found"}
        
        project = {
            "id": str(uuid.uuid4())[:8],
            "client_id": client_id,
            "name": project_info.get('name', 'SEO Project'),
            "type": project_info.get('type', 'SEO'),
            "status": "active",
            "start_date": datetime.now().isoformat(),
            "deadline": project_info.get('deadline', ''),
            "budget": project_info.get('budget', 0),
            "progress": 0,
            "deliverables": project_info.get('deliverables', []),
            "completed_deliverables": [],
            "notes": project_info.get('notes', ''),
            "messages": []
        }
        
        client['projects'].append(project)
        client['status'] = "active_client"
        client['last_activity'] = datetime.now().isoformat()
        
        # Update lead stage
        lead = self._find_lead(client['lead_id'])
        if lead:
            lead['stage'] = "active_client"
        
        self.projects.append(project)
        return project
    
    def add_message(self, client_id: str, message: Dict) -> Dict:
        """Add a message to client communication log"""
        msg = {
            "id": str(uuid.uuid4())[:8],
            "client_id": client_id,
            "direction": message.get('direction', 'outgoing'),
            "type": message.get('type', 'email'),
            "subject": message.get('subject', ''),
            "content": message.get('content', ''),
            "timestamp": datetime.now().isoformat(),
            "read": message.get('direction', 'outgoing') == 'outgoing',
            "attachments": message.get('attachments', [])
        }
        
        self.messages.append(msg)
        
        # Update client last activity
        client = self._find_client(client_id)
        if client:
            client['last_activity'] = datetime.now().isoformat()
        
        return msg
    
    def add_testimonial(self, client_id: str, testimonial: Dict) -> Dict:
        """Add client testimonial"""
        t = {
            "id": str(uuid.uuid4())[:8],
            "client_id": client_id,
            "content": testimonial.get('content', ''),
            "rating": testimonial.get('rating', 5),
            "platform": testimonial.get('platform', 'direct'),
            "date": datetime.now().isoformat(),
            "approved": False
        }
        
        self.testimonials.append(t)
        
        client = self._find_client(client_id)
        if client:
            client['testimonials'].append(t)
            client['satisfaction_score'] = t['rating']
        
        return t
    
    def add_referral(self, client_id: str, referral_info: Dict) -> Dict:
        """Add a referral from existing client"""
        referral = {
            "id": str(uuid.uuid4())[:8],
            "referring_client_id": client_id,
            "referred_company": referral_info.get('company', 'Unknown'),
            "referred_contact": referral_info.get('contact_name', 'Unknown'),
            "referred_email": referral_info.get('email', ''),
            "status": "new",
            "date": datetime.now().isoformat(),
            "notes": referral_info.get('notes', ''),
            "converted": False
        }
        
        self.referrals.append(referral)
        
        client = self._find_client(client_id)
        if client:
            client['referrals'].append(referral)
        
        return referral
    
    def upsell_client(self, client_id: str, upsell_info: Dict) -> Dict:
        """Upsell additional services to existing client"""
        client = self._find_client(client_id)
        if not client:
            return {"error": "Client not found"}
        
        upsell = {
            "id": str(uuid.uuid4())[:8],
            "client_id": client_id,
            "service": upsell_info.get('service', 'Additional SEO'),
            "amount": upsell_info.get('amount', 0),
            "status": "proposed",
            "proposed_at": datetime.now().isoformat(),
            "notes": upsell_info.get('notes', ''),
            "accepted": False
        }
        
        client['total_revenue'] += upsell['amount']
        client['lifetime_value'] += upsell['amount']
        
        # Update lead stage
        lead = self._find_lead(client['lead_id'])
        if lead:
            lead['stage'] = "upsell"
        
        return upsell
    
    def get_pipeline_summary(self) -> Dict:
        """Get complete pipeline summary"""
        stages = {}
        for stage in self.PIPELINE_STAGES:
            leads_in_stage = [l for l in self.leads if l['stage'] == stage]
            stages[stage] = {
                "count": len(leads_in_stage),
                "total_value": sum(l.get('proposal_amount', l.get('estimated_value', 0)) for l in leads_in_stage),
                "leads": leads_in_stage
            }
        
        return {
            "total_leads": len(self.leads),
            "active_clients": len([c for c in self.clients if c['status'] == 'active']),
            "total_revenue": sum(c.get('total_revenue', 0) for c in self.clients),
            "total_lifetime_value": sum(c.get('lifetime_value', 0) for c in self.clients),
            "pipeline_stages": stages,
            "conversion_rate": self._calculate_conversion_rate(),
            "average_deal_size": self._calculate_average_deal_size(),
            "pipeline_value": sum(
                l.get('proposal_amount', l.get('estimated_value', 0)) 
                for l in self.leads if l['stage'] not in ['won', 'active_client']
            ),
            "recent_activities": self._get_recent_activities(10)
        }
    
    def _calculate_conversion_rate(self) -> float:
        """Calculate lead-to-client conversion rate"""
        if not self.leads:
            return 0.0
        won = len([l for l in self.leads if l['stage'] in ['won', 'active_client']])
        return round((won / len(self.leads)) * 100, 1)
    
    def _calculate_average_deal_size(self) -> float:
        """Calculate average deal size"""
        won_deals = [l for l in self.leads if l.get('deal_value', 0) > 0]
        if not won_deals:
            return 0.0
        return sum(l['deal_value'] for l in won_deals) / len(won_deals)
    
    def _get_recent_activities(self, limit: int = 10) -> List[Dict]:
        """Get recent pipeline activities"""
        activities = []
        for lead in self.leads:
            for activity in lead.get('activities', []):
                activities.append({
                    "lead_name": lead['contact_name'],
                    "company": lead['company'],
                    "type": activity['type'],
                    "timestamp": activity['timestamp'],
                    "details": activity['details']
                })
        
        activities.sort(key=lambda x: x['timestamp'], reverse=True)
        return activities[:limit]
    
    def _find_lead(self, lead_id: str) -> Optional[Dict]:
        """Find lead by ID"""
        for lead in self.leads:
            if lead['id'] == lead_id:
                return lead
        return None
    
    def _find_client(self, client_id: str) -> Optional[Dict]:
        """Find client by ID"""
        for client in self.clients:
            if client['id'] == client_id:
                return client
        return None
    
    def get_dashboard_data(self) -> Dict:
        """Get CRM dashboard data"""
        pipeline = self.get_pipeline_summary()
        
        return {
            "summary": {
                "total_leads": pipeline['total_leads'],
                "active_clients": pipeline['active_clients'],
                "total_revenue": pipeline['total_revenue'],
                "pipeline_value": pipeline['pipeline_value'],
                "conversion_rate": pipeline['conversion_rate'],
                "average_deal_size": pipeline['average_deal_size']
            },
            "pipeline": pipeline['pipeline_stages'],
            "recent_messages": sorted(self.messages, key=lambda x: x['timestamp'], reverse=True)[:5],
            "upcoming_follow_ups": [
                {
                    "lead": l['contact_name'],
                    "company": l['company'],
                    "date": l['next_follow_up'],
                    "stage": l['stage']
                }
                for l in self.leads if l.get('next_follow_up')
            ][:5],
            "testimonials_pending_approval": [t for t in self.testimonials if not t['approved']],
            "referrals_pending": [r for r in self.referrals if not r['converted']]
        }


def demonstrate_crm_agent():
    """Demonstrate CRM Agent"""
    print(f"\n{'='*80}")
    print("CRM AGENT - Demonstration")
    print(f"{'='*80}\n")
    
    crm = CRMAgent()
    
    # 1. Add leads
    print("1. Adding Leads to Pipeline")
    print("─" * 60)
    
    leads_data = [
        {"company": "TechFlow SaaS", "name": "John Smith", "email": "john@techflow.com", 
         "source": "upwork", "budget_range": "$3000-$5000", "service_interest": "Monthly SEO",
         "estimated_value": 3000, "industry": "SaaS"},
        {"company": "GreenLeaf Ecom", "name": "Sarah Wilson", "email": "sarah@greenleaf.com",
         "source": "referral", "budget_range": "$2000-$4000", "service_interest": "SEO Audit",
         "estimated_value": 2000, "industry": "E-commerce"},
        {"company": "City Dental", "name": "Dr. Mike Brown", "email": "drbrown@citydental.com",
         "source": "direct", "budget_range": "$1000-$2000", "service_interest": "Local SEO",
         "estimated_value": 1500, "industry": "Healthcare"}
    ]
    
    for data in leads_data:
        lead = crm.add_lead(data)
        print(f"  ✓ Lead added: {lead['company']} (Score: {lead['score']}/100)")
    
    # 2. Qualify leads
    print("\n2. Qualifying Leads")
    print("─" * 60)
    for lead in crm.leads:
        qualified = crm.qualify_lead(lead['id'], {
            "notes": "Good fit for our services",
            "budget_confirmed": True,
            "timeline": "2 weeks",
            "decision_maker": lead['contact_name']
        })
        print(f"  ✓ {qualified['company']}: Qualified (Score: {qualified['score']}/100)")
    
    # 3. Send proposals
    print("\n3. Sending Proposals")
    print("─" * 60)
    for lead in crm.leads[:2]:
        proposal = crm.send_proposal(lead['id'], {
            "amount": lead['estimated_value'],
            "type": "standard",
            "content": f"Custom proposal for {lead['company']}"
        })
        print(f"  ✓ {proposal['company']}: Proposal sent - ${proposal['proposal_amount']:,.0f}")
    
    # 4. Schedule interviews
    print("\n4. Scheduling Interviews")
    print("─" * 60)
    for lead in crm.leads[:2]:
        interview = crm.schedule_interview(lead['id'], {
            "scheduled_at": (datetime.now() + timedelta(days=2)).isoformat(),
            "type": "video_call",
            "notes": "Discuss project scope"
        })
        print(f"  ✓ {interview['company']}: Interview scheduled")
    
    # 5. Win deals
    print("\n5. Winning Deals")
    print("─" * 60)
    for lead in crm.leads[:2]:
        result = crm.win_deal(lead['id'], {
            "amount": lead['estimated_value'],
            "contract_type": "monthly",
            "start_date": datetime.now().isoformat()
        })
        print(f"  ✓ {result['client']['company']}: Deal won - ${result['client']['deal_value']:,.0f}")
    
    # 6. Start projects
    print("\n6. Starting Projects")
    print("─" * 60)
    for client in crm.clients:
        project = crm.start_project(client['id'], {
            "name": f"SEO Strategy for {client['company']}",
            "type": "Monthly SEO",
            "budget": client['deal_value'],
            "deliverables": ["SEO Audit", "Keyword Research", "On-page Optimization", "Monthly Report"]
        })
        print(f"  ✓ Project started: {project['name']}")
    
    # 7. Add messages
    print("\n7. Client Communication")
    print("─" * 60)
    for client in crm.clients:
        msg = crm.add_message(client['id'], {
            "direction": "outgoing",
            "type": "email",
            "subject": f"Welcome to Nexora - {client['company']}",
            "content": f"Thank you for choosing us! Let's get started on your SEO journey."
        })
        print(f"  ✓ Message sent to {client['company']}")
    
    # 8. Add testimonials
    print("\n8. Client Testimonials")
    print("─" * 60)
    for client in crm.clients:
        testimonial = crm.add_testimonial(client['id'], {
            "content": f"Excellent SEO service! Our traffic increased by 150% in 3 months.",
            "rating": 5,
            "platform": "upwork"
        })
        print(f"  ✓ Testimonial added from {client['company']} (Rating: {testimonial['rating']}/5)")
    
    # 9. Add referrals
    print("\n9. Referrals")
    print("─" * 60)
    for client in crm.clients:
        referral = crm.add_referral(client['id'], {
            "company": f"Partner of {client['company']}",
            "contact_name": "Jane Doe",
            "email": "jane@partner.com",
            "notes": "Referred by satisfied client"
        })
        print(f"  ✓ Referral added from {client['company']}")
    
    # 10. Dashboard
    print("\n10. CRM Dashboard")
    print("─" * 60)
    dashboard = crm.get_dashboard_data()
    print(f"  📊 Total Leads: {dashboard['summary']['total_leads']}")
    print(f"  👥 Active Clients: {dashboard['summary']['active_clients']}")
    print(f"  💰 Total Revenue: ${dashboard['summary']['total_revenue']:,.0f}")
    print(f"  📈 Pipeline Value: ${dashboard['summary']['pipeline_value']:,.0f}")
    print(f"  🎯 Conversion Rate: {dashboard['summary']['conversion_rate']}%")
    print(f"  💵 Average Deal: ${dashboard['summary']['average_deal_size']:,.0f}")
    
    print(f"\n{'='*80}")
    print("CRM AGENT - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Complete pipeline management (8 stages)")
    print("✓ Lead scoring and qualification")
    print("✓ Proposal tracking")
    print("✓ Interview scheduling")
    print("✓ Deal management")
    print("✓ Project tracking")
    print("✓ Client communication log")
    print("✓ Testimonial management")
    print("✓ Referral tracking")
    print("✓ Upsell management")
    print("✓ Dashboard with key metrics")
    print("\nStages: Lead → Qualified → Proposal Sent → Interview → Won → Active Client → Upsell → Referral")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_crm_agent()
#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Platform-Specific Sales Agents
Automated sales workflows for Upwork, Fiverr, and Freelancer.com
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class UpworkAgent:
    """Upwork-specific sales automation"""
    
    def __init__(self):
        self.platform = "Upwork"
        
    def generate_proposal(self, job_posting: Dict, profile: Dict) -> str:
        """Generate personalized Upwork proposal"""
        proposal = f"""
Subject: SEO Expert for {job_posting.get('title', 'Your Project')} - {profile.get('name', 'SEO Specialist')}

Hi {job_posting.get('client_name', 'there')},

I read your job posting for {job_posting.get('title', 'SEO services')} and I'm confident I can help you achieve {job_posting.get('goal', 'your goals')}.

**Quick Summary:**
- {profile.get('experience_years', 5)}+ years of SEO experience
- {profile.get('client_satisfaction', 98)}% average client satisfaction
- Proven results: {profile.get('key_achievement', '150%+ traffic increases')}

**I noticed you need:**
{self._format_requirements(job_posting.get('requirements', []))}

**My approach:**
{self._format_approach(job_posting.get('services_needed', []))}

**Recent results:**
{self._format_results(profile.get('recent_results', []))}

I'd love to discuss your project in more detail. I'm available for a quick call at your convenience.

Best regards,
{profile.get('name', 'SEO Specialist')}
Nexora AI SEO Agency
{profile.get('portfolio_url', 'www.nexora.com')}

P.S. I can start {job_posting.get('availability', 'this week')} and deliver {job_posting.get('deliverable', 'comprehensive SEO audit')} within {job_posting.get('timeline', '10 business days')}.
"""
        return proposal
    
    def generate_follow_up(self, original_proposal: Dict, days_since: int) -> str:
        """Generate follow-up proposal"""
        follow_up = f"""
Subject: Following up: {original_proposal.get('job_title', 'SEO Project')}

Hi {original_proposal.get('client_name', 'there')},

I wanted to follow up on my proposal for {original_proposal.get('service', 'SEO services')} from {days_since} days ago.

I understand you're busy, so I'll keep this brief:

**Quick question:** Are you still looking for an SEO expert for this project?

If so, I've prepared a {original_proposal.get('value_add', 'free website analysis')} that shows exactly how I would approach your project.

Would you like me to send it over?

Best,
{original_proposal.get('name', 'SEO Specialist')}
"""
        return follow_up
    
    def _format_requirements(self, requirements: List[str]) -> str:
        """Format requirements list"""
        if not requirements:
            return "- Professional SEO services\n- Data-driven strategies\n- Proven results"
        return '\n'.join([f"- {req}" for req in requirements])
    
    def _format_approach(self, services: List[str]) -> str:
        """Format approach steps"""
        if not services:
            return "1. Comprehensive audit\n2. Strategic planning\n3. Implementation\n4. Monitoring & reporting"
        return '\n'.join([f"{i+1}. {service}" for i, service in enumerate(services[:4])])
    
    def _format_results(self, results: List[str]) -> str:
        """Format results list"""
        if not results:
            return "- 150% increase in organic traffic\n- 200+ keywords to top 10\n- 300% ROI"
        return '\n'.join([f"- {result}" for result in results[:3]])


class FiverrAgent:
    """Fiverr-specific sales automation"""
    
    def __init__(self):
        self.platform = "Fiverr"
        
    def generate_buyer_response(self, buyer_request: Dict, gig: Dict) -> str:
        """Generate response to buyer request"""
        response = f"""
Hi {buyer_request.get('buyer_name', 'there')},

I saw your request for {buyer_request.get('service_type', 'SEO services')} and I can definitely help you with that.

**What I offer:**
✅ {gig.get('benefit_1', 'Comprehensive SEO audit')}
✅ {gig.get('benefit_2', 'Keyword research & strategy')}
✅ {gig.get('benefit_3', 'On-page optimization')}
✅ {gig.get('benefit_4', 'Monthly reporting')}

**Why choose me:**
- {gig.get('experience_years', 5)}+ years of experience
- {gig.get('projects_completed', 150)}+ projects completed
- {gig.get('client_satisfaction', 98)}% client satisfaction
- {gig.get('key_achievement', 'Proven results with 150%+ traffic increases')}

**What you'll get:**
{self._format_deliverables(gig.get('deliverables', []))}

**Package:** {gig.get('package', 'Standard')} - ${gig.get('price', 500)}
**Delivery:** {gig.get('delivery_days', 7)} days
**Revisions:** {gig.get('revisions', 3)} revisions included

I'm ready to start right away. Let's discuss your project!

Best,
{gig.get('seller_name', 'SEO Expert')}
"""
        return response
    
    def generate_gig_description(self, gig_data: Dict) -> str:
        """Generate optimized gig description"""
        description = f"""
🚀 **{gig_data.get('headline', 'GET RANKED HIGHER ON GOOGLE')}** 🚀

{gig_data.get('subheadline', 'Professional SEO services that deliver real results')}

**What I Offer:**

✅ **Comprehensive SEO Audit** - Complete analysis of your website
✅ **Keyword Research** - High-value, low-competition keywords
✅ **On-Page Optimization** - Title tags, meta descriptions, content
✅ **Technical SEO** - Site speed, mobile optimization, schema
✅ **Content Strategy** - Content calendar and recommendations
✅ **Monthly Reporting** - Track your progress

**Why Choose Me:**

⭐ {gig_data.get('experience_years', 5)}+ years of SEO experience
⭐ {gig_data.get('projects_completed', 150)}+ successful projects
⭐ {gig_data.get('client_satisfaction', 98)}% client satisfaction rate
⭐ Proven results: {gig_data.get('key_achievement', '150%+ traffic increases')}
⭐ White-hat SEO only (no penalties!)

**My Process:**

1. **Audit** - Analyze your website
2. **Strategy** - Create custom SEO plan
3. **Optimize** - Implement changes
4. **Monitor** - Track results
5. **Report** - Monthly progress reports

**Packages:**

**BASIC** - ${gig_data.get('basic_price', 300)}
- SEO audit
- 10 keywords
- Basic recommendations
- 1 report

**STANDARD** - ${gig_data.get('standard_price', 600)} ⭐ MOST POPULAR
- Comprehensive audit
- 50 keywords
- Full optimization
- 3 months of support
- Monthly reports

**PREMIUM** - ${gig_data.get('premium_price', 1200)}
- Everything in Standard
- 100+ keywords
- Content strategy
- 6 months of support
- Weekly reports
- Priority support

**What You'll Get:**
- Higher Google rankings
- More organic traffic
- More customers
- Better ROI

**Let's get started!** Click the "Order Now" button and let's discuss your project.

**FAQ:**
Q: How long until I see results?
A: Most clients see improvements within 30-60 days.

Q: Do you guarantee results?
A: I guarantee professional, white-hat SEO that improves your rankings over time.

Q: What if I'm not satisfied?
A: I offer {gig_data.get('revisions', 3)} revisions to ensure you're happy.

Feel free to message me with any questions!

Best,
{gig_data.get('seller_name', 'SEO Expert')}
{gig_data.get('agency_name', 'Nexora AI SEO Agency')}
"""
        return description
    
    def _format_deliverables(self, deliverables: List[str]) -> str:
        """Format deliverables list"""
        if not deliverables:
            return "- Comprehensive SEO audit\n- Keyword research\n- On-page optimization\n- Monthly report"
        return '\n'.join([f"- {deliverable}" for deliverable in deliverables])


class FreelancerAgent:
    """Freelancer.com-specific sales automation"""
    
    def __init__(self):
        self.platform = "Freelancer.com"
        
    def generate_bid(self, project: Dict, profile: Dict) -> str:
        """Generate bid for Freelancer.com project"""
        cover_letter = f"""
Dear {project.get('client_name', 'Hiring Manager')},

I am writing to express my interest in your {project.get('project_type', 'SEO')} project.

**About Me:**
I am a professional SEO specialist with {profile.get('experience_years', 5)}+ years of experience helping businesses {profile.get('specialty', 'achieve top rankings')}. I specialize in {profile.get('specialties', ['technical SEO', 'content strategy', 'link building'])} and have successfully completed {profile.get('projects_completed', 100)}+ similar projects.

**Understanding of Your Project:**
Based on your requirements, I understand you need:
{self._format_requirements(project.get('requirements', []))}

**My Proposed Approach:**
{self._format_approach(project.get('services_needed', []))}

**Deliverables:**
{self._format_deliverables(project.get('deliverables', []))}

**Timeline:** {project.get('timeline', '10 business days')}
**Budget:** ${project.get('budget', 1000)}

**Why Choose Me:**
- {profile.get('experience_years', 5)}+ years of experience
- {profile.get('client_satisfaction', 98)}% client satisfaction
- {profile.get('key_achievement', 'Proven results')}
- Professional, reliable, results-driven

I am available to start immediately and can complete this project within your timeline.

I look forward to discussing this opportunity further.

Best regards,
{profile.get('name', 'SEO Specialist')}
{profile.get('agency_name', 'Nexora AI SEO Agency')}
{profile.get('portfolio_url', 'www.nexora.com')}
"""
        return cover_letter
    
    def generate_milestone_proposal(self, project: Dict) -> str:
        """Generate milestone-based proposal"""
        milestones = project.get('milestones', [
            {'name': 'Audit & Research', 'amount': 300, 'deliverables': ['SEO Audit', 'Keyword Research'], 'days': 3},
            {'name': 'Strategy & Planning', 'amount': 400, 'deliverables': ['SEO Strategy', 'Content Plan'], 'days': 3},
            {'name': 'Implementation', 'amount': 300, 'deliverables': ['On-page Optimization', 'Technical Fixes'], 'days': 4}
        ])
        
        proposal = f"""
Hi {project.get('client_name', 'there')},

Great idea to use milestones! This ensures transparency and mutual success.

**Proposed Milestones:**

"""
        total = 0
        for i, milestone in enumerate(milestones, 1):
            amount = milestone.get('amount', 0)
            total += amount
            proposal += f"""**Milestone {i}: {milestone.get('name', 'Milestone')} - ${amount}**
- Deliverables: {', '.join(milestone.get('deliverables', []))}
- Timeline: {milestone.get('days', 5)} days
- Completion criteria: {milestone.get('criteria', 'Client approval')}

"""
        
        proposal += f"""**Total:** ${total}
**Timeline:** {sum(m.get('days', 5) for m in milestones)} days total

**My commitment:**
- Regular updates on progress
- Open communication
- Quality deliverables
- On-time completion

Does this milestone structure work for you? I'm happy to adjust based on your preferences.

Best,
{project.get('name', 'SEO Specialist')}
"""
        return proposal
    
    def _format_requirements(self, requirements: List[str]) -> str:
        """Format requirements list"""
        if not requirements:
            return "- Professional SEO services\n- Data-driven strategies\n- Proven results"
        return '\n'.join([f"- {req}" for req in requirements])
    
    def _format_approach(self, services: List[str]) -> str:
        """Format approach steps"""
        if not services:
            return "1. Comprehensive audit\n2. Strategic planning\n3. Implementation\n4. Monitoring & reporting"
        return '\n'.join([f"{i+1}. {service}" for i, service in enumerate(services[:4])])
    
    def _format_deliverables(self, deliverables: List[str]) -> str:
        """Format deliverables list"""
        if not deliverables:
            return "- SEO Audit Report\n- Keyword Research\n- SEO Strategy\n- Monthly Reports"
        return '\n'.join([f"- {deliverable}" for deliverable in deliverables])


class PlatformSalesManager:
    """Manages all platform-specific sales agents"""
    
    def __init__(self):
        self.upwork_agent = UpworkAgent()
        self.fiverr_agent = FiverrAgent()
        self.freelancer_agent = FreelancerAgent()
        
    def generate_sales_content(self, platform: str, data: Dict, profile: Dict) -> str:
        """Generate sales content for specified platform"""
        if platform.lower() == "upwork":
            if data.get('type') == 'proposal':
                return self.upwork_agent.generate_proposal(data, profile)
            elif data.get('type') == 'follow_up':
                return self.upwork_agent.generate_follow_up(data, data.get('days_since', 3))
        elif platform.lower() == "fiverr":
            if data.get('type') == 'buyer_response':
                return self.fiverr_agent.generate_buyer_response(data, profile)
            elif data.get('type') == 'gig_description':
                return self.fiverr_agent.generate_gig_description(profile)
        elif platform.lower() == "freelancer":
            if data.get('type') == 'bid':
                return self.freelancer_agent.generate_bid(data, profile)
            elif data.get('type') == 'milestone':
                return self.freelancer_agent.generate_milestone_proposal(data)
        
        return "Invalid platform or content type"
    
    def get_platform_guidelines(self, platform: str) -> Dict:
        """Get platform-specific guidelines"""
        guidelines = {
            "upwork": {
                "proposal_length": "Under 400 words",
                "response_time": "Within 1-2 hours",
                "key_elements": ["Personalization", "Relevant experience", "Portfolio links", "Clear next steps"],
                "best_practices": [
                    "Address client by name",
                    "Reference specific requirements",
                    "Show relevant samples",
                    "Be concise and scannable",
                    "Include call-to-action"
                ]
            },
            "fiverr": {
                "response_length": "Under 200 words",
                "response_time": "Within 1-2 hours",
                "key_elements": ["Quick response", "Clear offer", "Package details", "FAQ"],
                "best_practices": [
                    "Use emojis sparingly",
                    "Highlight key benefits",
                    "Clear packages",
                    "Fast delivery options",
                    "Professional closing"
                ]
            },
            "freelancer": {
                "proposal_length": "300-500 words",
                "response_time": "Within 2-4 hours",
                "key_elements": ["Formal tone", "Detailed approach", "Timeline", "Budget"],
                "best_practices": [
                    "Be more formal",
                    "Show project understanding",
                    "Detailed methodology",
                    "Clear milestones",
                    "Professional presentation"
                ]
            }
        }
        return guidelines.get(platform.lower(), {})


def demonstrate_platform_sales():
    """Demonstrate platform-specific sales agents"""
    print("\n" + "="*80)
    print("PLATFORM-SPECIFIC SALES AGENTS DEMONSTRATION")
    print("="*80 + "\n")
    
    sales_manager = PlatformSalesManager()
    
    # Sample profile
    profile = {
        'name': 'Sarah Johnson',
        'experience_years': 5,
        'client_satisfaction': 98,
        'key_achievement': '150%+ traffic increases for SaaS clients',
        'recent_results': [
            'Increased organic traffic by 185% in 6 months',
            'Ranked 200+ keywords in top 10',
            'Generated $95,000+ in additional revenue'
        ],
        'portfolio_url': 'www.nexora.com',
        'agency_name': 'Nexora AI SEO Agency'
    }
    
    # Upwork Example
    print("1. UPWORK PROPOSAL")
    print("-" * 80)
    upwork_job = {
        'title': 'SEO Audit for SaaS Website',
        'client_name': 'John Smith',
        'goal': 'improve search rankings',
        'requirements': ['Technical SEO audit', 'Keyword research', 'Competitor analysis'],
        'services_needed': ['Audit', 'Research', 'Strategy'],
        'availability': 'this week',
        'deliverable': 'comprehensive SEO audit',
        'timeline': '10 business days'
    }
    upwork_proposal = sales_manager.generate_sales_content('upwork', {'type': 'proposal', **upwork_job}, profile)
    print(upwork_proposal[:500] + "...")
    
    # Fiverr Example
    print("\n\n2. FIVERR BUYER RESPONSE")
    print("-" * 80)
    fiverr_request = {
        'buyer_name': 'Mike',
        'service_type': 'SEO optimization',
        'package': 'Standard',
        'price': 500,
        'delivery_days': 7,
        'revisions': 3
    }
    fiverr_gig = {
        'benefit_1': 'Comprehensive SEO audit',
        'benefit_2': 'Keyword research & strategy',
        'benefit_3': 'On-page optimization',
        'benefit_4': 'Monthly reporting',
        'experience_years': 5,
        'projects_completed': 150,
        'client_satisfaction': 98,
        'key_achievement': '150%+ traffic increases',
        'deliverables': ['SEO Audit', 'Keyword Research', 'Optimization', 'Report'],
        'seller_name': 'Sarah Johnson',
        'agency_name': 'Nexora AI SEO Agency'
    }
    fiverr_response = sales_manager.generate_sales_content('fiverr', {'type': 'buyer_response', **fiverr_request}, fiverr_gig)
    print(fiverr_response[:500] + "...")
    
    # Freelancer Example
    print("\n\n3. FREELANCER.COM BID")
    print("-" * 80)
    freelancer_project = {
        'project_type': 'SEO Strategy',
        'client_name': 'Emma Wilson',
        'requirements': ['SEO strategy', 'Content plan', 'Link building'],
        'services_needed': ['Strategy', 'Content', 'Link Building'],
        'deliverables': ['SEO Strategy Document', 'Content Calendar', 'Link Building Plan'],
        'timeline': '2 weeks',
        'budget': 2000
    }
    freelancer_bid = sales_manager.generate_sales_content('freelancer', {'type': 'bid', **freelancer_project}, profile)
    print(freelancer_bid[:500] + "...")
    
    # Platform Guidelines
    print("\n\n4. PLATFORM GUIDELINES")
    print("-" * 80)
    for platform in ['upwork', 'fiverr', 'freelancer']:
        guidelines = sales_manager.get_platform_guidelines(platform)
        print(f"\n{platform.upper()}:")
        print(f"  Proposal Length: {guidelines.get('proposal_length', 'N/A')}")
        print(f"  Response Time: {guidelines.get('response_time', 'N/A')}")
        print(f"  Key Elements: {', '.join(guidelines.get('key_elements', []))}")
    
    print("\n" + "="*80)
    print("PLATFORM SALES AGENTS READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Upwork proposal generation")
    print("✓ Fiverr buyer responses")
    print("✓ Freelancer.com bids")
    print("✓ Platform-optimized content")
    print("✓ Follow-up automation")
    print("✓ Milestone proposals")
    print("\n")


if __name__ == "__main__":
    demonstrate_platform_sales()
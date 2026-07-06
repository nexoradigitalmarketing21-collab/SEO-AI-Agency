#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Proposal Agent
Automatically creates winning proposals for Upwork, Fiverr, Freelancer, and direct outreach.
Generates custom proposals based on industry, business size, competition, budget, and client pain points.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os


class ProposalAgent:
    """Proposal Agent - Generate winning proposals across platforms"""
    
    def __init__(self):
        self.proposal_templates = self._load_templates()
        self.industry_insights = self._load_industry_insights()
    
    def _load_templates(self) -> Dict:
        """Load proposal templates"""
        return {
            "upwork": {
                "structure": [
                    "greeting",
                    "understanding",
                    "experience",
                    "approach",
                    "deliverables",
                    "timeline",
                    "investment",
                    "cta"
                ],
                "max_length": 400,
                "style": "professional_concise",
                "format": "plain_text"
            },
            "fiverr": {
                "structure": [
                    "greeting",
                    "offer",
                    "experience",
                    "packages",
                    "faq",
                    "cta"
                ],
                "style": "persuasive",
                "format": "rich_text"
            },
            "freelancer": {
                "structure": [
                    "greeting",
                    "understanding",
                    "approach",
                    "milestones",
                    "timeline",
                    "investment",
                    "cta"
                ],
                "style": "formal",
                "format": "plain_text"
            },
            "direct_outreach": {
                "structure": [
                    "subject",
                    "greeting",
                    "hook",
                    "value_proposition",
                    "social_proof",
                    "offer",
                    "cta"
                ],
                "style": "personal",
                "format": "email"
            },
            "linkedin": {
                "structure": [
                    "subject",
                    "greeting",
                    "connection",
                    "value",
                    "offer",
                    "cta"
                ],
                "style": "professional_friendly",
                "format": "linkedin_message"
            }
        }
    
    def _load_industry_insights(self) -> Dict:
        """Load industry-specific insights"""
        return {
            "saas": {
                "pain_points": [
                    "Low organic traffic for high-value keywords",
                    "High customer acquisition costs",
                    "Poor conversion from free trials",
                    "Difficulty ranking for competitive terms"
                ],
                "metrics_that_matter": [
                    "Organic traffic growth",
                    "Keyword rankings",
                    "Trial-to-paid conversion",
                    "Customer acquisition cost"
                ],
                "case_studies": [
                    "Increased organic traffic by 185% for B2B SaaS",
                    "Ranked 200+ keywords in top 10 for SaaS platform",
                    "Reduced CAC by 40% through organic channels"
                ]
            },
            "ecommerce": {
                "pain_points": [
                    "Low product page rankings",
                    "High cart abandonment rates",
                    "Poor category page optimization",
                    "Competition from big brands"
                ],
                "metrics_that_matter": [
                    "Product page rankings",
                    "Organic revenue",
                    "Cart abandonment rate",
                    "Category page traffic"
                ],
                "case_studies": [
                    "3x organic revenue for Shopify store",
                    "Ranked 50+ product pages in top 5",
                    "Increased category page traffic by 250%"
                ]
            },
            "local_business": {
                "pain_points": [
                    "Not showing in Google Maps",
                    "Missing local keywords",
                    "Few Google reviews",
                    "Competitors dominating local pack"
                ],
                "metrics_that_matter": [
                    "Google Maps ranking",
                    "Local pack appearances",
                    "Review count and rating",
                    "Near-me keyword rankings"
                ],
                "case_studies": [
                    "Top 3 Google Maps ranking for 20+ cities",
                    "Generated 50+ verified reviews",
                    "200% increase in local phone calls"
                ]
            },
            "healthcare": {
                "pain_points": [
                    "Strict compliance requirements",
                    "Medical authority establishment",
                    "Local patient acquisition",
                    "Trust-building with E-E-A-T"
                ],
                "metrics_that_matter": [
                    "Local rankings",
                    "Patient inquiries",
                    "E-E-A-T signals",
                    "Google Business Profile views"
                ],
                "case_studies": [
                    "Compliant SEO for medical practice",
                    "Top 3 rankings for 30+ medical conditions",
                    "50% increase in new patient bookings"
                ]
            },
            "legal": {
                "pain_points": [
                    "High competition for legal terms",
                    "Local market domination",
                    "Practice area authority",
                    "Client trust and credibility"
                ],
                "metrics_that_matter": [
                    "Practice area rankings",
                    "Case inquiries",
                    "Local pack presence",
                    "Client testimonials"
                ],
                "case_studies": [
                    "Top 5 rankings for 40+ legal keywords",
                    "3x increase in consultation requests",
                    "Dominant local pack presence"
                ]
            }
        }
    
    def generate_proposal(self, platform: str, client_info: Dict, project_info: Dict) -> Dict:
        """Generate a complete proposal based on platform and client info"""
        
        industry = client_info.get('industry', 'saas').lower()
        industry_data = self.industry_insights.get(industry, self.industry_insights['saas'])
        template = self.proposal_templates.get(platform, self.proposal_templates['direct_outreach'])
        
        # Build understanding section
        pain_points = self._identify_pain_points(client_info, project_info, industry_data)
        
        # Build value proposition
        value_prop = self._build_value_proposition(client_info, project_info, industry_data)
        
        # Build approach
        approach = self._build_approach(project_info)
        
        # Calculate pricing
        pricing = self._calculate_pricing(project_info, client_info)
        
        # Generate proposal content
        proposal_content = self._assemble_proposal(
            platform, template, client_info, project_info,
            pain_points, value_prop, approach, pricing, industry_data
        )
        
        return {
            "platform": platform,
            "client_name": client_info.get('name', 'there'),
            "company": client_info.get('company', ''),
            "industry": industry,
            "project_type": project_info.get('type', 'SEO Services'),
            "generated_at": datetime.now().isoformat(),
            "proposal_content": proposal_content,
            "pricing": pricing,
            "pain_points_addressed": pain_points,
            "value_proposition": value_prop,
            "deliverables": project_info.get('deliverables', []),
            "timeline": project_info.get('timeline', '2-4 weeks'),
            "discovery_questions": self._generate_discovery_questions(client_info, project_info),
            "competitive_differentiators": self._get_differentiators(industry_data)
        }
    
    def _identify_pain_points(self, client_info: Dict, project_info: Dict, industry_data: Dict) -> List[str]:
        """Identify client pain points"""
        pain_points = list(industry_data.get('pain_points', []))
        
        # Customize based on client info
        if client_info.get('website_score') and client_info['website_score'] < 50:
            pain_points.insert(0, f"Poor website SEO score ({client_info['website_score']}/100)")
        
        if client_info.get('competition_level') == 'high':
            pain_points.append("Strong competition from established players")
        
        if project_info.get('budget', 0) > 2000:
            pain_points.append("Need comprehensive strategy for maximum ROI")
        
        return pain_points[:5]
    
    def _build_value_proposition(self, client_info: Dict, project_info: Dict, industry_data: Dict) -> str:
        """Build compelling value proposition"""
        templates = [
            f"Help your {client_info.get('company', 'business')} achieve top rankings in {client_info.get('industry', 'your industry')} through data-driven SEO strategies.",
            f"Drive measurable growth for {client_info.get('company', 'your business')} with proven SEO methodologies that deliver real results.",
            f"Transform your online presence and dominate search results in {client_info.get('industry', 'your market')} with comprehensive SEO."
        ]
        return templates[hash(str(client_info)) % len(templates)]
    
    def _build_approach(self, project_info: Dict) -> List[str]:
        """Build methodology approach"""
        return [
            "Phase 1: Deep Analysis & Strategy - Comprehensive audit and competitive research",
            "Phase 2: Foundation Optimization - Fix critical technical and on-page issues",
            "Phase 3: Content & Authority - Create optimized content and build authority",
            "Phase 4: Monitoring & Optimization - Track results and continuously improve"
        ]
    
    def _calculate_pricing(self, project_info: Dict, client_info: Dict) -> Dict:
        """Calculate project pricing"""
        base_prices = {
            "seo_audit": 250,
            "keyword_research": 200,
            "technical_seo": 500,
            "content_strategy": 400,
            "monthly_seo": 800,
            "local_seo": 350,
            "link_building": 600,
            "full_strategy": 1500
        }
        
        project_type = project_info.get('type', 'monthly_seo').lower().replace(' ', '_')
        base_price = base_prices.get(project_type, 500)
        
        # Adjust for project size
        complexity_multiplier = {
            "simple": 1.0,
            "medium": 1.3,
            "complex": 1.8
        }.get(project_info.get('complexity', 'medium'), 1.3)
        
        # Adjust for business size
        size_multiplier = {
            "small": 1.0,
            "medium": 1.2,
            "large": 1.5,
            "enterprise": 2.0
        }.get(client_info.get('business_size', 'small'), 1.0)
        
        calculated_price = base_price * complexity_multiplier * size_multiplier
        
        return {
            "base_price": base_price,
            "complexity_multiplier": complexity_multiplier,
            "size_multiplier": size_multiplier,
            "calculated_price": round(calculated_price, -1),  # Round to nearest 10
            "price_range": {
                "min": round(calculated_price * 0.8, -1),
                "max": round(calculated_price * 1.2, -1)
            },
            "payment_options": [
                "Full payment (5% discount)",
                "50% upfront, 50% on delivery",
                "Monthly installments for projects over $1000"
            ]
        }
    
    def _assemble_proposal(self, platform: str, template: Dict, client_info: Dict,
                          project_info: Dict, pain_points: List[str],
                          value_prop: str, approach: List[str],
                          pricing: Dict, industry_data: Dict) -> str:
        """Assemble complete proposal"""
        
        client_name = client_info.get('name', 'there')
        company = client_info.get('company', 'your company')
        
        if platform == "upwork":
            return self._build_upwork_proposal(client_name, company, project_info, pain_points, value_prop, approach, pricing, industry_data)
        elif platform == "fiverr":
            return self._build_fiverr_proposal(client_name, company, project_info, pain_points, pricing)
        elif platform == "freelancer":
            return self._build_freelancer_proposal(client_name, company, project_info, pain_points, approach, pricing)
        elif platform == "linkedin":
            return self._build_linkedin_message(client_name, company, pain_points, value_prop, industry_data)
        else:
            return self._build_direct_outreach(client_name, company, pain_points, value_prop, approach, industry_data)
    
    def _build_upwork_proposal(self, name: str, company: str, project: Dict,
                               pain_points: List[str], value_prop: str,
                               approach: List[str], pricing: Dict,
                               industry_data: Dict) -> str:
        """Build Upwork proposal"""
        return f"""Hi {name},

I read your posting about {project.get('title', 'SEO services')} for {company}, and I can help.

I specialize in helping {project.get('industry', 'businesses')} achieve measurable SEO results. Here's what I noticed about your situation:

**Understanding Your Needs:**
{'• ' + '\n• '.join(pain_points)}

**My Approach:**
{value_prop}

My methodology:
1. {approach[0]}
2. {approach[1]}
3. {approach[2]}
4. {approach[3]}

**What I'll Deliver:**
{'• ' + '\n• '.join(project.get('deliverables', [
    'Comprehensive SEO audit', 'Keyword research report',
    'On-page optimization', 'Technical SEO fixes',
    'Monthly performance report'
]))}

**Investment:** ${pricing['calculated_price']:,.0f} (range: ${pricing['price_range']['min']:,.0f} - ${pricing['price_range']['max']:,.0f})
**Timeline:** {project.get('timeline', '3-4 weeks')}

Here's a relevant result: {industry_data.get('case_studies', ['Proven results for similar clients'])[0]}

I'm available to start this week. Would you be open to a quick call to discuss your project in detail?

Best regards,
SEO Specialist
Nexora AI SEO Agency"""
    
    def _build_fiverr_proposal(self, name: str, company: str, project: Dict,
                               pain_points: List[str], pricing: Dict) -> str:
        """Build Fiverr proposal"""
        return f"""Hi {name},

I saw your request and I'm confident I can help you with {project.get('title', 'SEO')} for {company}.

**Quick Understanding:**
{'• ' + '\n• '.join(pain_points[:3])}

**What I Offer:**
✅ Comprehensive analysis and strategy
✅ Professional execution
✅ Detailed reporting
✅ Fast delivery

**Package Options:**
• Basic: ${pricing['price_range']['min']:,.0f} - Essential SEO improvements
• Standard: ${pricing['calculated_price']:,.0f} - Complete SEO package ★ RECOMMENDED
• Premium: ${pricing['price_range']['max']:,.0f} - Full SEO transformation

**Why Choose Me:**
🏆 5+ years of SEO experience
🏆 150+ successful projects
🏆 98% client satisfaction
🏆 Fast turnaround

Ready to start! Let's discuss your project.

Best,
SEO Expert
Nexora AI SEO Agency"""
    
    def _build_freelancer_proposal(self, name: str, company: str, project: Dict,
                                    pain_points: List[str], approach: List[str],
                                    pricing: Dict) -> str:
        """Build Freelancer.com proposal"""
        return f"""Dear {name},

I am writing to express my strong interest in your {project.get('title', 'SEO project')} for {company}. With extensive experience in SEO, I am confident in my ability to deliver exceptional results.

**Project Understanding:**
{value_prop if (value_prop := '') else f"I understand that {' and '.join(pain_points[:2])} are key challenges facing {company}."}

**Proposed Milestones:**
1. **Analysis & Strategy** (${pricing['calculated_price'] * 0.3:,.0f}) - Comprehensive audit and strategic planning
2. **Implementation** (${pricing['calculated_price'] * 0.4:,.0f}) - Execute optimizations and improvements
3. **Monitoring & Reporting** (${pricing['calculated_price'] * 0.3:,.0f}) - Track results and provide insights

**Total Investment:** ${pricing['calculated_price']:,.0f}
**Timeline:** {project.get('timeline', '4-6 weeks')}

**My Commitment:**
- Regular progress updates
- Transparent communication
- Quality deliverables
- On-time completion

I am ready to start immediately. Let's discuss this further.

Best regards,
SEO Specialist
Nexora AI SEO Agency"""
    
    def _build_linkedin_message(self, name: str, company: str, pain_points: List[str],
                                value_prop: str, industry_data: Dict) -> str:
        """Build LinkedIn outreach message"""
        return f"""Hi {name},

I noticed {company} has some great potential for SEO growth. 

A quick observation: {' and '.join(pain_points[:2])} 

I recently helped a similar company {industry_data.get('case_studies', ['achieve significant SEO improvements'])[0].lower()}.

Would you be open to a 10-minute chat about how we could do the same for {company}?

Best,
SEO Specialist
Nexora AI SEO Agency"""
    
    def _build_direct_outreach(self, name: str, company: str, pain_points: List[str],
                               value_prop: str, approach: List[str],
                               industry_data: Dict) -> str:
        """Build direct outreach email"""
        return f"""Subject: Helping {company} achieve top SEO rankings

Hi {name},

I've been following {company} and noticed some great opportunities to improve your SEO performance.

**Key Observations:**
{'• ' + '\n• '.join(pain_points[:3])}

**How I Can Help:**
{value_prop}

{approach[0]}
{approach[1]}
{approach[2]}

**Results You Can Expect:**
• Increased organic traffic
• Higher search rankings
• More qualified leads
• Better ROI

Here's proof: {industry_data.get('case_studies', ['I deliver measurable results'])[0]}

Would you have 15 minutes this week for a brief call to discuss how we can achieve similar results for {company}?

Best regards,
SEO Specialist
Nexora AI SEO Agency"""
    
    def _generate_discovery_questions(self, client_info: Dict, project_info: Dict) -> List[str]:
        """Generate discovery questions for the client"""
        return [
            "What are your primary business goals for the next 6-12 months?",
            "Who are your main competitors, and what are they doing well?",
            "What SEO efforts have you tried in the past?",
            "Do you have access to Google Search Console and Analytics?",
            "What's your budget range for SEO services?"
        ]
    
    def _get_differentiators(self, industry_data: Dict) -> List[str]:
        """Get competitive differentiators"""
        return [
            "Data-driven strategies based on actual performance data",
            "White-hat SEO techniques (no penalty risk)",
            "Transparent reporting with regular updates",
            "Industry-specific expertise",
            "Proven track record with measurable results",
            "Dedicated support and quick response times"
        ]
    
    def generate_multiple_platform_proposals(self, client_info: Dict, project_info: Dict) -> Dict:
        """Generate proposals for multiple platforms at once"""
        platforms = ["upwork", "fiverr", "freelancer", "linkedin", "direct_outreach"]
        proposals = {}
        
        for platform in platforms:
            proposals[platform] = self.generate_proposal(platform, client_info, project_info)
        
        return {
            "client": client_info.get('name', 'Unknown'),
            "company": client_info.get('company', 'Unknown'),
            "project_type": project_info.get('type', 'SEO Services'),
            "generated_at": datetime.now().isoformat(),
            "proposals": proposals,
            "recommended_platform": self._recommend_platform(proposals)
        }
    
    def _recommend_platform(self, proposals: Dict) -> str:
        """Recommend best platform for this proposal"""
        # Simple scoring logic
        scores = {}
        for platform, proposal in proposals.items():
            pricing = proposal.get('pricing', {})
            price = pricing.get('calculated_price', 500)
            if 200 <= price <= 2000:
                scores[platform] = 80
            else:
                scores[platform] = 50
        
        return max(scores, key=scores.get)


def demonstrate_proposal_agent():
    """Demonstrate Proposal Agent"""
    print(f"\n{'='*80}")
    print("PROPOSAL AGENT - Demonstration")
    print(f"{'='*80}\n")
    
    agent = ProposalAgent()
    
    # Sample client info
    client_info = {
        "name": "John Smith",
        "company": "TechFlow SaaS",
        "industry": "saas",
        "business_size": "medium",
        "website_score": 45,
        "competition_level": "high"
    }
    
    project_info = {
        "title": "Complete SEO Strategy and Implementation",
        "type": "monthly_seo",
        "industry": "saas",
        "budget": 3000,
        "complexity": "complex",
        "timeline": "3 months",
        "deliverables": [
            "Technical SEO audit and fixes",
            "Keyword research and strategy",
            "Content optimization plan",
            "Monthly performance reports",
            "Link building campaign"
        ]
    }
    
    print("Generating proposals for all platforms...\n")
    
    # Generate for all platforms
    results = agent.generate_multiple_platform_proposals(client_info, project_info)
    
    print(f"Client: {results['client']}")
    print(f"Company: {results['company']}")
    print(f"Project: {results['project_type']}")
    print(f"Recommended Platform: {results['recommended_platform'].upper()}")
    
    # Show each platform proposal preview
    for platform, proposal in results['proposals'].items():
        content = proposal['proposal_content']
        print(f"\n{'─'*60}")
        print(f"📋 {platform.upper()} PROPOSAL")
        print(f"{'─'*60}")
        print(f"  Pricing: ${proposal['pricing']['calculated_price']:,.0f}")
        print(f"  Pain Points: {', '.join(proposal['pain_points_addressed'][:2])}...")
        print(f"  Content Preview: {content[:200]}...")
    
    print(f"\n{'='*80}")
    print("PROPOSAL AGENT - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Platform-specific proposals (Upwork, Fiverr, Freelancer, LinkedIn, Email)")
    print("✓ Industry-aware content (SaaS, E-commerce, Local, Healthcare, Legal)")
    print("✓ Client pain point identification")
    print("✓ Smart pricing calculation")
    print("✓ Discovery question generation")
    print("✓ Competitive differentiators")
    print("✓ Multi-platform proposal generation")
    print("\nOutputs: Custom proposals, Pricing, Discovery questions, Pain points")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_proposal_agent()
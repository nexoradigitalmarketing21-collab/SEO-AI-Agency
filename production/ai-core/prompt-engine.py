#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Prompt Engine
Milestone 1: Centralized prompt management with versioning, templates, and dynamic context injection.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import os
import hashlib


class PromptTemplate:
    """Individual prompt template with versioning"""
    
    def __init__(self, template_id: str, name: str, system_prompt: str, 
                 task_prompt: str, version: str = "1.0.0"):
        self.id = template_id
        self.name = name
        self.system_prompt = system_prompt
        self.task_prompt = task_prompt
        self.version = version
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.version_history = [{
            "version": version,
            "system_prompt": system_prompt,
            "task_prompt": task_prompt,
            "timestamp": self.created_at
        }]
        self.metrics = {"uses": 0, "avg_score": 0.0, "total_score": 0}
    
    def update(self, system_prompt: str, task_prompt: str) -> str:
        """Update prompt template with new version"""
        import uuid
        new_version = f"{self.version.split('.')[0]}.{int(self.version.split('.')[1]) + 1}.0"
        
        self.version_history.append({
            "version": new_version,
            "system_prompt": system_prompt,
            "task_prompt": task_prompt,
            "timestamp": datetime.now().isoformat()
        })
        
        self.system_prompt = system_prompt
        self.task_prompt = task_prompt
        self.version = new_version
        self.updated_at = datetime.now().isoformat()
        
        return new_version
    
    def render(self, context: Dict = None) -> Dict:
        """Render prompt with context injection"""
        self.metrics["uses"] += 1
        
        rendered_system = self.system_prompt
        rendered_task = self.task_prompt
        
        if context:
            for key, value in context.items():
                placeholder = f"{{{{{key}}}}}"
                rendered_system = rendered_system.replace(placeholder, str(value))
                rendered_task = rendered_task.replace(placeholder, str(value))
        
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "system_prompt": rendered_system,
            "task_prompt": rendered_task,
            "has_context": bool(context)
        }
    
    def record_feedback(self, score: float):
        """Record quality feedback on prompt output"""
        self.metrics["total_score"] += score
        self.metrics["avg_score"] = round(
            self.metrics["total_score"] / self.metrics["uses"], 2
        )


class PromptEngine:
    """Centralized prompt management engine"""
    
    def __init__(self):
        self.templates = {}
        self.categories = {}
        self._load_default_templates()
    
    def _load_default_templates(self):
        """Load default prompt templates for all agents"""
        templates = {
            "seo_audit": PromptTemplate(
                "seo_audit", "SEO Audit Analysis",
                "You are a Senior SEO Auditor with 15+ years of experience. Analyze websites comprehensively and provide actionable recommendations.",
                """Perform a thorough SEO audit of {website_url}. Cover:
1. Technical SEO (crawlability, indexation, Core Web Vitals)
2. On-page SEO (meta tags, headers, content quality, keyword usage)
3. Off-page SEO (backlink profile, domain authority)
4. User Experience (mobile, page speed, navigation)
5. Competitor Analysis (top 3 competitors)
6. Action Plan (prioritized by impact/effort)

Format as a structured report with scores (0-100) and specific recommendations."""
            ),
            "keyword_research": PromptTemplate(
                "keyword_research", "Keyword Research",
                "You are a Keyword Research Specialist. Find high-value, low-competition keyword opportunities.",
                """Research keywords for: {topic}
Industry: {industry}
Target Location: {location}

Provide:
1. Seed keywords (20-30)
2. Long-tail opportunities (50-100)
3. Question-based keywords
4. Competitor keyword gaps
5. Search intent analysis
6. Priority recommendations based on volume/difficulty"""
            ),
            "content_strategy": PromptTemplate(
                "content_strategy", "Content Strategy",
                "You are a Content Strategist specialized in SEO-driven content marketing.",
                """Design a content strategy for {business_name} in the {industry} industry.

Include:
1. Content pillars (4-5 main topics)
2. Topic clusters for each pillar
3. Content calendar (90 days)
4. Keyword targeting per piece
5. Internal linking strategy
6. Content types (blog, video, infographic, guide)
7. Distribution channels
8. Success metrics and KPIs"""
            ),
            "technical_seo": PromptTemplate(
                "technical_seo", "Technical SEO Analysis",
                "You are a Technical SEO expert. Identify and fix complex technical issues.",
                """Analyze technical SEO for {website_url}:

1. Crawl Analysis
2. Indexation Status
3. Site Structure
4. Page Speed (Core Web Vitals)
5. Schema Markup
6. Mobile Optimization
7. Security (HTTPS, mixed content)
8. Log File Analysis Recommendations
9. JavaScript SEO Considerations
10. International SEO (hreflang, ccTLDs)

Provide severity ratings: Critical, High, Medium, Low"""
            ),
            "content_writing": PromptTemplate(
                "content_writing", "SEO Content Writing",
                "You are an expert SEO Content Writer. Create engaging, ranking content.",
                """Write SEO-optimized content about {topic}.

Target Keywords: {keywords}
Target Audience: {audience}
Word Count: {word_count}
Tone: {tone}

Structure:
1. Compelling headline (H1)
2. Introduction with hook
3. Subheadings (H2, H3) with keyword-rich content
4. Bullet points and lists for scannability
5. FAQ section
6. Conclusion with CTA

SEO Requirements:
- Meta title (under 60 chars)
- Meta description (under 160 chars)
- URL slug
- Internal linking suggestions
- Image alt text suggestions"""
            ),
            "outreach": PromptTemplate(
                "outreach", "Outreach & Link Building",
                "You are a Professional Outreach Specialist. Build relationships and earn quality backlinks.",
                """Write a personalized outreach message for:

Prospect: {prospect_name}
Company: {prospect_company}
Website: {prospect_website}
Opportunity: {link_opportunity}
Our Resource: {our_resource}

Tone: Professional, personalized, value-first
Goal: Secure a backlink or collaboration

Include:
1. Personalized opening (reference their content)
2. Value proposition (what's in it for them)
3. Specific resource or opportunity
4. Low-friction ask
5. Professional closing"""
            ),
            "reporting": PromptTemplate(
                "reporting", "SEO Performance Report",
                "You are a Reporting Analyst. Create clear, insightful SEO reports.",
                """Generate an SEO performance report for {client_name}.

Period: {report_period}
Key Metrics:
- Organic Traffic: {organic_traffic}
- Keyword Rankings: {keyword_rankings}
- Backlinks: {backlinks}
- Conversions: {conversions}

Report Sections:
1. Executive Summary
2. Traffic Analysis (trends, sources)
3. Keyword Performance (winners/losers)
4. Technical Health
5. Content Performance
6. Competitor Comparison
7. Recommendations & Next Steps"""
            ),
            "qa_review": PromptTemplate(
                "qa_review", "QA Review Checklist",
                "You are a QA Specialist. Ensure all deliverables meet quality standards.",
                """Review the following {deliverable_type} for quality:

Title: {title}
Content: {content}

Quality Checklist:
1. Accuracy (facts, data, claims)
2. Completeness (all required sections present)
3. SEO Optimization (keyword usage, structure)
4. Readability (grade level, flow)
5. Brand Voice (tone, style consistency)
6. Formatting (headings, lists, spacing)
7. Links (internal/external, working)
8. Originality (plagiarism check)

Provide pass/fail for each criteria and overall score."""
            ),
            "sales_proposal": PromptTemplate(
                "sales_proposal", "Sales Proposal Generation",
                "You are a Sales Expert. Write compelling proposals that close deals.",
                """Write a sales proposal for:

Client: {client_name}
Industry: {client_industry}
Services Needed: {services}
Budget Range: {budget_range}

Proposal Structure:
1. Understanding of Their Needs
2. Our Solution (customized)
3. Deliverables & Timeline
4. Investment & Pricing
5. Expected Results
6. Case Studies / Social Proof
7. Terms & Next Steps

Make it personalized, outcome-focused, and compelling."""
            ),
            "competitor_analysis": PromptTemplate(
                "competitor_analysis", "Competitor Analysis",
                "You are a Competitive Intelligence Analyst. Uncover competitor strategies and opportunities.",
                """Analyze competitors for {business_name} in the {industry} market.

Top Competitors: {competitors}

Analysis Areas:
1. SEO Strategy (keywords, content, backlinks)
2. Content Strategy (topics, formats, frequency)
3. Technical Setup (speed, structure, schema)
4. Social Media Presence
5. Paid Advertising
6. Pricing & Offerings
7. Gaps & Opportunities

Provide actionable insights and winning strategies."""
            ),
            "local_seo": PromptTemplate(
                "local_seo", "Local SEO Optimization",
                "You are a Local SEO Specialist. Dominate local search results.",
                """Create a local SEO strategy for {business_name}.

Location: {location}
Industry: {industry}
Current GBP: {google_business_profile_url}

Optimization Plan:
1. Google Business Profile Optimization
2. Local Citation Building
3. Review Management Strategy
4. Local Keyword Targeting
5. Local Content Creation
6. Map Pack Ranking Strategy
7. Local Link Building
8. Competitor Local Analysis"""
            )
        }
        
        for template in templates.values():
            self.register_template(template)
    
    def register_template(self, template: PromptTemplate, category: str = "general"):
        """Register a new prompt template"""
        self.templates[template.id] = template
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(template.id)
    
    def get_template(self, template_id: str) -> Optional[PromptTemplate]:
        """Get a prompt template by ID"""
        return self.templates.get(template_id)
    
    def render(self, template_id: str, context: Dict = None) -> Dict:
        """Render a prompt template with context"""
        template = self.get_template(template_id)
        if not template:
            return {"error": f"Template '{template_id}' not found"}
        return template.render(context)
    
    def create_custom_template(self, template_id: str, name: str, 
                               system_prompt: str, task_prompt: str,
                               category: str = "custom") -> PromptTemplate:
        """Create a custom prompt template"""
        template = PromptTemplate(template_id, name, system_prompt, task_prompt)
        self.register_template(template, category)
        return template
    
    def search_templates(self, query: str) -> List[Dict]:
        """Search templates by name or content"""
        results = []
        query = query.lower()
        for template in self.templates.values():
            if (query in template.name.lower() or 
                query in template.system_prompt.lower() or
                query in template.task_prompt.lower()):
                results.append({
                    "id": template.id,
                    "name": template.name,
                    "version": template.version,
                    "uses": template.metrics["uses"]
                })
        return results
    
    def get_engine_status(self) -> Dict:
        """Get prompt engine status"""
        return {
            "total_templates": len(self.templates),
            "categories": list(self.categories.keys()),
            "templates_by_category": {
                cat: len(templates) for cat, templates in self.categories.items()
            },
            "most_used": sorted(
                [{"id": t.id, "name": t.name, "uses": t.metrics["uses"]}
                 for t in self.templates.values()],
                key=lambda x: x["uses"], reverse=True
            )[:5]
        }


if __name__ == "__main__":
    engine = PromptEngine()
    print("Prompt Engine Status:")
    status = engine.get_engine_status()
    print(f"  Total Templates: {status['total_templates']}")
    print(f"  Categories: {', '.join(status['categories'])}")
    print("\nTemplate Rendering Examples:")
    for template_id in ["seo_audit", "content_writing", "sales_proposal"]:
        rendered = engine.render(template_id, {
            "website_url": "example.com",
            "topic": "SEO Best Practices",
            "keywords": "SEO, search engine optimization",
            "audience": "Business owners",
            "word_count": 1500,
            "tone": "Professional",
            "client_name": "TechFlow SaaS",
            "client_industry": "B2B SaaS",
            "services": "Monthly SEO + Content",
            "budget_range": "$2000-3000/month"
        })
        print(f"\n  {rendered['name']} (v{rendered['version']})")
        print(f"  System: {rendered['system_prompt'][:80]}...")
        print(f"  Task: {rendered['task_prompt'][:80]}...")
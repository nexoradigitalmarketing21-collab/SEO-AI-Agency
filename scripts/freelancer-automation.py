#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Freelancer.com Automation System
Complete system for Freelancer.com bidding and project management.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class FreelancerJobAnalyzer:
    """Analyze Freelancer.com job postings"""
    
    def analyze_job(self, job_posting: Dict) -> Dict:
        """Analyze Freelancer.com job posting"""
        
        analysis = {
            "job_id": job_posting.get('id', 'UNKNOWN'),
            "title": job_posting.get('title', ''),
            "description": job_posting.get('description', ''),
            "analyzed_at": datetime.now().isoformat(),
            
            # Job details
            "category": self._classify_job(job_posting.get('title', ''), job_posting.get('description', '')),
            "skills_required": job_posting.get('skills', []),
            "difficulty": self._assess_difficulty(job_posting),
            
            # Budget analysis
            "budget_range": self._parse_budget(job_posting.get('budget', '')),
            "budget_assessment": self._assess_budget(job_posting.get('budget', '')),
            "recommended_bid": self._recommend_bid(job_posting),
            
            # Competition
            "bids_count": job_posting.get('bids', 0),
            "competition_level": self._assess_competition(job_posting.get('bids', 0)),
            "win_probability": self._calculate_win_probability(job_posting),
            
            # Client info
            "client_rating": job_posting.get('client_rating', 0),
            "client_reviews": job_posting.get('client_reviews', 0),
            "client_quality": self._assess_client_quality(job_posting),
            
            # Fit assessment
            "fit_score": 0,
            "priority": "",
            "recommendation": "",
            "suggested_approach": ""
        }
        
        # Calculate metrics
        analysis['fit_score'] = self._calculate_fit_score(analysis)
        analysis['priority'] = self._assign_priority(analysis)
        analysis['recommendation'] = self._generate_recommendation(analysis)
        analysis['suggested_approach'] = self._suggest_approach(analysis)
        
        return analysis
    
    def _classify_job(self, title: str, description: str) -> str:
        """Classify job category"""
        text = (title + ' ' + description).lower()
        
        categories = {
            'SEO Audit': ['audit', 'analysis', 'seo audit'],
            'Keyword Research': ['keyword', 'keyword research'],
            'Content Writing': ['content', 'writing', 'blog'],
            'Technical SEO': ['technical seo', 'site speed'],
            'Link Building': ['backlink', 'link building'],
            'Local SEO': ['local seo', 'google my business'],
            'Monthly SEO': ['monthly', 'ongoing', 'retainer']
        }
        
        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                return category
        
        return 'General SEO'
    
    def _assess_difficulty(self, job: Dict) -> str:
        """Assess job difficulty"""
        description = job.get('description', '')
        word_count = len(description.split())
        budget = job.get('budget', '')
        
        # Parse budget
        import re
        numbers = re.findall(r'\$?(\d+)', budget)
        max_budget = int(numbers[-1]) if numbers else 0
        
        if word_count > 500 or max_budget > 5000:
            return 'High'
        elif word_count > 200 or max_budget > 1000:
            return 'Medium'
        else:
            return 'Low'
    
    def _parse_budget(self, budget: str) -> Dict:
        """Parse budget string"""
        import re
        numbers = re.findall(r'\$?(\d+)', budget)
        
        if numbers:
            return {
                'type': 'fixed',
                'min': int(numbers[0]),
                'max': int(numbers[-1]) if len(numbers) > 1 else int(numbers[0])
            }
        
        return {'type': 'unknown', 'min': 0, 'max': 0}
    
    def _assess_budget(self, budget: str) -> str:
        """Assess budget quality"""
        budget_data = self._parse_budget(budget)
        max_budget = budget_data.get('max', 0)
        
        if max_budget >= 5000:
            return 'Excellent'
        elif max_budget >= 2000:
            return 'Good'
        elif max_budget >= 500:
            return 'Fair'
        else:
            return 'Low'
    
    def _recommend_bid(self, job: Dict) -> Dict:
        """Recommend bid amount"""
        budget_data = self._parse_budget(job.get('budget', ''))
        max_budget = budget_data.get('max', 0)
        
        # Freelancer.com typically has more competition, so bid slightly lower
        recommended = max_budget * 0.90
        
        return {
            "recommended_bid": round(recommended, 2),
            "min_bid": round(recommended * 0.85, 2),
            "max_bid": round(recommended * 0.95, 2),
            "reasoning": "Competitive bid for Freelancer.com market"
        }
    
    def _assess_competition(self, bids: int) -> str:
        """Assess competition level"""
        if bids == 0:
            return 'None'
        elif bids < 10:
            return 'Low'
        elif bids < 30:
            return 'Medium'
        else:
            return 'High'
    
    def _calculate_win_probability(self, job: Dict) -> float:
        """Calculate win probability"""
        score = 50.0
        
        # Budget
        budget_data = self._parse_budget(job.get('budget', ''))
        if budget_data.get('max', 0) >= 2000:
            score += 15
        elif budget_data.get('max', 0) >= 500:
            score += 10
        
        # Competition
        bids = job.get('bids', 0)
        if bids < 10:
            score += 20
        elif bids < 30:
            score += 10
        else:
            score -= 10
        
        # Client quality
        if job.get('client_rating', 0) >= 4.5:
            score += 10
        if job.get('client_reviews', 0) >= 5:
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _assess_client_quality(self, job: Dict) -> str:
        """Assess client quality"""
        rating = job.get('client_rating', 0)
        reviews = job.get('client_reviews', 0)
        
        if rating >= 4.5 and reviews >= 5:
            return 'Excellent'
        elif rating >= 4.0 and reviews >= 3:
            return 'Good'
        elif rating >= 3.5:
            return 'Fair'
        else:
            return 'Poor'
    
    def _calculate_fit_score(self, analysis: Dict) -> float:
        """Calculate fit score"""
        score = 0.0
        
        # Budget (25%)
        if analysis['budget_assessment'] in ['Excellent', 'Good']:
            score += 25
        elif analysis['budget_assessment'] == 'Fair':
            score += 15
        
        # Competition (25%)
        if analysis['competition_level'] == 'Low':
            score += 25
        elif analysis['competition_level'] == 'Medium':
            score += 15
        elif analysis['competition_level'] == 'High':
            score += 5
        
        # Win probability (25%)
        score += analysis['win_probability'] * 0.25
        
        # Client quality (25%)
        if analysis['client_quality'] == 'Excellent':
            score += 25
        elif analysis['client_quality'] == 'Good':
            score += 20
        elif analysis['client_quality'] == 'Fair':
            score += 10
        
        return min(100.0, score)
    
    def _assign_priority(self, analysis: Dict) -> str:
        """Assign priority"""
        fit_score = analysis['fit_score']
        
        if fit_score >= 80:
            return 'HIGH'
        elif fit_score >= 60:
            return 'MEDIUM'
        elif fit_score >= 40:
            return 'LOW'
        else:
            return 'SKIP'
    
    def _generate_recommendation(self, analysis: Dict) -> str:
        """Generate recommendation"""
        fit_score = analysis['fit_score']
        win_prob = analysis['win_probability']
        
        if fit_score >= 75 and win_prob >= 60:
            return "STRONGLY RECOMMEND - High fit, high win probability"
        elif fit_score >= 60 and win_prob >= 40:
            return "RECOMMEND - Good opportunity"
        elif fit_score >= 40:
            return "CONSIDER - Moderate fit"
        else:
            return "SKIP - Low fit"
    
    def _suggest_approach(self, analysis: Dict) -> str:
        """Suggest approach"""
        approaches = []
        
        if analysis['competition_level'] == 'High':
            approaches.append("Stand out with detailed portfolio and case studies")
        
        if analysis['client_quality'] == 'Excellent':
            approaches.append("Emphasize long-term partnership and quality")
        
        if analysis['difficulty'] == 'High':
            approaches.append("Break project into clear milestones")
        
        if not approaches:
            approaches.append("Standard competitive bid with clear deliverables")
        
        return '. '.join(approaches)


class FreelancerProposalGenerator:
    """Generate Freelancer.com proposals"""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load proposal templates"""
        return {
            'seo_audit': {
                'subject': 'SEO Expert for {title} - {years}+ Years Experience',
                'greeting': 'Dear {client_name},',
                'opening': 'I am writing to express my interest in your {title} project. With {years}+ years of experience in SEO, I am confident I can deliver exceptional results.',
                'qualifications': '**My Qualifications:**\n• {years}+ years of SEO experience\n• {projects}+ successful projects\n• {satisfaction}% client satisfaction\n• Expertise in {skills}',
                'approach': '**My Approach:**\n1. Comprehensive analysis\n2. Strategic planning\n3. Implementation\n4. Monitoring & reporting',
                'deliverables': '**Deliverables:**\n• {deliverables}',
                'timeline': '**Timeline:** {timeline}',
                'closing': 'I am available to start immediately and can complete this project within your timeline. I look forward to discussing this opportunity further.\n\nBest regards,\n{name}\n{agency}'
            }
        }
    
    def generate_proposal(self, job_analysis: Dict, profile: Dict) -> str:
        """Generate Freelancer.com proposal"""
        
        template = self.templates.get('seo_audit', self.templates['seo_audit'])
        
        proposal = template['subject'].format(
            title=job_analysis.get('title', 'SEO Project'),
            years=profile.get('experience_years', 5)
        )
        
        proposal += '\n\n' + template['greeting'].format(
            client_name=job_analysis.get('client_name', 'Hiring Manager')
        )
        
        proposal += '\n\n' + template['opening'].format(
            title=job_analysis.get('title', 'SEO'),
            years=profile.get('experience_years', 5)
        )
        
        proposal += '\n\n' + template['qualifications'].format(
            years=profile.get('experience_years', 5),
            projects=profile.get('projects_completed', 100),
            satisfaction=profile.get('client_satisfaction', 98),
            skills=', '.join(job_analysis.get('skills_required', ['SEO']))
        )
        
        proposal += '\n\n' + template['approach']
        
        proposal += '\n\n' + template['deliverables'].format(
            deliverables='\n• '.join(job_analysis.get('services_needed', ['SEO Audit', 'Strategy']))
        )
        
        proposal += '\n\n' + template['timeline'].format(
            timeline=job_analysis.get('recommended_bid', {}).get('reasoning', '10 business days')
        )
        
        proposal += '\n\n' + template['closing'].format(
            name=profile.get('name', 'SEO Specialist'),
            agency=profile.get('agency', 'Nexora AI SEO Agency')
        )
        
        return proposal
    
    def generate_milestone_proposal(self, project: Dict) -> str:
        """Generate milestone-based proposal"""
        
        milestones = project.get('milestones', [
            {'name': 'Audit & Research', 'amount': 300, 'deliverables': ['SEO Audit', 'Keyword Research'], 'days': 3},
            {'name': 'Strategy & Planning', 'amount': 400, 'deliverables': ['SEO Strategy', 'Content Plan'], 'days': 3},
            {'name': 'Implementation', 'amount': 300, 'deliverables': ['On-page Optimization', 'Technical Fixes'], 'days': 4}
        ])
        
        proposal = f"""
Dear {project.get('client_name', 'Hiring Manager')},

I propose to break this project into clear milestones for transparency and mutual success:

**Proposed Milestones:**

"""
        
        total = 0
        for i, milestone in enumerate(milestones, 1):
            amount = milestone.get('amount', 0)
            total += amount
            proposal += f"""**Milestone {i}: {milestone.get('name', 'Milestone')} - ${amount}**
- Deliverables: {', '.join(milestone.get('deliverables', []))}
- Timeline: {milestone.get('days', 5)} days
- Completion criteria: Client approval

"""
        
        proposal += f"""**Total Investment:** ${total}
**Total Timeline:** {sum(m.get('days', 5) for m in milestones)} days

**My Commitment:**
- Regular progress updates
- Open communication
- Quality deliverables
- On-time completion

This milestone structure ensures transparency and allows us to adjust as needed. I'm happy to discuss modifications based on your preferences.

Best regards,
{project.get('name', 'SEO Specialist')}
{project.get('agency', 'Nexora AI SEO Agency')}
"""
        
        return proposal
    
    def generate_client_qa_response(self, question: str, project_context: Dict) -> str:
        """Generate response to client questions"""
        
        qa_templates = {
            'experience': 'I have {years}+ years of experience in SEO and have completed {projects}+ similar projects. I specialize in {skills}.',
            'timeline': 'The typical timeline for this type of project is {timeline}. I can adjust based on your specific needs.',
            'pricing': 'My pricing is based on the scope of work and value provided. I offer competitive rates while maintaining high quality standards.',
            'process': 'My process includes: 1) Analysis, 2) Strategy development, 3) Implementation, 4) Monitoring & reporting.',
            'guarantee': 'I guarantee professional, high-quality work using white-hat SEO techniques. While I cannot guarantee specific rankings (as search engines control this), I guarantee significant improvements.',
            'communication': 'I provide regular updates via {platform} and am available for questions throughout the project.'
        }
        
        # Match question to template
        question_lower = question.lower()
        
        if 'experience' in question_lower or 'background' in question_lower:
            answer = qa_templates['experience'].format(
                years=project_context.get('experience_years', 5),
                projects=project_context.get('projects_completed', 100),
                skills=', '.join(project_context.get('skills', ['SEO', 'Technical SEO']))
            )
        elif 'timeline' in question_lower or 'how long' in question_lower:
            answer = qa_templates['timeline'].format(timeline='10-14 business days')
        elif 'price' in question_lower or 'cost' in question_lower or 'budget' in question_lower:
            answer = qa_templates['pricing']
        elif 'process' in question_lower or 'approach' in question_lower:
            answer = qa_templates['process']
        elif 'guarantee' in question_lower or 'guaranteed' in question_lower:
            answer = qa_templates['guarantee']
        elif 'communicat' in question_lower or 'update' in question_lower:
            answer = qa_templates['communication'].format(platform='Freelancer.com messages and email')
        else:
            answer = 'Thank you for your question. Based on my experience with similar projects, I can assure you that I will deliver high-quality results. Please feel free to ask any specific questions you may have.'
        
        return answer


class FreelancerAutomationSystem:
    """Complete Freelancer.com automation system"""
    
    def __init__(self):
        self.job_analyzer = FreelancerJobAnalyzer()
        self.proposal_generator = FreelancerProposalGenerator()
    
    def process_job(self, job_posting: Dict, profile: Dict) -> Dict:
        """Process job posting"""
        
        # Analyze job
        analysis = self.job_analyzer.analyze_job(job_posting)
        
        result = {
            "analysis": analysis,
            "proposal": None,
            "milestone_proposal": None,
            "action": "skip"
        }
        
        # Generate proposal if recommended
        if analysis['priority'] in ['HIGH', 'MEDIUM']:
            proposal = self.proposal_generator.generate_proposal(analysis, profile)
            result['proposal'] = proposal
            
            # Also generate milestone proposal for larger projects
            if analysis['difficulty'] == 'High' or analysis['budget_range'].get('max', 0) > 3000:
                milestone_proposal = self.proposal_generator.generate_milestone_proposal({
                    'client_name': job_posting.get('client_name', 'Hiring Manager'),
                    'name': profile.get('name', 'SEO Specialist'),
                    'agency': profile.get('agency', 'Nexora AI SEO Agency')
                })
                result['milestone_proposal'] = milestone_proposal
            
            result['action'] = 'bid'
        
        return result
    
    def batch_bid(self, jobs: List[Dict], profile: Dict, max_bids: int = 10) -> Dict:
        """Batch bid on multiple jobs"""
        
        results = {
            "total_jobs": len(jobs),
            "bids_submitted": 0,
            "skipped": 0,
            "high_priority": 0,
            "medium_priority": 0,
            "low_priority": 0,
            "bids": []
        }
        
        for job in jobs[:max_bids]:
            processed = self.process_job(job, profile)
            
            if processed['action'] == 'bid':
                results['bids_submitted'] += 1
                results['bids'].append({
                    "job_id": job.get('id'),
                    "title": job.get('title'),
                    "priority": processed['analysis']['priority'],
                    "fit_score": processed['analysis']['fit_score'],
                    "win_probability": processed['analysis']['win_probability'],
                    "proposal": processed['proposal'],
                    "milestone_proposal": processed.get('milestone_proposal')
                })
                
                if processed['analysis']['priority'] == 'HIGH':
                    results['high_priority'] += 1
                elif processed['analysis']['priority'] == 'MEDIUM':
                    results['medium_priority'] += 1
            else:
                results['skipped'] += 1
                if processed['analysis']['priority'] == 'LOW':
                    results['low_priority'] += 1
        
        return results
    
    def respond_to_client_question(self, question: str, project_context: Dict) -> str:
        """Respond to client question"""
        return self.proposal_generator.generate_client_qa_response(question, project_context)


def demonstrate_freelancer_automation():
    """Demonstrate Freelancer.com automation"""
    print("\n" + "="*80)
    print("FREELANCER.COM AUTOMATION SYSTEM DEMONSTRATION")
    print("="*80 + "\n")
    
    freelancer = FreelancerAutomationSystem()
    
    # Sample job posting
    sample_job = {
        'id': 'FL-001',
        'title': 'SEO Strategy and Implementation for E-commerce Website',
        'description': 'Looking for an SEO expert to develop and implement a comprehensive SEO strategy for our e-commerce website. Need keyword research, on-page optimization, technical SEO fixes, and link building.',
        'budget': '$3,000 - $5,000',
        'bids': 15,
        'skills': ['SEO', 'Keyword Research', 'Link Building'],
        'client_name': 'John Smith',
        'client_rating': 4.7,
        'client_reviews': 8
    }
    
    # Sample profile
    profile = {
        'name': 'Sarah Johnson',
        'experience_years': 5,
        'projects_completed': 150,
        'client_satisfaction': 98,
        'key_achievement': '150%+ traffic increases',
        'agency': 'Nexora AI SEO Agency',
        'skills': ['SEO', 'Technical SEO', 'Keyword Research', 'Link Building']
    }
    
    print("Step 1: Analyzing Job Posting")
    print("-" * 80)
    print(f"Job: {sample_job['title']}")
    print(f"Budget: {sample_job['budget']}")
    print(f"Bids: {sample_job['bids']}")
    
    # Analyze job
    analysis = freelancer.job_analyzer.analyze_job(sample_job)
    
    print(f"\n📊 Job Analysis:")
    print(f"  Category: {analysis['category']}")
    print(f"  Skills Required: {', '.join(analysis['skills_required'])}")
    print(f"  Difficulty: {analysis['difficulty']}")
    print(f"  Budget Assessment: {analysis['budget_assessment']}")
    print(f"  Competition: {analysis['competition_level']}")
    print(f"  Win Probability: {analysis['win_probability']:.1f}%")
    print(f"  Client Quality: {analysis['client_quality']}")
    print(f"  Fit Score: {analysis['fit_score']:.1f}/100")
    print(f"  Priority: {analysis['priority']}")
    print(f"  Recommendation: {analysis['recommendation']}")
    
    print(f"\n💰 Recommended Bid:")
    bid = analysis['recommended_bid']
    print(f"  Recommended: ${bid['recommended_bid']:,.2f}")
    print(f"  Range: ${bid['min_bid']:,.2f} - ${bid['max_bid']:,.2f}")
    
    print("\n\nStep 2: Generating Proposal")
    print("-" * 80)
    
    # Generate proposal
    result = freelancer.process_job(sample_job, profile)
    
    if result['proposal']:
        print(f"✅ Proposal generated (Priority: {result['analysis']['priority']})")
        print(f"\n{result['proposal'][:600]}...")
    
    if result.get('milestone_proposal'):
        print(f"\n\n✅ Milestone proposal also generated (High-value project)")
        print(f"\n{result['milestone_proposal'][:400]}...")
    
    print("\n\nStep 3: Client Q&A Example")
    print("-" * 80)
    
    # Sample client questions
    questions = [
        "What is your experience with SEO?",
        "How long will this project take?",
        "Can you guarantee results?",
        "How will we communicate?"
    ]
    
    project_context = {
        'experience_years': 5,
        'projects_completed': 150,
        'skills': ['SEO', 'Technical SEO', 'Keyword Research'],
        'title': sample_job['title']
    }
    
    for question in questions:
        print(f"\nQ: {question}")
        answer = freelancer.respond_to_client_question(question, project_context)
        print(f"A: {answer[:150]}...")
    
    print("\n\nStep 4: Batch Bidding Example")
    print("-" * 80)
    
    # Sample multiple jobs
    sample_jobs = [
        {
            'id': f'FL-{i:03d}',
            'title': f'Sample SEO Job {i}',
            'description': 'Looking for SEO services...',
            'budget': f'${1000 + i*500} - ${2000 + i*500}',
            'bids': i * 2,
            'skills': ['SEO'],
            'client_name': f'Client {i}',
            'client_rating': 4.0 + (i % 10) / 10,
            'client_reviews': i + 1
        }
        for i in range(1, 11)
    ]
    
    batch_results = freelancer.batch_bid(sample_jobs, profile, max_bids=10)
    
    print(f"\n📊 Batch Bidding Results:")
    print(f"  Total Jobs Analyzed: {batch_results['total_jobs']}")
    print(f"  Bids Submitted: {batch_results['bids_submitted']}")
    print(f"  Skipped: {batch_results['skipped']}")
    print(f"  High Priority: {batch_results['high_priority']}")
    print(f"  Medium Priority: {batch_results['medium_priority']}")
    print(f"  Low Priority: {batch_results['low_priority']}")
    
    print("\n" + "="*80)
    print("FREELANCER.COM AUTOMATION READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Job analysis and fit scoring")
    print("✓ Win probability calculation")
    print("✓ Budget recommendation")
    print("✓ Formal proposal generation")
    print("✓ Milestone proposal generation")
    print("✓ Client Q&A automation")
    print("✓ Batch bidding")
    print("\nGoal: Submit competitive bids with high win rate")
    print("\n")


if __name__ == "__main__":
    demonstrate_freelancer_automation()
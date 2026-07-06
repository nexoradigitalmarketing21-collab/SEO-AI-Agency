#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Outreach Agent
Writes personalized outreach: cold emails, LinkedIn messages, follow-ups, meeting requests.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os


class OutreachAgent:
    """Outreach Agent - Generate personalized outreach communications"""
    
    def __init__(self):
        self.outreach_templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load outreach templates"""
        return {
            "cold_email": {
                "subject": "Helping {company} achieve better SEO results",
                "greeting": "Hi {name},",
                "hook": "I noticed {company} has great potential for SEO growth.",
                "value_proposition": "I specialize in helping {industry} businesses increase their organic traffic by 150%+.",
                "social_proof": "Recently helped a similar company achieve {result}.",
                "offer": "Would you be open to a quick 10-minute call to discuss how we could do the same for {company}?",
                "closing": "Best regards,\n{agent_name}\nNexora AI SEO Agency",
                "signature": True
            },
            "linkedin_message": {
                "greeting": "Hi {name},",
                "connection": "I've been following {company}'s work in {industry}.",
                "value": "I noticed some SEO opportunities that could help you generate more leads.",
                "offer": "Would you be open to a brief chat about it?",
                "closing": "Best,\n{agent_name}"
            },
            "follow_up": {
                "subject": "Re: Helping {company} with SEO",
                "greeting": "Hi {name},",
                "opening": "I wanted to follow up on my previous message about SEO opportunities for {company}.",
                "value_add": "Since we last spoke, I did a quick analysis of {company}'s website and found some interesting opportunities.",
                "social_proof": "For context, here's what I achieved for a similar company recently: {result}.",
                "offer": "Would you have 10 minutes this week for a quick call?",
                "closing": "Best,\n{agent_name}"
            },
            "meeting_request": {
                "subject": "Quick chat about {company}'s SEO?",
                "greeting": "Hi {name},",
                "opening": "I'd love to schedule a brief call to discuss how we can help {company} achieve better SEO results.",
                "availability": "I'm available: {times}",
                "options": "Would any of these times work for you? Alternatively, feel free to suggest a time.",
                "closing": "Looking forward to connecting!\n\nBest,\n{agent_name}"
            }
        }
    
    def generate_cold_email(self, prospect: Dict, campaign_info: Dict = None) -> Dict:
        """Generate personalized cold email"""
        template = self.outreach_templates['cold_email']
        
        subject = template['subject'].format(
            company=prospect.get('company', 'your company')
        )
        
        body = f"""{template['greeting'].format(name=prospect.get('name', 'there'))}

{template['hook'].format(company=prospect.get('company', 'your company'))}

{template['value_proposition'].format(industry=prospect.get('industry', 'your industry'))}

{template['social_proof'].format(result=prospect.get('recent_result', 'a 185% increase in organic traffic'))}

{template['offer'].format(company=prospect.get('company', 'your company'))}

{template['closing'].format(agent_name=prospect.get('agent_name', 'SEO Specialist'))}
"""
        
        return {
            "type": "cold_email",
            "to": prospect.get('email', ''),
            "subject": subject,
            "body": body,
            "personalization_score": self._calculate_personalization_score(prospect),
            "send_at": datetime.now().isoformat(),
            "follow_up_date": (datetime.now() + timedelta(days=3)).isoformat(),
            "tracking": {
                "opens": 0,
                "clicks": 0,
                "replies": 0
            }
        }
    
    def generate_linkedin_message(self, prospect: Dict) -> Dict:
        """Generate LinkedIn outreach message"""
        template = self.outreach_templates['linkedin_message']
        
        body = f"""{template['greeting'].format(name=prospect.get('name', 'there'))}

{template['connection'].format(company=prospect.get('company', 'your company'), industry=prospect.get('industry', 'your industry'))}

{template['value']}

{template['offer']}

{template['closing'].format(agent_name=prospect.get('agent_name', 'SEO Specialist'))}
"""
        
        return {
            "type": "linkedin_message",
            "recipient": prospect.get('linkedin_profile', ''),
            "body": body,
            "connection_request": True,
            "personalization_score": self._calculate_personalization_score(prospect),
            "send_at": datetime.now().isoformat(),
            "follow_up_date": (datetime.now() + timedelta(days=5)).isoformat()
        }
    
    def generate_follow_up(self, previous_outreach: Dict, prospect: Dict) -> Dict:
        """Generate follow-up message"""
        template = self.outreach_templates['follow_up']
        
        subject = template['subject'].format(
            company=prospect.get('company', 'your company')
        )
        
        body = f"""{template['greeting'].format(name=prospect.get('name', 'there'))}

{template['opening'].format(company=prospect.get('company', 'your company'))}

{template['value_add'].format(company=prospect.get('company', 'your company'))}

{template['social_proof'].format(result=prospect.get('recent_result', 'a significant increase in organic traffic'))}

{template['offer']}

{template['closing'].format(agent_name=prospect.get('agent_name', 'SEO Specialist'))}
"""
        
        return {
            "type": "follow_up",
            "previous_message_id": previous_outreach.get('type', 'unknown'),
            "subject": subject,
            "body": body,
            "follow_up_number": previous_outreach.get('follow_up_number', 0) + 1,
            "max_follow_ups": 3,
            "send_at": (datetime.now() + timedelta(days=3)).isoformat()
        }
    
    def generate_meeting_request(self, prospect: Dict, times: List[str] = None) -> Dict:
        """Generate meeting request"""
        template = self.outreach_templates['meeting_request']
        
        if times is None:
            times = ["Monday 10 AM", "Tuesday 2 PM", "Thursday 11 AM"]
        
        subject = template['subject'].format(
            company=prospect.get('company', 'your company')
        )
        
        body = f"""{template['greeting'].format(name=prospect.get('name', 'there'))}

{template['opening'].format(company=prospect.get('company', 'your company'))}

{template['availability'].format(times=', '.join(times))}

{template['options']}

{template['closing'].format(agent_name=prospect.get('agent_name', 'SEO Specialist'))}
"""
        
        return {
            "type": "meeting_request",
            "to": prospect.get('email', ''),
            "subject": subject,
            "body": body,
            "suggested_times": times,
            "calendar_link": None,
            "send_at": datetime.now().isoformat()
        }
    
    def generate_outreach_sequence(self, prospect: Dict, sequence_type: str = "cold_email") -> List[Dict]:
        """Generate complete outreach sequence"""
        sequence = []
        
        if sequence_type == "cold_email":
            # Step 1: Initial cold email
            sequence.append(self.generate_cold_email(prospect))
            
            # Step 2: Follow up (3 days later)
            follow_up_1 = self.generate_follow_up(sequence[-1], prospect)
            follow_up_1['send_at'] = (datetime.now() + timedelta(days=3)).isoformat()
            follow_up_1['follow_up_number'] = 1
            sequence.append(follow_up_1)
            
            # Step 3: Second follow up with value add (7 days later)
            follow_up_2 = self.generate_follow_up(sequence[-1], prospect)
            follow_up_2['send_at'] = (datetime.now() + timedelta(days=7)).isoformat()
            follow_up_2['follow_up_number'] = 2
            follow_up_2['body'] = self._enhance_follow_up_with_value(follow_up_2, prospect)
            sequence.append(follow_up_2)
            
            # Step 4: LinkedIn message (10 days later)
            linkedin_msg = self.generate_linkedin_message(prospect)
            linkedin_msg['send_at'] = (datetime.now() + timedelta(days=10)).isoformat()
            sequence.append(linkedin_msg)
            
            # Step 5: Meeting request (14 days later) - if no response
            meeting = self.generate_meeting_request(prospect)
            meeting['send_at'] = (datetime.now() + timedelta(days=14)).isoformat()
            sequence.append(meeting)
        
        elif sequence_type == "linkedin":
            # LinkedIn first, then email
            linkedin_msg = self.generate_linkedin_message(prospect)
            linkedin_msg['send_at'] = datetime.now().isoformat()
            sequence.append(linkedin_msg)
            
            # Follow up on LinkedIn
            follow_up = self.generate_follow_up(sequence[-1], prospect)
            follow_up['send_at'] = (datetime.now() + timedelta(days=4)).isoformat()
            follow_up['follow_up_number'] = 1
            sequence.append(follow_up)
            
            # Cold email (7 days later)
            email = self.generate_cold_email(prospect)
            email['send_at'] = (datetime.now() + timedelta(days=7)).isoformat()
            sequence.append(email)
        
        return sequence
    
    def _enhance_follow_up_with_value(self, follow_up: Dict, prospect: Dict) -> str:
        """Enhance follow up with specific value add"""
        value_add = f"""
Hi {prospect.get('name', 'there')},

I hope you're doing well. I wanted to share a quick insight I found about {prospect.get('company', 'your company')}'s website:

🔍 Quick SEO Observation:
Your website has some great content, but there are opportunities to improve your search visibility significantly. In particular, optimizing for {prospect.get('industry', 'your industry')}-specific keywords could drive substantial additional traffic.

📊 Quick Win:
Simply optimizing your title tags and meta descriptions could improve click-through rates by 20-30%.

Would you be open to a brief 10-minute call to discuss this further? I have some specific recommendations I'd love to share.

Best,
{prospect.get('agent_name', 'SEO Specialist')}
Nexora AI SEO Agency"""
        return value_add
    
    def _calculate_personalization_score(self, prospect: Dict) -> int:
        """Calculate how personalized the message is"""
        score = 0
        
        if prospect.get('name'):
            score += 20
        if prospect.get('company'):
            score += 20
        if prospect.get('industry'):
            score += 20
        if prospect.get('recent_result'):
            score += 20
        if prospect.get('website_analyzed'):
            score += 20
        
        return min(100, score)
    
    def generate_batch_outreach(self, prospects: List[Dict], campaign_type: str = "cold_email") -> Dict:
        """Generate outreach for multiple prospects"""
        batch_results = {
            "campaign_type": campaign_type,
            "total_prospects": len(prospects),
            "sequences": [],
            "estimated_time_to_complete": f"{len(prospects) * 14} days",
            "metrics": {
                "total_messages": 0,
                "follow_ups": 0,
                "meeting_requests": 0
            }
        }
        
        for prospect in prospects:
            sequence = self.generate_outreach_sequence(prospect, campaign_type)
            batch_results['sequences'].append({
                "prospect": prospect.get('name', 'Unknown'),
                "company": prospect.get('company', 'Unknown'),
                "sequence": sequence
            })
            
            # Update metrics
            batch_results['metrics']['total_messages'] += len(sequence)
            for msg in sequence:
                if msg['type'] == 'follow_up':
                    batch_results['metrics']['follow_ups'] += 1
                elif msg['type'] == 'meeting_request':
                    batch_results['metrics']['meeting_requests'] += 1
        
        return batch_results


def demonstrate_outreach_agent():
    """Demonstrate Outreach Agent"""
    print(f"\n{'='*80}")
    print("OUTREACH AGENT - Demonstration")
    print(f"{'='*80}\n")
    
    agent = OutreachAgent()
    
    # Sample prospect
    prospect = {
        "name": "Sarah Johnson",
        "company": "GrowthMetrics Inc.",
        "industry": "SaaS",
        "email": "sarah@growthmetrics.com",
        "linkedin_profile": "linkedin.com/in/sarahjohnson",
        "recent_result": "a 185% increase in organic traffic for a B2B SaaS company",
        "website_analyzed": True,
        "agent_name": "SEO Specialist"
    }
    
    print("1. Cold Email Generation")
    print("─" * 60)
    email = agent.generate_cold_email(prospect)
    print(f"To: {email['to']}")
    print(f"Subject: {email['subject']}")
    print(f"Personalization Score: {email['personalization_score']}/100")
    print(f"\nBody:\n{email['body'][:400]}...")
    
    print("\n\n2. LinkedIn Message")
    print("─" * 60)
    linkedin = agent.generate_linkedin_message(prospect)
    print(f"\n{linkedin['body']}")
    
    print("\n3. Follow-up Message")
    print("─" * 60)
    follow_up = agent.generate_follow_up(email, prospect)
    print(f"Subject: {follow_up['subject']}")
    print(f"Follow-up #{follow_up['follow_up_number']}")
    print(f"Send at: {follow_up['send_at']}")
    
    print("\n4. Meeting Request")
    print("─" * 60)
    meeting = agent.generate_meeting_request(prospect)
    print(f"Subject: {meeting['subject']}")
    print(f"\n{meeting['body'][:300]}...")
    
    print("\n\n5. Complete Outreach Sequence")
    print("─" * 60)
    sequence = agent.generate_outreach_sequence(prospect, "cold_email")
    print(f"Total Messages: {len(sequence)}")
    for i, msg in enumerate(sequence, 1):
        print(f"  Day {(datetime.fromisoformat(msg['send_at']) - datetime.now()).days}: {msg['type'].replace('_', ' ').title()} - {msg['subject'][:50]}...")
    
    print(f"\n{'='*80}")
    print("OUTREACH AGENT - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Cold email generation")
    print("✓ LinkedIn message generation")
    print("✓ Follow-up automation")
    print("✓ Meeting request generation")
    print("✓ Complete outreach sequences")
    print("✓ Batch outreach for multiple prospects")
    print("✓ Personalization scoring")
    print("✓ Timeline planning")
    print("\nOutputs: Cold emails, LinkedIn messages, Follow-ups, Meeting requests")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_outreach_agent()
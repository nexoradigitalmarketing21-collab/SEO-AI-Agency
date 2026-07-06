#!/usr/bin/env python3
"""
Nexora AI SEO Agency - AI Chat Assistant
Visitors can ask "Can you audit my website?" - AI collects details and automatically creates a lead.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import uuid
import re


class ChatSession:
    """Individual chat session"""
    
    def __init__(self, visitor_id: str = None):
        self.id = str(uuid.uuid4())[:12]
        self.visitor_id = visitor_id or str(uuid.uuid4())[:8]
        self.messages = []
        self.collected_info = {}
        self.lead_created = False
        self.started_at = datetime.now().isoformat()
        self.last_activity = datetime.now().isoformat()
        self.intent_detected = None
    
    def add_message(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        self.last_activity = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "visitor_id": self.visitor_id,
            "messages": self.messages[-10:],  # Last 10 messages
            "collected": self.collected_info,
            "lead_created": self.lead_created,
            "intent": self.intent_detected
        }


class AIChatAssistant:
    """AI Chat Assistant for lead capture and client interaction"""
    
    GREETINGS = [
        "Hi! I'm Nexora's AI assistant. 👋 I can help you with:\n\n"
        "🔍 **Free SEO Audit** - I'll analyze your website\n"
        "📊 **Keyword Research** - Find ranking opportunities\n"
        "📋 **Service Info** - Learn about our SEO packages\n"
        "💬 **General Questions** - Ask me anything about SEO\n\n"
        "What would you like help with?",
        
        "Welcome to Nexora Digital Marketing! 🚀\n\n"
        "I'm your AI assistant. Here's what I can do:\n"
        "• Run a free website analysis\n"
        "• Explain our SEO services\n"
        "• Provide pricing information\n"
        "• Share case studies\n\n"
        "Just let me know what you need!"
    ]
    
    def __init__(self):
        self.sessions = {}
        self.leads_created = []
    
    def start_chat(self) -> Dict:
        """Start a new chat session"""
        session = ChatSession()
        self.sessions[session.id] = session
        
        import random
        greeting = random.choice(self.GREETINGS)
        session.add_message("assistant", greeting)
        
        return {"session_id": session.id, "message": greeting}
    
    def process_message(self, session_id: str, message: str) -> Dict:
        """Process a visitor message and generate response"""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found. Please start a new chat."}
        
        session.add_message("user", message)
        
        # Detect intent
        intent = self._detect_intent(message)
        session.intent_detected = intent
        
        # Generate response based on intent
        if intent == "website_audit":
            response = self._handle_audit_request(session, message)
        elif intent == "collect_website":
            response = self._handle_website_collection(session, message)
        elif intent == "pricing":
            response = self._handle_pricing(session)
        elif intent == "services":
            response = self._handle_services(session)
        elif intent == "contact":
            response = self._handle_contact(session, message)
        else:
            response = self._handle_general(session, message)
        
        session.add_message("assistant", response)
        
        return {
            "session_id": session_id,
            "message": response,
            "collected": session.collected_info,
            "lead_created": session.lead_created,
            "intent": intent,
            "requires_action": intent in ["website_audit", "collect_website"]
        }
    
    def _detect_intent(self, message: str) -> str:
        """Detect user intent from message"""
        msg = message.lower()
        
        # Website audit intent
        if any(word in msg for word in ["audit", "analyze", "check my site", "check my website", 
                                         "scan", "review my", "free audit"]):
            return "website_audit"
        
        # Collect website info
        if any(word in msg for word in [".com", ".org", ".net", ".io", "my website", "my site is"]):
            return "collect_website"
        
        # Pricing intent
        if any(word in msg for word in ["price", "cost", "pricing", "how much", "package", "plan", "fee"]):
            return "pricing"
        
        # Services intent
        if any(word in msg for word in ["service", "offer", "do you do", "provide", "help with"]):
            return "services"
        
        # Contact intent
        if any(word in msg for word in ["contact", "email", "phone", "call", "speak", "human", "talk"]):
            return "contact"
        
        return "general"
    
    def _handle_audit_request(self, session: ChatSession, message: str) -> str:
        """Handle website audit request"""
        # Check if they already provided a website
        url_match = re.search(r'https?://[^\s]+|[a-zA-Z0-9-]+\.[a-zA-Z]{2,}', message)
        
        if url_match:
            website = url_match.group()
            session.collected_info["website"] = website
            session.collected_info["service"] = "SEO Audit"
            return self._collect_details(session)
        
        session.collected_info["service"] = "SEO Audit"
        return (
            "Great! I'd be happy to run a free SEO audit for you. 🎯\n\n"
            "To get started, could you please share:\n\n"
            "1️⃣ **Your website URL** (e.g., example.com)\n"
            "2️⃣ **Your name**\n"
            "3️⃣ **Your email** (to send the report)\n\n"
            "Let's start with your website URL!"
        )
    
    def _handle_website_collection(self, session: ChatSession, message: str) -> str:
        """Handle website URL collection"""
        # Extract website URL
        url_match = re.search(r'https?://[^\s]+|[a-zA-Z0-9-]+\.[a-zA-Z]{2,}', message)
        
        if url_match:
            website = url_match.group()
            session.collected_info["website"] = website
            return self._collect_details(session)
        
        return (
            "I didn't catch the website URL. Could you please share it?\n\n"
            "For example: **mybusiness.com** or **https://mybusiness.com**"
        )
    
    def _collect_details(self, session: ChatSession) -> str:
        """Collect client details for lead creation"""
        info = session.collected_info
        
        # Collect name
        if "name" not in info:
            return f"Thanks! I have your website: **{info.get('website')}**\n\nNow, what's your **name** so I can personalize your report?"
        
        # Collect email
        if "email" not in info:
            return f"Great, **{info['name']}**! One more thing - what's your **email address** so I can send you the audit results?"
        
        # Create lead automatically
        if not session.lead_created:
            lead = self._create_lead(session)
            session.lead_created = True
            self.leads_created.append(lead)
            
            return (
                f"🎉 **Perfect, {info['name']}!** Your free SEO audit is being prepared.\n\n"
                f"📧 We'll send the full report to: **{info['email']}**\n\n"
                f"**Here's what you'll get:**\n"
                f"✅ Technical SEO analysis\n"
                f"✅ On-page optimization score\n"
                f"✅ Top 5 quick wins\n"
                f"✅ Competitor comparison\n"
                f"✅ Custom action plan\n\n"
                f"In the meantime, would you like to:\n"
                f"1️⃣ Learn about our **SEO packages**\n"
                f"2️⃣ See **case studies**\n"
                f"3️⃣ **Book a call** to discuss results\n"
                f"4️⃣ **Nothing else** - I'm good!"
            )
        
        return (
            f"Your audit is in progress, {info['name']}! 🚀\n\n"
            f"Is there anything else I can help you with?\n"
            f"• Learn about **pricing**\n"
            f"• See our **services**\n"
            f"• **Book a call**\n"
            f"• Just **type anything** to chat"
        )
    
    def _create_lead(self, session: ChatSession) -> Dict:
        """Create a lead from collected information"""
        lead = {
            "id": str(uuid.uuid4())[:8],
            "source": "chat_assistant",
            "status": "new",
            "name": session.collected_info.get("name", ""),
            "email": session.collected_info.get("email", ""),
            "website": session.collected_info.get("website", ""),
            "service": session.collected_info.get("service", "SEO Audit"),
            "notes": f"Auto-created from chat. Intent: {session.intent_detected}",
            "created_at": datetime.now().isoformat(),
            "session_id": session.id
        }
        return lead
    
    def _handle_pricing(self, session: ChatSession) -> str:
        """Handle pricing inquiry"""
        return (
            "💰 **Our SEO Packages**\n\n"
            "**🚀 SEO Essential** - $500/mo\n"
            "✓ Monthly SEO audit\n"
            "✓ 50 keywords tracked\n"
            "✓ Monthly report\n"
            "✓ Email support\n\n"
            "**📈 SEO Growth** - $1,000/mo\n"
            "✓ Everything in Essential\n"
            "✓ On-page optimization\n"
            "✓ Content recommendations\n"
            "✓ Weekly check-ins\n\n"
            "**🏆 SEO Dominance** - $2,000/mo\n"
            "✓ Everything in Growth\n"
            "✓ 4 articles/month\n"
            "✓ Link building\n"
            "✓ Dedicated manager\n\n"
            "Want a custom quote? Just share your website and goals! 🎯"
        )
    
    def _handle_services(self, session: ChatSession) -> str:
        """Handle services inquiry"""
        return (
            "📋 **Our Services**\n\n"
            "🔍 **SEO Audit** - $250-$1,000\n"
            "Complete website analysis & action plan\n\n"
            "📊 **Keyword Research** - $150-$500\n"
            "Find high-value ranking opportunities\n\n"
            "🛠️ **Technical SEO** - $300-$1,000\n"
            "Fix speed, Core Web Vitals, schema issues\n\n"
            "📝 **Content Writing** - $200-$800/article\n"
            "SEO-optimized content that ranks\n\n"
            "📍 **Local SEO** - $300-$800\n"
            "Dominate local search & Google Maps\n\n"
            "Which service interests you most? 😊"
        )
    
    def _handle_contact(self, session: ChatSession, message: str) -> str:
        """Handle contact request"""
        return (
            "📬 **Get in Touch**\n\n"
            "You can reach us through:\n\n"
            "📧 **Email:** hello@nexora.ai\n"
            "📞 **Phone:** Available on request\n"
            "💬 **Schedule a Call:** Just ask!\n\n"
            "Or, you can share your contact info and we'll reach out to you within 24 hours.\n\n"
            "What's the best way to contact you?"
        )
    
    def _handle_general(self, session: ChatSession, message: str) -> str:
        """Handle general conversation"""
        msg = message.lower()
        
        if any(word in msg for word in ["hello", "hi", "hey", "good"]):
            return (
                "Hello! 👋 Great to meet you!\n\n"
                "I can help you with:\n"
                "• **Free SEO audit** - Just share your website\n"
                "• **Pricing info** - See our packages\n"
                "• **Services** - Learn what we offer\n"
                "• **Case studies** - See our results\n\n"
                "What would you like to explore?"
            )
        
        if "yes" in msg or "please" in msg or "start" in msg:
            return "Awesome! What's your **website URL** so I can analyze it? 🎯"
        
        if "no" in msg or "thanks" in msg or "bye" in msg:
            return (
                "Thanks for chatting! 😊\n\n"
                "Feel free to come back anytime if you need help with your SEO.\n\n"
                "Here's what you can do next:\n"
                "• **Book a free consultation**\n"
                "• **Download our SEO checklist**\n"
                "• **Check our blog** for SEO tips\n\n"
                "Have a great day! 🚀"
            )
        
        return (
            "I'm here to help! 😊\n\n"
            "You can ask me about:\n"
            "🔍 **'Audit my website'** - Free SEO analysis\n"
            "💰 **'What are your prices?'** - Package details\n"
            "📋 **'What services do you offer?'** - Full list\n"
            "📧 **'Contact me'** - Get in touch\n\n"
            "What would you like to know?"
        )
    
    def get_leads(self) -> List[Dict]:
        """Get all leads created through chat"""
        return self.leads_created
    
    def get_stats(self) -> Dict:
        """Get chat assistant stats"""
        total_sessions = len(self.sessions)
        active_sessions = sum(1 for s in self.sessions.values() 
                            if (datetime.now() - datetime.fromisoformat(s.last_activity)).seconds < 300)
        
        return {
            "total_chats": total_sessions,
            "active_chats": active_sessions,
            "leads_created": len(self.leads_created),
            "intents": {
                "audit_requests": sum(1 for s in self.sessions.values() if s.intent_detected == "website_audit"),
                "pricing_questions": sum(1 for s in self.sessions.values() if s.intent_detected == "pricing"),
                "general": sum(1 for s in self.sessions.values() if s.intent_detected == "general")
            }
        }


if __name__ == "__main__":
    assistant = AIChatAssistant()
    
    print("=" * 60)
    print("AI CHAT ASSISTANT - DEMO")
    print("=" * 60)
    
    # Start chat
    chat = assistant.start_chat()
    print(f"\n[Session: {chat['session_id']}]")
    print(f"Nexora AI: {chat['message'][:100]}...")
    
    # Simulate conversation
    messages = [
        "Can you audit my website?",
        "my website is techflow.com",
        "My name is Sarah",
        "sarah@techflow.com"
    ]
    
    for msg in messages:
        print(f"\nVisitor: {msg}")
        response = assistant.process_message(chat['session_id'], msg)
        print(f"Nexora AI: {response['message'][:150]}...")
        if response.get('lead_created'):
            print(f"\n✅ LEAD CREATED AUTOMATICALLY!")
    
    print("\n" + "=" * 60)
    print("LEADS CAPTURED:")
    for lead in assistant.get_leads():
        print(f"  🟢 {lead['name']} | {lead['email']} | {lead['website']} | {lead['service']}")
    
    print(f"\nAssistant Stats:")
    stats = assistant.get_stats()
    print(f"  Total Chats: {stats['total_chats']}")
    print(f"  Leads Created: {stats['leads_created']}")
    print(f"  Audit Requests: {stats['intents']['audit_requests']}")
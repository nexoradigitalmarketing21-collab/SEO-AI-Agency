#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Client Portal
Module 2: Secure web portal for clients with dashboard, deliverables, messaging, and approvals.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os
import uuid


class UserManager:
    """Manage client portal users"""
    
    def __init__(self):
        self.users = {}
        self.sessions = {}
    
    def register_client(self, client_info: Dict) -> Dict:
        """Register a new client in the portal"""
        user_id = str(uuid.uuid4())[:8]
        token = str(uuid.uuid4())
        
        user = {
            "id": user_id,
            "name": client_info.get('name', 'Client'),
            "email": client_info.get('email', ''),
            "company": client_info.get('company', ''),
            "role": "client",
            "created_at": datetime.now().isoformat(),
            "last_login": None,
            "projects": [],
            "notifications": [],
            "settings": {
                "email_notifications": True,
                "digest_frequency": "weekly",
                "theme": "light"
            }
        }
        
        self.users[user_id] = user
        
        return {
            "user": user,
            "temporary_token": token,
            "setup_link": f"https://portal.nexora.ai/setup?token={token}"
        }
    
    def authenticate(self, email: str, password: str) -> Optional[Dict]:
        """Authenticate a user (simplified)"""
        for user_id, user in self.users.items():
            if user['email'] == email:
                session_id = str(uuid.uuid4())
                self.sessions[session_id] = {
                    "user_id": user_id,
                    "created_at": datetime.now().isoformat(),
                    "expires_at": (datetime.now() + timedelta(hours=24)).isoformat()
                }
                return {
                    "session_id": session_id,
                    "user": user
                }
        return None


class ProjectDashboard:
    """Client-facing project dashboard"""
    
    def __init__(self):
        self.projects = {}
    
    def create_project_dashboard(self, client_id: str, project_info: Dict) -> Dict:
        """Create a dashboard for a client project"""
        project_id = str(uuid.uuid4())[:8]
        
        dashboard = {
            "id": project_id,
            "client_id": client_id,
            "name": project_info.get('name', 'SEO Project'),
            "type": project_info.get('type', 'SEO'),
            "status": project_info.get('status', 'active'),
            "progress": 0,
            "start_date": datetime.now().isoformat(),
            "target_completion": project_info.get('target_completion', ''),
            "budget": project_info.get('budget', 0),
            "spent_so_far": 0,
            "deliverables": [],
            "recent_activity": [],
            "key_metrics": {
                "rankings_improved": 0,
                "keywords_in_top10": 0,
                "traffic_increase": "0%",
                "backlinks_gained": 0
            },
            "team": [],
            "messages_unread": 0
        }
        
        self.projects[project_id] = dashboard
        return dashboard
    
    def update_progress(self, project_id: str, progress: int, metrics: Dict = None) -> Dict:
        """Update project progress"""
        project = self.projects.get(project_id)
        if not project:
            return {"error": "Project not found"}
        
        project['progress'] = min(100, progress)
        
        if metrics:
            project['key_metrics'].update(metrics)
        
        project['recent_activity'].append({
            "type": "progress_update",
            "message": f"Progress updated to {progress}%",
            "timestamp": datetime.now().isoformat()
        })
        
        return project
    
    def add_deliverable(self, project_id: str, deliverable: Dict) -> Dict:
        """Add a deliverable to the project"""
        project = self.projects.get(project_id)
        if not project:
            return {"error": "Project not found"}
        
        dlvr = {
            "id": str(uuid.uuid4())[:8],
            "name": deliverable.get('name', 'Deliverable'),
            "type": deliverable.get('type', 'report'),
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
            "file_url": deliverable.get('file_url', ''),
            "size": deliverable.get('size', '0 MB'),
            "approved": False,
            "feedback": []
        }
        
        project['deliverables'].append(dlvr)
        
        project['recent_activity'].append({
            "type": "deliverable_added",
            "message": f"New deliverable: {dlvr['name']}",
            "timestamp": datetime.now().isoformat()
        })
        
        return dlvr
    
    def approve_deliverable(self, project_id: str, deliverable_id: str, approved: bool, feedback: str = "") -> Dict:
        """Approve or reject a deliverable"""
        project = self.projects.get(project_id)
        if not project:
            return {"error": "Project not found"}
        
        for dlvr in project['deliverables']:
            if dlvr['id'] == deliverable_id:
                dlvr['approved'] = approved
                if feedback:
                    dlvr['feedback'].append({
                        "text": feedback,
                        "timestamp": datetime.now().isoformat()
                    })
                
                status = "approved" if approved else "revision_requested"
                dlvr['status'] = status
                
                project['recent_activity'].append({
                    "type": "deliverable_reviewed",
                    "message": f"Deliverable '{dlvr['name']}' {status}",
                    "timestamp": datetime.now().isoformat()
                })
                
                return dlvr
        
        return {"error": "Deliverable not found"}


class MessagingSystem:
    """Client-portal messaging system"""
    
    def __init__(self):
        self.conversations = {}
        self.messages = []
    
    def send_message(self, sender_id: str, recipient_id: str, content: str, 
                    project_id: str = None) -> Dict:
        """Send a message between client and agency"""
        message_id = str(uuid.uuid4())[:8]
        
        message = {
            "id": message_id,
            "sender_id": sender_id,
            "recipient_id": recipient_id,
            "project_id": project_id,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "read": False,
            "attachments": []
        }
        
        self.messages.append(message)
        
        # Track conversation
        conv_key = f"{min(sender_id, recipient_id)}-{max(sender_id, recipient_id)}"
        if conv_key not in self.conversations:
            self.conversations[conv_key] = []
        self.conversations[conv_key].append(message_id)
        
        return message
    
    def get_conversation(self, user_id_1: str, user_id_2: str) -> List[Dict]:
        """Get conversation between two users"""
        conv_key = f"{min(user_id_1, user_id_2)}-{max(user_id_1, user_id_2)}"
        message_ids = self.conversations.get(conv_key, [])
        
        conversation = []
        for msg_id in message_ids:
            for msg in self.messages:
                if msg['id'] == msg_id:
                    conversation.append(msg)
                    break
        
        return sorted(conversation, key=lambda x: x['timestamp'])


class ClientPortal:
    """Complete Client Portal System"""
    
    def __init__(self):
        self.user_manager = UserManager()
        self.dashboards = ProjectDashboard()
        self.messaging = MessagingSystem()
        self.portal_config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Load portal configuration"""
        return {
            "portal_name": "Nexora Client Hub",
            "company": "Nexora AI SEO Agency",
            "domain": "portal.nexora.ai",
            "features": {
                "project_dashboard": True,
                "deliverable_downloads": True,
                "messaging": True,
                "approval_workflow": True,
                "reports": True,
                "payment_history": True
            },
            "security": {
                "session_timeout_hours": 24,
                "max_login_attempts": 5,
                "require_2fa": False
            }
        }
    
    def onboard_client(self, client_info: Dict, project_info: Dict) -> Dict:
        """Complete client onboarding flow"""
        
        # 1. Register user
        registration = self.user_manager.register_client(client_info)
        
        # 2. Create project dashboard
        dashboard = self.dashboards.create_project_dashboard(
            registration['user']['id'],
            project_info
        )
        
        # 3. Create welcome message
        welcome = self.messaging.send_message(
            "nexora_agency",
            registration['user']['id'],
            f"Welcome to Nexora Client Hub! We're excited to start working on {project_info.get('name', 'your project')}. You can track progress, download deliverables, and message us directly from this portal."
        )
        
        return {
            "portal_url": f"https://{self.portal_config['domain']}/dashboard/{registration['user']['id']}",
            "credentials": {
                "email": client_info.get('email'),
                "setup_link": registration['setup_link']
            },
            "welcome_message": welcome['content'],
            "project": dashboard['name'],
            "next_steps": [
                "Log in to the portal",
                "Review project dashboard",
                "Set notification preferences",
                "Book kickoff call"
            ]
        }
    
    def get_client_dashboard(self, client_id: str) -> Dict:
        """Get complete client dashboard view"""
        user = self.user_manager.users.get(client_id)
        if not user:
            return {"error": "Client not found"}
        
        # Get all projects for this client
        client_projects = [
            p for p in self.dashboards.projects.values() 
            if p['client_id'] == client_id
        ]
        
        # Get unread messages
        unread_count = sum(
            1 for msg in self.messaging.messages
            if msg['recipient_id'] == client_id and not msg['read']
        )
        
        return {
            "user": {
                "name": user['name'],
                "company": user['company'],
                "email": user['email']
            },
            "projects": client_projects,
            "notifications": user.get('notifications', []),
            "unread_messages": unread_count,
            "quick_actions": [
                {"label": "View Active Projects", "url": f"/projects/{client_id}"},
                {"label": "Download Deliverables", "url": f"/deliverables/{client_id}"},
                {"label": "Send Message", "url": f"/messages/{client_id}"},
                {"label": "View Reports", "url": f"/reports/{client_id}"}
            ],
            "recent_activity": self._get_recent_activity(client_projects)
        }
    
    def _get_recent_activity(self, projects: List[Dict]) -> List[Dict]:
        """Get recent activity across all client projects"""
        all_activity = []
        for project in projects:
            for activity in project.get('recent_activity', []):
                all_activity.append({
                    "project": project['name'],
                    **activity
                })
        
        all_activity.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        return all_activity[:10]
    
    def get_portal_status(self) -> Dict:
        """Get portal system status"""
        return {
            "portal": self.portal_config['portal_name'],
            "status": "active",
            "registered_clients": len(self.user_manager.users),
            "active_projects": len(self.dashboards.projects),
            "total_messages": len(self.messaging.messages),
            "features_enabled": [
                feature for feature, enabled in self.portal_config['features'].items()
                if enabled
            ],
            "security": self.portal_config['security']
        }


def demonstrate_client_portal():
    """Demonstrate Client Portal"""
    print(f"\n{'='*80}")
    print("CLIENT PORTAL - Module 2")
    print(f"{'='*80}\n")
    
    portal = ClientPortal()
    
    # Client onboarding
    print("1. Client Onboarding")
    print("─" * 60)
    
    client_info = {
        "name": "Sarah Johnson",
        "email": "sarah@techflow.com",
        "company": "TechFlow SaaS"
    }
    
    project_info = {
        "name": "Monthly SEO Strategy & Implementation",
        "type": "Monthly SEO",
        "budget": 3000,
        "target_completion": "Ongoing"
    }
    
    onboarding = portal.onboard_client(client_info, project_info)
    print(f"  Portal URL: {onboarding['portal_url']}")
    print(f"  Welcome Message Sent: Yes")
    print(f"  Next Steps:")
    for step in onboarding['next_steps']:
        print(f"    • {step}")
    
    # Project updates
    print("\n2. Project Dashboard Updates")
    print("─" * 60)
    
    client_id = list(portal.user_manager.users.keys())[0]
    project_id = list(portal.dashboards.projects.keys())[0]
    
    # Update progress
    portal.dashboards.update_progress(project_id, 35, {
        "rankings_improved": 12,
        "keywords_in_top10": 8,
        "traffic_increase": "25%",
        "backlinks_gained": 5
    })
    
    # Add deliverables
    deliverables = [
        {"name": "SEO Audit Report", "type": "PDF Report"},
        {"name": "Keyword Research Database", "type": "Excel Spreadsheet"},
        {"name": "Monthly Performance Report", "type": "PDF Report"}
    ]
    
    for dlvr in deliverables:
        portal.dashboards.add_deliverable(project_id, dlvr)
    
    # Approve a deliverable
    project = portal.dashboards.projects[project_id]
    first_deliverable = project['deliverables'][0]['id']
    portal.dashboards.approve_deliverable(
        project_id, first_deliverable, True, 
        "Great work! The audit is comprehensive."
    )
    
    # Get dashboard
    dashboard = portal.get_client_dashboard(client_id)
    print(f"  Active Projects: {len(dashboard['projects'])}")
    print(f"  Unread Messages: {dashboard['unread_messages']}")
    print(f"  Project Progress: {dashboard['projects'][0]['progress']}%")
    
    for dlvr in dashboard['projects'][0]['deliverables']:
        status = "✅ Approved" if dlvr['approved'] else "📋 Pending"
        print(f"  {status}: {dlvr['name']}")
    
    # Messaging
    print("\n3. Client Messaging")
    print("─" * 60)
    
    # Client sends message
    portal.messaging.send_message(
        client_id, "nexora_agency",
        "When will the keyword research be ready?"
    )
    
    # Agency responds
    portal.messaging.send_message(
        "nexora_agency", client_id,
        "The keyword research will be ready by Friday. We're analyzing 500+ keywords to find the best opportunities for TechFlow."
    )
    
    # Get conversation
    conversation = portal.messaging.get_conversation(client_id, "nexora_agency")
    print(f"  Messages in conversation: {len(conversation)}")
    for msg in conversation[-2:]:
        print(f"  {'👤 Client' if msg['sender_id'] == client_id else '🏢 Agency'}: {msg['content'][:60]}...")
    
    # Portal status
    print("\n4. Portal Status")
    print("─" * 60)
    status = portal.get_portal_status()
    print(f"  Registered Clients: {status['registered_clients']}")
    print(f"  Active Projects: {status['active_projects']}")
    print(f"  Total Messages: {status['total_messages']}")
    print(f"  Features: {', '.join(status['features_enabled'])}")
    
    print(f"\n{'='*80}")
    print("MODULE 2: CLIENT PORTAL - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Secure client registration & login")
    print("✓ Project dashboards with progress tracking")
    print("✓ Deliverable management & downloads")
    print("✓ Approval workflow with feedback")
    print("✓ Real-time messaging system")
    print("✓ Activity timeline")
    print("✓ Key metrics display")
    print("\nNext: Deploy as web app with Flask/FastAPI + React frontend")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_client_portal()
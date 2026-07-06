#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Team Mode (Milestone 7)
Role-based access control for Admin, SEO Manager, Writer, Developer, Sales, VA, and Client.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import uuid


class Role:
    """Team role with specific permissions"""
    
    ROLES = {
        "admin": {
            "name": "Admin",
            "permissions": [
                "manage_team", "manage_clients", "manage_billing", "manage_settings",
                "view_analytics", "manage_all_projects", "delete_content",
                "manage_integrations", "view_revenue", "manage_automation"
            ],
            "max_clients": float('inf'),
            "can_delete": True,
            "can_manage_billing": True,
            "description": "Full system access"
        },
        "seo_manager": {
            "name": "SEO Manager",
            "permissions": [
                "manage_projects", "assign_agents", "review_deliverables",
                "manage_strategy", "view_analytics", "approve_content",
                "client_communication", "manage_keywords"
            ],
            "max_clients": 50,
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Manages SEO strategy and team"
        },
        "writer": {
            "name": "Writer",
            "permissions": [
                "create_content", "edit_content", "view_projects",
                "view_keywords", "submit_for_review"
            ],
            "max_clients": 20,
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Creates SEO-optimized content"
        },
        "developer": {
            "name": "Developer",
            "permissions": [
                "technical_seo", "fix_issues", "implement_changes",
                "view_projects", "view_analytics"
            ],
            "max_clients": 30,
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Technical SEO implementation"
        },
        "sales": {
            "name": "Sales",
            "permissions": [
                "view_leads", "manage_proposals", "send_outreach",
                "view_pricing", "create_proposals", "view_client_info"
            ],
            "max_clients": float('inf'),
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Client acquisition and sales"
        },
        "va": {
            "name": "Virtual Assistant",
            "permissions": [
                "view_projects", "view_calendar", "manage_tasks",
                "client_communication", "upload_deliverables"
            ],
            "max_clients": 10,
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Administrative support"
        },
        "client": {
            "name": "Client",
            "permissions": [
                "view_own_projects", "view_own_deliverables", "send_messages",
                "approve_deliverables", "view_own_reports", "view_invoices"
            ],
            "max_clients": 1,
            "can_delete": False,
            "can_manage_billing": False,
            "description": "Client portal access"
        }
    }


class TeamMember:
    """Individual team member"""
    
    def __init__(self, name: str, email: str, role: str):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.role = role
        self.permissions = Role.ROLES.get(role, {}).get("permissions", [])
        self.assigned_projects = []
        self.active_clients = 0
        self.is_active = True
        self.joined_at = datetime.now().isoformat()
        self.last_active = datetime.now().isoformat()
        self.performance_score = 100.0
        self.tasks_completed = 0
    
    def has_permission(self, permission: str) -> bool:
        """Check if member has a specific permission"""
        return permission in self.permissions
    
    def can_take_client(self) -> bool:
        """Check if member can take more clients"""
        role_config = Role.ROLES.get(self.role, {})
        max_clients = role_config.get("max_clients", 0)
        return self.active_clients < max_clients
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active,
            "active_clients": self.active_clients,
            "tasks_completed": self.tasks_completed,
            "performance": self.performance_score
        }


class TeamManager:
    """Team management with role-based access"""
    
    def __init__(self):
        self.members = {}
        self.activity_log = []
    
    def add_member(self, name: str, email: str, role: str) -> Dict:
        """Add a new team member"""
        if role not in Role.ROLES:
            return {"error": f"Invalid role: {role}. Valid roles: {list(Role.ROLES.keys())}"}
        
        member = TeamMember(name, email, role)
        self.members[member.id] = member
        
        self._log_activity("member_added", f"{name} joined as {role}")
        
        return member.to_dict()
    
    def assign_to_project(self, member_id: str, project_id: str) -> Dict:
        """Assign a team member to a project"""
        member = self.members.get(member_id)
        if not member:
            return {"error": "Member not found"}
        
        if not member.can_take_client():
            return {"error": "Member has reached maximum client capacity"}
        
        member.assigned_projects.append(project_id)
        member.active_clients += 1
        
        self._log_activity("assignment", f"{member.name} assigned to project {project_id}")
        
        return member.to_dict()
    
    def check_permission(self, member_id: str, permission: str) -> bool:
        """Check if a member has permission"""
        member = self.members.get(member_id)
        if not member:
            return False
        return member.has_permission(permission)
    
    def get_team_summary(self) -> Dict:
        """Get team summary"""
        return {
            "total_members": len(self.members),
            "by_role": {
                role: sum(1 for m in self.members.values() if m.role == role)
                for role in Role.ROLES
            },
            "active_members": sum(1 for m in self.members.values() if m.is_active),
            "total_clients_across_team": sum(m.active_clients for m in self.members.values()),
            "total_tasks_completed": sum(m.tasks_completed for m in self.members.values()),
            "roles_available": list(Role.ROLES.keys()),
            "recent_activity": self.activity_log[-5:]
        }
    
    def get_role_permissions(self, role: str) -> Dict:
        """Get permissions for a role"""
        role_config = Role.ROLES.get(role)
        if not role_config:
            return {"error": f"Role '{role}' not found"}
        return role_config
    
    def _log_activity(self, action: str, details: str):
        """Log team activity"""
        self.activity_log.append({
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_manager_status(self) -> Dict:
        """Get team manager status"""
        return self.get_team_summary()


if __name__ == "__main__":
    tm = TeamManager()
    
    # Add team members
    tm.add_member("Alex CEO", "alex@agency.com", "admin")
    tm.add_member("Sarah Strategist", "sarah@agency.com", "seo_manager")
    tm.add_member("Mike Writer", "mike@agency.com", "writer")
    tm.add_member("Dev Dave", "dave@agency.com", "developer")
    tm.add_member("Sally Sales", "sally@agency.com", "sales")
    
    print("Team Manager Status:")
    summary = tm.get_team_summary()
    print(f"  Total Members: {summary['total_members']}")
    print(f"  By Role:")
    for role, count in summary['by_role'].items():
        if count > 0:
            print(f"    {role:15s}: {count}")
    print(f"\n  Permissions by Role:")
    for role in ["admin", "seo_manager", "writer", "client"]:
        config = tm.get_role_permissions(role)
        print(f"    {role:15s}: {len(config['permissions'])} permissions - {config['description']}")
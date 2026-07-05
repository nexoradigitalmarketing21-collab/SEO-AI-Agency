#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Client Intake System
Automated client onboarding and project creation.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import json
import os

@dataclass
class ClientIntake:
    """Client intake data structure"""
    # Business Information
    client_name: str
    company_name: str
    website: str
    industry: str
    contact_email: str
    contact_phone: str
    
    # Project Details
    services_required: List[str]
    budget: str
    timeline: str
    target_country: str
    competitors: List[str]
    
    # Metadata
    intake_date: datetime
    intake_id: str
    status: str
    assigned_to: str

class ClientIntakeSystem:
    """Automated client intake and project creation system"""
    
    def __init__(self):
        self.intakes = []
        self.project_counter = 1
        
    def create_intake_form(self) -> dict:
        """Generate standardized intake form"""
        return {
            "form_title": "Nexora AI SEO Agency - Client Intake Form",
            "sections": {
                "business_information": {
                    "title": "Business Information",
                    "fields": [
                        {"name": "client_name", "type": "text", "required": True, "label": "Your Name"},
                        {"name": "company_name", "type": "text", "required": True, "label": "Company Name"},
                        {"name": "website", "type": "url", "required": True, "label": "Website URL"},
                        {"name": "industry", "type": "text", "required": True, "label": "Industry"},
                        {"name": "contact_email", "type": "email", "required": True, "label": "Email Address"},
                        {"name": "contact_phone", "type": "tel", "required": True, "label": "Phone Number"}
                    ]
                },
                "project_details": {
                    "title": "Project Details",
                    "fields": [
                        {"name": "services_required", "type": "multiselect", "required": True, 
                         "label": "Services Required", 
                         "options": ["SEO Audit", "Keyword Research", "Technical SEO", 
                                    "Content Writing", "Monthly SEO", "Local SEO", "Link Building"]},
                        {"name": "budget", "type": "select", "required": True,
                         "label": "Budget Range",
                         "options": ["$1,000-$2,500", "$2,500-$5,000", "$5,000-$10,000", 
                                    "$10,000-$25,000", "$25,000+", "Not sure"]},
                        {"name": "timeline", "type": "select", "required": True,
                         "label": "Timeline",
                         "options": ["ASAP", "Within 2 weeks", "Within 1 month", 
                                    "Within 3 months", "Flexible"]},
                        {"name": "target_country", "type": "text", "required": True, 
                         "label": "Target Country/Market"},
                        {"name": "competitors", "type": "textarea", "required": False,
                         "label": "Main Competitors (one per line)"}
                    ]
                },
                "additional_info": {
                    "title": "Additional Information",
                    "fields": [
                        {"name": "current_seo", "type": "textarea", "required": False,
                         "label": "Current SEO Situation"},
                        {"name": "goals", "type": "textarea", "required": True,
                         "label": "Business Goals"},
                        {"name": "challenges", "type": "textarea", "required": False,
                         "label": "Current Challenges"}
                    ]
                }
            }
        }
    
    def process_intake(self, form_data: dict) -> ClientIntake:
        """Process submitted intake form"""
        intake_id = f"INT-{datetime.now().strftime('%Y%m%d')}-{self.project_counter:04d}"
        
        intake = ClientIntake(
            client_name=form_data.get('client_name', ''),
            company_name=form_data.get('company_name', ''),
            website=form_data.get('website', ''),
            industry=form_data.get('industry', ''),
            contact_email=form_data.get('contact_email', ''),
            contact_phone=form_data.get('contact_phone', ''),
            services_required=form_data.get('services_required', []),
            budget=form_data.get('budget', ''),
            timeline=form_data.get('timeline', ''),
            target_country=form_data.get('target_country', ''),
            competitors=form_data.get('competitors', '').split('\n') if form_data.get('competitors') else [],
            intake_date=datetime.now(),
            intake_id=intake_id,
            status="New",
            assigned_to="Sales Agent"
        )
        
        self.intakes.append(intake)
        self.project_counter += 1
        
        # Auto-create project structure
        self.create_client_workspace(intake)
        
        # Notify Sales Agent
        self.notify_sales_agent(intake)
        
        return intake
    
    def create_client_workspace(self, intake: ClientIntake):
        """Automatically create client workspace folder structure"""
        client_folder = f"clients/{intake.company_name.replace(' ', '_')}"
        
        folders = [
            "01 Intake",
            "02 Audit",
            "03 Keywords",
            "04 Content",
            "05 Reports",
            "06 Deliverables",
            "07 Invoices",
            "08 Assets"
        ]
        
        for folder in folders:
            folder_path = os.path.join(client_folder, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Create README in each folder
            readme_path = os.path.join(folder_path, "README.md")
            with open(readme_path, 'w') as f:
                f.write(f"# {folder}\n\nThis folder contains {folder.lower()} files for {intake.company_name}.\n")
        
        # Create intake summary
        intake_file = os.path.join(client_folder, "01 Intake", f"{intake.intake_id}_intake_summary.md")
        with open(intake_file, 'w') as f:
            f.write(self.generate_intake_summary(intake))
        
        print(f"✓ Created client workspace: {client_folder}")
    
    def generate_intake_summary(self, intake: ClientIntake) -> str:
        """Generate intake summary document"""
        return f"""# Client Intake Summary

**Intake ID:** {intake.intake_id}
**Date:** {intake.intake_date.strftime('%Y-%m-%d %H:%M')}
**Status:** {intake.status}

## Business Information

- **Client Name:** {intake.client_name}
- **Company Name:** {intake.company_name}
- **Website:** {intake.website}
- **Industry:** {intake.industry}
- **Contact Email:** {intake.contact_email}
- **Contact Phone:** {intake.contact_phone}

## Project Details

**Services Required:**
{chr(10).join(['- ' + service for service in intake.services_required])}

**Budget:** {intake.budget}
**Timeline:** {intake.timeline}
**Target Country:** {intake.target_country}

**Competitors:**
{chr(10).join(['- ' + comp for comp in intake.competitors]) if intake.competitors else '- None specified'}

## Next Steps

1. [ ] Sales Agent to contact client within 24 hours
2. [ ] Schedule discovery call
3. [ ] Create proposal
4. [ ] Send agreement
5. [ ] Begin project

## Assigned To

**Sales Agent:** {intake.assigned_to}

---

**Created:** {intake.intake_date.strftime('%Y-%m-%d %H:%M')}
"""
    
    def notify_sales_agent(self, intake: ClientIntake):
        """Notify Sales Agent of new intake"""
        notification = f"""
╔══════════════════════════════════════════════════════════════╗
║                    NEW CLIENT INTAKE                         ║
╚══════════════════════════════════════════════════════════════╝

Intake ID: {intake.intake_id}
Client: {intake.client_name} ({intake.company_name})
Website: {intake.website}
Services: {', '.join(intake.services_required)}
Budget: {intake.budget}
Timeline: {intake.timeline}

ACTION REQUIRED: Contact client within 24 hours

Client workspace created at: clients/{intake.company_name.replace(' ', '_')}/
"""
        print(notification)
        
        # In production, this would send to actual agent
        # For now, we log it
        with open('logs/intake-notifications.log', 'a') as f:
            f.write(f"{datetime.now()} - New intake: {intake.intake_id} - {intake.company_name}\n")
    
    def get_intake_stats(self) -> dict:
        """Get intake statistics"""
        total = len(self.intakes)
        by_status = {}
        by_service = {}
        
        for intake in self.intakes:
            # By status
            status = intake.status
            by_status[status] = by_status.get(status, 0) + 1
            
            # By service
            for service in intake.services_required:
                by_service[service] = by_service.get(service, 0) + 1
        
        return {
            "total_intakes": total,
            "by_status": by_status,
            "by_service": by_service,
            "conversion_rate": "Calculate based on won vs lost"
        }


def demonstrate_intake_system():
    """Demonstrate the client intake system"""
    print("\n" + "="*80)
    print("CLIENT INTAKE SYSTEM DEMONSTRATION")
    print("="*80 + "\n")
    
    intake_system = ClientIntakeSystem()
    
    # Sample intake data
    sample_intake = {
        'client_name': 'John Smith',
        'company_name': 'TechStart Solutions',
        'website': 'https://techstartsolutions.com',
        'industry': 'SaaS / Technology',
        'contact_email': 'john@techstartsolutions.com',
        'contact_phone': '+1-555-0123',
        'services_required': ['SEO Audit', 'Keyword Research', 'Technical SEO'],
        'budget': '$5,000-$10,000',
        'timeline': 'Within 1 month',
        'target_country': 'United States',
        'competitors': 'competitor1.com\ncompetitor2.com\ncompetitor3.com'
    }
    
    print("Step 1: Client submits intake form")
    print("-" * 80)
    print(f"Client: {sample_intake['client_name']}")
    print(f"Company: {sample_intake['company_name']}")
    print(f"Services: {', '.join(sample_intake['services_required'])}")
    print(f"Budget: {sample_intake['budget']}")
    
    print("\nStep 2: Processing intake...")
    print("-" * 80)
    intake = intake_system.process_intake(sample_intake)
    
    print(f"\n✓ Intake created: {intake.intake_id}")
    print(f"✓ Client workspace created")
    print(f"✓ Sales Agent notified")
    
    print("\nStep 3: Intake Summary")
    print("-" * 80)
    print(intake_system.generate_intake_summary(intake))
    
    print("\n" + "="*80)
    print("INTAKE SYSTEM READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Standardized intake form")
    print("✓ Automatic project creation")
    print("✓ Client workspace setup")
    print("✓ Sales Agent notification")
    print("✓ Intake tracking and statistics")
    print("\n")


if __name__ == "__main__":
    demonstrate_intake_system()
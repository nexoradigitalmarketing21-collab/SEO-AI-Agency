#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Client Workspace Automation
Automated project setup and file management.
"""

from typing import Dict, List, Optional
from datetime import datetime
import os
import shutil

class ClientWorkspaceManager:
    """Manages client workspace creation and automation"""
    
    def __init__(self, base_path: str = "clients"):
        self.base_path = base_path
        self.workspace_structure = {
            "01 Intake": [
                "client-brief.md",
                "discovery-call-notes.md",
                "questionnaire-responses.md",
                "access-credentials.md",
                "contract-signed.pdf",
                "onboarding-checklist.md",
                "proposals/",
                "contracts/",
                "invoices/"
            ],
            "02 Audit": [
                "technical-audit-report.md",
                "seo-audit-report.md",
                "audit-presentation.pdf",
                "audit-summary.md",
                "priority-issues.md",
                "crawl-data/",
                "screenshots/",
                "data/",
                "competitors/"
            ],
            "03 Keywords": [
                "keyword-database.xlsx",
                "keyword-research-report.md",
                "content-roadmap.md",
                "keyword-prioritization.md",
                "competitor-keywords.md",
                "databases/",
                "analysis/",
                "opportunities/"
            ],
            "04 Strategy": [
                "seo-strategy.md",
                "content-strategy.md",
                "link-building-strategy.md",
                "local-seo-strategy.md",
                "implementation-roadmap.md",
                "kpi-dashboard.md",
                "presentations/",
                "roadmaps/",
                "metrics/"
            ],
            "05 Content": [
                "content-calendar.md",
                "content-guidelines.md",
                "briefs/",
                "drafts/",
                "published/",
                "images/"
            ],
            "06 Reports": [
                "performance-dashboard.md",
                "rank-tracking.md",
                "traffic-analysis.md",
                "monthly/",
                "quarterly/",
                "custom/"
            ],
            "07 Deliverables": [
                "reports/",
                "presentations/",
                "documents/",
                "content/"
            ],
            "08 Assets": [
                "brand-guidelines.pdf",
                "logos/",
                "images/",
                "templates/",
                "documents/",
                "tools/"
            ]
        }
        
    def create_client_workspace(self, client_name: str, company_name: str, 
                                services: List[str], intake_data: Dict) -> Dict:
        """
        Create complete client workspace with all folders and initial files
        
        Returns workspace information
        """
        # Create safe folder name
        safe_name = company_name.replace(' ', '_').replace('/', '_')
        workspace_path = os.path.join(self.base_path, safe_name)
        
        # Create main folders
        print(f"\nCreating workspace for: {company_name}")
        print("-" * 80)
        
        for folder, contents in self.workspace_structure.items():
            folder_path = os.path.join(workspace_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Create subfolders and files
            for item in contents:
                item_path = os.path.join(folder_path, item)
                if item.endswith('/'):
                    # It's a subfolder
                    os.makedirs(item_path, exist_ok=True)
                else:
                    # It's a file - create placeholder
                    with open(item_path, 'w') as f:
                        f.write(self._get_placeholder_content(item, client_name, company_name))
            
            print(f"✓ Created: {folder}/")
        
        # Create initial documents
        self._create_initial_documents(workspace_path, client_name, company_name, 
                                       services, intake_data)
        
        # Create project metadata
        metadata = self._create_project_metadata(client_name, company_name, services, intake_data)
        metadata_path = os.path.join(workspace_path, "project-metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"\n✓ Workspace created: {workspace_path}")
        
        return {
            "workspace_path": workspace_path,
            "client_name": client_name,
            "company_name": company_name,
            "services": services,
            "created_at": datetime.now().isoformat(),
            "folders_created": len(self.workspace_structure),
            "metadata_file": metadata_path
        }
    
    def _get_placeholder_content(self, filename: str, client_name: str, 
                                 company_name: str) -> str:
        """Generate placeholder content for files"""
        placeholders = {
            "client-brief.md": self._generate_client_brief_template(client_name, company_name),
            "discovery-call-notes.md": self._generate_discovery_notes_template(client_name),
            "questionnaire-responses.md": "# Client Questionnaire Responses\n\n[To be completed during onboarding]\n",
            "access-credentials.md": self._generate_credentials_template(),
            "contract-signed.pdf": "[Contract to be uploaded after signing]",
            "onboarding-checklist.md": self._generate_onboarding_checklist(),
            "technical-audit-report.md": "# Technical SEO Audit Report\n\n[To be generated by Technical SEO Agent]\n",
            "seo-audit-report.md": "# SEO Audit Report\n\n[To be generated by SEO Strategist]\n",
            "audit-presentation.pdf": "[Presentation to be created]\n",
            "audit-summary.md": "# Audit Summary\n\n[Executive summary to be generated]\n",
            "priority-issues.md": "# Priority Issues\n\n[To be populated from audit findings]\n",
            "keyword-database.xlsx": "[Keyword database to be created]\n",
            "keyword-research-report.md": "# Keyword Research Report\n\n[To be generated by Keyword Research Agent]\n",
            "content-roadmap.md": "# Content Roadmap\n\n[To be created by SEO Strategist]\n",
            "keyword-prioritization.md": "# Keyword Prioritization\n\n[To be generated]\n",
            "competitor-keywords.md": "# Competitor Keywords\n\n[To be analyzed]\n",
            "seo-strategy.md": "# SEO Strategy\n\n[To be developed by SEO Strategist]\n",
            "content-strategy.md": "# Content Strategy\n\n[To be developed by Content Strategist]\n",
            "link-building-strategy.md": "# Link Building Strategy\n\n[To be developed]\n",
            "local-seo-strategy.md": "# Local SEO Strategy\n\n[To be developed if applicable]\n",
            "implementation-roadmap.md": "# Implementation Roadmap\n\n[To be created]\n",
            "kpi-dashboard.md": "# KPI Dashboard\n\n[To be set up]\n",
            "content-calendar.md": "# Content Calendar\n\n[To be created]\n",
            "content-guidelines.md": "# Content Guidelines\n\n[To be defined based on brand voice]\n",
            "performance-dashboard.md": "# Performance Dashboard\n\n[To be updated monthly]\n",
            "rank-tracking.md": "# Rank Tracking\n\n[To be tracked weekly]\n",
            "traffic-analysis.md": "# Traffic Analysis\n\n[To be analyzed monthly]\n",
            "brand-guidelines.pdf": "[Brand guidelines to be provided by client]\n"
        }
        
        return placeholders.get(filename, f"# {filename}\n\n[To be populated]\n")
    
    def _generate_client_brief_template(self, client_name: str, company_name: str) -> str:
        """Generate client brief template"""
        return f"""# Client Brief: {company_name}

## Business Information
- **Client Name:** {client_name}
- **Company Name:** {company_name}
- **Website:** [URL]
- **Industry:** [Industry]
- **Contact:** [Email, Phone]

## Business Overview
- **Products/Services:** [Description]
- **Target Market:** [Description]
- **Unique Value Proposition:** [What makes them different]

## Goals & Objectives
- **Primary Goal:** [Main goal]
- **Secondary Goals:** [List]
- **Timeline:** [When]

## Current Situation
- **Current SEO:** [Description]
- **Current Traffic:** [X] visits/month
- **Current Rankings:** [X] keywords in top 10

## Budget & Resources
- **Budget:** $[Amount]
- **Timeline:** [X] months
- **Decision Maker:** [Name]

## Services Required
- [ ] SEO Audit
- [ ] Keyword Research
- [ ] Technical SEO
- [ ] Content Writing
- [ ] Monthly SEO
- [ ] Local SEO
- [ ] Link Building

## Next Steps
- [ ] Send proposal
- [ ] Schedule call
- [ ] Sign agreement
- [ ] Begin work

---

**Created:** {datetime.now().strftime('%Y-%m-%d')}
**Status:** New Client
"""
    
    def _generate_discovery_notes_template(self, client_name: str) -> str:
        """Generate discovery call notes template"""
        return f"""# Discovery Call Notes: {client_name}

**Date:** [Date]
**Duration:** [X] minutes
**Participants:** [Names]

## Key Points Discussed

### Business
- [Point 1]
- [Point 2]
- [Point 3]

### Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

### Challenges
- [Challenge 1]
- [Challenge 2]
- [Challenge 3]

### Budget
- [Budget discussion]

### Timeline
- [Timeline discussion]

## Action Items
- [ ] [Action 1] - [Owner] - [Due date]
- [ ] [Action 2] - [Owner] - [Due date]
- [ ] [Action 3] - [Owner] - [Due date]

## Next Steps
- [Next step 1]
- [Next step 2]

## Notes
[Any additional notes]

---

**Created:** {datetime.now().strftime('%Y-%m-%d')}
"""
    
    def _generate_credentials_template(self) -> str:
        """Generate credentials template"""
        return """# Access Credentials

## IMPORTANT: Keep this file secure and private

### Google Search Console
- **URL:** https://search.google.com/search-console
- **Access:** [To be provided by client]
- **Username:** [To be provided]
- **Notes:** [Any special access instructions]

### Google Analytics
- **URL:** https://analytics.google.com
- **Property ID:** [To be provided]
- **Access:** [To be provided by client]
- **Notes:** [Any special access instructions]

### CMS/Website Admin
- **Platform:** [WordPress/Shopify/etc.]
- **Admin URL:** [To be provided]
- **Username:** [To be provided]
- **Notes:** [Any special access instructions]

### Hosting
- **Provider:** [To be provided]
- **Control Panel:** [cPanel/Plesk/etc.]
- **Access:** [To be provided by client]
- **Notes:** [Any special access instructions]

### Other Tools
- [Tool name]: [Access details]

---

**Created:** {datetime.now().strftime('%Y-%m-%d')}
**Security:** Store encrypted, limit access
""".format(date=datetime.now().strftime('%Y-%m-%d'))
    
    def _generate_onboarding_checklist(self) -> str:
        """Generate onboarding checklist"""
        return """# Onboarding Checklist

## Pre-Onboarding
- [ ] Contract signed
- [ ] First payment received
- [ ] Welcome email sent
- [ ] Calendar invite sent for kickoff call

## Discovery Phase
- [ ] Discovery call completed
- [ ] Client brief completed
- [ ] Access credentials collected
- [ ] Tools and accounts set up

## Audit Phase
- [ ] Technical audit initiated
- [ ] Crawl completed
- [ ] Audit report generated
- [ ] Audit presentation delivered

## Strategy Phase
- [ ] Keyword research completed
- [ ] Competitor analysis completed
- [ ] SEO strategy developed
- [ ] Strategy presentation delivered

## Content Phase
- [ ] Content calendar created
- [ ] Content briefs prepared
- [ ] Content creation started
- [ ] Content published

## Reporting Phase
- [ ] Monthly report template set up
- [ ] Tracking configured
- [ ] First report delivered
- [ ] Reporting schedule established

## Ongoing
- [ ] Weekly check-ins scheduled
- [ ] Communication channels established
- [ ] Support process defined
- [ ] Escalation path clear

---

**Created:** {datetime.now().strftime('%Y-%m-%d')}
**Status:** In Progress
""".format(date=datetime.now().strftime('%Y-%m-%d'))
    
    def _create_initial_documents(self, workspace_path: str, client_name: str, 
                                  company_name: str, services: List[str], 
                                  intake_data: Dict):
        """Create initial project documents"""
        # Create project README
        readme_path = os.path.join(workspace_path, "README.md")
        with open(readme_path, 'w') as f:
            f.write(f"""# {company_name} - Project Workspace

**Client:** {client_name}
**Company:** {company_name}
**Project Start:** {datetime.now().strftime('%Y-%m-%d')}
**Services:** {', '.join(services)}

## Workspace Structure

```
{company_name.replace(' ', '_')}/
├── 01 Intake/          - Client information and onboarding
├── 02 Audit/           - SEO and technical audits
├── 03 Keywords/        - Keyword research and analysis
├── 04 Strategy/        - SEO strategy and planning
├── 05 Content/         - Content creation and management
├── 06 Reports/         - Performance reports
├── 07 Deliverables/    - Final client deliverables
└── 08 Assets/          - Brand assets and resources
```

## Quick Links

- [Client Brief](01%20Intake/client-brief.md)
- [Project Metadata](project-metadata.json)
- [SEO Strategy](04%20Strategy/seo-strategy.md)
- [Latest Report](06%20Reports/)

## Team

- **SEO Strategist:** [Assigned]
- **Technical SEO:** [Assigned]
- **Content Writer:** [Assigned]
- **Reporting:** [Assigned]

## Status

**Current Phase:** Discovery
**Next Milestone:** [To be set]

---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
""")
        
        # Create services-specific folders
        if 'Content Writing' in services:
            content_briefs_path = os.path.join(workspace_path, "05 Content", "briefs")
            os.makedirs(content_briefs_path, exist_ok=True)
        
        if 'Monthly SEO' in services:
            monthly_reports_path = os.path.join(workspace_path, "06 Reports", "monthly")
            os.makedirs(monthly_reports_path, exist_ok=True)
    
    def _create_project_metadata(self, client_name: str, company_name: str, 
                                 services: List[str], intake_data: Dict) -> Dict:
        """Create project metadata JSON"""
        return {
            "project_id": f"PROJ-{datetime.now().strftime('%Y%m%d')}-{hash(company_name) % 10000:04d}",
            "client_name": client_name,
            "company_name": company_name,
            "services": services,
            "status": "Active",
            "phase": "Discovery",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "intake_data": intake_data,
            "team": {
                "seo_strategist": None,
                "technical_seo": None,
                "content_writer": None,
                "reporting": None,
                "qa": None
            },
            "milestones": [],
            "deliverables": [],
            "reports": [],
            "invoices": []
        }
    
    def get_workspace_info(self, company_name: str) -> Optional[Dict]:
        """Get workspace information"""
        safe_name = company_name.replace(' ', '_').replace('/', '_')
        workspace_path = os.path.join(self.base_path, safe_name)
        
        if not os.path.exists(workspace_path):
            return None
        
        metadata_path = os.path.join(workspace_path, "project-metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                return json.load(f)
        
        return {"path": workspace_path, "exists": True}
    
    def list_all_workspaces(self) -> List[Dict]:
        """List all client workspaces"""
        workspaces = []
        
        if not os.path.exists(self.base_path):
            return workspaces
        
        for folder in os.listdir(self.base_path):
            folder_path = os.path.join(self.base_path, folder)
            if os.path.isdir(folder_path):
                metadata_path = os.path.join(folder_path, "project-metadata.json")
                if os.path.exists(metadata_path):
                    with open(metadata_path, 'r') as f:
                        metadata = json.load(f)
                        workspaces.append(metadata)
                else:
                    workspaces.append({
                        "company_name": folder.replace('_', ' '),
                        "path": folder_path,
                        "exists": True
                    })
        
        return workspaces
    
    def archive_workspace(self, company_name: str) -> bool:
        """Archive completed client workspace"""
        safe_name = company_name.replace(' ', '_').replace('/', '_')
        workspace_path = os.path.join(self.base_path, safe_name)
        
        if not os.path.exists(workspace_path):
            return False
        
        # Create archive folder
        archive_path = os.path.join(self.base_path, "_Archived", safe_name)
        os.makedirs(archive_path, exist_ok=True)
        
        # Move workspace to archive
        shutil.move(workspace_path, archive_path)
        
        print(f"✓ Archived workspace: {company_name}")
        return True


def demonstrate_workspace_automation():
    """Demonstrate workspace automation"""
    print("\n" + "="*80)
    print("CLIENT WORKSPACE AUTOMATION DEMONSTRATION")
    print("="*80 + "\n")
    
    workspace_manager = ClientWorkspaceManager()
    
    # Sample client data
    client_data = {
        'client_name': 'John Smith',
        'company_name': 'TechStart Solutions',
        'services_required': ['SEO Audit', 'Keyword Research', 'Technical SEO', 'Content Writing'],
        'budget': '$5,000-$10,000',
        'timeline': 'Within 1 month',
        'target_country': 'United States'
    }
    
    print("Step 1: Creating client workspace...")
    print("-" * 80)
    print(f"Client: {client_data['company_name']}")
    print(f"Services: {', '.join(client_data['services_required'])}")
    
    # Create workspace
    workspace_info = workspace_manager.create_client_workspace(
        client_name=client_data['client_name'],
        company_name=client_data['company_name'],
        services=client_data['services_required'],
        intake_data=client_data
    )
    
    print(f"\n✓ Workspace created successfully")
    print(f"  Path: {workspace_info['workspace_path']}")
    print(f"  Folders: {workspace_info['folders_created']}")
    
    print("\nStep 2: Workspace structure")
    print("-" * 80)
    
    # List created folders
    for folder in sorted(os.listdir(workspace_info['workspace_path'])):
        folder_path = os.path.join(workspace_info['workspace_path'], folder)
        if os.path.isdir(folder_path):
            items = os.listdir(folder_path)
            print(f"  {folder}/ ({len(items)} items)")
    
    print("\nStep 3: Project metadata")
    print("-" * 80)
    print(f"  Project ID: {workspace_info['workspace_path']}/project-metadata.json")
    print(f"  Created: {workspace_info['created_at']}")
    
    print("\nStep 4: Listing all workspaces")
    print("-" * 80)
    
    # List all workspaces
    all_workspaces = workspace_manager.list_all_workspaces()
    print(f"Total workspaces: {len(all_workspaces)}")
    for ws in all_workspaces:
        print(f"  - {ws.get('company_name', 'Unknown')}")
    
    print("\n" + "="*80)
    print("WORKSPACE AUTOMATION READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Automatic workspace creation")
    print("✓ Standardized folder structure")
    print("✓ Template files generated")
    print("✓ Project metadata tracking")
    print("✓ Workspace management")
    print("✓ Archive functionality")
    print("\n")


if __name__ == "__main__":
    demonstrate_workspace_automation()
# Phase 4 — Client Acquisition System (Revenue First)

> **Revenue should come before scale.**  
> This system helps you consistently find, qualify, pitch, and manage leads across multiple channels.

---

## 📁 Directory Structure

```
acquisition/
│
├── lead-hunter-agent.py     # Find & prioritize SEO opportunities
├── website-analyzer.py      # Analyze websites for SEO issues
├── proposal-agent.py        # Generate custom proposals per platform
├── outreach-agent.py        # Cold emails, LinkedIn, follow-ups
├── crm-agent.py             # 8-stage pipeline management
├── pricing-agent.py         # Country/competition-based pricing
├── revenue-dashboard.py     # CEO-level revenue tracking
├── acquisition-orchestrator.py  # Tie everything together
│
├── marketplace/
│   ├── upwork/              # Upwork-specific assets
│   ├── fiverr/              # Fiverr-specific assets
│   └── freelancer/          # Freelancer.com-specific assets
│
├── outreach/
│   ├── cold-email/          # Email templates
│   ├── linkedin/            # LinkedIn message templates
│   └── local-business/      # Local business outreach
│
├── crm/                     # CRM data storage
├── proposals/               # Generated proposals
├── automation/              # Automation scripts
└── analytics/               # Performance data
```

---

## 🎯 New AI Agents

### 1. Lead Hunter Agent
**Purpose:** Find SEO opportunities and prioritize high-value prospects.

**Outputs:**
- Prospect lists with contact information
- Opportunity reports with priority scores
- Competitor gap analysis
- Estimated pipeline value

**Methods:** `scan_job_board()`, `discover_local_businesses()`, `analyze_competitor_gap()`, `prioritize_prospects()`

### 2. Website Analyzer
**Purpose:** Inspect websites and generate instant SEO scores — perfect for Upwork proposals.

**Outputs:**
- Overall SEO score (0-100)
- Technical, on-page, content, performance, mobile scores
- Critical issues and quick wins
- Keyword opportunities with volume/difficulty
- Traffic estimates and competitor gaps

**Methods:** `analyze_website()`, `generate_proposal_insights()`

### 3. Proposal Agent
**Purpose:** Automatically create winning proposals for any platform.

**Platforms:** Upwork, Fiverr, Freelancer, LinkedIn, Direct Outreach

**Industries:** SaaS, E-commerce, Local Business, Healthcare, Legal

**Outputs:**
- Platform-specific proposals
- Industry-aware content
- Smart pricing calculations
- Discovery questions
- Competitive differentiators

**Methods:** `generate_proposal()`, `generate_multiple_platform_proposals()`

### 4. Outreach Agent
**Purpose:** Write personalized outreach communications.

**Outputs:**
- Cold emails
- LinkedIn messages
- Follow-up sequences (up to 3)
- Meeting requests
- Complete outreach sequences (5-step: email → follow-up → value-add → LinkedIn → meeting)

**Methods:** `generate_cold_email()`, `generate_linkedin_message()`, `generate_follow_up()`, `generate_outreach_sequence()`

### 5. CRM Agent
**Purpose:** Manage complete client pipeline.

**Pipeline Stages:**
```
Lead → Qualified → Proposal Sent → Interview → Won → Active Client → Upsell → Referral
```

**Features:**
- Lead scoring (0-100)
- Proposal tracking
- Interview scheduling
- Deal management
- Project tracking
- Communication log
- Testimonial & referral management

**Methods:** `add_lead()`, `qualify_lead()`, `send_proposal()`, `win_deal()`, `start_project()`, `get_pipeline_summary()`

### 6. Pricing Agent
**Purpose:** Recommend pricing based on multiple factors.

**Factors:** Country (18 countries), Competition (4 levels), Client budget, Website size (4 sizes), Complexity (4 levels)

**Outputs:**
- Base prices for 11 services
- 3-tier packages (Basic/Standard/Premium)
- Market position analysis
- Competitor price comparison
- Confidence scoring

**Methods:** `calculate_price()`, `get_service_catalog()`, `compare_competitors()`

### 7. Revenue Dashboard
**Purpose:** Track every revenue metric for the CEO Agent.

**Metrics Tracked:**
- Today's leads, proposals, won/lost jobs, revenue
- Total revenue, MRR, average deal size, LTV
- Pipeline value and weighted pipeline
- Conversion rates (lead→qualified→proposal→won)
- Platform performance (Upwork, Fiverr, Freelancer, Direct, LinkedIn)
- Revenue trends and 6-month projections
- Growth metrics (MoM, QoQ, YoY)
- Alerts and recommended actions

**Methods:** `generate_dashboard()`, `get_executive_summary()`

---

## 🚀 How to Use

### Run Individual Agents

```bash
# Lead Hunter
python acquisition/lead-hunter-agent.py

# Website Analyzer
python acquisition/website-analyzer.py

# Proposal Agent
python acquisition/proposal-agent.py

# Outreach Agent
python acquisition/outreach-agent.py

# CRM Agent
python acquisition/crm-agent.py

# Pricing Agent
python acquisition/pricing-agent.py

# Revenue Dashboard
python acquisition/revenue-dashboard.py

# Full Orchestrator
python acquisition/acquisition-orchestrator.py
```

### Orchestrate Full Acquisition Cycle

```python
from acquisition.acquisition_orchestrator import AcquisitionOrchestrator

orchestrator = AcquisitionOrchestrator()

# Run complete cycle for a target market
results = orchestrator.run_full_acquisition_cycle({
    "location": "New York",
    "industry": "Dental",
    "country": "United States",
    "competition": "medium"
})

# Get executive summary
summary = orchestrator.run_daily_operations()
```

---

## ✅ Phase 4 Deliverables Checklist

| # | Capability | Status |
|---|-----------|--------|
| 1 | Find SEO leads | ✅ |
| 2 | Analyze websites | ✅ |
| 3 | Generate proposals | ✅ |
| 4 | Manage CRM | ✅ |
| 5 | Track every opportunity | ✅ |
| 6 | Track revenue | ✅ |
| 7 | Prepare Fiverr gigs | ✅ |
| 8 | Prepare Upwork bids | ✅ |
| 9 | Prepare Freelancer bids | ✅ |
| 10 | Follow up automatically | ✅ |

---

## 📊 Key Metrics Target

| Metric | Target |
|--------|--------|
| Apply to 20 jobs/day (Upwork) | < 30 minutes |
| Win rate | > 30% |
| Client satisfaction | > 95% |
| Repeat business | > 40% |
| Referral rate | > 20% |
| Response time | < 2 hours |

---

## 🔗 Integration Points

- **CEO Agent** → Receives revenue dashboard data
- **Sales Agent** → Uses proposals and outreach
- **SEO Strategist** → Gets pre-qualified leads
- **Workflow Orchestrator** → Coordinates delivery after deal won
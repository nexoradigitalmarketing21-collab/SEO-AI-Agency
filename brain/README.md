# Brain - Central Agency Intelligence

## Purpose
The brain/ directory serves as the **central nervous system** of the Nexora AI SEO Agency. It contains the core rules, standards, and decision frameworks that every agent must follow to ensure consistency, quality, and alignment with agency values.

## How It Works

Every AI agent in the agency **must consult** the brain/ files before:
- Making strategic decisions
- Producing client deliverables
- Communicating with clients
- Executing workflows
- Making recommendations

This ensures:
- **Consistency:** All agents follow the same rules and standards
- **Quality:** Uniform quality requirements across all outputs
- **Brand Alignment:** All outputs reflect agency values and voice
- **Decision Quality:** Agents make decisions based on established frameworks

## Brain Files Overview

### 1. agency-rules.md
**Purpose:** Core rules governing agency operations
**Contains:**
- Agency mission, vision, and values
- Client communication protocols
- Delivery standards and SLAs
- Pricing philosophy
- Conflict resolution procedures
- Escalation paths

**Used by:** All agents, especially CEO, PM, and Client Success agents

### 2. quality-standards.md
**Purpose:** Quality requirements for all deliverables
**Contains:**
- Minimum quality thresholds
- Review and approval processes
- Error handling standards
- Client satisfaction metrics
- Continuous improvement requirements

**Used by:** All agents, especially QA, Content Writer, and Technical SEO agents

### 3. workflow-rules.md
**Purpose:** Standard procedures and workflows
**Contains:**
- Complete agency workflow (client order → delivery)
- Agent coordination rules
- Handoff procedures
- Quality gates
- Reporting cadence
- Timeline standards

**Used by:** Project Manager, all execution agents

### 4. decision-framework.md (Phase 2)
**Purpose:** Decision-making frameworks
**Contains:**
- Strategic decision trees
- Prioritization matrices
- Risk assessment frameworks
- Resource allocation guidelines

**Used by:** CEO, SEO Strategist, Project Manager

### 5. writing-style.md (Phase 2)
**Purpose:** Brand voice and writing standards
**Contains:**
- Tone and voice guidelines
- Writing style preferences
- Terminology standards
- Formatting rules

**Used by:** Content Writer, all client-facing agents

### 6. client-communication.md (Phase 2)
**Purpose:** Client interaction standards
**Contains:**
- Communication protocols
- Response time standards
- Meeting guidelines
- Report formatting
- Escalation procedures

**Used by:** All client-facing agents

### 7. pricing.md (Phase 2)
**Purpose:** Pricing guidelines and structures
**Contains:**
- Service pricing tiers
- Discount policies
- Package definitions
- Upsell guidelines

**Used by:** Sales, CEO, Project Manager

## Usage Pattern

### For Each Task:
1. **Read relevant brain/ files** at task start
2. **Apply rules and standards** throughout execution
3. **Validate output** against quality standards
4. **Follow workflow** for handoffs and approvals
5. **Document decisions** based on decision frameworks

### Example: Technical SEO Audit
```
1. Read brain/quality-standards.md (understand quality requirements)
2. Read brain/workflow-rules.md (understand audit process)
3. Read knowledge-base/technical-seo.md (technical knowledge)
4. Conduct audit following standards
5. Produce deliverable using deliverables/seo-audit/template.md
6. Validate against quality-standards.md checklist
7. Follow workflow-rules.md for client delivery
```

## Integration with Agents

Every agent's system-prompt.md includes:
```
MANDATORY: Before beginning any task, consult the following brain/ files:
- agency-rules.md (for agency standards)
- quality-standards.md (for output quality)
- workflow-rules.md (for process compliance)
```

## Maintenance

- **Version Control:** All brain/ files are version controlled
- **Updates:** Changes require CEO approval
- **Communication:** All agents notified of brain/ updates
- **Review:** Quarterly review of all brain/ files

## Best Practices

1. **Always Consult:** Never skip reading relevant brain/ files
2. **Follow Exactly:** Adhere to rules without deviation
3. **Flag Conflicts:** Report contradictions between brain/ and task requirements
4. **Suggest Updates:** Propose brain/ improvements based on experience
5. **Document Exceptions:** Record any necessary deviations with justification

## Success Metrics

- **Consistency Score:** % of outputs following brain/ standards
- **Quality Score:** Client satisfaction ratings
- **Compliance Rate:** % of workflows following brain/ procedures
- **Update Frequency:** How often brain/ evolves based on learnings

## Related Directories

- **agents/** - All agents that use brain/
- **knowledge-base/** - Technical knowledge agents reference
- **SOP/** - Detailed procedures (referenced by brain/)
- **deliverables/** - Output templates (aligned with brain/ standards)

## Notes

- brain/ is the **single source of truth** for agency operations
- When in doubt, consult brain/ first
- brain/ overrides individual agent preferences
- brain/ evolves based on agency learnings and client feedback
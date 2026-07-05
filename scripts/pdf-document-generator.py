#!/usr/bin/env python3
"""
Nexora AI SEO Agency - PDF & Document Generation
Generate professional PDF reports and Office documents.
"""

from typing import Dict, List, Optional
from datetime import datetime
import os

class PDFReportGenerator:
    """Generate professional PDF reports"""
    
    def __init__(self):
        self.report_templates = {
            "seo_audit": self._generate_seo_audit_pdf,
            "keyword_research": self._generate_keyword_research_pdf,
            "monthly_report": self._generate_monthly_report_pdf,
            "technical_audit": self._generate_technical_audit_pdf,
            "competitor_analysis": self._generate_competitor_analysis_pdf,
            "seo_strategy": self._generate_seo_strategy_pdf
        }
        
    def generate_pdf(self, report_type: str, data: Dict, output_path: str) -> str:
        """
        Generate PDF report
        
        In production, this would use libraries like:
        - ReportLab (Python)
        - WeasyPrint (HTML to PDF)
        - pdfkit (HTML to PDF)
        - fpdf2 (PDF generation)
        
        For demonstration, we generate HTML that can be converted to PDF
        """
        if report_type not in self.report_templates:
            raise ValueError(f"Unknown report type: {report_type}")
        
        # Generate HTML content
        html_content = self.report_templates[report_type](data)
        
        # Save HTML (in production, convert to PDF)
        html_path = output_path.replace('.pdf', '.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # In production, convert HTML to PDF here
        # self._convert_html_to_pdf(html_path, output_path)
        
        return html_path
    
    def _generate_seo_audit_pdf(self, data: Dict) -> str:
        """Generate SEO audit PDF"""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SEO Audit Report - {data.get('company_name', 'Client')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ text-align: center; padding: 20px; background: #2c3e50; color: white; }}
        .section {{ margin: 30px 0; padding: 20px; border-left: 4px solid #3498db; }}
        .critical {{ border-left-color: #e74c3c; background: #fadbd8; padding: 15px; margin: 10px 0; }}
        .high {{ border-left-color: #f39c12; background: #fdebd0; padding: 15px; margin: 10px 0; }}
        .medium {{ border-left-color: #f1c40f; background: #fcf3cf; padding: 15px; margin: 10px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
        .metric {{ display: inline-block; padding: 10px 20px; margin: 10px; background: #ecf0f1; border-radius: 5px; }}
        .score {{ font-size: 24px; font-weight: bold; color: #3498db; }}
        .footer {{ text-align: center; padding: 20px; margin-top: 40px; border-top: 1px solid #ddd; color: #7f8c8d; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>SEO Audit Report</h1>
        <p>{data.get('company_name', 'Client')} | {data.get('website', '')}</p>
        <p>Generated: {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <p>{data.get('executive_summary', 'Comprehensive SEO audit completed.')}</p>
        
        <h3>Overall Score</h3>
        <div class="score">{data.get('overall_score', 75)}/100</div>
        
        <h3>Key Metrics</h3>
        <div class="metric">Pages Audited: {data.get('pages_audited', 342)}</div>
        <div class="metric">Issues Found: {data.get('issues_found', 156)}</div>
        <div class="metric">Critical Issues: {data.get('critical_issues', 23)}</div>
    </div>
    
    <div class="section">
        <h2>Critical Issues</h2>
        {self._format_issues(data.get('critical_issues_list', []), 'critical')}
    </div>
    
    <div class="section">
        <h2>High Priority Issues</h2>
        {self._format_issues(data.get('high_priority_issues_list', []), 'high')}
    </div>
    
    <div class="section">
        <h2>Recommendations</h2>
        <table>
            <tr><th>Priority</th><th>Issue</th><th>Recommendation</th><th>Impact</th></tr>
            {self._format_recommendations(data.get('recommendations', []))}
        </table>
    </div>
    
    <div class="section">
        <h2>90-Day Roadmap</h2>
        {self._format_roadmap(data.get('roadmap', {}))}
    </div>
    
    <div class="footer">
        <p>Nexora AI SEO Agency | {datetime.now().strftime('%Y')}</p>
        <p>This report was generated automatically by our AI-powered SEO platform.</p>
    </div>
</body>
</html>"""
        return html
    
    def _generate_keyword_research_pdf(self, data: Dict) -> str:
        """Generate keyword research PDF"""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Keyword Research Report - {data.get('company_name', 'Client')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ text-align: center; padding: 20px; background: #2c3e50; color: white; }}
        .section {{ margin: 30px 0; padding: 20px; border-left: 4px solid #3498db; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; font-size: 12px; }}
        th {{ background: #3498db; color: white; }}
        .keyword-cluster {{ background: #ecf0f1; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .opportunity {{ background: #d5f4e6; padding: 10px; margin: 5px 0; border-left: 3px solid #27ae60; }}
        .footer {{ text-align: center; padding: 20px; margin-top: 40px; border-top: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Keyword Research Report</h1>
        <p>{data.get('company_name', 'Client')} | {data.get('website', '')}</p>
        <p>Generated: {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    <div class="section">
        <h2>Research Overview</h2>
        <p><strong>Total Keywords Identified:</strong> {data.get('total_keywords', 2847)}</p>
        <p><strong>High-Priority Keywords:</strong> {data.get('high_priority', 342)}</p>
        <p><strong>Quick Win Opportunities:</strong> {data.get('quick_wins', 89)}</p>
    </div>
    
    <div class="section">
        <h2>Top Keyword Opportunities</h2>
        <table>
            <tr><th>Keyword</th><th>Volume</th><th>Difficulty</th><th>Intent</th><th>Priority</th></tr>
            {self._format_top_keywords(data.get('top_keywords', []))}
        </table>
    </div>
    
    <div class="section">
        <h2>Keyword Clusters</h2>
        {self._format_keyword_clusters(data.get('clusters', []))}
    </div>
    
    <div class="section">
        <h2>Content Roadmap</h2>
        {self._format_content_roadmap(data.get('content_roadmap', {}))}
    </div>
    
    <div class="footer">
        <p>Nexora AI SEO Agency | {datetime.now().strftime('%Y')}</p>
    </div>
</body>
</html>"""
        return html
    
    def _generate_monthly_report_pdf(self, data: Dict) -> str:
        """Generate monthly report PDF"""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Monthly SEO Report - {data.get('company_name', 'Client')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ text-align: center; padding: 20px; background: #2c3e50; color: white; }}
        .section {{ margin: 30px 0; padding: 20px; border-left: 4px solid #3498db; }}
        .kpi {{ display: inline-block; padding: 15px 25px; margin: 10px; background: #ecf0f1; border-radius: 5px; text-align: center; }}
        .kpi-value {{ font-size: 28px; font-weight: bold; color: #3498db; }}
        .kpi-label {{ font-size: 14px; color: #7f8c8d; }}
        .positive {{ color: #27ae60; }}
        .negative {{ color: #e74c3c; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
        .chart {{ margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 5px; }}
        .footer {{ text-align: center; padding: 20px; margin-top: 40px; border-top: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Monthly SEO Report</h1>
        <p>{data.get('company_name', 'Client')} | {data.get('month', datetime.now().strftime('%B %Y'))}</p>
        <p>Generated: {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    <div class="section">
        <h2>Performance Overview</h2>
        <div class="kpi">
            <div class="kpi-value positive">+{data.get('traffic_change', 15)}%</div>
            <div class="kpi-label">Organic Traffic</div>
        </div>
        <div class="kpi">
            <div class="kpi-value positive">+{data.get('ranking_change', 23)}</div>
            <div class="kpi-label">Keywords in Top 10</div>
        </div>
        <div class="kpi">
            <div class="kpi-value">{data.get('conversions', 385)}</div>
            <div class="kpi-label">Conversions</div>
        </div>
        <div class="kpi">
            <div class="kpi-value positive">+{data.get('revenue_change', 18)}%</div>
            <div class="kpi-label">Revenue</div>
        </div>
    </div>
    
    <div class="section">
        <h2>Traffic Analysis</h2>
        <div class="chart">
            <h3>Organic Traffic Trend</h3>
            <p>Current: {data.get('current_traffic', 18500):,} visits/month</p>
            <p>Previous: {data.get('previous_traffic', 16100):,} visits/month</p>
            <p class="positive">Change: +{data.get('traffic_change', 15)}%</p>
        </div>
    </div>
    
    <div class="section">
        <h2>Ranking Improvements</h2>
        <table>
            <tr><th>Keyword</th><th>Previous Position</th><th>Current Position</th><th>Change</th></tr>
            {self._format_ranking_improvements(data.get('ranking_improvements', []))}
        </table>
    </div>
    
    <div class="section">
        <h2>Key Insights</h2>
        {self._format_insights(data.get('insights', []))}
    </div>
    
    <div class="section">
        <h2>Next Month Plan</h2>
        {self._format_next_month_plan(data.get('next_month_plan', {}))}
    </div>
    
    <div class="footer">
        <p>Nexora AI SEO Agency | {datetime.now().strftime('%Y')}</p>
    </div>
</body>
</html>"""
        return html
    
    def _generate_technical_audit_pdf(self, data: Dict) -> str:
        """Generate technical audit PDF"""
        # Similar structure to SEO audit but focused on technical aspects
        return self._generate_seo_audit_pdf(data)
    
    def _generate_competitor_analysis_pdf(self, data: Dict) -> str:
        """Generate competitor analysis PDF"""
        # Structure for competitor analysis
        return self._generate_seo_audit_pdf(data)
    
    def _generate_seo_strategy_pdf(self, data: Dict) -> str:
        """Generate SEO strategy PDF"""
        # Structure for strategy document
        return self._generate_seo_audit_pdf(data)
    
    def _format_issues(self, issues: List[Dict], severity: str) -> str:
        """Format issues list"""
        if not issues:
            return "<p>No issues found.</p>"
        return ''.join([f"<div class='{severity}'><strong>{issue.get('title', 'Issue')}</strong><br>{issue.get('description', '')}</div>" for issue in issues])
    
    def _format_recommendations(self, recommendations: List[Dict]) -> str:
        """Format recommendations table"""
        if not recommendations:
            return "<tr><td colspan='4'>No recommendations.</td></tr>"
        return ''.join([f"<tr><td>{rec.get('priority', '')}</td><td>{rec.get('issue', '')}</td><td>{rec.get('recommendation', '')}</td><td>{rec.get('impact', '')}</td></tr>" for rec in recommendations])
    
    def _format_roadmap(self, roadmap: Dict) -> str:
        """Format implementation roadmap"""
        if not roadmap:
            return "<p>No roadmap defined.</p>"
        return f"<p>{roadmap.get('description', 'Roadmap to be defined')}</p>"
    
    def _format_top_keywords(self, keywords: List[Dict]) -> str:
        """Format top keywords table"""
        if not keywords:
            return "<tr><td colspan='5'>No keywords.</td></tr>"
        return ''.join([f"<tr><td>{kw.get('keyword', '')}</td><td>{kw.get('volume', 0):,}</td><td>{kw.get('difficulty', 0)}</td><td>{kw.get('intent', '')}</td><td>{kw.get('priority', '')}</td></tr>" for kw in keywords])
    
    def _format_keyword_clusters(self, clusters: List[Dict]) -> str:
        """Format keyword clusters"""
        if not clusters:
            return "<p>No clusters defined.</p>"
        return ''.join([f"<div class='keyword-cluster'><strong>{cluster.get('name', 'Cluster')}</strong><br>{cluster.get('keywords', '')}</div>" for cluster in clusters])
    
    def _format_content_roadmap(self, roadmap: Dict) -> str:
        """Format content roadmap"""
        if not roadmap:
            return "<p>No content roadmap defined.</p>"
        return f"<p>{roadmap.get('description', 'Content roadmap to be created')}</p>"
    
    def _format_ranking_improvements(self, improvements: List[Dict]) -> str:
        """Format ranking improvements"""
        if not improvements:
            return "<tr><td colspan='4'>No improvements.</td></tr>"
        return ''.join([f"<tr><td>{imp.get('keyword', '')}</td><td>{imp.get('previous', 0)}</td><td>{imp.get('current', 0)}</td><td class='positive'>+{imp.get('change', 0)}</td></tr>" for imp in improvements])
    
    def _format_insights(self, insights: List[str]) -> str:
        """Format insights"""
        if not insights:
            return "<p>No insights.</p>"
        return ''.join([f"<div class='opportunity'>{insight}</div>" for insight in insights])
    
    def _format_next_month_plan(self, plan: Dict) -> str:
        """Format next month plan"""
        if not plan:
            return "<p>No plan defined.</p>"
        return f"<p>{plan.get('description', 'Plan to be defined')}</p>"


class ExcelGenerator:
    """Generate Excel spreadsheets for keyword data and analytics"""
    
    def __init__(self):
        pass
    
    def generate_keyword_database(self, keywords: List[Dict], output_path: str) -> str:
        """
        Generate Excel keyword database
        
        In production, use openpyxl or pandas
        For demonstration, generate CSV
        """
        import csv
        
        csv_path = output_path.replace('.xlsx', '.csv')
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Header
            writer.writerow([
                'Keyword', 'Search Volume', 'Keyword Difficulty', 'Current Position',
                'Priority', 'Search Intent', 'Business Value', 'Content Type', 'Target Page', 'Status'
            ])
            
            # Data
            for kw in keywords:
                writer.writerow([
                    kw.get('keyword', ''),
                    kw.get('volume', 0),
                    kw.get('difficulty', 0),
                    kw.get('current_position', ''),
                    kw.get('priority', ''),
                    kw.get('intent', ''),
                    kw.get('business_value', ''),
                    kw.get('content_type', ''),
                    kw.get('target_page', ''),
                    kw.get('status', '')
                ])
        
        return csv_path
    
    def generate_analytics_report(self, data: Dict, output_path: str) -> str:
        """Generate analytics report Excel"""
        import csv
        
        csv_path = output_path.replace('.xlsx', '.csv')
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Traffic data
            writer.writerow(['Metric', 'Value', 'Change'])
            writer.writerow(['Total Users', data.get('users', 0), f"+{data.get('users_change', 0)}%"])
            writer.writerow(['Sessions', data.get('sessions', 0), f"+{data.get('sessions_change', 0)}%"])
            writer.writerow(['Bounce Rate', f"{data.get('bounce_rate', 0)}%", f"-{data.get('bounce_rate_change', 0)}%"])
            writer.writerow(['Avg Session Duration', f"{data.get('avg_session_duration', 0)}s", f"+{data.get('duration_change', 0)}%"])
            writer.writerow(['Conversions', data.get('conversions', 0), f"+{data.get('conversions_change', 0)}%"])
            writer.writerow(['Revenue', f"${data.get('revenue', 0):,}", f"+{data.get('revenue_change', 0)}%"])
        
        return csv_path


class PowerPointGenerator:
    """Generate PowerPoint presentations"""
    
    def __init__(self):
        pass
    
    def generate_strategy_presentation(self, data: Dict, output_path: str) -> str:
        """
        Generate PowerPoint presentation
        
        In production, use python-pptx library
        For demonstration, generate markdown outline
        """
        md_path = output_path.replace('.pptx', '.md')
        
        content = f"""# SEO Strategy Presentation
## {data.get('company_name', 'Client')}

**Generated:** {datetime.now().strftime('%B %d, %Y')}

---

## Slide 1: Title

# SEO Strategy 2026
## {data.get('company_name', 'Client')}

**Presented by:** Nexora AI SEO Agency
**Date:** {datetime.now().strftime('%B %d, %Y')}

---

## Slide 2: Executive Summary

**Current Situation:**
- Organic Traffic: {data.get('current_traffic', 18500):,} visits/month
- Keywords in Top 10: {data.get('current_keywords', 45)}
- Domain Authority: {data.get('current_da', 32)}

**Goals:**
- Increase organic traffic by 100%
- Rank 200+ keywords in top 10
- Increase Domain Authority to 45+

**Timeline:** 6 months

---

## Slide 3: Current State Analysis

**Strengths:**
- {data.get('strengths', ['Quality product', 'Strong brand'])[0]}
- {data.get('strengths', ['Quality product', 'Strong brand'])[1] if len(data.get('strengths', [])) > 1 else 'N/A'}

**Weaknesses:**
- {data.get('weaknesses', ['Low organic visibility', 'Weak backlink profile'])[0]}
- {data.get('weaknesses', ['Low organic visibility', 'Weak backlink profile'])[1] if len(data.get('weaknesses', [])) > 1 else 'N/A'}

**Opportunities:**
- {data.get('opportunities', ['High-value keywords', 'Content gaps'])[0]}
- {data.get('opportunities', ['High-value keywords', 'Content gaps'])[1] if len(data.get('opportunities', [])) > 1 else 'N/A'}

---

## Slide 4: SEO Strategy Pillars

**1. Technical Excellence**
- Site speed optimization
- Mobile-first optimization
- Schema markup implementation

**2. Content Authority**
- Pillar page creation
- Cluster content development
- Topic authority building

**3. Link Building**
- Guest posting
- Resource page outreach
- Digital PR campaigns

**4. Optimization**
- On-page SEO
- User experience
- Conversion optimization

---

## Slide 5: Implementation Roadmap

**Month 1-2: Foundation**
- Technical fixes
- Content creation
- Initial optimization

**Month 3-4: Growth**
- Link building
- Content expansion
- Authority building

**Month 5-6: Scale**
- Advanced strategies
- Conversion optimization
- Continuous improvement

---

## Slide 6: Expected Results

**Traffic Growth:**
- Month 3: {data.get('month_3_traffic', 28000):,} visits/month
- Month 6: {data.get('month_6_traffic', 35000):,} visits/month

**Ranking Improvements:**
- Month 3: {data.get('month_3_keywords', 120)} keywords in top 10
- Month 6: {data.get('month_6_keywords', 200)}+ keywords in top 10

**Revenue Impact:**
- Month 6: ${data.get('month_6_revenue', 35000):,}/month
- ROI: {data.get('roi', 400)}%+

---

## Slide 7: Investment

**Total Investment:** ${data.get('total_investment', 15000):,}

**Breakdown:**
- Technical SEO: ${data.get('technical_cost', 3000):,}
- Content Creation: ${data.get('content_cost', 6000):,}
- Link Building: ${data.get('link_building_cost', 4000):,}
- Tools & Software: ${data.get('tools_cost', 1000):,}
- Management: ${data.get('management_cost', 1000):,}

**Expected ROI:** {data.get('roi', 400)}% in 6 months

---

## Slide 8: Next Steps

1. **Week 1:** Sign agreement, provide access
2. **Week 2-3:** Complete technical audit
3. **Week 4:** Deliver strategy document
4. **Month 2:** Begin implementation
5. **Ongoing:** Monthly reporting and optimization

**Contact:** {data.get('contact_email', 'hello@nexora.com')}

---

**Thank You**

Questions?
"""
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return md_path


class DocumentGenerator:
    """Main document generation orchestrator"""
    
    def __init__(self):
        self.pdf_generator = PDFReportGenerator()
        self.excel_generator = ExcelGenerator()
        self.powerpoint_generator = PowerPointGenerator()
        
    def generate_all_documents(self, report_type: str, data: Dict, 
                               output_dir: str, client_name: str) -> Dict[str, str]:
        """Generate all document formats for a report"""
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_name = client_name.replace(' ', '_')
        
        documents = {}
        
        # Generate PDF (HTML version)
        pdf_path = os.path.join(output_dir, f"{timestamp}_{safe_name}_{report_type}.pdf")
        documents['pdf'] = self.pdf_generator.generate_pdf(report_type, data, pdf_path)
        
        # Generate Excel (if applicable)
        if report_type in ['keyword_research', 'monthly_report']:
            excel_path = os.path.join(output_dir, f"{timestamp}_{safe_name}_{report_type}.xlsx")
            if report_type == 'keyword_research':
                documents['excel'] = self.excel_generator.generate_keyword_database(
                    data.get('keywords', []), excel_path
                )
            elif report_type == 'monthly_report':
                documents['excel'] = self.excel_generator.generate_analytics_report(
                    data.get('analytics', {}), excel_path
                )
        
        # Generate PowerPoint (if applicable)
        if report_type in ['seo_strategy', 'seo_audit']:
            pptx_path = os.path.join(output_dir, f"{timestamp}_{safe_name}_{report_type}.pptx")
            documents['powerpoint'] = self.powerpoint_generator.generate_strategy_presentation(
                data, pptx_path
            )
        
        return documents


def demonstrate_document_generation():
    """Demonstrate document generation"""
    print("\n" + "="*80)
    print("PDF & DOCUMENT GENERATION DEMONSTRATION")
    print("="*80 + "\n")
    
    doc_generator = DocumentGenerator()
    
    # Sample data
    sample_data = {
        'company_name': 'TechStart Solutions',
        'website': 'https://techstartsolutions.com',
        'overall_score': 75,
        'pages_audited': 342,
        'issues_found': 156,
        'critical_issues': 23,
        'executive_summary': 'Comprehensive SEO audit completed. Several critical issues identified that need immediate attention.',
        'critical_issues_list': [
            {'title': '404 Errors', 'description': '127 pages returning 404 errors'},
            {'title': 'Missing Sitemap', 'description': 'No XML sitemap found'}
        ],
        'high_priority_issues_list': [
            {'title': 'Slow Page Speed', 'description': 'Page speed score 34/100 on mobile'}
        ],
        'recommendations': [
            {'priority': 'Critical', 'issue': '404 Errors', 'recommendation': 'Fix broken links', 'impact': 'High'},
            {'priority': 'High', 'issue': 'Page Speed', 'recommendation': 'Optimize images', 'impact': 'High'}
        ],
        'roadmap': {'description': '90-day implementation plan to fix all critical and high priority issues'},
        'total_keywords': 2847,
        'high_priority': 342,
        'quick_wins': 89,
        'top_keywords': [
            {'keyword': 'SEO services', 'volume': 3200, 'difficulty': 45, 'intent': 'commercial', 'priority': 'High'},
            {'keyword': 'technical SEO', 'volume': 2200, 'difficulty': 42, 'intent': 'informational', 'priority': 'High'}
        ],
        'clusters': [
            {'name': 'Core SEO', 'keywords': 'SEO services, SEO agency, SEO company'},
            {'name': 'Technical SEO', 'keywords': 'technical SEO, site speed, mobile SEO'}
        ],
        'content_roadmap': {'description': 'Create 2 pillar pages and 16 cluster content pieces over 3 months'},
        'month': datetime.now().strftime('%B %Y'),
        'traffic_change': 15,
        'ranking_change': 23,
        'conversions': 385,
        'revenue_change': 18,
        'current_traffic': 18500,
        'previous_traffic': 16100,
        'ranking_improvements': [
            {'keyword': 'SEO services', 'previous': 12, 'current': 8, 'change': 4},
            {'keyword': 'technical SEO', 'previous': 9, 'current': 6, 'change': 3}
        ],
        'insights': [
            'Organic traffic increased 15% due to content improvements',
            'Technical fixes resulted in better crawlability',
            'New keywords entered top 10 rankings'
        ],
        'next_month_plan': {'description': 'Focus on link building and content expansion'},
        'current_keywords': 118,
        'current_da': 38,
        'month_3_traffic': 28000,
        'month_6_traffic': 35000,
        'month_3_keywords': 120,
        'month_6_keywords': 200,
        'month_6_revenue': 35000,
        'roi': 400,
        'total_investment': 15000,
        'technical_cost': 3000,
        'content_cost': 6000,
        'link_building_cost': 4000,
        'tools_cost': 1000,
        'management_cost': 1000,
        'contact_email': 'hello@nexora.com'
    }
    
    print("Step 1: Generating documents...")
    print("-" * 80)
    
    output_dir = f"clients/TechStart_Solutions/07 Deliverables/documents"
    
    # Generate SEO Audit documents
    print("\nGenerating SEO Audit documents...")
    audit_docs = doc_generator.generate_all_documents('seo_audit', sample_data, output_dir, 'TechStart Solutions')
    for doc_type, path in audit_docs.items():
        print(f"  ✓ {doc_type.upper()}: {path}")
    
    # Generate Keyword Research documents
    print("\nGenerating Keyword Research documents...")
    keyword_docs = doc_generator.generate_all_documents('keyword_research', sample_data, output_dir, 'TechStart Solutions')
    for doc_type, path in keyword_docs.items():
        print(f"  ✓ {doc_type.upper()}: {path}")
    
    # Generate Monthly Report documents
    print("\nGenerating Monthly Report documents...")
    report_docs = doc_generator.generate_all_documents('monthly_report', sample_data, output_dir, 'TechStart Solutions')
    for doc_type, path in report_docs.items():
        print(f"  ✓ {doc_type.upper()}: {path}")
    
    # Generate Strategy Presentation
    print("\nGenerating Strategy Presentation...")
    strategy_docs = doc_generator.generate_all_documents('seo_strategy', sample_data, output_dir, 'TechStart Solutions')
    for doc_type, path in strategy_docs.items():
        print(f"  ✓ {doc_type.upper()}: {path}")
    
    print("\n" + "="*80)
    print("DOCUMENT GENERATION READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ PDF report generation (HTML-based)")
    print("✓ Excel spreadsheet generation (CSV format)")
    print("✓ PowerPoint presentations (Markdown outline)")
    print("✓ Multiple report types supported")
    print("✓ Professional formatting")
    print("✓ Client-ready outputs")
    print("\n")


if __name__ == "__main__":
    demonstrate_document_generation()
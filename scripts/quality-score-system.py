#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Quality Score System
Automated quality scoring for all deliverables before client delivery.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class QualityScoreSystem:
    """Automated quality scoring and validation system"""
    
    def __init__(self, threshold: float = 90.0):
        self.threshold = threshold  # Minimum score to deliver
        self.scoring_criteria = self._load_scoring_criteria()
        
    def _load_scoring_criteria(self) -> Dict:
        """Load scoring criteria for different deliverable types"""
        return {
            "seo_audit": {
                "accuracy": {"weight": 0.25, "description": "Data accuracy and technical correctness"},
                "completeness": {"weight": 0.20, "description": "All required sections present"},
                "actionability": {"weight": 0.20, "description": "Recommendations are clear and actionable"},
                "formatting": {"weight": 0.15, "description": "Professional formatting and presentation"},
                "seo_best_practices": {"weight": 0.10, "description": "Follows SEO best practices"},
                "client_readiness": {"weight": 0.10, "description": "Ready for client delivery"}
            },
            "keyword_research": {
                "accuracy": {"weight": 0.25, "description": "Keyword data accuracy"},
                "completeness": {"weight": 0.20, "description": "Comprehensive keyword coverage"},
                "prioritization": {"weight": 0.20, "description": "Proper keyword prioritization"},
                "formatting": {"weight": 0.15, "description": "Clear presentation"},
                "seo_best_practices": {"weight": 0.10, "description": "Follows keyword research best practices"},
                "client_readiness": {"weight": 0.10, "description": "Ready for client delivery"}
            },
            "monthly_report": {
                "accuracy": {"weight": 0.25, "description": "Data accuracy"},
                "completeness": {"weight": 0.20, "description": "All metrics included"},
                "insights": {"weight": 0.20, "description": "Valuable insights provided"},
                "formatting": {"weight": 0.15, "description": "Professional formatting"},
                "seo_best_practices": {"weight": 0.10, "description": "Follows reporting best practices"},
                "client_readiness": {"weight": 0.10, "description": "Ready for client delivery"}
            },
            "content_brief": {
                "accuracy": {"weight": 0.20, "description": "Accurate keyword and intent data"},
                "completeness": {"weight": 0.25, "description": "All brief sections complete"},
                "clarity": {"weight": 0.20, "description": "Clear instructions for writer"},
                "formatting": {"weight": 0.15, "description": "Professional formatting"},
                "seo_best_practices": {"weight": 0.10, "description": "Follows content best practices"},
                "client_readiness": {"weight": 0.10, "description": "Ready for writer"}
            },
            "seo_strategy": {
                "accuracy": {"weight": 0.20, "description": "Strategic accuracy"},
                "completeness": {"weight": 0.20, "description": "Comprehensive strategy"},
                "actionability": {"weight": 0.20, "description": "Actionable recommendations"},
                "formatting": {"weight": 0.15, "description": "Professional presentation"},
                "seo_best_practices": {"weight": 0.15, "description": "Follows SEO best practices"},
                "client_readiness": {"weight": 0.10, "description": "Ready for client delivery"}
            }
        }
    
    def score_deliverable(self, deliverable_type: str, deliverable_content: str, 
                         metadata: Dict) -> Dict:
        """
        Score a deliverable across all criteria
        
        Returns detailed scoring report
        """
        if deliverable_type not in self.scoring_criteria:
            return {
                "error": f"Unknown deliverable type: {deliverable_type}",
                "overall_score": 0
            }
        
        criteria = self.scoring_criteria[deliverable_type]
        scores = {}
        
        # Score each criterion
        for criterion, config in criteria.items():
            score = self._score_criterion(criterion, deliverable_content, metadata)
            scores[criterion] = {
                "score": score,
                "weight": config["weight"],
                "weighted_score": score * config["weight"],
                "description": config["description"]
            }
        
        # Calculate overall score
        overall_score = sum(s["weighted_score"] for s in scores.values())
        
        # Determine if deliverable passes threshold
        passes_threshold = overall_score >= self.threshold
        
        # Generate feedback
        feedback = self._generate_feedback(scores, overall_score)
        
        return {
            "deliverable_type": deliverable_type,
            "overall_score": round(overall_score, 2),
            "passes_threshold": passes_threshold,
            "threshold": self.threshold,
            "scores": scores,
            "feedback": feedback,
            "timestamp": datetime.now().isoformat(),
            "recommendation": "APPROVED" if passes_threshold else "NEEDS_REVISION"
        }
    
    def _score_criterion(self, criterion: str, content: str, metadata: Dict) -> float:
        """Score individual criterion"""
        scores = {
            "accuracy": self._score_accuracy(content, metadata),
            "completeness": self._score_completeness(content, metadata),
            "actionability": self._score_actionability(content),
            "clarity": self._score_clarity(content),
            "formatting": self._score_formatting(content),
            "seo_best_practices": self._score_seo_best_practices(content),
            "client_readiness": self._score_client_readiness(content),
            "insights": self._score_insights(content)
        }
        
        return scores.get(criterion, 0.0)
    
    def _score_accuracy(self, content: str, metadata: Dict) -> float:
        """Score data accuracy"""
        score = 85.0
        
        # Check for placeholder text
        if "[" in content and "]" in content:
            score -= 20
        
        # Check for specific data points
        if metadata.get('data_points_verified', False):
            score += 10
        
        # Check for numbers and metrics
        import re
        numbers = re.findall(r'\d+', content)
        if len(numbers) > 10:
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _score_completeness(self, content: str, metadata: Dict) -> float:
        """Score completeness"""
        score = 80.0
        
        # Check for required sections
        required_sections = metadata.get('required_sections', [])
        for section in required_sections:
            if section.lower() in content.lower():
                score += 5
        
        # Check content length
        word_count = len(content.split())
        if word_count > 1000:
            score += 10
        elif word_count < 500:
            score -= 10
        
        return min(100.0, max(0.0, score))
    
    def _score_actionability(self, content: str) -> float:
        """Score actionability of recommendations"""
        score = 75.0
        
        # Check for action words
        action_words = ['implement', 'fix', 'optimize', 'improve', 'update', 'create', 'add']
        action_count = sum(1 for word in action_words if word in content.lower())
        
        if action_count > 5:
            score += 15
        elif action_count > 2:
            score += 10
        
        # Check for specific recommendations
        if 'recommendation' in content.lower() or 'recommend' in content.lower():
            score += 10
        
        return min(100.0, max(0.0, score))
    
    def _score_clarity(self, content: str) -> float:
        """Score clarity of content"""
        score = 80.0
        
        # Check for clear structure
        if '##' in content or '###' in content:
            score += 10
        
        # Check for bullet points
        if '-' in content or '*' in content:
            score += 5
        
        # Check for tables
        if '|' in content:
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _score_formatting(self, content: str) -> float:
        """Score formatting quality"""
        score = 85.0
        
        # Check for headers
        lines = content.split('\n')
        header_count = sum(1 for line in lines if line.startswith('#'))
        if header_count > 5:
            score += 10
        
        # Check for consistent formatting
        if '---' in content:
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _score_seo_best_practices(self, content: str) -> float:
        """Score SEO best practices adherence"""
        score = 80.0
        
        # Check for keyword usage
        if 'keyword' in content.lower():
            score += 5
        
        # Check for metrics
        if 'ctr' in content.lower() or 'conversion' in content.lower():
            score += 5
        
        # Check for actionable insights
        if 'recommendation' in content.lower():
            score += 10
        
        return min(100.0, max(0.0, score))
    
    def _score_client_readiness(self, content: str) -> float:
        """Score client readiness"""
        score = 75.0
        
        # Check for executive summary
        if 'executive summary' in content.lower():
            score += 10
        
        # Check for professional language
        professional_indicators = ['recommendation', 'strategy', 'implementation', 'roadmap']
        prof_count = sum(1 for word in professional_indicators if word in content.lower())
        if prof_count > 2:
            score += 10
        
        # Check for no placeholder text
        if '[' not in content or ']' not in content:
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _score_insights(self, content: str) -> float:
        """Score quality of insights"""
        score = 70.0
        
        # Check for insights section
        if 'insight' in content.lower():
            score += 15
        
        # Check for data analysis
        if 'analysis' in content.lower() or 'analyze' in content.lower():
            score += 10
        
        # Check for recommendations
        if 'recommend' in content.lower():
            score += 5
        
        return min(100.0, max(0.0, score))
    
    def _generate_feedback(self, scores: Dict, overall_score: float) -> List[str]:
        """Generate feedback based on scores"""
        feedback = []
        
        # Overall feedback
        if overall_score >= 95:
            feedback.append("Excellent! Deliverable exceeds quality standards.")
        elif overall_score >= self.threshold:
            feedback.append("Good! Deliverable meets quality standards.")
        else:
            feedback.append(f"Needs improvement. Score {overall_score:.2f} is below threshold {self.threshold}.")
        
        # Specific feedback
        for criterion, data in scores.items():
            if data["score"] < 70:
                feedback.append(f"⚠️  {criterion.replace('_', ' ').title()}: {data['score']:.2f}/100 - Needs improvement")
            elif data["score"] >= 90:
                feedback.append(f"✓ {criterion.replace('_', ' ').title()}: {data['score']:.2f}/100 - Excellent")
        
        return feedback
    
    def generate_qa_report(self, deliverable_type: str, deliverable_content: str,
                          metadata: Dict, reviewer: str) -> Dict:
        """Generate complete QA report"""
        # Score the deliverable
        scoring_result = self.score_deliverable(deliverable_type, deliverable_content, metadata)
        
        # Generate QA report
        qa_report = {
            "qa_report_id": f"QA-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "deliverable_type": deliverable_type,
            "reviewer": reviewer,
            "review_date": datetime.now().isoformat(),
            "scoring": scoring_result,
            "decision": "APPROVED" if scoring_result["passes_threshold"] else "NEEDS_REVISION",
            "action_required": None if scoring_result["passes_threshold"] else "Revise and resubmit",
            "notes": self._generate_qa_notes(scoring_result),
            "approval_chain": [
                {"role": "QA Agent", "status": "Completed", "reviewer": reviewer}
            ]
        }
        
        return qa_report
    
    def _generate_qa_notes(self, scoring_result: Dict) -> List[str]:
        """Generate QA notes based on scoring"""
        notes = []
        
        if not scoring_result["passes_threshold"]:
            notes.append("Deliverable does not meet minimum quality threshold.")
            
            # Add specific issues
            for criterion, data in scoring_result["scores"].items():
                if data["score"] < 70:
                    notes.append(f"Focus on improving: {criterion.replace('_', ' ')}")
        
        return notes
    
    def batch_score_deliverables(self, deliverables: List[Dict]) -> Dict:
        """Score multiple deliverables"""
        results = {
            "total": len(deliverables),
            "approved": 0,
            "needs_revision": 0,
            "average_score": 0.0,
            "deliverables": []
        }
        
        total_score = 0
        
        for deliverable in deliverables:
            score_result = self.score_deliverable(
                deliverable['type'],
                deliverable['content'],
                deliverable.get('metadata', {})
            )
            
            results["deliverables"].append({
                "id": deliverable.get('id'),
                "type": deliverable['type'],
                "score": score_result["overall_score"],
                "passes": score_result["passes_threshold"]
            })
            
            if score_result["passes_threshold"]:
                results["approved"] += 1
            else:
                results["needs_revision"] += 1
            
            total_score += score_result["overall_score"]
        
        if len(deliverables) > 0:
            results["average_score"] = total_score / len(deliverables)
        
        return results


def demonstrate_quality_score_system():
    """Demonstrate quality score system"""
    print("\n" + "="*80)
    print("QUALITY SCORE SYSTEM DEMONSTRATION")
    print("="*80 + "\n")
    
    quality_system = QualityScoreSystem(threshold=90.0)
    
    # Sample SEO Audit deliverable
    sample_audit = """# SEO Audit Report

## Executive Summary

This comprehensive SEO audit identified several critical issues that need immediate attention.

**Overall Score: 75/100**

## Technical Findings

### Critical Issues
1. 404 Errors - 127 pages returning 404 errors
2. Missing Sitemap - No XML sitemap found
3. No HTTPS - Website not using HTTPS

### High Priority Issues
1. Page Speed - Score 34/100 on mobile
2. Missing Meta Descriptions - 89 pages affected
3. Duplicate Title Tags - 45 pages affected

## Recommendations

1. Fix 404 errors with 301 redirects
2. Create and submit XML sitemap
3. Install SSL certificate
4. Optimize page speed
5. Write unique meta descriptions

## 90-Day Roadmap

Week 1-2: Fix critical issues
Week 3-4: Address high priority issues
Month 2-3: Medium priority improvements
"""
    
    metadata = {
        "required_sections": ["executive summary", "technical findings", "recommendations", "roadmap"],
        "data_points_verified": True
    }
    
    print("Step 1: Scoring SEO Audit deliverable...")
    print("-" * 80)
    
    # Score the deliverable
    score_result = quality_system.score_deliverable("seo_audit", sample_audit, metadata)
    
    print(f"\nDeliverable Type: {score_result['deliverable_type']}")
    print(f"Overall Score: {score_result['overall_score']}/100")
    print(f"Threshold: {score_result['threshold']}/100")
    print(f"Passes: {'✓ YES' if score_result['passes_threshold'] else '✗ NO'}")
    print(f"Recommendation: {score_result['recommendation']}")
    
    print("\nDetailed Scores:")
    for criterion, data in score_result['scores'].items():
        bar = "█" * int(data['score'] // 10) + "░" * (10 - int(data['score'] // 10))
        print(f"  {criterion.replace('_', ' ').title():25s} {bar} {data['score']:6.2f}/100 (weight: {data['weight']})")
    
    print("\nFeedback:")
    for feedback in score_result['feedback']:
        print(f"  {feedback}")
    
    print("\n\nStep 2: Generating QA Report...")
    print("-" * 80)
    
    # Generate QA report
    qa_report = quality_system.generate_qa_report(
        "seo_audit",
        sample_audit,
        metadata,
        "QA Agent"
    )
    
    print(f"\nQA Report ID: {qa_report['qa_report_id']}")
    print(f"Reviewer: {qa_report['reviewer']}")
    print(f"Decision: {qa_report['decision']}")
    print(f"Action Required: {qa_report['action_required'] or 'None - Approved for delivery'}")
    
    if qa_report['notes']:
        print("\nQA Notes:")
        for note in qa_report['notes']:
            print(f"  • {note}")
    
    print("\n\nStep 3: Batch Scoring Example")
    print("-" * 80)
    
    # Batch scoring
    deliverables = [
        {"id": "DEL-001", "type": "seo_audit", "content": sample_audit, "metadata": metadata},
        {"id": "DEL-002", "type": "keyword_research", "content": "Sample keyword research content", "metadata": metadata},
        {"id": "DEL-003", "type": "monthly_report", "content": "Sample monthly report content", "metadata": metadata}
    ]
    
    batch_results = quality_system.batch_score_deliverables(deliverables)
    
    print(f"\nTotal Deliverables: {batch_results['total']}")
    print(f"Approved: {batch_results['approved']}")
    print(f"Needs Revision: {batch_results['needs_revision']}")
    print(f"Average Score: {batch_results['average_score']:.2f}/100")
    
    print("\nIndividual Results:")
    for del_result in batch_results['deliverables']:
        status = "✓" if del_result['passes'] else "✗"
        print(f"  {status} {del_result['id']} ({del_result['type']}): {del_result['score']:.2f}/100")
    
    print("\n" + "="*80)
    print("QUALITY SCORE SYSTEM READY")
    print("="*80)
    print("\nFeatures:")
    print("✓ Multi-criteria scoring")
    print("✓ Weighted scoring system")
    print("✓ Automated quality checks")
    print("✓ Threshold-based approval")
    print("✓ Detailed feedback generation")
    print("✓ QA report generation")
    print("✓ Batch scoring capability")
    print("\n")


if __name__ == "__main__":
    demonstrate_quality_score_system()
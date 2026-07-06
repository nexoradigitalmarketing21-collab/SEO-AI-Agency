#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Payment & Contracts System
Module 4: Stripe integration, invoice generation, contract templates, subscription management.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os
import uuid


class ContractManager:
    """Contract and agreement management"""
    
    def __init__(self):
        self.contracts = {}
        self.contract_templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load contract templates"""
        return {
            "seo_audit": {
                "title": "SEO Audit Service Agreement",
                "type": "one_time",
                "sections": [
                    "Services Provided",
                    "Deliverables",
                    "Timeline",
                    "Payment Terms",
                    "Client Responsibilities",
                    "Confidentiality",
                    "Termination",
                    "Limitation of Liability"
                ]
            },
            "monthly_seo": {
                "title": "Monthly SEO Retainer Agreement",
                "type": "subscription",
                "sections": [
                    "Services Provided",
                    "Monthly Deliverables",
                    "Contract Term",
                    "Payment Terms",
                    "Cancellation Policy",
                    "Client Responsibilities",
                    "Reporting",
                    "Confidentiality",
                    "Termination"
                ]
            },
            "project_based": {
                "title": "Project-Based SEO Services Agreement",
                "type": "project",
                "sections": [
                    "Project Scope",
                    "Deliverables",
                    "Milestones",
                    "Payment Schedule",
                    "Timeline",
                    "Client Responsibilities",
                    "Change Orders",
                    "Confidentiality",
                    "Termination"
                ]
            }
        }
    
    def generate_contract(self, contract_type: str, client_info: Dict, project_info: Dict) -> Dict:
        """Generate a contract"""
        template = self.contract_templates.get(contract_type, self.contract_templates['project_based'])
        
        contract_id = str(uuid.uuid4())[:8]
        
        contract = {
            "id": contract_id,
            "type": contract_type,
            "title": template['title'],
            "client": {
                "name": client_info.get('name', 'Client'),
                "company": client_info.get('company', ''),
                "email": client_info.get('email', ''),
                "address": client_info.get('address', '')
            },
            "project": {
                "name": project_info.get('name', 'SEO Project'),
                "description": project_info.get('description', ''),
                "budget": project_info.get('budget', 0),
                "timeline": project_info.get('timeline', '30 days')
            },
            "terms": {
                "payment_terms": "Net 15",
                "late_fee": "5% after 30 days",
                "cancellation": "30 days written notice",
                "revisions": project_info.get('revisions', 2)
            },
            "status": "draft",
            "created_at": datetime.now().isoformat(),
            "signed_at": None,
            "sections": template['sections']
        }
        
        self.contracts[contract_id] = contract
        return contract
    
    def sign_contract(self, contract_id: str, signature: str) -> Dict:
        """Sign a contract"""
        contract = self.contracts.get(contract_id)
        if not contract:
            return {"error": "Contract not found"}
        
        contract['status'] = "signed"
        contract['signed_at'] = datetime.now().isoformat()
        contract['signature'] = signature
        
        return contract


class InvoiceGenerator:
    """Invoice generation and management"""
    
    def __init__(self):
        self.invoices = {}
        self.invoice_number = 1000
    
    def generate_invoice(self, client_info: Dict, items: List[Dict], 
                        tax_rate: float = 0.0, discount: float = 0.0) -> Dict:
        """Generate an invoice"""
        self.invoice_number += 1
        invoice_id = f"INV-{self.invoice_number}"
        
        subtotal = sum(item.get('amount', 0) for item in items)
        discount_amount = subtotal * (discount / 100)
        tax_amount = (subtotal - discount_amount) * (tax_rate / 100)
        total = subtotal - discount_amount + tax_amount
        
        invoice = {
            "id": invoice_id,
            "client": {
                "name": client_info.get('name', 'Client'),
                "company": client_info.get('company', ''),
                "email": client_info.get('email', ''),
                "address": client_info.get('address', '')
            },
            "agency": {
                "name": "Nexora AI SEO Agency",
                "email": "billing@nexora.ai",
                "address": "Digital Valley, Tech City"
            },
            "items": items,
            "subtotal": subtotal,
            "discount_percent": discount,
            "discount_amount": round(discount_amount, 2),
            "tax_rate": tax_rate,
            "tax_amount": round(tax_amount, 2),
            "total": round(total, 2),
            "currency": "USD",
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "due_date": (datetime.now() + timedelta(days=15)).isoformat(),
            "paid_at": None,
            "notes": "Thank you for your business!"
        }
        
        self.invoices[invoice_id] = invoice
        return invoice
    
    def mark_paid(self, invoice_id: str, payment_method: str = "stripe") -> Dict:
        """Mark invoice as paid"""
        invoice = self.invoices.get(invoice_id)
        if not invoice:
            return {"error": "Invoice not found"}
        
        invoice['status'] = "paid"
        invoice['paid_at'] = datetime.now().isoformat()
        invoice['payment_method'] = payment_method
        
        return invoice
    
    def get_invoice_summary(self) -> Dict:
        """Get invoice summary"""
        total_invoiced = sum(i['total'] for i in self.invoices.values())
        total_paid = sum(i['total'] for i in self.invoices.values() if i['status'] == 'paid')
        total_pending = sum(i['total'] for i in self.invoices.values() if i['status'] == 'pending')
        
        return {
            "total_invoices": len(self.invoices),
            "total_invoiced": round(total_invoiced, 2),
            "total_paid": round(total_paid, 2),
            "total_pending": round(total_pending, 2),
            "paid_count": sum(1 for i in self.invoices.values() if i['status'] == 'paid'),
            "pending_count": sum(1 for i in self.invoices.values() if i['status'] == 'pending')
        }


class SubscriptionManager:
    """Subscription management for monthly retainers"""
    
    def __init__(self):
        self.subscriptions = {}
        self.plans = self._load_plans()
    
    def _load_plans(self) -> Dict:
        """Load subscription plans"""
        return {
            "seo_essential": {
                "name": "SEO Essential",
                "price": 500,
                "features": [
                    "Monthly SEO audit",
                    "Keyword tracking (50 keywords)",
                    "Monthly report",
                    "Email support"
                ],
                "billing_cycle": "monthly"
            },
            "seo_growth": {
                "name": "SEO Growth",
                "price": 1000,
                "features": [
                    "Everything in Essential",
                    "On-page optimization",
                    "Content recommendations",
                    "Technical SEO fixes",
                    "Weekly check-ins"
                ],
                "billing_cycle": "monthly"
            },
            "seo_dominance": {
                "name": "SEO Dominance",
                "price": 2000,
                "features": [
                    "Everything in Growth",
                    "Content creation (4 articles/month)",
                    "Link building",
                    "Competitor analysis",
                    "Dedicated account manager",
                    "Priority support"
                ],
                "billing_cycle": "monthly"
            }
        }
    
    def create_subscription(self, client_info: Dict, plan_id: str) -> Dict:
        """Create a subscription"""
        plan = self.plans.get(plan_id)
        if not plan:
            return {"error": f"Unknown plan: {plan_id}"}
        
        sub_id = str(uuid.uuid4())[:8]
        
        subscription = {
            "id": sub_id,
            "client": {
                "name": client_info.get('name', 'Client'),
                "email": client_info.get('email', ''),
                "company": client_info.get('company', '')
            },
            "plan": plan,
            "status": "active",
            "current_period_start": datetime.now().isoformat(),
            "current_period_end": (datetime.now() + timedelta(days=30)).isoformat(),
            "billing_cycle": plan['billing_cycle'],
            "amount": plan['price'],
            "payment_method": client_info.get('payment_method', 'stripe'),
            "created_at": datetime.now().isoformat(),
            "cancelled_at": None
        }
        
        self.subscriptions[sub_id] = subscription
        return subscription
    
    def cancel_subscription(self, sub_id: str, reason: str = "") -> Dict:
        """Cancel a subscription"""
        sub = self.subscriptions.get(sub_id)
        if not sub:
            return {"error": "Subscription not found"}
        
        sub['status'] = "cancelled"
        sub['cancelled_at'] = datetime.now().isoformat()
        sub['cancellation_reason'] = reason
        
        return sub
    
    def get_mrr(self) -> Dict:
        """Get Monthly Recurring Revenue"""
        active_subs = [s for s in self.subscriptions.values() if s['status'] == 'active']
        mrr = sum(s['amount'] for s in active_subs)
        
        return {
            "mrr": mrr,
            "active_subscriptions": len(active_subs),
            "arr": mrr * 12,
            "average_revenue_per_client": round(mrr / max(len(active_subs), 1), 2),
            "plans_breakdown": {
                plan_id: {
                    "count": sum(1 for s in active_subs if s['plan']['name'] == plan_data['name']),
                    "revenue": sum(s['amount'] for s in active_subs if s['plan']['name'] == plan_data['name'])
                }
                for plan_id, plan_data in self.plans.items()
            }
        }


class PaymentSystem:
    """Complete Payment & Contracts System"""
    
    def __init__(self):
        self.contracts = ContractManager()
        self.invoices = InvoiceGenerator()
        self.subscriptions = SubscriptionManager()
    
    def onboard_with_payment(self, client_info: Dict, project_info: Dict, 
                            plan_id: str = None) -> Dict:
        """Complete onboarding with contract, invoice, and subscription"""
        
        results = {
            "client": client_info.get('name'),
            "company": client_info.get('company'),
            "contract": None,
            "invoice": None,
            "subscription": None
        }
        
        # 1. Generate contract
        contract_type = "monthly_seo" if plan_id else "project_based"
        contract = self.contracts.generate_contract(contract_type, client_info, project_info)
        results['contract'] = contract
        
        # 2. Generate invoice
        items = [
            {"description": project_info.get('name', 'SEO Services'), 
             "quantity": 1, 
             "amount": project_info.get('budget', 0)}
        ]
        invoice = self.invoices.generate_invoice(client_info, items)
        results['invoice'] = invoice
        
        # 3. Create subscription if plan specified
        if plan_id:
            sub = self.subscriptions.create_subscription(client_info, plan_id)
            results['subscription'] = sub
        
        return results
    
    def get_financial_summary(self) -> Dict:
        """Get complete financial summary"""
        mrr_data = self.subscriptions.get_mrr()
        invoice_summary = self.invoices.get_invoice_summary()
        
        return {
            "mrr": mrr_data['mrr'],
            "arr": mrr_data['arr'],
            "active_subscriptions": mrr_data['active_subscriptions'],
            "total_invoiced": invoice_summary['total_invoiced'],
            "total_paid": invoice_summary['total_paid'],
            "total_pending": invoice_summary['total_pending'],
            "outstanding": invoice_summary['total_pending'],
            "revenue_breakdown": {
                "subscriptions": mrr_data['mrr'],
                "one_time_projects": invoice_summary['total_paid'] - mrr_data['mrr']
            }
        }


def demonstrate_payment_system():
    """Demonstrate Payment & Contracts System"""
    print(f"\n{'='*80}")
    print("PAYMENT & CONTRACTS SYSTEM - Module 4")
    print(f"{'='*80}\n")
    
    system = PaymentSystem()
    
    # Client info
    client = {
        "name": "Sarah Johnson",
        "company": "TechFlow SaaS",
        "email": "sarah@techflow.com",
        "address": "123 Tech Street, Silicon Valley, CA"
    }
    
    # 1. Contract Generation
    print("1. Contract Generation")
    print("─" * 60)
    contract = system.contracts.generate_contract("monthly_seo", client, {
        "name": "Monthly SEO Services",
        "description": "Comprehensive monthly SEO management",
        "budget": 2000,
        "timeline": "Ongoing"
    })
    print(f"  Contract: {contract['title']}")
    print(f"  Type: {contract['type']}")
    print(f"  Status: {contract['status']}")
    print(f"  Sections: {', '.join(contract['sections'])}")
    
    # 2. Invoice Generation
    print("\n2. Invoice Generation")
    print("─" * 60)
    invoice = system.invoices.generate_invoice(client, [
        {"description": "Monthly SEO Retainer - January", "quantity": 1, "amount": 2000},
        {"description": "Keyword Research Add-on", "quantity": 1, "amount": 500}
    ], tax_rate=8.5)
    print(f"  Invoice: {invoice['id']}")
    print(f"  Subtotal: ${invoice['subtotal']:,.2f}")
    print(f"  Tax (8.5%): ${invoice['tax_amount']:,.2f}")
    print(f"  Total: ${invoice['total']:,.2f}")
    print(f"  Due: {invoice['due_date']}")
    
    # 3. Mark as paid
    system.invoices.mark_paid(invoice['id'], "stripe")
    print(f"\n  ✅ Invoice {invoice['id']} marked as paid")
    
    # 4. Subscription Management
    print("\n3. Subscription Plans")
    print("─" * 60)
    for plan_id, plan in system.subscriptions.plans.items():
        print(f"  {plan['name']:20s}: ${plan['price']:>4}/month")
    
    # Create subscriptions
    system.subscriptions.create_subscription(client, "seo_growth")
    system.subscriptions.create_subscription({
        "name": "Mike Brown", "email": "mike@citydental.com", "company": "City Dental"
    }, "seo_essential")
    
    # MRR Report
    print("\n4. MRR Report")
    print("─" * 60)
    mrr = system.subscriptions.get_mrr()
    print(f"  Monthly Recurring Revenue: ${mrr['mrr']:,}")
    print(f"  Annual Run Rate (ARR): ${mrr['arr']:,}")
    print(f"  Active Subscriptions: {mrr['active_subscriptions']}")
    print(f"  Avg Revenue/Client: ${mrr['average_revenue_per_client']:,.2f}")
    
    # 5. Financial Summary
    print("\n5. Complete Financial Summary")
    print("─" * 60)
    summary = system.get_financial_summary()
    print(f"  MRR: ${summary['mrr']:,}")
    print(f"  ARR: ${summary['arr']:,}")
    print(f"  Total Invoiced: ${summary['total_invoiced']:,.2f}")
    print(f"  Total Paid: ${summary['total_paid']:,.2f}")
    print(f"  Outstanding: ${summary['outstanding']:,.2f}")
    
    print(f"\n{'='*80}")
    print("MODULE 4: PAYMENT & CONTRACTS - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Contract templates (SEO Audit, Monthly Retainer, Project-Based)")
    print("✓ Invoice generation with tax and discounts")
    print("✓ Subscription management (3 plans)")
    print("✓ MRR/ARR tracking")
    print("✓ Payment status tracking")
    print("✓ Financial summaries")
    print("\nNext: Integrate with Stripe for real payment processing")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_payment_system()
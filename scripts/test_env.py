#!/usr/bin/env python3
"""
Nexora AI Agency - Environment Variables Test
Verifies all required API keys and configuration are set
"""

import os
from typing import Dict, List


REQUIRED_VARS = {
    "DATABASE_URL": "PostgreSQL database connection",
    "OPENAI_API_KEY": "OpenAI GPT-4 access",
    "ANTHROPIC_API_KEY": "Claude access",
    "GOOGLE_CLIENT_ID": "Google OAuth client ID",
    "GOOGLE_CLIENT_SECRET": "Google OAuth secret",
    "GSC_REFRESH_TOKEN": "Google Search Console refresh token",
    "GA4_PROPERTY_ID": "Google Analytics 4 property ID",
    "STRIPE_SECRET_KEY": "Stripe payment processing",
    "STRIPE_WEBHOOK_SECRET": "Stripe webhook verification",
    "AHREFS_API_KEY": "Ahrefs SEO data access",
    "SEMRUSH_API_KEY": "SEMrush API access"
}


def check_env_vars() -> Dict:
    """Check all required environment variables"""
    results = {
        "configured": [],
        "missing": [],
        "total": len(REQUIRED_VARS),
        "ready": False
    }
    
    for var, description in REQUIRED_VARS.items():
        value = os.environ.get(var)
        if value and value != "" and not value.startswith("your-") and not value.startswith("sk_test_"):
            results["configured"].append({"var": var, "description": description})
        else:
            results["missing"].append({"var": var, "description": description})
    
    results["ready"] = len(results["missing"]) == 0
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("ENVIRONMENT VARIABLES CHECK")
    print("=" * 60)
    
    results = check_env_vars()
    
    print(f"\nConfigured ({len(results['configured'])}/{results['total']}):")
    for item in results["configured"]:
        print(f"  ✅ {item['var']}")
    
    print(f"\nMissing ({len(results['missing'])}/{results['total']}):")
    for item in results["missing"]:
        print(f"  ⚠️ {item['var']} - {item['description']}")
    
    print("\n" + "=" * 60)
    if results["ready"]:
        print("✅ READY FOR INTEGRATION TESTS")
    else:
        print("⚠️ CONFIGURATION INCOMPLETE - Set missing variables in .env")
    print("=" * 60)
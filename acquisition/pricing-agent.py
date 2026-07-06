#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Pricing Agent
Recommends pricing based on country, competition, client budget, website size, and project complexity.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os


class PricingAgent:
    """Pricing Agent - Intelligent pricing recommendations"""
    
    def __init__(self):
        self.base_prices = self._load_base_prices()
        self.country_adjustments = self._load_country_adjustments()
        self.competition_factors = self._load_competition_factors()
    
    def _load_base_prices(self) -> Dict:
        """Load base prices for services"""
        return {
            "seo_audit": {
                "base": 250,
                "hourly_rate": 75,
                "estimated_hours": 3,
                "description": "Comprehensive SEO audit and analysis"
            },
            "keyword_research": {
                "base": 200,
                "hourly_rate": 60,
                "estimated_hours": 3,
                "description": "In-depth keyword research and strategy"
            },
            "technical_seo": {
                "base": 400,
                "hourly_rate": 80,
                "estimated_hours": 5,
                "description": "Technical SEO fixes and optimization"
            },
            "onpage_seo": {
                "base": 300,
                "hourly_rate": 70,
                "estimated_hours": 4,
                "description": "On-page SEO optimization"
            },
            "content_strategy": {
                "base": 350,
                "hourly_rate": 65,
                "estimated_hours": 5,
                "description": "Content strategy development"
            },
            "link_building": {
                "base": 500,
                "hourly_rate": 75,
                "estimated_hours": 7,
                "description": "Link building campaign"
            },
            "local_seo": {
                "base": 300,
                "hourly_rate": 65,
                "estimated_hours": 4,
                "description": "Local SEO optimization"
            },
            "monthly_seo": {
                "base": 800,
                "hourly_rate": 70,
                "estimated_hours": 12,
                "description": "Monthly SEO management"
            },
            "premium_seo": {
                "base": 1200,
                "hourly_rate": 90,
                "estimated_hours": 15,
                "description": "Premium monthly SEO services"
            },
            "ecommerce_seo": {
                "base": 600,
                "hourly_rate": 80,
                "estimated_hours": 8,
                "description": "E-commerce SEO optimization"
            },
            "migration_seo": {
                "base": 1000,
                "hourly_rate": 85,
                "estimated_hours": 12,
                "description": "Website migration SEO"
            }
        }
    
    def _load_country_adjustments(self) -> Dict:
        """Load country-specific pricing adjustments"""
        return {
            "United States": {"multiplier": 1.0, "label": "US Market Rate"},
            "United Kingdom": {"multiplier": 0.95, "label": "UK Market Rate"},
            "Canada": {"multiplier": 0.90, "label": "CA Market Rate"},
            "Australia": {"multiplier": 0.95, "label": "AU Market Rate"},
            "Germany": {"multiplier": 0.90, "label": "DE Market Rate"},
            "France": {"multiplier": 0.85, "label": "FR Market Rate"},
            "India": {"multiplier": 0.50, "label": "IN Market Rate"},
            "Philippines": {"multiplier": 0.40, "label": "PH Market Rate"},
            "Pakistan": {"multiplier": 0.35, "label": "PK Market Rate"},
            "Bangladesh": {"multiplier": 0.30, "label": "BD Market Rate"},
            "Indonesia": {"multiplier": 0.45, "label": "ID Market Rate"},
            "Brazil": {"multiplier": 0.55, "label": "BR Market Rate"},
            "Mexico": {"multiplier": 0.50, "label": "MX Market Rate"},
            "Nigeria": {"multiplier": 0.35, "label": "NG Market Rate"},
            "South Africa": {"multiplier": 0.55, "label": "ZA Market Rate"},
            "UAE": {"multiplier": 0.85, "label": "UAE Market Rate"},
            "Singapore": {"multiplier": 0.90, "label": "SG Market Rate"},
            "global": {"multiplier": 0.75, "label": "Global Market Rate"}
        }
    
    def _load_competition_factors(self) -> Dict:
        """Load competition-based pricing factors"""
        return {
            "low": {
                "multiplier": 0.85,
                "strategy": "Competitive pricing to capture market share",
                "description": "Few competitors, less price pressure"
            },
            "medium": {
                "multiplier": 1.0,
                "strategy": "Market-rate pricing with value emphasis",
                "description": "Moderate competition, standard pricing"
            },
            "high": {
                "multiplier": 1.15,
                "strategy": "Premium pricing with differentiation",
                "description": "Many competitors, differentiate on quality"
            },
            "very_high": {
                "multiplier": 1.25,
                "strategy": "Premium pricing, emphasize unique value",
                "description": "Extremely competitive market"
            }
        }
    
    def calculate_price(self, service_type: str, context: Dict) -> Dict:
        """Calculate recommended price based on context"""
        
        service_data = self.base_prices.get(service_type)
        if not service_data:
            return {"error": f"Unknown service type: {service_type}"}
        
        base_price = service_data['base']
        
        # Country adjustment
        country = context.get('country', 'global')
        country_data = self.country_adjustments.get(country, self.country_adjustments['global'])
        country_multiplier = country_data['multiplier']
        
        # Competition adjustment
        competition = context.get('competition', 'medium')
        competition_data = self.competition_factors.get(competition, self.competition_factors['medium'])
        competition_multiplier = competition_data['multiplier']
        
        # Client budget adjustment
        client_budget = context.get('client_budget', 0)
        budget_multiplier = self._calculate_budget_multiplier(client_budget, base_price)
        
        # Website size adjustment
        website_size = context.get('website_size', 'small')
        size_multiplier = self._calculate_size_multiplier(website_size)
        
        # Complexity adjustment
        complexity = context.get('complexity', 'medium')
        complexity_multiplier = self._calculate_complexity_multiplier(complexity)
        
        # Calculate final price
        final_price = base_price * country_multiplier * competition_multiplier * budget_multiplier * size_multiplier * complexity_multiplier
        
        # Calculate package prices
        packages = self._generate_packages(final_price, service_type)
        
        return {
            "service": service_type,
            "service_description": service_data['description'],
            "base_price": base_price,
            "calculated_price": round(final_price, -1),  # Round to nearest 10
            "price_breakdown": {
                "base_price": base_price,
                "country_adjustment": {
                    "factor": country_multiplier,
                    "description": country_data['label']
                },
                "competition_adjustment": {
                    "factor": competition_multiplier,
                    "description": competition_data['description']
                },
                "budget_adjustment": {
                    "factor": budget_multiplier,
                    "description": "Adjusted for client budget range"
                },
                "size_adjustment": {
                    "factor": size_multiplier,
                    "description": f"Adjusted for {website_size} website"
                },
                "complexity_adjustment": {
                    "factor": complexity_multiplier,
                    "description": f"Adjusted for {complexity} complexity"
                }
            },
            "packages": packages,
            "competition_strategy": competition_data['strategy'],
            "recommended_hours": service_data['estimated_hours'],
            "hourly_rate_equivalent": round(final_price / service_data['estimated_hours'], -1),
            "market_position": self._determine_market_position(final_price, base_price),
            "confidence_score": self._calculate_confidence(context)
        }
    
    def _calculate_budget_multiplier(self, client_budget: float, base_price: float) -> float:
        """Calculate budget-based multiplier"""
        if client_budget <= 0:
            return 1.0
        
        ratio = client_budget / base_price
        
        if ratio >= 3:
            return 1.3  # Client has high budget, can charge premium
        elif ratio >= 2:
            return 1.15  # Good budget
        elif ratio >= 1.5:
            return 1.0  # In range
        elif ratio >= 1.0:
            return 0.9  # Slightly below
        else:
            return 0.8  # Limited budget
    
    def _calculate_size_multiplier(self, website_size: str) -> float:
        """Calculate website size multiplier"""
        multipliers = {
            "small": 0.8,     # < 10 pages
            "medium": 1.0,    # 10-50 pages
            "large": 1.3,     # 50-200 pages
            "enterprise": 1.6 # 200+ pages
        }
        return multipliers.get(website_size, 1.0)
    
    def _calculate_complexity_multiplier(self, complexity: str) -> float:
        """Calculate complexity multiplier"""
        multipliers = {
            "simple": 0.7,
            "medium": 1.0,
            "complex": 1.4,
            "very_complex": 1.8
        }
        return multipliers.get(complexity, 1.0)
    
    def _generate_packages(self, calculated_price: float, service_type: str) -> List[Dict]:
        """Generate pricing packages"""
        return [
            {
                "name": "Basic",
                "price": round(calculated_price * 0.7, -1),
                "description": "Essential features",
                "recommended": False,
                "savings": None
            },
            {
                "name": "Standard",
                "price": round(calculated_price, -1),
                "description": "Comprehensive service",
                "recommended": True,
                "savings": None
            },
            {
                "name": "Premium",
                "price": round(calculated_price * 1.4, -1),
                "description": "Full package with extras",
                "recommended": False,
                "savings": "20% more value"
            }
        ]
    
    def _determine_market_position(self, calculated_price: float, base_price: float) -> str:
        """Determine market position"""
        ratio = calculated_price / base_price
        
        if ratio >= 1.3:
            return "Premium"
        elif ratio >= 1.0:
            return "Market Rate"
        elif ratio >= 0.7:
            return "Competitive"
        else:
            return "Budget"
    
    def _calculate_confidence(self, context: Dict) -> float:
        """Calculate confidence score for pricing recommendation"""
        confidence = 50  # Base confidence
        
        if context.get('country'):
            confidence += 15
        if context.get('competition'):
            confidence += 10
        if context.get('client_budget'):
            confidence += 15
        if context.get('website_size'):
            confidence += 5
        if context.get('complexity'):
            confidence += 5
        
        return min(100, confidence)
    
    def get_service_catalog(self, context: Dict = None) -> Dict:
        """Get complete service catalog with prices"""
        if context is None:
            context = {
                "country": "global",
                "competition": "medium",
                "client_budget": 0,
                "website_size": "small",
                "complexity": "medium"
            }
        
        catalog = {}
        for service_type in self.base_prices:
            catalog[service_type] = self.calculate_price(service_type, context)
        
        return catalog
    
    def get_pricing_guide(self) -> Dict:
        """Get pricing guide with recommendations"""
        return {
            "quick_prices": {
                "SEO Audit": "$100 - $500",
                "Keyword Research": "$150 - $500",
                "Technical SEO": "$300 - $1,000",
                "Monthly SEO": "$600 - $2,500",
                "Premium SEO": "$1,200 - $5,000",
                "Local SEO": "$300 - $800",
                "E-commerce SEO": "$500 - $2,000"
            },
            "pricing_strategy": {
                "approach": "Value-based pricing",
                "factors": [
                    "Country market rates",
                    "Competition level",
                    "Client budget",
                    "Website size",
                    "Project complexity",
                    "Urgency",
                    "ROI potential"
                ],
                "principles": [
                    "Price based on value, not time",
                    "Offer packages for different budgets",
                    "Premium positioning for quality clients",
                    "Competitive pricing for portfolio building"
                ]
            }
        }
    
    def compare_competitors(self, service_type: str, competitor_prices: List[float]) -> Dict:
        """Compare pricing with competitors"""
        our_price = self.calculate_price(service_type, {
            "country": "global",
            "competition": "medium",
            "client_budget": 0,
            "website_size": "small",
            "complexity": "medium"
        })
        
        avg_competitor = sum(competitor_prices) / len(competitor_prices) if competitor_prices else 0
        
        return {
            "service": service_type,
            "our_price": our_price['calculated_price'],
            "average_competitor_price": round(avg_competitor, -1),
            "price_difference": round(our_price['calculated_price'] - avg_competitor, -1),
            "position": "premium" if our_price['calculated_price'] > avg_competitor else "competitive",
            "recommendation": "Maintain current pricing" if our_price['calculated_price'] > avg_competitor else "Consider increasing prices"
        }


def demonstrate_pricing_agent():
    """Demonstrate Pricing Agent"""
    print(f"\n{'='*80}")
    print("PRICING AGENT - Demonstration")
    print(f"{'='*80}\n")
    
    agent = PricingAgent()
    
    # Example 1: Calculate price for a US client
    print("1. Price Calculation Example (US Client)")
    print("─" * 60)
    
    context = {
        "country": "United States",
        "competition": "high",
        "client_budget": 3000,
        "website_size": "medium",
        "complexity": "medium"
    }
    
    price = agent.calculate_price("monthly_seo", context)
    print(f"Service: Monthly SEO")
    print(f"Base Price: ${price['base_price']}")
    print(f"Calculated Price: ${price['calculated_price']:,}")
    print(f"Market Position: {price['market_position']}")
    print(f"Confidence: {price['confidence_score']}/100")
    
    print(f"\nPrice Breakdown:")
    for factor, data in price['price_breakdown'].items():
        print(f"  • {factor.replace('_', ' ').title()}: {data['factor']}x ({data['description']})")
    
    print(f"\nPackages:")
    for pkg in price['packages']:
        flag = " ★ RECOMMENDED" if pkg['recommended'] else ""
        print(f"  • {pkg['name']}: ${pkg['price']:,}{flag}")
    
    print(f"\nStrategy: {price['competition_strategy']}")
    
    # Example 2: Price comparison across countries
    print("\n\n2. Price Comparison Across Countries")
    print("─" * 60)
    
    countries = ["United States", "United Kingdom", "India", "Bangladesh", "UAE"]
    for country in countries:
        context = {
            "country": country,
            "competition": "medium",
            "client_budget": 0,
            "website_size": "small",
            "complexity": "medium"
        }
        price = agent.calculate_price("seo_audit", context)
        print(f"  {country:20s}: ${price['calculated_price']:>5,} ({price['market_position']})")
    
    # Example 3: Quick pricing guide
    print("\n\n3. Quick Pricing Guide")
    print("─" * 60)
    guide = agent.get_pricing_guide()
    for service, price_range in guide['quick_prices'].items():
        print(f"  • {service:25s}: {price_range}")
    
    # Example 4: Competitor comparison
    print("\n\n4. Competitor Price Comparison")
    print("─" * 60)
    comparison = agent.compare_competitors("monthly_seo", [500, 750, 600, 900, 650])
    print(f"  Our Price: ${comparison['our_price']:,}")
    print(f"  Avg Competitor: ${comparison['average_competitor_price']:,}")
    print(f"  Difference: ${comparison['price_difference']:,}")
    print(f"  Position: {comparison['position'].title()}")
    
    # Example 5: Full service catalog
    print("\n\n5. Service Catalog (US Market)")
    print("─" * 60)
    context = {
        "country": "United States",
        "competition": "medium",
        "client_budget": 2000,
        "website_size": "medium",
        "complexity": "medium"
    }
    catalog = agent.get_service_catalog(context)
    for service, data in catalog.items():
        print(f"  • {service.replace('_', ' ').title():25s}: ${data['calculated_price']:>5,} ({data['market_position']})")
    
    print(f"\n{'='*80}")
    print("PRICING AGENT - READY")
    print(f"{'='*80}")
    print("\nFeatures:")
    print("✓ Country-specific pricing (18 countries)")
    print("✓ Competition-based adjustments")
    print("✓ Client budget optimization")
    print("✓ Website size scaling")
    print("✓ Complexity-based pricing")
    print("✓ 3-tier package generation")
    print("✓ Competitor price comparison")
    print("✓ Market position analysis")
    print("✓ Confidence scoring")
    print("\nOutputs: Recommended prices, Packages, Market position, Strategy")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    demonstrate_pricing_agent()
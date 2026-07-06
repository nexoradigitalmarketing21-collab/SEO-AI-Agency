#!/usr/bin/env python3
"""
Nexora AI SEO Agency - LLM Router
Milestone 1: Intelligent routing between AI providers (OpenAI, Gemini, OpenRouter, Anthropic, Groq)
with automatic fallback, cost optimization, and health monitoring.
"""

from typing import Dict, List, Optional, Callable, Any
from datetime import datetime, timedelta
import json
import os
import time
import hashlib
import threading


class ProviderHealth:
    """Track provider health and availability"""
    
    def __init__(self, provider: str):
        self.provider = provider
        self.success_count = 0
        self.failure_count = 0
        self.total_latency = 0.0
        self.last_failure = None
        self.consecutive_failures = 0
        self.is_available = True
        self.rate_limit_remaining = 1000
        self.rate_limit_reset = datetime.now()
    
    def record_success(self, latency: float):
        """Record a successful call"""
        self.success_count += 1
        self.total_latency += latency
        self.consecutive_failures = 0
        self.is_available = True
    
    def record_failure(self, error_type: str = "unknown"):
        """Record a failure"""
        self.failure_count += 1
        self.last_failure = datetime.now()
        self.consecutive_failures += 1
        if self.consecutive_failures >= 3:
            self.is_available = False
            # Auto-recover after 60 seconds
            threading.Timer(60.0, self._recover).start()
    
    def _recover(self):
        """Attempt to recover provider"""
        self.consecutive_failures = 0
        self.is_available = True
    
    def get_avg_latency(self) -> float:
        """Get average latency"""
        total = self.success_count + self.failure_count
        if total == 0:
            return 0.0
        return round(self.total_latency / max(self.success_count, 1), 2)
    
    def get_uptime(self) -> float:
        """Get uptime percentage"""
        total = self.success_count + self.failure_count
        if total == 0:
            return 100.0
        return round((self.success_count / total) * 100, 1)


class LLMRouter:
    """
    Intelligent LLM router with multi-provider support.
    Routes requests based on task type, cost, latency, and availability.
    """
    
    PROVIDERS = {
        "openai": {
            "base_url": "https://api.openai.com/v1",
            "api_key_env": "OPENAI_API_KEY",
            "models": {
                "gpt-4o": {"cost_input": 0.01, "cost_output": 0.03, "context": 128000, "tier": "premium"},
                "gpt-4o-mini": {"cost_input": 0.0015, "cost_output": 0.006, "context": 128000, "tier": "balanced"},
                "gpt-3.5-turbo": {"cost_input": 0.0005, "cost_output": 0.0015, "context": 16385, "tier": "budget"},
                "o1-mini": {"cost_input": 0.003, "cost_output": 0.012, "context": 128000, "tier": "premium"}
            },
            "rate_limit": {"requests_per_min": 500, "tokens_per_min": 200000}
        },
        "anthropic": {
            "base_url": "https://api.anthropic.com/v1",
            "api_key_env": "ANTHROPIC_API_KEY",
            "models": {
                "claude-3-opus": {"cost_input": 0.015, "cost_output": 0.075, "context": 200000, "tier": "premium"},
                "claude-3-sonnet": {"cost_input": 0.003, "cost_output": 0.015, "context": 200000, "tier": "premium"},
                "claude-3-haiku": {"cost_input": 0.00025, "cost_output": 0.00125, "context": 200000, "tier": "budget"},
                "claude-3-5-sonnet": {"cost_input": 0.003, "cost_output": 0.015, "context": 200000, "tier": "premium"}
            },
            "rate_limit": {"requests_per_min": 200, "tokens_per_min": 100000}
        },
        "gemini": {
            "base_url": "https://generativelanguage.googleapis.com/v1",
            "api_key_env": "GEMINI_API_KEY",
            "models": {
                "gemini-1.5-pro": {"cost_input": 0.0035, "cost_output": 0.0105, "context": 1000000, "tier": "premium"},
                "gemini-1.5-flash": {"cost_input": 0.00035, "cost_output": 0.00105, "context": 1000000, "tier": "budget"},
                "gemini-2.0-flash": {"cost_input": 0.0001, "cost_output": 0.0004, "context": 1000000, "tier": "budget"}
            },
            "rate_limit": {"requests_per_min": 360, "tokens_per_min": 120000}
        },
        "openrouter": {
            "base_url": "https://openrouter.ai/api/v1",
            "api_key_env": "OPENROUTER_API_KEY",
            "models": {
                "openrouter/auto": {"cost_input": 0.001, "cost_output": 0.003, "context": 128000, "tier": "balanced"},
                "mistral/mixtral-8x7b": {"cost_input": 0.0006, "cost_output": 0.0018, "context": 32768, "tier": "balanced"},
                "meta-llama/llama-3-70b": {"cost_input": 0.0008, "cost_output": 0.0024, "context": 8192, "tier": "balanced"},
                "mistral/mistral-small": {"cost_input": 0.0004, "cost_output": 0.0012, "context": 32768, "tier": "budget"}
            },
            "rate_limit": {"requests_per_min": 300, "tokens_per_min": 150000}
        },
        "groq": {
            "base_url": "https://api.groq.com/openai/v1",
            "api_key_env": "GROQ_API_KEY",
            "models": {
                "llama3-70b-8192": {"cost_input": 0.00059, "cost_output": 0.00079, "context": 8192, "tier": "budget"},
                "llama3-8b-8192": {"cost_input": 0.00005, "cost_output": 0.00008, "context": 8192, "tier": "budget"},
                "mixtral-8x7b-32768": {"cost_input": 0.00024, "cost_output": 0.00036, "context": 32768, "tier": "balanced"},
                "gemma2-9b-it": {"cost_input": 0.00005, "cost_output": 0.00008, "context": 8192, "tier": "budget"}
            },
            "rate_limit": {"requests_per_min": 30, "tokens_per_min": 15000}
        }
    }
    
    TASK_ROUTING = {
        "content_creation": {"provider": "openai", "model": "gpt-4o", "tier": "premium"},
        "content_editing": {"provider": "anthropic", "model": "claude-3-haiku", "tier": "budget"},
        "code_generation": {"provider": "anthropic", "model": "claude-3-sonnet", "tier": "premium"},
        "code_review": {"provider": "openai", "model": "gpt-4o-mini", "tier": "balanced"},
        "research": {"provider": "gemini", "model": "gemini-1.5-pro", "tier": "premium"},
        "analysis": {"provider": "openai", "model": "gpt-4o-mini", "tier": "balanced"},
        "outreach": {"provider": "anthropic", "model": "claude-3-haiku", "tier": "budget"},
        "reporting": {"provider": "openai", "model": "gpt-4o-mini", "tier": "balanced"},
        "data_extraction": {"provider": "groq", "model": "llama3-70b-8192", "tier": "budget"},
        "summarization": {"provider": "groq", "model": "mixtral-8x7b-32768", "tier": "budget"},
        "keyword_analysis": {"provider": "openai", "model": "gpt-4o-mini", "tier": "balanced"},
        "technical_audit": {"provider": "openai", "model": "gpt-4o", "tier": "premium"},
        "sales_proposal": {"provider": "anthropic", "model": "claude-3-sonnet", "tier": "premium"},
        "email_draft": {"provider": "gemini", "model": "gemini-1.5-flash", "tier": "budget"},
        "qa_review": {"provider": "anthropic", "model": "claude-3-haiku", "tier": "balanced"}
    }
    
    def __init__(self):
        self.health = {provider: ProviderHealth(provider) for provider in self.PROVIDERS}
        self.available_providers = self._check_available_providers()
        self.cache = {}
        self.cache_enabled = True
        self.cache_ttl = 3600  # 1 hour default
        self.request_queue = []
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.total_cost = 0.0
    
    def _check_available_providers(self) -> Dict:
        """Check which providers have API keys configured"""
        available = {}
        for provider_name, config in self.PROVIDERS.items():
            api_key = os.environ.get(config["api_key_env"])
            if api_key:
                available[provider_name] = {
                    "available": True,
                    "models": list(config["models"].keys()),
                    "tiers": list(set(m["tier"] for m in config["models"].values()))
                }
            else:
                available[provider_name] = {
                    "available": False,
                    "models": [],
                    "tiers": []
                }
        return available
    
    def route_request(self, task_type: str, context: Dict = None) -> Dict:
        """
        Route a request to the optimal provider and model.
        Considers task type, budget, latency, and provider health.
        """
        budget = (context or {}).get("budget", "balanced")
        
        # Get default routing for task type
        route = self.TASK_ROUTING.get(task_type, self.TASK_ROUTING["analysis"])
        
        # Adjust for budget
        if budget == "budget":
            route = self._get_budget_route(task_type)
        elif budget == "premium" and route.get("tier") != "premium":
            route = self._get_premium_route(task_type)
        
        # Check if primary provider is available and healthy
        primary = self._get_healthy_provider(route["provider"])
        if primary:
            return {
                "provider": primary,
                "model": route["model"],
                "tier": route.get("tier", "balanced"),
                "status": "primary"
            }
        
        # Fallback logic
        fallback = self._find_fallback(task_type, budget)
        if fallback:
            return {**fallback, "status": "fallback"}
        
        return {"provider": None, "model": None, "status": "no_providers_available"}
    
    def _get_healthy_provider(self, preferred: str) -> Optional[str]:
        """Check if preferred provider is healthy, return it or None"""
        if preferred in self.health and self.health[preferred].is_available:
            if self.available_providers.get(preferred, {}).get("available"):
                return preferred
        return None
    
    def _get_budget_route(self, task_type: str) -> Dict:
        """Get budget-friendly routing"""
        budget_routes = {
            "content_creation": {"provider": "groq", "model": "llama3-70b-8192", "tier": "budget"},
            "analysis": {"provider": "groq", "model": "mixtral-8x7b-32768", "tier": "budget"},
            "research": {"provider": "gemini", "model": "gemini-1.5-flash", "tier": "budget"},
            "summarization": {"provider": "groq", "model": "gemma2-9b-it", "tier": "budget"}
        }
        return budget_routes.get(task_type, {"provider": "openrouter", "model": "openrouter/auto", "tier": "budget"})
    
    def _get_premium_route(self, task_type: str) -> Dict:
        """Get premium routing"""
        premium_routes = {
            "analysis": {"provider": "openai", "model": "gpt-4o", "tier": "premium"},
            "research": {"provider": "anthropic", "model": "claude-3-5-sonnet", "tier": "premium"}
        }
        return premium_routes.get(task_type, {"provider": "openai", "model": "gpt-4o", "tier": "premium"})
    
    def _find_fallback(self, task_type: str, budget: str) -> Optional[Dict]:
        """Find fallback provider when primary is unavailable"""
        fallback_chain = [
            {"provider": "openai", "model": "gpt-4o-mini", "tier": "balanced"},
            {"provider": "anthropic", "model": "claude-3-haiku", "tier": "budget"},
            {"provider": "gemini", "model": "gemini-1.5-flash", "tier": "budget"},
            {"provider": "openrouter", "model": "openrouter/auto", "tier": "balanced"},
            {"provider": "groq", "model": "mixtral-8x7b-32768", "tier": "budget"}
        ]
        
        for fb in fallback_chain:
            if self._get_healthy_provider(fb["provider"]):
                return fb
        
        return None
    
    def get_fallback_chain(self, primary_provider: str, primary_model: str) -> List[Dict]:
        """Get ordered fallback chain"""
        chain = [{"provider": primary_provider, "model": primary_model}]
        
        fallbacks = [
            {"provider": "openai", "model": "gpt-4o-mini"},
            {"provider": "anthropic", "model": "claude-3-haiku"},
            {"provider": "gemini", "model": "gemini-1.5-flash"},
            {"provider": "openrouter", "model": "openrouter/auto"},
            {"provider": "groq", "model": "mixtral-8x7b-32768"}
        ]
        
        for fb in fallbacks:
            if fb["provider"] != primary_provider or fb["model"] != primary_model:
                chain.append(fb)
        
        return chain
    
    def record_result(self, provider: str, success: bool, latency: float, cost: float = 0.0):
        """Record request result for health tracking"""
        self.total_requests += 1
        
        if provider in self.health:
            if success:
                self.health[provider].record_success(latency)
                self.successful_requests += 1
                self.total_cost += cost
            else:
                self.health[provider].record_failure()
                self.failed_requests += 1
    
    def get_cache_key(self, prompt: str, model: str, temperature: float = 0.7) -> str:
        """Generate cache key"""
        return hashlib.md5(f"{prompt}:{model}:{temperature}".encode()).hexdigest()
    
    def check_cache(self, prompt: str, model: str, temperature: float = 0.7) -> Optional[str]:
        """Check if response is cached"""
        if not self.cache_enabled:
            return None
        key = self.get_cache_key(prompt, model, temperature)
        cached = self.cache.get(key)
        if cached:
            timestamp = cached.get("timestamp", 0)
            if time.time() - timestamp < self.cache_ttl:
                return cached["response"]
            else:
                del self.cache[key]
        return None
    
    def set_cache(self, prompt: str, model: str, response: str, temperature: float = 0.7):
        """Cache a response"""
        if not self.cache_enabled:
            return
        key = self.get_cache_key(prompt, model, temperature)
        self.cache[key] = {
            "response": response,
            "timestamp": time.time(),
            "model": model
        }
    
    def get_router_status(self) -> Dict:
        """Get complete router status"""
        return {
            "total_requests": self.total_requests,
            "successful": self.successful_requests,
            "failed": self.failed_requests,
            "success_rate": round((self.successful_requests / max(self.total_requests, 1)) * 100, 1),
            "total_cost": round(self.total_cost, 4),
            "cache_size": len(self.cache),
            "cache_enabled": self.cache_enabled,
            "providers": {
                name: {
                    "available": info["available"],
                    "healthy": self.health[name].is_available,
                    "uptime": self.health[name].get_uptime(),
                    "avg_latency": self.health[name].get_avg_latency(),
                    "models": info["models"],
                    "tiers": info["tiers"]
                }
                for name, info in self.available_providers.items()
            },
            "task_routes": list(self.TASK_ROUTING.keys())
        }


if __name__ == "__main__":
    router = LLMRouter()
    print("LLM Router Status:")
    status = router.get_router_status()
    print(f"  Cache Size: {status['cache_size']}")
    print(f"  Providers Configured: {sum(1 for p in status['providers'].values() if p['available'])}/{len(status['providers'])}")
    print(f"  Available Task Routes: {len(status['task_routes'])}")
    print("\nProvider Status:")
    for name, info in status['providers'].items():
        icon = "✅" if info['available'] else "⬜"
        health_icon = "🟢" if info['healthy'] else "🔴"
        print(f"  {icon} {name:12s} | Models: {len(info['models'])} | Tiers: {', '.join(info['tiers'])} | {health_icon}")
    print("\nRouting Examples:")
    for task in ["content_creation", "research", "analysis", "outreach", "data_extraction"]:
        route = router.route_request(task, {"budget": "balanced"})
        prov = route['provider'] or 'N/A'
        model = route['model'] or 'N/A'
        print(f"  {task:20s} → {prov:10s}/{model:25s} ({route['status']})")

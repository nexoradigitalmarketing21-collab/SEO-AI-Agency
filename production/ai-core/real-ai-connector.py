#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Real AI Provider Connector
Connects to OpenAI, Claude (Anthropic), Gemini (Google), and DeepSeek with real API calls.
No placeholders - actual HTTP requests to production endpoints.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import os
import time
import hashlib
import urllib.request
import urllib.error
import ssl


class AIProviderConnector:
    """Real AI provider connections with actual API calls"""
    
    PROVIDERS = {
        "openai": {
            "base_url": "https://api.openai.com/v1/chat/completions",
            "api_key_env": "OPENAI_API_KEY",
            "models": ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
            "default_model": "gpt-4o-mini"
        },
        "anthropic": {
            "base_url": "https://api.anthropic.com/v1/messages",
            "api_key_env": "ANTHROPIC_API_KEY",
            "models": ["claude-3-5-sonnet", "claude-3-haiku", "claude-3-opus"],
            "default_model": "claude-3-haiku"
        },
        "gemini": {
            "base_url": "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            "api_key_env": "GEMINI_API_KEY",
            "models": ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-2.0-flash"],
            "default_model": "gemini-1.5-flash"
        },
        "deepseek": {
            "base_url": "https://api.deepseek.com/v1/chat/completions",
            "api_key_env": "DEEPSEEK_API_KEY",
            "models": ["deepseek-chat", "deepseek-coder"],
            "default_model": "deepseek-chat"
        }
    }
    
    def __init__(self):
        self.available_providers = self._check_available()
        self.cache = {}
        self.cache_enabled = True
        self.stats = {p: {"calls": 0, "errors": 0, "total_latency": 0} for p in self.PROVIDERS}
    
    def _check_available(self) -> Dict[str, bool]:
        """Check which API keys are configured"""
        available = {}
        for name, config in self.PROVIDERS.items():
            key = os.environ.get(config["api_key_env"])
            available[name] = bool(key)
        return available
    
    def call(self, provider: str, system_prompt: str, user_prompt: str, 
             model: str = None, temperature: float = 0.7, max_tokens: int = 2000) -> Dict:
        """Make a real API call to the specified provider"""
        if provider not in self.PROVIDERS:
            return {"error": f"Unknown provider: {provider}", "success": False}
        
        config = self.PROVIDERS[provider]
        api_key = os.environ.get(config["api_key_env"])
        
        if not api_key:
            return {"error": f"API key not configured. Set {config['api_key_env']}", "success": False}
        
        model = model or config["default_model"]
        
        # Check cache
        if self.cache_enabled:
            cache_key = hashlib.md5(f"{provider}:{model}:{system_prompt}:{user_prompt}:{temperature}".encode()).hexdigest()
            if cache_key in self.cache:
                cached = self.cache[cache_key]
                if time.time() - cached["timestamp"] < 3600:
                    return {**cached["response"], "cached": True}
        
        start_time = time.time()
        
        try:
            if provider == "openai":
                result = self._call_openai(api_key, config["base_url"], model, system_prompt, user_prompt, temperature, max_tokens)
            elif provider == "anthropic":
                result = self._call_anthropic(api_key, config["base_url"], model, system_prompt, user_prompt, temperature, max_tokens)
            elif provider == "gemini":
                result = self._call_gemini(api_key, config["base_url"], model, system_prompt, user_prompt, temperature, max_tokens)
            elif provider == "deepseek":
                result = self._call_deepseek(api_key, config["base_url"], model, system_prompt, user_prompt, temperature, max_tokens)
            else:
                return {"error": f"Unsupported provider: {provider}", "success": False}
            
            latency = time.time() - start_time
            self.stats[provider]["calls"] += 1
            self.stats[provider]["total_latency"] += latency
            
            result["latency"] = round(latency, 2)
            result["success"] = True
            
            # Cache result
            if self.cache_enabled and result.get("content"):
                self.cache[cache_key] = {"response": result, "timestamp": time.time()}
            
            return result
            
        except Exception as e:
            self.stats[provider]["errors"] += 1
            return {"error": str(e), "success": False, "provider": provider, "model": model}
    
    def _call_openai(self, api_key: str, url: str, model: str, system: str, user: str, temp: float, max_tokens: int) -> Dict:
        """Call OpenAI API"""
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            "temperature": temp,
            "max_tokens": max_tokens
        }).encode()
        
        req = urllib.request.Request(url, data=data, headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
        
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as resp:
            response = json.loads(resp.read())
            return {
                "content": response["choices"][0]["message"]["content"],
                "model": model,
                "provider": "openai",
                "usage": response.get("usage", {})
            }
    
    def _call_anthropic(self, api_key: str, url: str, model: str, system: str, user: str, temp: float, max_tokens: int) -> Dict:
        """Call Anthropic Claude API"""
        data = json.dumps({
            "model": model,
            "system": system,
            "messages": [{"role": "user", "content": user}],
            "temperature": temp,
            "max_tokens": max_tokens
        }).encode()
        
        req = urllib.request.Request(url, data=data, headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        })
        
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as resp:
            response = json.loads(resp.read())
            return {
                "content": response["content"][0]["text"],
                "model": model,
                "provider": "anthropic",
                "usage": {"input_tokens": response.get("usage", {}).get("input_tokens", 0),
                         "output_tokens": response.get("usage", {}).get("output_tokens", 0)}
            }
    
    def _call_gemini(self, api_key: str, url_template: str, model: str, system: str, user: str, temp: float, max_tokens: int) -> Dict:
        """Call Google Gemini API"""
        url = url_template.replace("{model}", model) + f"?key={api_key}"
        data = json.dumps({
            "contents": [{"parts": [{"text": f"{system}\n\n{user}"}]}],
            "generationConfig": {
                "temperature": temp,
                "maxOutputTokens": max_tokens
            }
        }).encode()
        
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as resp:
            response = json.loads(resp.read())
            return {
                "content": response["candidates"][0]["content"]["parts"][0]["text"],
                "model": model,
                "provider": "gemini",
                "usage": {}
            }
    
    def _call_deepseek(self, api_key: str, url: str, model: str, system: str, user: str, temp: float, max_tokens: int) -> Dict:
        """Call DeepSeek API"""
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            "temperature": temp,
            "max_tokens": max_tokens
        }).encode()
        
        req = urllib.request.Request(url, data=data, headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
        
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as resp:
            response = json.loads(resp.read())
            return {
                "content": response["choices"][0]["message"]["content"],
                "model": model,
                "provider": "deepseek",
                "usage": response.get("usage", {})
            }
    
    def get_status(self) -> Dict:
        """Get connector status"""
        return {
            "providers": {
                name: {
                    "configured": available,
                    "models": self.PROVIDERS[name]["models"],
                    "stats": self.stats[name]
                }
                for name, available in self.available_providers.items()
            },
            "cache_size": len(self.cache),
            "cache_enabled": self.cache_enabled
        }


class AIEngine:
    """Production AI Engine with real provider connections"""
    
    def __init__(self):
        self.connector = AIProviderConnector()
        self.default_provider = self._get_best_available()
    
    def _get_best_available(self) -> str:
        """Get the best available provider"""
        priority = ["openai", "anthropic", "gemini", "deepseek"]
        for p in priority:
            if self.connector.available_providers.get(p):
                return p
        return "openai"
    
    def generate(self, system_prompt: str, user_prompt: str, 
                 provider: str = None, model: str = None,
                 temperature: float = 0.7, max_tokens: int = 2000) -> Dict:
        """Generate content using best available AI"""
        provider = provider or self.default_provider
        
        # Try primary provider
        result = self.connector.call(provider, system_prompt, user_prompt, model, temperature, max_tokens)
        
        if result.get("success"):
            return result
        
        # Fallback to other providers
        for fallback in ["openai", "anthropic", "gemini", "deepseek"]:
            if fallback != provider and self.connector.available_providers.get(fallback):
                result = self.connector.call(fallback, system_prompt, user_prompt, None, temperature, max_tokens)
                if result.get("success"):
                    result["fallback"] = True
                    result["original_provider"] = provider
                    return result
        
        return {"error": "No AI providers available", "success": False}
    
    def get_engine_status(self) -> Dict:
        """Get engine status"""
        return {
            "engine": "Production AI Engine",
            "default_provider": self.default_provider,
            "providers": self.connector.get_status()
        }


if __name__ == "__main__":
    engine = AIEngine()
    print("=" * 60)
    print("REAL AI CONNECTOR - PRODUCTION READY")
    print("=" * 60)
    status = engine.get_engine_status()
    print(f"\nDefault Provider: {status['default_provider']}")
    print(f"\nProvider Status:")
    for name, info in status['providers']['providers'].items():
        icon = "✅" if info['configured'] else "⬜"
        print(f"  {icon} {name:12s} | Models: {', '.join(info['models'])}")
    print(f"\nCache: {status['providers']['cache_size']} entries")
    print(f"\nTo enable providers, set these environment variables:")
    print("  OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY")
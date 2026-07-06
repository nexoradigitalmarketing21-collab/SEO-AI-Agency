#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Token Monitor
Milestone 1: Real-time token usage monitoring, rate limiting, and usage analytics.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta, date
import json
import time
import threading


class TokenBucket:
    """Token bucket rate limiter"""
    
    def __init__(self, rate: float, burst: int):
        self.rate = rate  # tokens per second
        self.burst = burst  # max burst size
        self.tokens = burst
        self.last_refill = time.time()
        self.lock = threading.Lock()
    
    def consume(self, tokens: int = 1) -> bool:
        """Try to consume tokens. Returns True if allowed."""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill
            self.tokens = min(self.burst, self.tokens + elapsed * self.rate)
            self.last_refill = now
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
    
    def get_available(self) -> float:
        """Get available tokens"""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill
            return min(self.burst, self.tokens + elapsed * self.rate)


class TokenUsage:
    """Track token usage for a single request"""
    
    def __init__(self, provider: str, model: str, task_type: str):
        self.provider = provider
        self.model = model
        self.task_type = task_type
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0
        self.start_time = time.time()
        self.end_time = None
        self.latency_ms = 0
    
    def complete(self, prompt_tokens: int, completion_tokens: int):
        """Record completion"""
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = prompt_tokens + completion_tokens
        self.end_time = time.time()
        self.latency_ms = int((self.end_time - self.start_time) * 1000)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "provider": self.provider,
            "model": self.model,
            "task_type": self.task_type,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
            "latency_ms": self.latency_ms
        }


class TokenMonitor:
    """Real-time token usage monitoring and analytics"""
    
    RATE_LIMITS = {
        "openai": TokenBucket(500/60, 500),  # 500 RPM
        "anthropic": TokenBucket(200/60, 200),
        "gemini": TokenBucket(360/60, 360),
        "groq": TokenBucket(30/60, 30),
        "openrouter": TokenBucket(300/60, 300)
    }
    
    def __init__(self):
        self.usage_history = []
        self.active_sessions = {}
        self.daily_usage = {}
        self.provider_totals = {}
        self.model_totals = {}
        self.warnings = []
        self.lock = threading.Lock()
        
        # Start background monitoring
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
    
    def start_session(self, session_id: str, provider: str, model: str, task_type: str) -> TokenUsage:
        """Start tracking a new API session"""
        usage = TokenUsage(provider, model, task_type)
        self.active_sessions[session_id] = usage
        return usage
    
    def end_session(self, session_id: str, prompt_tokens: int, completion_tokens: int) -> Dict:
        """End a session and record usage"""
        usage = self.active_sessions.pop(session_id, None)
        if not usage:
            return {"error": "Session not found"}
        
        usage.complete(prompt_tokens, completion_tokens)
        
        with self.lock:
            self.usage_history.append(usage)
            
            # Update daily totals
            today = date.today().isoformat()
            if today not in self.daily_usage:
                self.daily_usage[today] = {"tokens": 0, "calls": 0}
            self.daily_usage[today]["tokens"] += usage.total_tokens
            self.daily_usage[today]["calls"] += 1
            
            # Update provider totals
            if usage.provider not in self.provider_totals:
                self.provider_totals[usage.provider] = {"tokens": 0, "calls": 0}
            self.provider_totals[usage.provider]["tokens"] += usage.total_tokens
            self.provider_totals[usage.provider]["calls"] += 1
            
            # Update model totals
            model_key = f"{usage.provider}/{usage.model}"
            if model_key not in self.model_totals:
                self.model_totals[model_key] = {"tokens": 0, "calls": 0}
            self.model_totals[model_key]["tokens"] += usage.total_tokens
            self.model_totals[model_key]["calls"] += 1
        
        return usage.to_dict()
    
    def check_rate_limit(self, provider: str, tokens: int = 1) -> bool:
        """Check if request is within rate limits"""
        limiter = self.RATE_LIMITS.get(provider)
        if not limiter:
            return True  # No limit for unknown providers
        return limiter.consume(tokens)
    
    def get_available_tokens(self, provider: str) -> float:
        """Get available tokens for a provider"""
        limiter = self.RATE_LIMITS.get(provider)
        if not limiter:
            return float('inf')
        return limiter.get_available()
    
    def _monitor_loop(self):
        """Background monitoring loop"""
        while self.monitoring:
            time.sleep(60)  # Check every minute
            
            # Check for anomalies
            with self.lock:
                # Check daily usage spikes
                today = date.today().isoformat()
                if today in self.daily_usage:
                    daily_tokens = self.daily_usage[today]["tokens"]
                    # Compare to average
                    avg = self._get_daily_average()
                    if avg > 0 and daily_tokens > avg * 2:
                        self.warnings.append({
                            "type": "usage_spike",
                            "message": f"Daily token usage ({daily_tokens:,}) is 2x above average ({avg:,})",
                            "timestamp": datetime.now().isoformat()
                        })
    
    def _get_daily_average(self) -> float:
        """Get average daily token usage"""
        if len(self.daily_usage) < 2:
            return 0.0
        total = sum(d["tokens"] for d in list(self.daily_usage.values())[:-1])  # Exclude today
        return total / max(len(self.daily_usage) - 1, 1)
    
    def get_daily_usage(self, days: int = 30) -> List[Dict]:
        """Get daily token usage"""
        today = date.today()
        result = []
        
        for i in range(days - 1, -1, -1):
            d = (today - timedelta(days=i)).isoformat()
            usage = self.daily_usage.get(d, {"tokens": 0, "calls": 0})
            result.append({
                "date": d,
                "tokens": usage["tokens"],
                "calls": usage["calls"]
            })
        
        return result
    
    def get_recent_usage(self, limit: int = 10) -> List[Dict]:
        """Get most recent usage entries"""
        recent = self.usage_history[-limit:] if len(self.usage_history) > 0 else []
        return [u.to_dict() for u in recent]
    
    def get_warnings(self, clear: bool = True) -> List[Dict]:
        """Get current warnings"""
        warnings = self.warnings.copy()
        if clear:
            self.warnings = []
        return warnings
    
    def get_monitor_status(self) -> Dict:
        """Get token monitor status"""
        today = date.today().isoformat()
        today_usage = self.daily_usage.get(today, {"tokens": 0, "calls": 0})
        
        # Total all-time
        total_tokens = sum(u.total_tokens for u in self.usage_history)
        total_calls = len(self.usage_history)
        
        return {
            "today": {
                "tokens": today_usage["tokens"],
                "calls": today_usage["calls"]
            },
            "all_time": {
                "tokens": total_tokens,
                "calls": total_calls,
                "avg_tokens_per_call": round(total_tokens / max(total_calls, 1))
            },
            "active_sessions": len(self.active_sessions),
            "rate_limits": {
                provider: {
                    "available_tokens": round(limiter.get_available(), 1),
                    "burst": limiter.burst
                }
                for provider, limiter in self.RATE_LIMITS.items()
            },
            "by_provider": self.provider_totals,
            "by_model": self.model_totals,
            "warnings_count": len(self.warnings)
        }


if __name__ == "__main__":
    monitor = TokenMonitor()
    
    # Simulate some API calls
    sessions = [
        ("session-1", "openai", "gpt-4o", "content_creation"),
        ("session-2", "anthropic", "claude-3-haiku", "outreach"),
        ("session-3", "gemini", "gemini-1.5-pro", "research"),
    ]
    
    for sid, provider, model, task in sessions:
        monitor.start_session(sid, provider, model, task)
        
    # End sessions with token counts
    monitor.end_session("session-1", 1500, 3000)
    monitor.end_session("session-2", 500, 800)
    monitor.end_session("session-3", 2000, 1000)
    
    print("Token Monitor Status:")
    status = monitor.get_monitor_status()
    print(f"  Today: {status['today']['tokens']:,} tokens ({status['today']['calls']} calls)")
    print(f"  All Time: {status['all_time']['tokens']:,} tokens ({status['all_time']['calls']} calls)")
    print(f"  Active Sessions: {status['active_sessions']}")
    print(f"  Warnings: {status['warnings_count']}")
    print(f"\n  By Provider:")
    for provider, data in status['by_provider'].items():
        print(f"    {provider:12s}: {data['tokens']:,} tokens ({data['calls']} calls)")
    print(f"\n  Recent Usage:")
    for usage in monitor.get_recent_usage(3):
        print(f"    {usage['provider']:10s}/{usage['model']:20s} | {usage['total_tokens']:5d} tokens | {usage['latency_ms']}ms")
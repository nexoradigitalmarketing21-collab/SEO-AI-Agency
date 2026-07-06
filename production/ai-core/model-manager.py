#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Model Manager
Milestone 1: Manage AI model lifecycle, versioning, fine-tuning, and model selection.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import os


class ModelRegistry:
    """Registry of all available AI models with metadata"""
    
    MODELS = {
        "gpt-4o": {
            "provider": "openai",
            "version": "2024-08-06",
            "capabilities": ["text", "vision", "function_calling", "json_mode"],
            "context_window": 128000,
            "max_output": 16384,
            "tier": "premium",
            "best_for": ["content_creation", "analysis", "strategy", "complex_reasoning"],
            "release_date": "2024-08-06",
            "status": "stable"
        },
        "gpt-4o-mini": {
            "provider": "openai",
            "version": "2024-07-18",
            "capabilities": ["text", "vision", "function_calling", "json_mode"],
            "context_window": 128000,
            "max_output": 16384,
            "tier": "balanced",
            "best_for": ["analysis", "keyword_research", "reporting", "classification"],
            "release_date": "2024-07-18",
            "status": "stable"
        },
        "claude-3-5-sonnet": {
            "provider": "anthropic",
            "version": "2024-10-22",
            "capabilities": ["text", "vision", "function_calling", "code"],
            "context_window": 200000,
            "max_output": 8192,
            "tier": "premium",
            "best_for": ["code_generation", "sales_proposal", "technical_audit"],
            "release_date": "2024-10-22",
            "status": "stable"
        },
        "claude-3-haiku": {
            "provider": "anthropic",
            "version": "2024-03-07",
            "capabilities": ["text", "vision", "function_calling"],
            "context_window": 200000,
            "max_output": 4096,
            "tier": "budget",
            "best_for": ["outreach", "qa_review", "content_editing", "summarization"],
            "release_date": "2024-03-07",
            "status": "stable"
        },
        "gemini-1.5-pro": {
            "provider": "gemini",
            "version": "2024-09-24",
            "capabilities": ["text", "vision", "code", "multimodal"],
            "context_window": 1000000,
            "max_output": 8192,
            "tier": "premium",
            "best_for": ["research", "data_analysis", "long_context", "multimodal"],
            "release_date": "2024-09-24",
            "status": "stable"
        },
        "gemini-1.5-flash": {
            "provider": "gemini",
            "version": "2024-09-24",
            "capabilities": ["text", "vision", "code", "multimodal"],
            "context_window": 1000000,
            "max_output": 8192,
            "tier": "budget",
            "best_for": ["email_draft", "quick_analysis", "data_extraction"],
            "release_date": "2024-09-24",
            "status": "stable"
        },
        "llama3-70b-8192": {
            "provider": "groq",
            "version": "2024-04-19",
            "capabilities": ["text", "function_calling"],
            "context_window": 8192,
            "max_output": 4096,
            "tier": "budget",
            "best_for": ["data_extraction", "classification", "batch_processing"],
            "release_date": "2024-04-19",
            "status": "stable"
        },
        "mixtral-8x7b-32768": {
            "provider": "groq",
            "version": "2024-03-07",
            "capabilities": ["text", "function_calling"],
            "context_window": 32768,
            "max_output": 4096,
            "tier": "balanced",
            "best_for": ["summarization", "analysis", "batch_processing"],
            "release_date": "2024-03-07",
            "status": "stable"
        }
    }
    
    @classmethod
    def get_model(cls, model_id: str) -> Optional[Dict]:
        """Get model details by ID"""
        return cls.MODELS.get(model_id)
    
    @classmethod
    def get_models_by_tier(cls, tier: str) -> List[Dict]:
        """Get all models in a tier"""
        return [m for m in cls.MODELS.values() if m["tier"] == tier]
    
    @classmethod
    def get_models_by_capability(cls, capability: str) -> List[Dict]:
        """Get all models with a specific capability"""
        return [{"id": k, **v} for k, v in cls.MODELS.items() if capability in v["capabilities"]]
    
    @classmethod
    def get_best_model(cls, task: str, tier: str = "balanced") -> Optional[Dict]:
        """Get the best model for a task and tier"""
        candidates = []
        for model_id, info in cls.MODELS.items():
            if info["tier"] == tier and task in info["best_for"]:
                candidates.append({"id": model_id, **info})
        
        if not candidates:
            # Fallback to any model in tier
            for model_id, info in cls.MODELS.items():
                if info["tier"] == tier:
                    candidates.append({"id": model_id, **info})
        
        return candidates[0] if candidates else None


class ModelManager:
    """Manage AI model lifecycle, versioning, and selection"""
    
    def __init__(self):
        self.registry = ModelRegistry()
        self.active_models = {}
        self.model_versions = {}
        self.performance_history = {}
        self.fine_tuned_models = {}
    
    def select_model(self, task: str, context: Dict = None) -> Dict:
        """Select the optimal model for a task"""
        tier = (context or {}).get("tier", "balanced")
        budget = (context or {}).get("budget", "balanced")
        
        # Map budget to tier
        tier_map = {"premium": "premium", "balanced": "balanced", "budget": "budget"}
        effective_tier = tier_map.get(budget, tier)
        
        model = self.registry.get_best_model(task, effective_tier)
        if not model:
            model = self.registry.get_best_model(task, "balanced")
        
        if model:
            return {
                "model_id": model["id"],
                "provider": model["provider"],
                "tier": model["tier"],
                "context_window": model["context_window"],
                "max_output": model["max_output"],
                "capabilities": model["capabilities"],
                "version": model["version"]
            }
        
        return {"error": "No suitable model found"}
    
    def get_model_performance(self, model_id: str) -> Dict:
        """Get performance metrics for a model"""
        history = self.performance_history.get(model_id, [])
        if not history:
            return {
                "model_id": model_id,
                "avg_latency": 0,
                "avg_cost": 0,
                "success_rate": 100,
                "total_calls": 0
            }
        
        total = len(history)
        successes = sum(1 for h in history if h.get("success", False))
        avg_latency = sum(h.get("latency", 0) for h in history) / total
        avg_cost = sum(h.get("cost", 0) for h in history) / total
        
        return {
            "model_id": model_id,
            "avg_latency": round(avg_latency, 2),
            "avg_cost": round(avg_cost, 6),
            "success_rate": round((successes / total) * 100, 1),
            "total_calls": total
        }
    
    def record_performance(self, model_id: str, success: bool, latency: float, cost: float):
        """Record model performance data"""
        if model_id not in self.performance_history:
            self.performance_history[model_id] = []
        
        self.performance_history[model_id].append({
            "success": success,
            "latency": latency,
            "cost": cost,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep last 1000 records
        if len(self.performance_history[model_id]) > 1000:
            self.performance_history[model_id] = self.performance_history[model_id][-1000:]
    
    def register_fine_tuned_model(self, model_id: str, base_model: str, 
                                  training_data: Dict, metrics: Dict) -> Dict:
        """Register a fine-tuned model"""
        ft_id = f"ft-{base_model}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        ft_model = {
            "id": ft_id,
            "base_model": base_model,
            "provider": self.registry.get_model(base_model, {}).get("provider", "openai"),
            "training_data": training_data,
            "metrics": metrics,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }
        
        self.fine_tuned_models[ft_id] = ft_model
        return ft_model
    
    def get_model_versions(self, model_id: str) -> List[Dict]:
        """Get version history for a model"""
        return self.model_versions.get(model_id, [])
    
    def compare_models(self, task: str) -> List[Dict]:
        """Compare all models suitable for a task"""
        comparisons = []
        for model_id, info in self.registry.MODELS.items():
            if task in info["best_for"]:
                perf = self.get_model_performance(model_id)
                comparisons.append({
                    "model_id": model_id,
                    "provider": info["provider"],
                    "tier": info["tier"],
                    "context_window": info["context_window"],
                    "performance": perf
                })
        
        return sorted(comparisons, key=lambda x: x["performance"]["success_rate"], reverse=True)
    
    def get_manager_status(self) -> Dict:
        """Get model manager status"""
        return {
            "total_models": len(self.registry.MODELS),
            "models_by_tier": {
                "premium": len(self.registry.get_models_by_tier("premium")),
                "balanced": len(self.registry.get_models_by_tier("balanced")),
                "budget": len(self.registry.get_models_by_tier("budget"))
            },
            "fine_tuned_models": len(self.fine_tuned_models),
            "active_models": len(self.active_models),
            "providers": list(set(m["provider"] for m in self.registry.MODELS.values()))
        }


if __name__ == "__main__":
    manager = ModelManager()
    print("Model Manager Status:")
    status = manager.get_manager_status()
    print(f"  Total Models: {status['total_models']}")
    print(f"  By Tier: {status['models_by_tier']}")
    print(f"  Providers: {', '.join(status['providers'])}")
    print("\nModel Selection Examples:")
    for task in ["content_creation", "code_generation", "research", "outreach", "data_extraction"]:
        for tier in ["premium", "balanced", "budget"]:
            model = manager.select_model(task, {"budget": tier})
            print(f"  {task:20s} [{tier:8s}] → {model.get('model_id', 'N/A'):25s} ({model.get('provider', 'N/A')})")
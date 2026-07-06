#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Scale Manager (Milestone 10)
Support 10, 100, 1000+ clients without changing architecture.
Horizontal scaling, load balancing, and resource management.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import uuid


class ScaleTier:
    """Scale tier configuration"""
    
    TIERS = {
        "startup": {
            "name": "Startup",
            "max_clients": 10,
            "agents_per_client": 3,
            "storage_gb": 50,
            "api_calls_per_day": 1000,
            "features": ["basic_analytics", "email_support", "weekly_reports"]
        },
        "growth": {
            "name": "Growth",
            "max_clients": 100,
            "agents_per_client": 5,
            "storage_gb": 500,
            "api_calls_per_day": 10000,
            "features": ["advanced_analytics", "priority_support", "daily_reports", "api_access"]
        },
        "enterprise": {
            "name": "Enterprise",
            "max_clients": 1000,
            "agents_per_client": 8,
            "storage_gb": 5000,
            "api_calls_per_day": 100000,
            "features": ["all_features", "dedicated_infrastructure", "24_7_support", "custom_integrations"]
        },
        "unlimited": {
            "name": "Unlimited",
            "max_clients": float('inf'),
            "agents_per_client": 10,
            "storage_gb": float('inf'),
            "api_calls_per_day": float('inf'),
            "features": ["all_features", "white_label", "multi_region", "sla_99_99"]
        }
    }


class ResourcePool:
    """Resource pool for horizontal scaling"""
    
    def __init__(self):
        self.instances = []
        self.load_distribution = {}
    
    def add_instance(self, instance_type: str, capacity: int) -> Dict:
        """Add a new instance to the pool"""
        instance = {
            "id": f"inst_{len(self.instances) + 1}",
            "type": instance_type,
            "capacity": capacity,
            "current_load": 0,
            "status": "active",
            "added_at": datetime.now().isoformat()
        }
        self.instances.append(instance)
        return instance
    
    def get_available_instance(self) -> Optional[Dict]:
        """Get the least loaded instance"""
        available = [i for i in self.instances if i["status"] == "active" and i["current_load"] < i["capacity"]]
        if not available:
            return None
        return min(available, key=lambda x: x["current_load"] / x["capacity"])
    
    def assign_load(self, instance_id: str, load: int = 1):
        """Assign load to an instance"""
        for instance in self.instances:
            if instance["id"] == instance_id:
                instance["current_load"] += load
                break
    
    def get_pool_status(self) -> Dict:
        """Get resource pool status"""
        total_capacity = sum(i["capacity"] for i in self.instances)
        total_load = sum(i["current_load"] for i in self.instances)
        
        return {
            "total_instances": len(self.instances),
            "active_instances": sum(1 for i in self.instances if i["status"] == "active"),
            "total_capacity": total_capacity,
            "total_load": total_load,
            "utilization": round((total_load / max(total_capacity, 1)) * 100, 1),
            "instances": self.instances
        }


class ScaleManager:
    """Manage scaling across client tiers"""
    
    def __init__(self):
        self.resource_pool = ResourcePool()
        self.client_tiers = {}
        self.scaling_events = []
        
        # Initialize with base instances
        self.resource_pool.add_instance("api_worker", 100)
        self.resource_pool.add_instance("ai_worker", 50)
        self.resource_pool.add_instance("storage_node", 1000)
    
    def assign_client_tier(self, client_id: str, tier: str) -> Dict:
        """Assign a client to a scale tier"""
        tier_config = ScaleTier.TIERS.get(tier)
        if not tier_config:
            return {"error": f"Invalid tier: {tier}"}
        
        self.client_tiers[client_id] = {
            "tier": tier,
            "config": tier_config,
            "assigned_at": datetime.now().isoformat(),
            "resource_usage": {
                "api_calls": 0,
                "storage_mb": 0,
                "agent_hours": 0
            }
        }
        
        # Assign resources
        instance = self.resource_pool.get_available_instance()
        if instance:
            self.resource_pool.assign_load(instance["id"])
        
        self._log_scaling_event("client_assigned", f"Client {client_id} assigned to {tier} tier")
        
        return self.client_tiers[client_id]
    
    def get_tier_capacity(self, tier: str) -> Dict:
        """Get remaining capacity for a tier"""
        config = ScaleTier.TIERS.get(tier)
        if not config:
            return {"error": f"Invalid tier: {tier}"}
        
        current = sum(1 for c in self.client_tiers.values() if c["tier"] == tier)
        max_clients = config["max_clients"]
        
        return {
            "tier": tier,
            "current_clients": current,
            "max_clients": max_clients if max_clients != float('inf') else "unlimited",
            "remaining": (max_clients - current) if max_clients != float('inf') else "unlimited",
            "utilization": round((current / max_clients) * 100, 1) if max_clients != float('inf') else 0
        }
    
    def auto_scale(self) -> Dict:
        """Auto-scale resources based on demand"""
        pool_status = self.resource_pool.get_pool_status()
        
        actions = []
        
        # Scale up if utilization > 80%
        if pool_status["utilization"] > 80:
            new_instance = self.resource_pool.add_instance("api_worker", 100)
            actions.append(f"Scaled up: Added {new_instance['id']}")
            self._log_scaling_event("scale_up", f"Added new instance due to {pool_status['utilization']}% utilization")
        
        # Scale down if utilization < 30% and we have spare instances
        elif pool_status["utilization"] < 30 and len(self.resource_pool.instances) > 3:
            # Remove least loaded instance
            instances = sorted(self.resource_pool.instances, key=lambda x: x["current_load"])
            if instances:
                removed = instances[0]
                removed["status"] = "removed"
                actions.append(f"Scaled down: Removed {removed['id']}")
                self._log_scaling_event("scale_down", f"Removed instance due to low utilization")
        
        return {
            "actions": actions,
            "pool_status": pool_status,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_scale_summary(self) -> Dict:
        """Get scaling summary"""
        return {
            "total_clients": len(self.client_tiers),
            "tier_distribution": {
                tier: sum(1 for c in self.client_tiers.values() if c["tier"] == tier)
                for tier in ScaleTier.TIERS
            },
            "resource_pool": self.resource_pool.get_pool_status(),
            "tier_capacities": {
                tier: self.get_tier_capacity(tier)
                for tier in ScaleTier.TIERS
            },
            "scaling_events": self.scaling_events[-10:],
            "architecture": "Horizontally scalable - add instances for more capacity"
        }
    
    def _log_scaling_event(self, event_type: str, details: str):
        """Log a scaling event"""
        self.scaling_events.append({
            "type": event_type,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_manager_status(self) -> Dict:
        """Get scale manager status"""
        return self.get_scale_summary()


if __name__ == "__main__":
    sm = ScaleManager()
    
    # Assign clients to tiers
    for i in range(5):
        sm.assign_client_tier(f"client_{i+1}", "startup")
    for i in range(3):
        sm.assign_client_tier(f"client_{i+6}", "growth")
    sm.assign_client_tier("client_enterprise", "enterprise")
    
    print("Scale Manager Status:")
    summary = sm.get_scale_summary()
    print(f"  Total Clients: {summary['total_clients']}")
    print(f"  Tier Distribution:")
    for tier, count in summary['tier_distribution'].items():
        if count > 0:
            print(f"    {tier:12s}: {count} clients")
    print(f"\n  Resource Pool:")
    pool = summary['resource_pool']
    print(f"    Instances: {pool['active_instances']}")
    print(f"    Utilization: {pool['utilization']}%")
    print(f"    Load: {pool['total_load']}/{pool['total_capacity']}")
    print(f"\n  Architecture: {summary['architecture']}")
    
    # Test auto-scaling
    print("\n  Auto-Scale Test:")
    scale_result = sm.auto_scale()
    for action in scale_result['actions']:
        print(f"    {action}")
#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Memory Manager
Milestone 1: Persistent memory system for AI agents - short-term, long-term, and episodic memory.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import uuid
import hashlib


class MemoryItem:
    """Individual memory item with metadata"""
    
    def __init__(self, content: str, memory_type: str = "episodic", 
                 importance: float = 0.5, source: str = "", tags: List[str] = None):
        self.id = str(uuid.uuid4())[:12]
        self.content = content
        self.memory_type = memory_type  # "short_term", "long_term", "episodic", "semantic"
        self.importance = importance  # 0.0 to 1.0
        self.source = source
        self.tags = tags or []
        self.created_at = datetime.now().isoformat()
        self.last_accessed = datetime.now().isoformat()
        self.access_count = 0
        self.strength = 1.0  # Memory strength (decays over time)
        self.embedding = None  # Vector embedding for semantic search
    
    def access(self):
        """Record memory access"""
        self.access_count += 1
        self.last_accessed = datetime.now().isoformat()
        self.strength = min(1.0, self.strength + 0.1)
    
    def decay(self, hours_passed: float):
        """Apply time-based decay to memory strength"""
        decay_factor = 0.95 ** (hours_passed / 24)  # 5% decay per day
        self.strength = max(0.1, self.strength * decay_factor)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "content": self.content[:200],
            "type": self.memory_type,
            "importance": self.importance,
            "strength": round(self.strength, 2),
            "access_count": self.access_count,
            "tags": self.tags,
            "created_at": self.created_at
        }


class MemoryStore:
    """Storage for different memory types"""
    
    def __init__(self, max_short_term: int = 100, max_long_term: int = 10000):
        self.short_term = {}  # Recent, limited capacity
        self.long_term = {}   # Important, persistent
        self.episodic = {}    # Specific experiences
        self.semantic = {}    # General knowledge
        self.max_short_term = max_short_term
        self.max_long_term = max_long_term
    
    def store(self, item: MemoryItem):
        """Store a memory item"""
        if item.memory_type == "short_term":
            self._store_short_term(item)
        elif item.memory_type == "long_term":
            self._store_long_term(item)
        elif item.memory_type == "episodic":
            self.episodic[item.id] = item
        elif item.memory_type == "semantic":
            self.semantic[item.id] = item
    
    def _store_short_term(self, item: MemoryItem):
        """Store in short-term memory with capacity management"""
        if len(self.short_term) >= self.max_short_term:
            # Consolidate oldest to long-term if important
            oldest = min(self.short_term.values(), key=lambda x: x.last_accessed)
            if oldest.importance > 0.5:
                oldest.memory_type = "long_term"
                self._store_long_term(oldest)
            del self.short_term[oldest.id]
        
        self.short_term[item.id] = item
    
    def _store_long_term(self, item: MemoryItem):
        """Store in long-term memory"""
        if len(self.long_term) >= self.max_long_term:
            # Remove weakest memories
            weakest = min(self.long_term.values(), key=lambda x: x.strength)
            del self.long_term[weakest.id]
        
        self.long_term[item.id] = item
    
    def retrieve(self, memory_id: str) -> Optional[MemoryItem]:
        """Retrieve a memory by ID"""
        for store in [self.short_term, self.long_term, self.episodic, self.semantic]:
            if memory_id in store:
                item = store[memory_id]
                item.access()
                return item
        return None
    
    def search(self, query: str, memory_type: str = None, 
               min_importance: float = 0.0, limit: int = 10) -> List[MemoryItem]:
        """Search memories by content"""
        results = []
        query = query.lower()
        
        stores = []
        if not memory_type or memory_type == "short_term":
            stores.append(self.short_term)
        if not memory_type or memory_type == "long_term":
            stores.append(self.long_term)
        if not memory_type or memory_type == "episodic":
            stores.append(self.episodic)
        if not memory_type or memory_type == "semantic":
            stores.append(self.semantic)
        
        for store in stores:
            for item in store.values():
                if item.importance >= min_importance and query in item.content.lower():
                    results.append(item)
        
        # Sort by relevance (importance * strength)
        results.sort(key=lambda x: x.importance * x.strength, reverse=True)
        return results[:limit]
    
    def consolidate(self):
        """Consolidate short-term to long-term memories"""
        for item_id, item in list(self.short_term.items()):
            if item.importance > 0.7 or item.access_count > 5:
                item.memory_type = "long_term"
                self._store_long_term(item)
                del self.short_term[item_id]
    
    def apply_decay(self):
        """Apply decay to all memories"""
        now = datetime.now()
        for store in [self.short_term, self.long_term, self.episodic, self.semantic]:
            for item in store.values():
                last = datetime.fromisoformat(item.last_accessed)
                hours_passed = (now - last).total_seconds() / 3600
                item.decay(hours_passed)


class MemoryManager:
    """Central memory management system for AI agents"""
    
    def __init__(self):
        self.store = MemoryStore()
        self.agent_memories = {}  # agent_name -> [memory_ids]
        self.session_memories = {}  # session_id -> [memory_ids]
    
    def remember(self, agent: str, content: str, memory_type: str = "episodic",
                 importance: float = 0.5, source: str = "", tags: List[str] = None,
                 session_id: str = None) -> MemoryItem:
        """Store a new memory"""
        item = MemoryItem(content, memory_type, importance, source, tags)
        self.store.store(item)
        
        # Index by agent
        if agent not in self.agent_memories:
            self.agent_memories[agent] = []
        self.agent_memories[agent].append(item.id)
        
        # Index by session
        if session_id:
            if session_id not in self.session_memories:
                self.session_memories[session_id] = []
            self.session_memories[session_id].append(item.id)
        
        return item
    
    def recall(self, agent: str, query: str, limit: int = 5) -> List[MemoryItem]:
        """Recall memories for an agent"""
        agent_memory_ids = self.agent_memories.get(agent, [])
        
        results = []
        for mem_id in agent_memory_ids:
            item = self.store.retrieve(mem_id)
            if item and query.lower() in item.content.lower():
                results.append(item)
        
        results.sort(key=lambda x: x.importance * x.strength, reverse=True)
        return results[:limit]
    
    def recall_by_session(self, session_id: str, query: str = "", limit: int = 10) -> List[MemoryItem]:
        """Recall memories from a specific session"""
        session_ids = self.session_memories.get(session_id, [])
        
        results = []
        for mem_id in session_ids:
            item = self.store.retrieve(mem_id)
            if item:
                if not query or query.lower() in item.content.lower():
                    results.append(item)
        
        return results[:limit]
    
    def forget(self, memory_id: str) -> bool:
        """Delete a memory"""
        for store in [self.store.short_term, self.store.long_term, 
                      self.store.episodic, self.store.semantic]:
            if memory_id in store:
                del store[memory_id]
                return True
        return False
    
    def get_agent_summary(self, agent: str) -> Dict:
        """Get memory summary for an agent"""
        agent_ids = self.agent_memories.get(agent, [])
        memories = []
        
        for mem_id in agent_ids:
            item = self.store.retrieve(mem_id)
            if item:
                memories.append(item.to_dict())
        
        return {
            "agent": agent,
            "total_memories": len(memories),
            "by_type": {
                "short_term": sum(1 for m in memories if m["type"] == "short_term"),
                "long_term": sum(1 for m in memories if m["type"] == "long_term"),
                "episodic": sum(1 for m in memories if m["type"] == "episodic"),
                "semantic": sum(1 for m in memories if m["type"] == "semantic")
            },
            "recent_memories": sorted(memories, key=lambda x: x["created_at"], reverse=True)[:5]
        }
    
    def get_manager_status(self) -> Dict:
        """Get memory manager status"""
        return {
            "total_memories": (len(self.store.short_term) + len(self.store.long_term) + 
                              len(self.store.episodic) + len(self.store.semantic)),
            "short_term": len(self.store.short_term),
            "long_term": len(self.store.long_term),
            "episodic": len(self.store.episodic),
            "semantic": len(self.store.semantic),
            "agents_with_memories": len(self.agent_memories),
            "active_sessions": len(self.session_memories)
        }


if __name__ == "__main__":
    manager = MemoryManager()
    
    # Store memories
    manager.remember("content_writer", "Client prefers conversational tone with industry expertise", 
                     "semantic", 0.8, tags=["client_preference", "tone"])
    manager.remember("content_writer", "Wrote article about Core Web Vitals - received positive feedback",
                     "episodic", 0.6, tags=["article", "feedback"])
    manager.remember("technical_seo", "example.com has slow LCP (4.2s) - needs image optimization",
                     "episodic", 0.9, tags=["issue", "pagespeed"])
    
    print("Memory Manager Status:")
    status = manager.get_manager_status()
    print(f"  Total Memories: {status['total_memories']}")
    print(f"  Short Term: {status['short_term']}")
    print(f"  Long Term: {status['long_term']}")
    print(f"  Episodic: {status['episodic']}")
    print(f"  Semantic: {status['semantic']}")
    print(f"  Agents: {status['agents_with_memories']}")
    
    print("\nAgent Memory Summary:")
    summary = manager.get_agent_summary("content_writer")
    print(f"  Agent: {summary['agent']}")
    print(f"  Total: {summary['total_memories']}")
    print(f"  Recent: {[m['content'] for m in summary['recent_memories']]}")
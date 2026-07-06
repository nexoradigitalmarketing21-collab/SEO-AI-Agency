#!/usr/bin/env python3
"""
Nexora AI SEO Agency - Context Manager
Milestone 1: Manage conversation context, session state, and contextual memory for AI interactions.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import uuid


class ConversationContext:
    """Track conversation context for AI interactions"""
    
    def __init__(self, session_id: str, agent: str, task: str):
        self.session_id = session_id
        self.agent = agent
        self.task = task
        self.messages = []
        self.metadata = {}
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.token_count = 0
        self.interaction_count = 0
    
    def add_message(self, role: str, content: str, tokens: int = 0):
        """Add a message to the conversation"""
        self.messages.append({
            "role": role,
            "content": content,
            "tokens": tokens,
            "timestamp": datetime.now().isoformat()
        })
        self.token_count += tokens
        self.interaction_count += 1
        self.updated_at = datetime.now().isoformat()
    
    def get_recent_context(self, max_tokens: int = 4000) -> List[Dict]:
        """Get recent context within token limit"""
        context = []
        token_so_far = 0
        
        for msg in reversed(self.messages):
            if token_so_far + msg["tokens"] > max_tokens:
                break
            context.insert(0, msg)
            token_so_far += msg["tokens"]
        
        return context
    
    def summarize(self) -> Dict:
        """Get conversation summary"""
        return {
            "session_id": self.session_id,
            "agent": self.agent,
            "task": self.task,
            "messages": len(self.messages),
            "tokens_used": self.token_count,
            "duration": (datetime.fromisoformat(self.updated_at) - 
                        datetime.fromisoformat(self.created_at)).total_seconds(),
            "metadata": self.metadata
        }


class ContextWindow:
    """Manage context window limitations and optimization"""
    
    MAX_CONTEXT_WINDOWS = {
        "gpt-4o": 128000,
        "gpt-4o-mini": 128000,
        "claude-3-haiku": 200000,
        "claude-3-sonnet": 200000,
        "claude-3-5-sonnet": 200000,
        "gemini-1.5-pro": 1000000,
        "gemini-1.5-flash": 1000000,
        "llama3-70b-8192": 8192,
        "mixtral-8x7b-32768": 32768
    }
    
    @classmethod
    def get_max_tokens(cls, model: str) -> int:
        """Get max tokens for a model"""
        return cls.MAX_CONTEXT_WINDOWS.get(model, 128000)
    
    @classmethod
    def optimize_context(cls, context: List[Dict], model: str, 
                         reserve_output: int = 4000) -> List[Dict]:
        """Optimize context to fit within model limits"""
        max_tokens = cls.get_max_tokens(model) - reserve_output
        current_tokens = sum(msg.get("tokens", 0) for msg in context)
        
        if current_tokens <= max_tokens:
            return context
        
        # Need to trim - keep system messages and recent history
        system_msgs = [msg for msg in context if msg.get("role") == "system"]
        non_system = [msg for msg in context if msg.get("role") != "system"]
        
        # Keep most recent non-system messages
        trimmed = system_msgs.copy()
        token_count = sum(msg.get("tokens", 0) for msg in system_msgs)
        
        for msg in reversed(non_system):
            if token_count + msg.get("tokens", 0) > max_tokens:
                break
            trimmed.insert(len(system_msgs), msg)
            token_count += msg.get("tokens", 0)
        
        return trimmed


class ContextManager:
    """Central context management for all AI interactions"""
    
    def __init__(self, max_contexts: int = 1000, context_ttl_hours: int = 24):
        self.contexts = {}
        self.max_contexts = max_contexts
        self.context_ttl = timedelta(hours=context_ttl_hours)
        self.window = ContextWindow()
    
    def create_context(self, agent: str, task: str, 
                      initial_context: Dict = None) -> ConversationContext:
        """Create a new conversation context"""
        session_id = str(uuid.uuid4())[:12]
        context = ConversationContext(session_id, agent, task)
        
        if initial_context:
            context.metadata = initial_context
        
        self.contexts[session_id] = context
        self._cleanup_old_contexts()
        
        return context
    
    def get_context(self, session_id: str) -> Optional[ConversationContext]:
        """Get context by session ID"""
        context = self.contexts.get(session_id)
        if not context:
            return None
        
        # Check if context has expired
        updated = datetime.fromisoformat(context.updated_at)
        if datetime.now() - updated > self.context_ttl:
            self.archive_context(session_id)
            return None
        
        return context
    
    def update_context(self, session_id: str, role: str, content: str, tokens: int = 0) -> bool:
        """Add message to existing context"""
        context = self.get_context(session_id)
        if not context:
            return False
        
        context.add_message(role, content, tokens)
        return True
    
    def merge_contexts(self, session_ids: List[str], new_agent: str, new_task: str) -> str:
        """Merge multiple contexts into one"""
        merged = self.create_context(new_agent, new_task)
        
        for sid in session_ids:
            ctx = self.contexts.get(sid)
            if ctx:
                merged.messages.extend(ctx.messages)
                merged.token_count += ctx.token_count
                merged.metadata.update(ctx.metadata)
        
        return merged.session_id
    
    def archive_context(self, session_id: str):
        """Archive an expired context"""
        if session_id in self.contexts:
            # In production, save to database
            del self.contexts[session_id]
    
    def search_contexts(self, query: str, agent: str = None) -> List[Dict]:
        """Search across contexts"""
        results = []
        query = query.lower()
        
        for ctx in self.contexts.values():
            if agent and ctx.agent != agent:
                continue
            
            for msg in ctx.messages:
                if query in msg["content"].lower():
                    results.append({
                        "session_id": ctx.session_id,
                        "agent": ctx.agent,
                        "task": ctx.task,
                        "message_role": msg["role"],
                        "message_preview": msg["content"][:200],
                        "timestamp": msg["timestamp"]
                    })
                    break
        
        return results[:20]
    
    def get_context_summary(self, session_id: str) -> Dict:
        """Get summary of a context"""
        context = self.get_context(session_id)
        if not context:
            return {"error": "Context not found"}
        return context.summarize()
    
    def _cleanup_old_contexts(self):
        """Clean up old contexts when limit is reached"""
        if len(self.contexts) >= self.max_contexts:
            # Remove oldest contexts
            sorted_contexts = sorted(
                self.contexts.items(),
                key=lambda x: x[1].updated_at
            )
            # Remove bottom 10%
            to_remove = len(sorted_contexts) // 10
            for session_id, _ in sorted_contexts[:to_remove]:
                self.archive_context(session_id)
    
    def get_manager_status(self) -> Dict:
        """Get context manager status"""
        return {
            "active_contexts": len(self.contexts),
            "max_contexts": self.max_contexts,
            "context_ttl_hours": self.context_ttl.total_seconds() / 3600,
            "total_messages": sum(len(c.messages) for c in self.contexts.values()),
            "total_tokens": sum(c.token_count for c in self.contexts.values()),
            "active_agents": list(set(c.agent for c in self.contexts.values()))
        }


if __name__ == "__main__":
    manager = ContextManager()
    
    # Create contexts for different agents
    ctx1 = manager.create_context("content_writer", "write_article", 
                                   {"topic": "SEO Best Practices"})
    ctx2 = manager.create_context("technical_seo", "audit_website",
                                   {"website": "example.com"})
    
    # Add messages
    manager.update_context(ctx1.session_id, "user", "Write about on-page SEO", 50)
    manager.update_context(ctx1.session_id, "assistant", "Here's an article about on-page SEO...", 500)
    manager.update_context(ctx2.session_id, "user", "Audit example.com for technical issues", 30)
    
    print("Context Manager Status:")
    status = manager.get_manager_status()
    print(f"  Active Contexts: {status['active_contexts']}")
    print(f"  Total Messages: {status['total_messages']}")
    print(f"  Total Tokens: {status['total_tokens']}")
    print(f"  Active Agents: {', '.join(status['active_agents'])}")
    print(f"\nContext Summary:")
    print(json.dumps(manager.get_context_summary(ctx1.session_id), indent=2))
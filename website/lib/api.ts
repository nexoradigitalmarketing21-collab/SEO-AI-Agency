// API client for connecting to Phase 5 AI system

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export interface AIOperation {
  input: string
  type: string
  callback_url?: string
}

export interface AIAuditRequest {
  url: string
  email: string
}

export interface AIAuditResponse {
  audit_id: string
  status: 'processing' | 'completed'
  score: number
  issues: number
  recommendations: string[]
}

export interface Project {
  id: string
  name: string
  domain: string
  status: 'active' | 'paused' | 'completed'
  audit?: AIAuditResponse
}

export interface Keyword {
  keyword: string
  position: number
  volume: number
  difficulty: number
}

export async function submitAudit(request: AIAuditRequest): Promise<AIAuditResponse> {
  const response = await fetch(`${API_BASE_URL}/api/audit`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.AI_API_KEY}`,
    },
    body: JSON.stringify(request),
  })
  return response.json()
}

export async function getProjects(): Promise<Project[]> {
  const response = await fetch(`${API_BASE_URL}/api/projects`, {
    headers: {
      Authorization: `Bearer ${process.env.AI_API_KEY}`,
    },
  })
  return response.json()
}

export async function getKeywords(projectId: string): Promise<Keyword[]> {
  const response = await fetch(`${API_BASE_URL}/api/projects/${projectId}/keywords`, {
    headers: {
      Authorization: `Bearer ${process.env.AI_API_KEY}`,
    },
  })
  return response.json()
}

export async function triggerAIWorkflow(data: AIOperation) {
  const response = await fetch(`${API_BASE_URL}/api/orchestrate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.AI_API_KEY}`,
    },
    body: JSON.stringify(data),
  })
  return response.json()
}
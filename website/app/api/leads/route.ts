import { NextRequest, NextResponse } from 'next/server'
import { triggerAIWorkflow } from '@/lib/api'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { name, email, company, website, message } = body

    // Trigger AI workflow for lead
    const result = await triggerAIWorkflow({
      input: JSON.stringify({
        lead_type: 'website_form',
        name,
        email,
        company,
        website,
        message,
        source: 'website',
      }),
      type: 'lead_capture',
    })

    return NextResponse.json({ success: true, id: result.id })
  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to process lead' },
      { status: 500 }
    )
  }
}
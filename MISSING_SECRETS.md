# Missing Secrets - Action Required

These environment variables must be configured before accepting paying clients:

## Required Secrets (Add to `.env`)

| Variable | Description | Where to Get |
|----------|-------------|--------------|
| DATABASE_URL | PostgreSQL connection string | Supabase/Neon/other provider |
| NEXTAUTH_SECRET | Auth encryption secret | `openssl rand -base64 32` |
| STRIPE_SECRET_KEY | Stripe API key | dashboard.stripe.com |
| STRIPE_WEBHOOK_SECRET | Webhook signing secret | Stripe Dashboard |
| GOOGLE_CLIENT_ID | Google OAuth client ID | console.cloud.google.com |
| GOOGLE_CLIENT_SECRET | Google OAuth secret | console.cloud.google.com |
| OPENAI_API_KEY | OpenAI API key | platform.openai.com |
| ANTHROPIC_API_KEY | Anthropic Claude API key | console.anthropic.com |
| GEMINI_API_KEY | Google Gemini API key | ai.google.dev |

## GitHub Actions Secrets (Repository Settings → Secrets)

| Secret | Required for |
|--------|--------------|
| VERCEL_TOKEN | Vercel deployment |
| VERCEL_ORG_ID | Vercel organization |
| VERCEL_PROJECT_ID | Vercel project |
| DATABASE_URL | Prisma generation |

## Next Steps

1. Fill `.env` with real values
2. Run `npx prisma db push`
3. Test Stripe webhook endpoint
4. Verify AI connections work
5. Deploy to production
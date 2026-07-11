# Health Check Configuration

## Sentry Monitoring

Add to `.env`:
```
SENTRY_DSN=https://your-dsn@sentry.io/project-id
SENTRY_ORG=your-org
SENTRY_PROJECT=your-project
```

Add to `website/next.config.js`:
```js
const sentryOptions = {
  silent: true,
  org: process.env.SENTRY_ORG,
  project: process.env.SENTRY_PROJECT,
}

const nextConfig = {
  // ...existing config
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.resolve.fallback = {
        ...config.resolve.fallback,
        '@sentry/nextjs': false,
      }
    }
    return config
  },
}
```

## Application Health Checks

### API Endpoints
- `GET /api/health` - Application health status
- `GET /api/leads` - Lead submission endpoint

### Database Health
- PostgreSQL connection pool
- Query response times < 100ms

### AI Engine Health
- Multi-provider API availability
- Token usage within limits
- Cost tracking enabled

## Monitoring Setup

1. Create Sentry account at sentry.io
2. Create Next.js project
3. Install: `npm install @sentry/nextjs`
4. Run: `npx @sentry/wizard@latest -i nextjs`
5. Add DSN to `.env`
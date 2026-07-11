# Nexora Digital Marketing - Premium Agency Website

A $50k+ agency-grade website built with Next.js 15, React 19, TypeScript, and Tailwind CSS.

## 🚀 Features

### Frontend
- **Premium Design**: Agency-quality design inspired by WebFX, DesignJoy, Linear
- **Full Responsiveness**: Mobile-first design with flawless mobile experience
- **Framer Motion Animations**: Smooth scroll animations and micro-interactions
- **GSAP Integration**: Advanced animations for premium feel
- **shadcn/ui Components**: Modern, accessible UI components

### SEO & Performance
- **Dynamic sitemap.xml** - Auto-generated sitemap for all pages
- **robots.txt** - Proper crawling rules
- **Schema.org JSON-LD** - Organization and Website structured data
- **OpenGraph & Twitter Cards** - Rich social sharing
- **Server-side Rendering** - Fast initial loads
- **Image Optimization** - Automatic optimization with Next.js

### Tech Stack
- Next.js 15 (App Router)
- React 19
- TypeScript
- Tailwind CSS 3
- Framer Motion
- GSAP
- Prisma ORM
- PostgreSQL
- NextAuth.js
- Stripe
- React Hook Form + Zod

### Pages Structure
```
/
├── homepage (hero, services, workflow, case studies, CTA)
├── /services
│   ├── /seo-audit
│   ├── /technical-seo
│   ├── /keyword-research
│   ├── /local-seo
│   ├── /content-strategy
│   ├── /monthly-seo
│   └── /ai-seo (future)
├── /industries
├── /case-studies
├── /pricing
├── /resources
│   ├── /blog
│   ├── /seo-guides
│   └── /free-tools
├── /client-portal (coming soon)
├── /book-strategy-call
└── /contact
```

## 🛠️ Development

```bash
# Install dependencies
npm install --legacy-peer-deps

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## 📊 Database Setup

```bash
# Generate Prisma client
npx prisma generate

# Push schema to database
npx prisma db push

# View database
npx prisma studio
```

## 🔌 Integrations

### Stripe Payments
```bash
# Setup Stripe webhook
npm run stripe:webhooks
```

### AI Backend Integration
The website connects to your Phase 5 AI system:
- `/lib/api` - API client for AI engine
- `/lib/seo-tools` - SEO tool integrations

## 🚀 Deployment

### Vercel (Recommended)
```bash
npm run deploy
```

### Environment Variables (.env)
```bash
DATABASE_URL="postgresql://..."
NEXTAUTH_SECRET="your-secret"
NEXTAUTH_URL="https://nexora.ai"
STRIPE_SECRET_KEY="sk_live..."
GA4_MEASUREMENT_ID="G-..."
CLARITY_PROJECT_ID="..."
```

## 🎯 Premium Features

### Hero Section
- Animated gradient background
- AI-powered SEO dashboard mockup
- Trust badges and statistics
- Dual CTAs (Free Audit + Strategy Call)

### Services Grid
- 6 premium service cards with hover effects
- Gradient icons for visual appeal
- Clear value propositions

### AI Workflow
- 7-step process visualization
- Animated timeline
- AI-powered research stage highlighted

### Case Studies
- Before/after charts
- Revenue metrics
- Client testimonials
- Industry-specific results

### Pricing
- Transparent 3-tier pricing
- Most popular badge
- No long-term contracts

### Client Portal (Coming Soon)
- Login with NextAuth
- Project dashboard
- Report viewing/downloading
- Invoice payments via Stripe
- Chat with AI agents

## 📈 Analytics

- Google Analytics 4 (GA4)
- Microsoft Clarity
- Custom event tracking for conversions

## 🤝 Integration with Existing System

Connects directly to your Phase 5 system:
- `production/ai-core` - AI agents
- `production/client-portal` - Existing portal logic
- `production/seo-data` - SEO data integrations
- `production/payments` - Payment system

## 📝 License

MIT License - Nexora Digital Marketing
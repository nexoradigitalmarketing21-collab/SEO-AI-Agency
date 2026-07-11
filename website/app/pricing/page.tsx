import Link from 'next/link'
import { CheckIcon } from '@heroicons/react/24/outline'

export const metadata = {
  title: 'Pricing | Nexora Digital Marketing',
  description: 'Transparent SEO pricing for businesses of all sizes. Choose from SEO audits, ongoing monthly SEO, or custom packages.',
}

const plans = [
  {
    name: 'SEO Audit',
    price: '$297',
    description: 'One-time comprehensive website analysis',
    features: [
      'Full technical SEO audit',
      'On-page optimization review',
      'Competitor analysis',
      'Keyword research (100 keywords)',
      '90-day action plan',
    ],
    mostPopular: false,
  },
  {
    name: 'Monthly SEO',
    price: '$500',
    period: '/month',
    description: 'Ongoing SEO management for consistent growth',
    features: [
      'Everything in SEO Audit',
      'Keyword rank tracking',
      'Content optimization (4 articles/month)',
      'Technical SEO fixes',
      'Link building',
      'Monthly reporting',
    ],
    mostPopular: true,
  },
  {
    name: 'Enterprise',
    price: 'Custom',
    description: 'Full-scale SEO for large businesses',
    features: [
      'Everything in Monthly SEO',
      'Dedicated account manager',
      'Unlimited content',
      'Advanced competitor analysis',
      'Custom reporting dashboard',
      'Priority support',
    ],
    mostPopular: false,
  },
]

export default function PricingPage() {
  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Simple, Transparent Pricing
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              No hidden fees. No long-term contracts. Choose the plan that fits your business needs.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 lg:grid-cols-3">
            {plans.map((plan) => (
              <div
                key={plan.name}
                className={`card relative flex flex-col ${
                  plan.mostPopular ? 'border-2 border-primary' : ''
                }`}
              >
                {plan.mostPopular && (
                  <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                    <span className="rounded-full bg-primary px-4 py-1 text-xs font-semibold text-white">
                      Most Popular
                    </span>
                  </div>
                )}
                <h3 className="text-xl font-semibold text-gray-900">{plan.name}</h3>
                <p className="mt-2 text-sm text-gray-600">{plan.description}</p>
                <div className="mt-6 flex items-baseline gap-1">
                  <span className="text-4xl font-bold text-gray-900">{plan.price}</span>
                  {plan.period && <span className="text-gray-600">{plan.period}</span>}
                </div>
                <ul className="mt-6 space-y-4">
                  {plan.features.map((feature) => (
                    <li key={feature} className="flex items-start gap-3">
                      <CheckIcon className="h-5 w-5 text-primary" />
                      <span className="text-gray-600">{feature}</span>
                    </li>
                  ))}
                </ul>
                <div className="mt-8">
                  <Link
                    href="/book-strategy-call"
                    className={`w-full inline-flex justify-center rounded-md px-6 py-3 text-sm font-medium transition-colors ${
                      plan.mostPopular
                        ? 'bg-primary text-white hover:bg-primary/90'
                        : 'border border-gray-300 text-gray-700 hover:bg-gray-50'
                    }`}
                  >
                    {plan.name === 'Enterprise' ? 'Contact Sales' : 'Get Started'}
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
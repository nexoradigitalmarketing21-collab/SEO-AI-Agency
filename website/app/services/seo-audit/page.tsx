'use client'

import Link from 'next/link'
import { ChartBarIcon, ArrowRightIcon } from '@heroicons/react/24/outline'

export default function SEOAuditPage() {
  const features = [
    'Technical SEO analysis',
    'On-page optimization review',
    'Backlink profile audit',
    'Competitor comparison',
    'Content gap analysis',
    '90-day action plan',
  ]

  const benefits = [
    'Identify critical issues fast',
    'Get a clear roadmap to rankings',
    'Understand your competitive position',
    'Prioritize fixes by impact',
    'Improve user experience',
    'Increase organic traffic',
  ]

  return (
    <div className="pt-24">
      {/* Hero */}
      <section className="py-24 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              SEO Audit
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Comprehensive website analysis with actionable recommendations to improve your search rankings.
            </p>
            <div className="mt-8">
              <Link href="/book-strategy-call" className="btn-primary inline-flex items-center gap-2">
                Get Your Free Audit
                <ArrowRightIcon className="h-4 w-4" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-24 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-2">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">What\'s Included</h2>
              <ul className="mt-6 space-y-4">
                {features.map((feature) => (
                  <li key={feature} className="flex items-start gap-3">
                    <div className="flex-shrink-0">
                      <div className="flex h-6 w-6 items-center justify-center rounded-full bg-primary">
                        <svg className="h-4 w-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M16.704 4.254a.75.75 0 01.142.706l-4.5 15.5a.75.75 0 01-1.428.293l-2.5-3.75a.75.75 0 01.162-.88l2.25-1.5-2.5-3.75a.75.75 0 01.293-1.06z" clipRule="evenodd" />
                        </svg>
                      </div>
                    </div>
                    <span className="text-gray-600">{feature}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h2 className="text-2xl font-bold text-gray-900">Benefits</h2>
              <ul className="mt-6 space-y-4">
                {benefits.map((benefit) => (
                  <li key={benefit} className="flex items-start gap-3">
                    <div className="flex-shrink-0">
                      <div className="flex h-6 w-6 items-center justify-center rounded-full bg-accent">
                        <svg className="h-4 w-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M16.704 4.254a.75.75 0 01.142.706l-4.5 15.5a.75.75 0 01-1.428.293l-2.5-3.75a.75.75 0 01.162-.88l2.25-1.5-2.5-3.75a.75.75 0 01.293-1.06z" clipRule="evenodd" />
                        </svg>
                      </div>
                    </div>
                    <span className="text-gray-600">{benefit}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 bg-primary">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h2 className="text-3xl font-bold tracking-tight text-white">
              Ready to Improve Your SEO?
            </h2>
            <p className="mt-4 text-lg text-white">
              Book a free consultation to discuss your SEO audit needs.
            </p>
            <div className="mt-8">
              <Link
                href="/book-strategy-call"
                className="inline-flex items-center justify-center rounded-md bg-white px-6 py-3 text-sm font-medium text-primary transition-colors hover:bg-gray-100"
              >
                Book Free Consultation
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
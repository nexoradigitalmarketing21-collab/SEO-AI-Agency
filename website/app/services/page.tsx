import Link from 'next/link'
import { ServicesGrid } from '@/components/services-grid'

export const metadata = {
  title: 'SEO Services | Nexora Digital Marketing',
  description: 'Comprehensive AI-powered SEO services including SEO audits, technical SEO, keyword research, local SEO, content strategy, and monthly SEO management.',
}

export default function ServicesPage() {
  return (
    <div className="pt-24">
      {/* Services Header */}
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Premium SEO Services
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Data-driven SEO solutions that deliver measurable results. 
              We combine AI automation with proven strategies to grow your organic traffic.
            </p>
          </div>
        </div>
      </section>

      {/* Services Grid */}
      <ServicesGrid />

      {/* CTA */}
      <section className="py-24 bg-primary">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Ready to Get Started?
            </h2>
            <p className="mt-4 text-lg text-white">
              Book a free consultation and get a custom SEO strategy for your business.
            </p>
            <div className="mt-8">
              <Link
                href="/book-strategy-call"
                className="inline-flex items-center justify-center rounded-md bg-white px-6 py-3 text-sm font-medium text-primary transition-colors hover:bg-gray-100"
              >
                Book Free Strategy Call
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
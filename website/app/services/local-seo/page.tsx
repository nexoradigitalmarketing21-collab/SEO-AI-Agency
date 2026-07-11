import Link from 'next/link'
import { ArrowRightIcon } from '@heroicons/react/24/outline'

export const metadata = {
  title: 'Local SEO | Nexora Digital Marketing',
  description: 'Dominate your local market. Get found by customers near you searching for your services.',
}

export default function LocalSEOPage() {
  const features = [
    'Google Business Profile optimization',
    'Local citation building',
    'Review management',
    'Local keyword targeting',
    'Map pack optimization',
    'Local competitor analysis',
  ]

  const benefits = [
    'Show up in Google Maps',
    'Get more local phone calls',
    'Beat competitors in local pack',
    'Attract nearby customers',
  ]

  return (
    <div className="pt-24">
      <section className="py-24 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Local SEO
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Dominate your local market and get found by customers near you.
            </p>
            <div className="mt-8">
              <Link href="/book-strategy-call" className="btn-primary inline-flex items-center gap-2">
                Get Local SEO
                <ArrowRightIcon className="h-4 w-4" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      <section className="py-24 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-2">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">What We Do</h2>
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

      <section className="py-24 bg-primary">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h2 className="text-3xl font-bold tracking-tight text-white">
              Ready to Dominate Local Search?
            </h2>
            <p className="mt-4 text-lg text-white">
              Book a free consultation to discuss your local SEO needs.
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
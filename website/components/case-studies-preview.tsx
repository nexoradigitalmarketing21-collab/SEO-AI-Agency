'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'

const caseStudies = [
  {
    client: 'TechFlow SaaS',
    industry: 'SaaS',
    result: '185% traffic increase',
    metric: '+185%',
    timeframe: '6 months',
    image: '/case-study-1.jpg',
  },
  {
    client: 'City Dental',
    industry: 'Healthcare',
    result: '#1 for local searches',
    metric: '+250%',
    timeframe: '4 months',
    image: '/case-study-2.jpg',
  },
  {
    client: 'EcoShop E-commerce',
    industry: 'E-commerce',
    result: '300% revenue growth',
    metric: '+300%',
    timeframe: '8 months',
    image: '/case-study-3.jpg',
  },
]

export function CaseStudiesPreview() {
  return (
    <section className="py-24 bg-white">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Success Stories
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            See how we\'ve helped businesses achieve exceptional SEO results.
          </p>
        </div>
        <div className="mt-16 grid grid-cols-1 gap-8 md:grid-cols-3">
          {caseStudies.map((study, index) => (
            <motion.div
              key={study.client}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <Link href="/case-studies" className="group block">
                <div className="card">
                  <div className="aspect-video rounded-lg bg-gray-200" />
                  <div className="mt-6">
                    <h3 className="text-xl font-semibold text-gray-900 group-hover:text-primary transition-colors">
                      {study.client}
                    </h3>
                    <p className="mt-1 text-sm text-gray-600">{study.industry} • {study.timeframe}</p>
                    <div className="mt-4 flex items-baseline gap-2">
                      <span className="text-3xl font-bold text-primary">{study.metric}</span>
                      <span className="text-sm text-gray-600">{study.result}</span>
                    </div>
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
        <div className="mt-12 text-center">
          <Link href="/case-studies" className="btn-secondary inline-flex items-center gap-2">
            View All Case Studies
            <span className="text-primary">→</span>
          </Link>
        </div>
      </div>
    </section>
  )
}
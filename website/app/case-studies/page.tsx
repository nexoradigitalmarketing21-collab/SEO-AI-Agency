'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'

export default function CaseStudiesPage() {
  const caseStudies = [
    {
      client: 'TechFlow SaaS',
      industry: 'SaaS',
      challenge: 'Low organic traffic and poor search visibility despite having a quality product.',
      solution: 'Comprehensive SEO audit, technical fixes, content optimization, and link building strategy.',
      results: [
        { label: 'Traffic Increase', value: '185%' },
        { label: 'Keywords in Top 10', value: '200+' },
        { label: 'Revenue Generated', value: '$95,000' },
      ],
      timeframe: '6 months',
      quote: 'The best SEO investment we\'ve made. Our traffic increased by 185% in 6 months.',
    },
    {
      client: 'City Dental',
      industry: 'Healthcare',
      challenge: 'Need to rank for competitive local keywords in a saturated market.',
      solution: 'Local SEO optimization, Google Business Profile, citation building, and review management.',
      results: [
        { label: 'Local Rankings', value: '#1 for 50+ keywords' },
        { label: 'Call Volume Increase', value: '+250%' },
        { label: 'New Patient Leads', value: '120+/month' },
      ],
      timeframe: '4 months',
      quote: 'Finally found an SEO agency that delivers on their promises.',
    },
    {
      client: 'EcoShop E-commerce',
      industry: 'E-commerce',
      challenge: 'High competition in sustainable products niche with low conversion rates.',
      solution: 'Product page optimization, category SEO, content marketing, and technical improvements.',
      results: [
        { label: 'Organic Revenue', value: '+300%' },
        { label: 'Product Pages Indexed', value: '5,000+' },
        { label: 'Cart Abandonment Reduction', value: '-25%' },
      ],
      timeframe: '8 months',
      quote: 'Our SEO investment paid for itself within the first 3 months.',
    },
  ]

  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Success Stories
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Real results from real businesses. See how we\'ve helped companies grow their organic traffic.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="space-y-24">
            {caseStudies.map((study, index) => (
              <motion.div
                key={study.client}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="card"
              >
                <div className="grid grid-cols-1 gap-8 lg:grid-cols-3">
                  <div className="lg:col-span-2">
                    <h2 className="text-2xl font-bold text-gray-900">{study.client}</h2>
                    <p className="mt-1 text-sm text-gray-600">{study.industry} • {study.timeframe}</p>
                    
                    <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
                      <div>
                        <h3 className="font-semibold text-gray-900">Challenge</h3>
                        <p className="mt-2 text-gray-600">{study.challenge}</p>
                      </div>
                      <div>
                        <h3 className="font-semibold text-gray-900">Solution</h3>
                        <p className="mt-2 text-gray-600">{study.solution}</p>
                      </div>
                    </div>
                    
                    <div className="mt-6">
                      <p className="text-lg italic text-gray-700">"{study.quote}"</p>
                    </div>
                  </div>
                  
                  <div>
                    <h3 className="font-semibold text-gray-900">Results</h3>
                    <div className="mt-4 space-y-4">
                      {study.results.map((result) => (
                        <div key={result.label} className="rounded-lg bg-gray-50 p-4">
                          <div className="text-2xl font-bold text-primary">{result.value}</div>
                          <div className="text-sm text-gray-600">{result.label}</div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
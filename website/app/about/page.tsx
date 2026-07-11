'use client'

import { motion } from 'framer-motion'

export default function AboutPage() {
  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              About Nexora
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              We combine cutting-edge AI technology with proven SEO methodologies to deliver 
              exceptional results for businesses worldwide.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-2">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">Our Story</h2>
              <p className="mt-4 text-gray-600">
                Nexora Digital Marketing was founded with a simple mission: make exceptional SEO 
                accessible to every business. We recognized that traditional SEO agencies were 
                expensive and slow, while DIY tools couldn't deliver real results.
              </p>
              <p className="mt-4 text-gray-600">
                Our solution? Combine artificial intelligence with proven SEO strategies. 
                Our team of 8 specialized AI agents work in orchestration to deliver measurable results, 
                from technical audits to content optimization, at a fraction of traditional costs.
              </p>
            </div>
            <div className="aspect-video rounded-lg bg-gray-200" />
          </div>
        </div>
      </section>

      <section className="py-16 bg-gray-50">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <h2 className="text-center text-2xl font-bold text-gray-900">Our Values</h2>
          <div className="mt-12 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
            {[
              { title: 'Data-Driven', description: 'Every decision is backed by data and measurable metrics.' },
              { title: 'Transparent', description: 'Clear reporting and communication throughout the process.' },
              { title: 'White-Hat', description: 'Only ethical SEO practices that stand the test of time.' },
              { title: 'Results First', description: 'We focus on delivering real business growth.' },
            ].map((value) => (
              <div key={value.title} className="card text-center">
                <h3 className="font-semibold text-gray-900">{value.title}</h3>
                <p className="mt-2 text-gray-600">{value.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
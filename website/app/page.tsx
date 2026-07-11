'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'
import { HeroSection } from '@/components/hero-section'
import { ServicesGrid } from '@/components/services-grid'
import { AIWorkflow } from '@/components/ai-workflow'
import { CaseStudiesPreview } from '@/components/case-studies-preview'
import { Testimonials } from '@/components/testimonials'
import { FAQSection } from '@/components/faq-section'
import { AnimatedGradient } from '@/components/animated-gradient'
import { ArrowRightIcon } from '@heroicons/react/24/outline'

export default function Home() {
  return (
    <div className="relative">
      {/* Animated Gradient Background */}
      <AnimatedGradient />
      
      {/* Hero Section */}
      <HeroSection />

      {/* Trusted By */}
      <section className="py-12 bg-white border-y border-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <p className="text-center text-sm font-medium text-gray-600 mb-8">
            Trusted by leading brands worldwide
          </p>
          <div className="grid grid-cols-2 gap-8 md:grid-cols-4 lg:grid-cols-6 items-center opacity-60">
            {['Google', 'Microsoft', 'Shopify', 'HubSpot', 'Salesforce', 'AWS'].map((company) => (
              <div key={company} className="text-center">
                <span className="text-lg font-bold text-gray-400">{company}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Statistics */}
      <section className="py-24 bg-gray-50">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
            {[
              { value: '200+', label: 'SEO Audits' },
              { value: '100+', label: 'Projects' },
              { value: '95%', label: 'Client Satisfaction' },
              { value: '24/7', label: 'AI Automation' },
            ].map((stat, index) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, scale: 0.5 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="text-center"
              >
                <div className="text-4xl font-bold text-primary">{stat.value}</div>
                <div className="mt-2 text-gray-600">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Grid */}
      <ServicesGrid />

      {/* AI Workflow */}
      <AIWorkflow />

      {/* Case Studies Preview */}
      <CaseStudiesPreview />

      {/* Testimonials */}
      <Testimonials />

      {/* FAQ */}
      <FAQSection />

      {/* Final CTA */}
      <section className="py-24 bg-primary">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Ready to Grow Your Organic Traffic?
            </h2>
            <p className="mt-4 text-lg text-white/80">
              Get your free SEO audit and discover how we can 10x your search visibility.
            </p>
            <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/book-strategy-call"
                className="inline-flex items-center justify-center rounded-lg bg-white px-8 py-4 text-lg font-medium text-primary transition-all hover:bg-gray-100"
              >
                Book Strategy Call
              </Link>
              <Link
                href="/contact"
                className="inline-flex items-center justify-center rounded-lg border border-white/30 px-8 py-4 text-lg font-medium text-white transition-all hover:bg-white/10"
              >
                Contact Us
                <ArrowRightIcon className="ml-2 h-5 w-5" />
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
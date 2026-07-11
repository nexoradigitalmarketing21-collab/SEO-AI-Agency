'use client'

import { motion } from 'framer-motion'
import { PlusIcon, MinusIcon } from '@heroicons/react/24/outline'
import { useState } from 'react'

const faqs = [
  {
    question: 'How long does it take to see SEO results?',
    answer: 'Most clients see improvements within 30-60 days. Significant ranking improvements typically occur within 3-6 months, with substantial traffic growth by 6-12 months.',
  },
  {
    question: 'Do you offer long-term contracts?',
    answer: 'No. Our monthly SEO plans are month-to-month with no long-term contracts. You can cancel anytime.',
  },
  {
    question: 'What makes you different from other SEO agencies?',
    answer: 'We combine AI automation with proven SEO strategies. Our 8 specialized AI agents work 24/7 to monitor, analyze, and optimize your SEO, delivering faster results at a fraction of traditional costs.',
  },
  {
    question: 'How do you measure SEO success?',
    answer: 'We track organic traffic growth, keyword rankings, conversion rates, and revenue. Every month, you receive a detailed report showing progress and ROI.',
  },
  {
    question: 'Do you work with businesses in my industry?',
    answer: 'Yes! We serve SaaS, healthcare, e-commerce, professional services, and many other industries. Check our industries page for specific experience.',
  },
  {
    question: 'What\'s included in your SEO audit?',
    answer: 'Our comprehensive audit includes technical SEO analysis, on-page optimization review, content evaluation, competitor comparison, and a 90-day action plan.',
  },
]

export function FAQSection() {
  const [openIndex, setOpenIndex] = useState<number | null>(null)

  return (
    <section className="py-24 bg-white">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Frequently Asked Questions
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            Everything you need to know about our SEO services.
          </p>
        </div>
        <div className="mt-16 max-w-3xl mx-auto">
          {faqs.map((faq, index) => (
            <motion.div
              key={faq.question}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.05 }}
              className="border-b border-gray-200 py-4"
            >
              <button
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
                className="flex w-full items-center justify-between text-left"
              >
                <span className="text-lg font-medium text-gray-900">{faq.question}</span>
                {openIndex === index ? (
                  <MinusIcon className="h-5 w-5 text-primary" />
                ) : (
                  <PlusIcon className="h-5 w-5 text-gray-500" />
                )}
              </button>
              {openIndex === index && (
                <motion.p
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: 'auto' }}
                  className="mt-4 text-gray-600"
                >
                  {faq.answer}
                </motion.p>
              )}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
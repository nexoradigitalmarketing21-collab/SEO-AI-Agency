'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'
import { ChartBarIcon, ArrowRightIcon, CalendarIcon } from '@heroicons/react/24/outline'

export function HeroSection() {
  return (
    <section className="relative min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">
      {/* Background animation */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 h-80 w-80 rounded-full bg-primary/10 blur-3xl" />
        <div className="absolute -bottom-40 -left-40 h-80 w-80 rounded-full bg-accent/10 blur-3xl" />
      </div>

      <div className="relative mx-auto max-w-7xl px-6 pt-32 pb-24 lg:px-8">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-2 lg:gap-8">
          {/* Left side - Content */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="flex flex-col justify-center"
          >
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl lg:text-6xl">
              <span className="block">AI-Powered SEO That</span>
              <span className="block gradient-text">Drives Rankings,</span>
              <span className="block">Leads & Revenue</span>
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Nexora Digital Marketing combines AI automation with proven SEO strategies to help businesses increase organic traffic, generate qualified leads, and grow revenue. We deliver measurable results through data-driven optimization.
            </p>
            <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:gap-6">
              <Link href="/services/seo-audit" className="btn-primary inline-flex items-center gap-2">
                Get Free SEO Audit
                <ArrowRightIcon className="h-4 w-4" />
              </Link>
              <Link href="/book-strategy-call" className="btn-secondary inline-flex items-center gap-2">
                Book Strategy Call
                <CalendarIcon className="h-4 w-4" />
              </Link>
            </div>

            {/* Statistics */}
            <div className="mt-16 grid grid-cols-2 gap-8 sm:grid-cols-4">
              {[
                { value: '200+', label: 'SEO Audits' },
                { value: '100+', label: 'Projects' },
                { value: '95%', label: 'Client Satisfaction' },
                { value: '24/7', label: 'AI Automation' },
              ].map((stat, index) => (
                <motion.div
                  key={stat.label}
                  initial={{ opacity: 0, scale: 0.8 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.5, delay: 0.2 + index * 0.1 }}
                  className="text-center"
                >
                  <div className="text-3xl font-bold text-primary">{stat.value}</div>
                  <div className="text-sm text-gray-600">{stat.label}</div>
                </motion.div>
              ))}
            </div>
          </motion.div>

          {/* Right side - Animated Dashboard */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="flex items-center justify-center"
          >
            <div className="relative w-full max-w-md">
              {/* Animated SEO Dashboard Mockup */}
              <div className="relative rounded-2xl bg-white p-6 shadow-2xl">
                <div className="mb-4 flex items-center justify-between">
                  <h3 className="text-lg font-semibold text-gray-900">SEO Dashboard</h3>
                  <div className="flex space-x-2">
                    <div className="h-3 w-3 rounded-full bg-red-500" />
                    <div className="h-3 w-3 rounded-full bg-yellow-500" />
                    <div className="h-3 w-3 rounded-full bg-green-500" />
                  </div>
                </div>
                
                {/* Traffic Chart */}
                <div className="space-y-4">
                  <div>
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Organic Traffic</span>
                      <span className="font-medium text-primary">+185%</span>
                    </div>
                    <div className="mt-2 h-2 w-full rounded-full bg-gray-200">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: '85%' }}
                        transition={{ duration: 1, delay: 0.5 }}
                        className="h-full rounded-full bg-gradient-to-r from-primary to-accent"
                      />
                    </div>
                  </div>
                  
                  <div>
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Keywords Ranked</span>
                      <span className="font-medium text-primary">200+</span>
                    </div>
                    <div className="mt-2 h-2 w-full rounded-full bg-gray-200">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: '70%' }}
                        transition={{ duration: 1, delay: 0.7 }}
                        className="h-full rounded-full bg-gradient-to-r from-primary to-accent"
                      />
                    </div>
                  </div>

                  <div>
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Domain Authority</span>
                      <span className="font-medium text-primary">+45 pts</span>
                    </div>
                    <div className="mt-2 h-2 w-full rounded-full bg-gray-200">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: '60%' }}
                        transition={{ duration: 1, delay: 0.9 }}
                        className="h-full rounded-full bg-gradient-to-r from-primary to-accent"
                      />
                    </div>
                  </div>
                </div>

                {/* AI Status */}
                <div className="mt-6 flex items-center justify-center gap-2 rounded-lg bg-gray-50 py-3">
                  <div className="h-2 w-2 animate-pulse rounded-full bg-green-500" />
                  <span className="text-sm text-gray-600">AI Monitoring Active</span>
                </div>
              </div>

              {/* Floating elements */}
              <motion.div
                animate={{ y: [-10, 10, -10] }}
                transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
                className="absolute -top-4 -right-4 rounded-lg bg-white p-4 shadow-lg"
              >
                <ChartBarIcon className="h-8 w-8 text-primary" />
              </motion.div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  )
}
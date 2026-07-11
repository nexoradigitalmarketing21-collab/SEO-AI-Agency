'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'
import { 
  ChartBarIcon, 
  CogIcon, 
  MagnifyingGlassIcon, 
  MapPinIcon, 
  DocumentTextIcon, 
  CalendarIcon 
} from '@heroicons/react/24/outline'

const services = [
  {
    name: 'SEO Audit',
    description: 'Comprehensive website analysis with actionable recommendations to improve your search rankings.',
    icon: ChartBarIcon,
    href: '/services/seo-audit',
    color: 'from-blue-500 to-indigo-600',
  },
  {
    name: 'Technical SEO',
    description: 'Fix what\'s holding your site back - speed, Core Web Vitals, crawl issues, and more.',
    icon: CogIcon,
    href: '/services/technical-seo',
    color: 'from-purple-500 to-pink-600',
  },
  {
    name: 'Keyword Research',
    description: 'Discover high-value search opportunities your competitors are missing.',
    icon: MagnifyingGlassIcon,
    href: '/services/keyword-research',
    color: 'from-green-500 to-emerald-600',
  },
  {
    name: 'Local SEO',
    description: 'Dominate your local market and get found by customers near you.',
    icon: MapPinIcon,
    href: '/services/local-seo',
    color: 'from-red-500 to-orange-600',
  },
  {
    name: 'Content Strategy',
    description: 'Create content that ranks, engages, and converts visitors into customers.',
    icon: DocumentTextIcon,
    href: '/services/content-strategy',
    color: 'from-yellow-500 to-amber-600',
  },
  {
    name: 'Monthly SEO',
    description: 'Ongoing SEO management that delivers consistent growth month after month.',
    icon: CalendarIcon,
    href: '/services/monthly-seo',
    color: 'from-cyan-500 to-sky-600',
  },
]

export function ServicesGrid() {
  return (
    <section className="py-24 bg-white">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Premium SEO Services
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            Comprehensive SEO solutions tailored to your business goals and industry.
          </p>
        </div>
        <div className="mt-16 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {services.map((service, index) => (
            <motion.div
              key={service.name}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <Link href={service.href} className="card block h-full hover:shadow-lg transition-shadow">
                <div className={`mb-4 inline-flex rounded-lg bg-gradient-to-r p-3 ${service.color}`}>
                  <service.icon className="h-6 w-6 text-white" aria-hidden="true" />
                </div>
                <h3 className="text-xl font-semibold text-gray-900">{service.name}</h3>
                <p className="mt-2 text-gray-600">{service.description}</p>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
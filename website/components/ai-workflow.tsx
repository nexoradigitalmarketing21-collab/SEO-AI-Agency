'use client'

import { motion } from 'framer-motion'
import { 
  MagnifyingGlassIcon,
  CogIcon,
  ChartBarIcon,
  RocketLaunchIcon,
  DocumentChartBarIcon,
  ArrowTrendingUpIcon,
  SparklesIcon
} from '@heroicons/react/24/outline'

const workflowSteps = [
  {
    name: 'Discovery',
    description: 'We analyze your business goals, target audience, and current SEO performance.',
    icon: MagnifyingGlassIcon,
  },
  {
    name: 'Website Analysis',
    description: 'Deep technical audit and competitive analysis to identify opportunities.',
    icon: CogIcon,
  },
  {
    name: 'AI Research',
    description: 'Our AI analyzes search patterns, keywords, and content gaps for maximum impact.',
    icon: SparklesIcon,
  },
  {
    name: 'SEO Strategy',
    description: 'Custom strategy combining AI insights with proven SEO methodologies.',
    icon: ChartBarIcon,
  },
  {
    name: 'Implementation',
    description: 'Execution of on-page, technical, and off-page SEO optimizations.',
    icon: RocketLaunchIcon,
  },
  {
    name: 'Reporting',
    description: 'Transparent tracking and detailed reports on rankings and traffic growth.',
    icon: DocumentChartBarIcon,
  },
  {
    name: 'Growth',
    description: 'Continuous optimization for sustained results and ongoing improvement.',
    icon: ArrowTrendingUpIcon,
  },
]

export function AIWorkflow() {
  return (
    <section className="py-24 bg-gray-50">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Our AI-Powered SEO Process
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            We combine artificial intelligence with expert SEO strategies for maximum results.
          </p>
        </div>
        <div className="mt-16">
          <div className="relative">
            {/* Connecting line */}
            <div className="absolute left-4 top-0 hidden h-full w-0.5 bg-primary/20 lg:left-1/2 lg:block lg:-translate-x-1/2" />
            
            <div className="space-y-12 lg:space-y-16">
              {workflowSteps.map((step, index) => (
                <motion.div
                  key={step.name}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className={`relative flex flex-col gap-6 lg:flex-row lg:items-center ${
                    index % 2 === 0 ? 'lg:flex-row-reverse' : ''
                  }`}
                >
                  <div className="flex-1 lg:text-center">
                    <div className="inline-flex items-center justify-center rounded-xl bg-white p-4 shadow-lg">
                      <step.icon className="h-8 w-8 text-primary" />
                    </div>
                  </div>
                  <div className="flex-1">
                    <div className="card lg:ml-0">
                      <h3 className="text-xl font-semibold text-gray-900">{step.name}</h3>
                      <p className="mt-2 text-gray-600">{step.description}</p>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
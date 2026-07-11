'use client'

import { motion } from 'framer-motion'
import { StarIcon } from '@heroicons/react/24/solid'

const testimonials = [
  {
    name: 'Sarah Johnson',
    company: 'TechFlow SaaS',
    testimonial: 'The best SEO investment we\'ve made. Our traffic increased by 185% in just 6 months. The AI-powered approach really delivers results.',
    rating: 5,
  },
  {
    name: 'Mike Brown',
    company: 'City Dental',
    testimonial: 'Finally found an SEO agency that delivers on their promises. We now rank #1 for all our important local keywords.',
    rating: 5,
  },
  {
    name: 'Jennifer Lee',
    company: 'EcoShop',
    testimonial: 'Our SEO investment paid for itself within the first 3 months. The ongoing management keeps delivering consistent growth.',
    rating: 5,
  },
]

export function Testimonials() {
  return (
    <section className="py-24 bg-gray-50">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            What Our Clients Say
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            Real feedback from businesses we\'ve helped grow.
          </p>
        </div>
        <div className="mt-16 grid grid-cols-1 gap-8 md:grid-cols-3">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={testimonial.name}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="card"
            >
              <div className="flex gap-1 mb-4">
                {Array.from({ length: 5 }).map((_, i) => (
                  <StarIcon
                    key={i}
                    className={`h-5 w-5 ${
                      i < testimonial.rating ? 'text-yellow-400' : 'text-gray-300'
                    }`}
                  />
                ))}
              </div>
              <p className="text-gray-600 italic">"{testimonial.testimonial}"</p>
              <div className="mt-6">
                <p className="font-semibold text-gray-900">{testimonial.name}</p>
                <p className="text-sm text-gray-600">{testimonial.company}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
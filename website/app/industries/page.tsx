import Link from 'next/link'
import { BuildingOfficeIcon, HeartIcon, ShoppingCartIcon, AcademicCapIcon, BanknotesIcon } from '@heroicons/react/24/outline'

export const metadata = {
  title: 'Industries | Nexora Digital Marketing',
  description: 'SEO services tailored to your industry. We specialize in SaaS, healthcare, e-commerce, education, and finance.',
}

const industries = [
  {
    name: 'SaaS',
    description: 'Drive trial signups and subscriptions with SEO that converts.',
    icon: BuildingOfficeIcon,
  },
  {
    name: 'Healthcare',
    description: 'Attract patients and establish authority in the healthcare space.',
    icon: HeartIcon,
  },
  {
    name: 'E-commerce',
    description: 'Increase product visibility and sales with product SEO.',
    icon: ShoppingCartIcon,
  },
  {
    name: 'Education',
    description: 'Rank for educational keywords and grow student enrollment.',
    icon: AcademicCapIcon,
  },
  {
    name: 'Finance',
    description: 'Build trust and attract clients with compliant SEO strategies.',
    icon: BanknotesIcon,
  },
]

export default function IndustriesPage() {
  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Industries We Serve
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              We provide SEO services tailored to your specific industry needs.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {industries.map((industry) => (
              <div key={industry.name} className="card text-center">
                <div className="inline-flex items-center justify-center rounded-lg bg-primary p-4">
                  <industry.icon className="h-8 w-8 text-white" />
                </div>
                <h3 className="mt-4 text-xl font-semibold text-gray-900">{industry.name}</h3>
                <p className="mt-2 text-gray-600">{industry.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
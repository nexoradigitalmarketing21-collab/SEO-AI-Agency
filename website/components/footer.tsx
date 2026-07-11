'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'

const navigation = {
  services: [
    { name: 'SEO Audit', href: '/services/seo-audit' },
    { name: 'Technical SEO', href: '/services/technical-seo' },
    { name: 'Keyword Research', href: '/services/keyword-research' },
    { name: 'Local SEO', href: '/services/local-seo' },
    { name: 'Content Strategy', href: '/services/content-strategy' },
    { name: 'Monthly SEO', href: '/services/monthly-seo' },
  ],
  company: [
    { name: 'About', href: '/about' },
    { name: 'Case Studies', href: '/case-studies' },
    { name: 'Pricing', href: '/pricing' },
    { name: 'Contact', href: '/contact' },
  ],
  resources: [
    { name: 'Blog', href: '/resources/blog' },
    { name: 'SEO Guides', href: '/resources/seo-guides' },
    { name: 'Free Tools', href: '/resources/free-tools' },
  ],
}

export function Footer() {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="mx-auto max-w-7xl px-6 py-12 lg:px-8">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-4">
          {/* Brand */}
          <div className="md:col-span-1">
            <Link href="/" className="text-2xl font-bold">
              <span className="gradient-text">Nexora</span>
            </Link>
            <p className="mt-4 text-sm text-gray-400">
              AI-powered SEO that drives rankings, leads, and revenue for businesses worldwide.
            </p>
            <div className="mt-6 flex space-x-4">
              <a href="#" className="text-gray-400 hover:text-primary transition-colors">
                <span className="sr-only">LinkedIn</span>
                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-9h3v9zm-1.5-10.268c-.966 0-1.722-.756-1.722-1.722s.756-1.722 1.722-1.722 1.722.756 1.722 1.722-.756 1.722-1.722 1.722zm13.5 10.268h-3v-4.5c0-1.078-.02-2.476-1.492-2.476-1.494 0-1.693 1.099-1.693 2.324v4.722h-3v-9h2.908v1.236h.041c.2-.4.621-.814 1.159-.814 1.812 0 2.872 1.912 2.872 4.912v5.872z" />
                </svg>
              </a>
              <a href="#" className="text-gray-400 hover:text-primary transition-colors">
                <span className="sr-only">Twitter</span>
                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M23.953 4.57a9.818 9.818 0 01-2.828.775 9.82 9.82 0 002.163-.394 9.825 9.825 0 01-3.058 3.625 9.758 9.758 0 01-2.627-1.875v.892a9.82 9.82 0 002.581-.724 9.8 9.8 0 01-1.144.175 9.825 9.825 0 01-.836.084 9.825 9.825 0 009.244 8.336c0 6.985-5.642 12.448-12.448 12.448a12.448 12.448 0 007.244 2.24c7.244 0 12.448-5.642 12.448-12.448 0-.19-.006-.379-.015-.566A8.96 8.96 0 0024 4.59z" />
                </svg>
              </a>
            </div>
          </div>

          {/* Services */}
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider">Services</h3>
            <ul className="mt-4 space-y-3">
              {navigation.services.map((item) => (
                <li key={item.name}>
                  <Link href={item.href} className="text-sm text-gray-400 hover:text-primary transition-colors">
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Company */}
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider">Company</h3>
            <ul className="mt-4 space-y-3">
              {navigation.company.map((item) => (
                <li key={item.name}>
                  <Link href={item.href} className="text-sm text-gray-400 hover:text-primary transition-colors">
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Resources & Contact */}
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider">Resources</h3>
            <ul className="mt-4 space-y-3">
              {navigation.resources.map((item) => (
                <li key={item.name}>
                  <Link href={item.href} className="text-sm text-gray-400 hover:text-primary transition-colors">
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
            <div className="mt-6">
              <h3 className="text-sm font-semibold uppercase tracking-wider">Contact</h3>
              <p className="mt-4 text-sm text-gray-400">hello@nexora.ai</p>
            </div>
          </div>
        </div>

        <div className="mt-12 border-t border-gray-800 pt-8">
          <p className="text-center text-sm text-gray-400">
            &copy; {new Date().getFullYear()} Nexora Digital Marketing. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}
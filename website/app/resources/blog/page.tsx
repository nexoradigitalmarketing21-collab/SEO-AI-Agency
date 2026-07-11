'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'

export default function BlogPage() {
  const posts = [
    {
      title: 'Complete SEO Guide for 2025',
      excerpt: 'Everything you need to know about SEO in 2025 - from technical optimization to content strategy.',
      date: '2025-01-15',
      readTime: '8 min read',
      slug: 'complete-seo-guide-2025',
    },
    {
      title: 'Local SEO: The Complete Guide for Small Businesses',
      excerpt: 'Dominate local search and attract more customers with these proven strategies.',
      date: '2025-01-10',
      readTime: '6 min read',
      slug: 'local-seo-guide-small-businesses',
    },
    {
      title: 'Technical SEO Checklist: 50+ Points to Check',
      excerpt: 'A comprehensive technical SEO audit checklist to improve your website\'s performance.',
      date: '2025-01-05',
      readTime: '10 min read',
      slug: 'technical-seo-checklist',
    },
  ]

  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              SEO Blog
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Latest strategies, tips, and insights from our team.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="space-y-12">
            {posts.map((post, index) => (
              <motion.div
                key={post.slug}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="card"
              >
                <h2 className="text-2xl font-bold text-gray-900">
                  <Link href={`/resources/blog/${post.slug}`} className="hover:text-primary transition-colors">
                    {post.title}
                  </Link>
                </h2>
                <p className="mt-2 text-gray-600">{post.excerpt}</p>
                <div className="mt-4 flex items-center gap-4 text-sm text-gray-500">
                  <span>{new Date(post.date).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</span>
                  <span>•</span>
                  <span>{post.readTime}</span>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
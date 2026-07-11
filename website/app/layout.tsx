import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Navbar } from '@/components/navbar'
import { Footer } from '@/components/footer'
import { OrganizationSchema, WebsiteSchema } from '@/components/schema-org'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Nexora Digital Marketing - AI-Powered SEO Agency',
  description: 'AI-Powered SEO That Drives Rankings, Leads & Revenue',
  keywords: 'SEO, AI SEO, digital marketing, search engine optimization, content strategy',
  authors: [{ name: 'Nexora Digital Marketing' }],
  creator: 'Nexora Digital Marketing',
  publisher: 'Nexora Digital Marketing',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://nexora.ai',
    siteName: 'Nexora Digital Marketing',
    images: [
      {
        url: 'https://nexora.ai/og-image.png',
        width: 1200,
        height: 630,
        alt: 'Nexora Digital Marketing - AI-Powered SEO',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Nexora Digital Marketing - AI-Powered SEO Agency',
    description: 'AI-Powered SEO That Drives Rankings, Leads & Revenue',
    images: ['https://nexora.ai/og-image.png'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <OrganizationSchema />
        <WebsiteSchema />
      </head>
      <body className={`${inter.className} bg-white text-gray-900 antialiased`}>
        <Navbar />
        <main className="min-h-screen">{children}</main>
        <Footer />
      </body>
    </html>
  )
}
export const dynamic = 'force-static'

export async function GET() {
  const robotsTxt = `
User-agent: *
Allow: /

Sitemap: https://nexora.ai/sitemap.xml
Sitemap: https://nexora.ai/server-sitemap.xml

Disallow: /api/
Disallow: /admin/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /
`
  return new Response(robotsTxt, {
    headers: {
      'Content-Type': 'text/plain',
    },
  })
}
# Technical SEO Knowledge Base

## Purpose

This comprehensive guide covers all aspects of technical SEO, providing the foundational knowledge needed to optimize websites for search engines and ensure maximum crawlability, indexation, and performance.

**This knowledge base is the definitive reference for all technical SEO implementations.**

---

## Table of Contents

1. [Crawlability & Indexation](#crawlability--indexation)
2. [Site Architecture](#site-architecture)
3. [Page Speed & Core Web Vitals](#page-speed--core-web-vitals)
4. [Mobile Optimization](#mobile-optimization)
5. [Security (HTTPS)](#security-https)
6. [Structured Data & Schema](#structured-data--schema)
7. [URL Structure](#url-structure)
8. [Canonicalization](#canonicalization)
9. [Redirects](#redirects)
10. [International SEO](#international-seo)
11. [Technical SEO Tools](#technical-seo-tools)
12. [Common Technical SEO Issues](#common-technical-seo-issues)

---

## Crawlability & Indexation

### Robots.txt

**Purpose:** Control search engine crawler access to website sections

**Best Practices:**
- Place in root directory (example.com/robots.txt)
- Use proper syntax: User-agent, Disallow, Allow, Crawl-delay
- Don't block CSS or JavaScript files
- Test with Google's Robots.txt Tester
- Include sitemap reference

**Example:**
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Sitemap: https://example.com/sitemap.xml
```

### XML Sitemaps

**Purpose:** Help search engines discover and understand website content

**Best Practices:**
- Create XML sitemap for all important pages
- Include only canonical, indexable pages
- Update sitemap when content changes
- Submit to Google Search Console and Bing Webmaster Tools
- Keep sitemap under 50,000 URLs (split if needed)
- Use proper XML syntax
- Include lastmod dates
- Compress large sitemaps (.gz)

**Sitemap Types:**
- XML sitemap (pages)
- Image sitemap (images)
- Video sitemap (videos)
- News sitemap (news content)
- Mobile sitemap (mobile-specific)

### Meta Robots Tags

**Purpose:** Control how search engines index and display pages

**Directives:**
- `index` - Allow indexing (default)
- `noindex` - Prevent indexing
- `follow` - Follow links (default)
- `nofollow` - Don't follow links
- `noarchive` - Don't show cached version
- `nosnippet` - Don't show snippet in results
- `noimageindex` - Don't index images on page

**Implementation:**
```html
<meta name="robots" content="index, follow">
<meta name="robots" content="noindex, nofollow">
```

### Crawl Budget Optimization

**What is Crawl Budget?**
- Number of pages Google crawls on your site
- Based on site authority, freshness, and server response

**Optimization Strategies:**
- Fix crawl errors (404s, 5xx errors)
- Improve site speed
- Update content regularly
- Use internal linking strategically
- Remove duplicate content
- Block low-value pages with robots.txt
- Use URL parameters carefully
- Optimize server response time

---

## Site Architecture

### Information Architecture

**Principles:**
- Keep important pages within 3 clicks from homepage
- Use logical, hierarchical structure
- Implement breadcrumb navigation
- Create clear category structure
- Use silo structure for topical authority
- Ensure every page is reachable via internal links

**Best Practices:**
- Plan architecture before development
- Use logical URL structure
- Implement breadcrumbs
- Create XML sitemap reflecting architecture
- Use internal linking to reinforce structure
- Avoid orphan pages (no internal links)

### Internal Linking

**Purpose:** Distribute link equity, help crawlers discover content, establish topical relevance

**Best Practices:**
- Link to important pages from homepage
- Use descriptive anchor text
- Link contextually within content
- Create topic clusters with pillar pages
- Use breadcrumb navigation
- Link to related content
- Avoid excessive linking (100+ links per page)
- Fix broken internal links
- Use nofollow for untrusted/external links

**Internal Linking Strategies:**
- Silo structure
- Topic clusters
- Contextual linking
- Navigational linking
- Footer linking
- Related posts linking

### URL Structure

**Best Practices:**
- Keep URLs short and descriptive
- Use hyphens to separate words
- Include target keywords naturally
- Use lowercase letters
- Avoid special characters
- Avoid session IDs and parameters when possible
- Use HTTPS
- Avoid duplicate URLs for same content
- Match URL to page title/topic

**Example:**
```
Good: https://example.com/seo-services/technical-seo
Bad: https://example.com/p=123&cat=45&id=789
```

---

## Page Speed & Core Web Vitals

### Core Web Vitals (CWV)

**Google's Page Experience Metrics:**

#### 1. Largest Contentful Paint (LCP)
- **What:** Loading performance
- **Target:** < 2.5 seconds
- **Optimization:**
  - Optimize images (WebP, lazy loading)
  - Use CDN
  - Minimize render-blocking resources
  - Implement caching
  - Use fast hosting

#### 2. First Input Delay (FID)
- **What:** Interactivity
- **Target:** < 100 milliseconds
- **Optimization:**
  - Minimize JavaScript
  - Break up long tasks
  - Use web workers
  - Remove unused JavaScript
  - Compress JavaScript files

#### 3. Cumulative Layout Shift (CLS)
- **What:** Visual stability
- **Target:** < 0.1
- **Optimization:**
  - Set size attributes on images/videos
  - Avoid inserting content above existing content
  - Use transform animations
  - Preload fonts
  - Reserve space for ads/embeds

### Page Speed Optimization

**Image Optimization:**
- Use modern formats (WebP, AVIF)
- Compress images (TinyPNG, Squoosh)
- Implement lazy loading
- Use responsive images (srcset)
- Specify image dimensions
- Use CDN for images

**Code Optimization:**
- Minify HTML, CSS, JavaScript
- Remove unused code
- Combine files where appropriate
- Use CSS instead of images when possible
- Optimize CSS delivery
- Defer non-critical JavaScript
- Use async/defer attributes

**Caching:**
- Implement browser caching
- Use CDN
- Cache static assets
- Set appropriate cache headers
- Use service workers

**Server Optimization:**
- Use fast hosting
- Implement CDN
- Optimize database queries
- Use server-side caching
- Enable compression (Gzip/Brotli)
- Use HTTP/2 or HTTP/3
- Reduce server response time (TTFB < 600ms)

**Tools:**
- Google PageSpeed Insights
- GTmetrix
- WebPageTest
- Lighthouse
- Core Web Vitals report in GSC

---

## Mobile Optimization

### Mobile-First Indexing

**What is It?**
- Google primarily uses mobile version for indexing and ranking
- Mobile and desktop content should match

**Requirements:**
- Same content on mobile and desktop
- Same structured data on both versions
- Same meta tags on both versions
- Ensure mobile version is crawlable
- Check for mobile-specific errors

### Responsive Design

**Best Practices:**
- Use responsive design (recommended)
- Or use dynamic serving with proper Vary HTTP header
- Or use separate mobile URLs (m.example.com) with proper annotations
- Test on multiple devices and screen sizes
- Ensure touch targets are large enough (48x48px minimum)
- Use readable font sizes (16px minimum)
- Avoid horizontal scrolling
- Optimize for portrait and landscape

### Mobile Usability

**Common Issues:**
- Viewport not set
- Touch elements too close
- Fixed-width content
- Content wider than screen
- Font size too small

**Testing:**
- Google Mobile-Friendly Test
- Search Console Mobile Usability report
- Real device testing
- Browser dev tools device emulation

---

## Security (HTTPS)

### HTTPS Implementation

**Why HTTPS?**
- Ranking signal
- Security for users
- Required for HTTP/2
- Required for many modern web features
- Builds trust

**Implementation Steps:**
1. Obtain SSL/TLS certificate
2. Install certificate on server
3. Configure server to use HTTPS
4. Update all internal links to HTTPS
5. Implement 301 redirects from HTTP to HTTPS
6. Update canonical tags to HTTPS
7. Update XML sitemaps to HTTPS
8. Update robots.txt to HTTPS
9. Update Google Search Console property
10. Update third-party tools

**Best Practices:**
- Use 301 redirects (not 302)
- Use HSTS header
- Update all resources to HTTPS
- Avoid mixed content (HTTP resources on HTTPS pages)
- Use secure cookies
- Implement proper certificate management

### Mixed Content

**What is It?**
- HTTPS page loading HTTP resources (images, scripts, stylesheets)

**Fix:**
- Update all URLs to HTTPS
- Use protocol-relative URLs (//example.com/image.jpg)
- Test with browser console
- Use Google Search Console to identify

---

## Structured Data & Schema

### What is Structured Data?

**Purpose:**
- Help search engines understand content
- Enable rich results in search
- Improve click-through rates
- Enhance search appearance

**Common Schema Types:**
- Article
- BlogPosting
- LocalBusiness
- Organization
- Product
- Review
- FAQ
- HowTo
- Recipe
- Event
- VideoObject
- BreadcrumbList
- WebSite
- Organization

### Implementation Methods

**1. JSON-LD (Recommended)**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png"
}
</script>
```

**2. Microdata**
```html
<div itemscope itemtype="https://schema.org/Organization">
  <span itemprop="name">Company Name</span>
</div>
```

**3. RDFa**
```html
<div vocab="https://schema.org/" typeof="Organization">
  <span property="name">Company Name</span>
</div>
```

### Schema Best Practices

- Use JSON-LD when possible
- Follow Google's guidelines
- Test with Rich Results Test
- Validate with Schema.org validator
- Don't use schema for deceptive purposes
- Keep schema updated
- Use required properties
- Use recommended properties when possible
- Monitor for errors in Search Console

---

## URL Structure

### URL Best Practices

**Do:**
- Keep URLs short and descriptive
- Use hyphens to separate words
- Include target keywords naturally
- Use lowercase letters
- Match URL to page content
- Use HTTPS
- Keep URL structure consistent

**Don't:**
- Use underscores (use hyphens)
- Use special characters
- Use uppercase letters
- Make URLs too long (>100 characters)
- Use unnecessary parameters
- Use session IDs in URLs
- Create duplicate URLs for same content

### URL Parameters

**Issues:**
- Can create duplicate content
- Waste crawl budget
- Cause indexing issues

**Solutions:**
- Use URL parameter handling in Search Console
- Use canonical tags
- Use robots.txt to block problematic parameters
- Use static URLs when possible
- Keep parameters to minimum

---

## Canonicalization

### What is Canonicalization?

**Purpose:** Tell search engines which version of a URL is the preferred/primary version

**When to Use:**
- Duplicate content across multiple URLs
- URL parameters creating duplicates
- HTTP vs HTTPS
- www vs non-www
- Trailing slashes
- Case sensitivity

### Canonical Tag Implementation

```html
<link rel="canonical" href="https://example.com/preferred-url/">
```

**Best Practices:**
- Use absolute URLs
- Point to the preferred version
- Use on all duplicate pages
- Ensure canonical URL is accessible
- Don't canonicalize to 404 pages
- Use consistent canonical across site
- Include in XML sitemaps

### Common Canonical Issues

- Canonical chain (A → B → C)
- Canonical to redirect
- Canonical to 404
- Multiple canonicals on one page
- Canonical not matching sitemap
- Canonical on unique pages

---

## Redirects

### 301 Redirect (Permanent)

**Use When:**
- Page permanently moved
- URL structure changed
- HTTP to HTTPS
- www to non-www (or vice versa)
- Domain change

**Implementation:**
- Apache (.htaccess): `Redirect 301 /old-url /new-url`
- Nginx: `return 301 /new-url;`
- PHP: `header("HTTP/1.1 301 Moved Permanently");`
- WordPress: Use Redirection plugin

### 302 Redirect (Temporary)

**Use When:**
- Page temporarily moved
- A/B testing
- Geographic redirects
- Device-specific redirects

**Note:** Search engines may continue to index original URL

### Redirect Chains & Loops

**Issues:**
- Waste crawl budget
- Slow down site
- Lose link equity
- Poor user experience

**Solutions:**
- Avoid redirect chains (redirect directly to final URL)
- Fix redirect loops
- Update internal links to point directly to final URL
- Regularly audit redirects

### Redirect Best Practices

- Use 301 for permanent changes
- Redirect to equivalent content
- Update internal links
- Update XML sitemaps
- Monitor for errors
- Keep chains short (ideally 0-1 redirects)
- Don't redirect to irrelevant pages

---

## International SEO

### Hreflang Implementation

**Purpose:** Tell search engines about different language/region versions of a page

**Implementation Methods:**

**1. HTML Link Elements:**
```html
<link rel="alternate" hreflang="en-us" href="https://example.com/en-us/page" />
<link rel="alternate" hreflang="en-gb" href="https://example.com/en-gb/page" />
<link rel="alternate" hreflang="es" href="https://example.com/es/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

**2. HTTP Headers:**
```
Link: <https://example.com/en-us/page>; rel="alternate"; hreflang="en-us"
```

**3. XML Sitemap:**
```xml
<xhtml:link rel="alternate" hreflang="en-us" href="https://example.com/en-us/page" />
```

### Hreflang Best Practices

- Include all language/region versions
- Include self-referencing tag
- Include x-default for fallback
- Use ISO language and country codes
- Ensure bidirectional linking
- Use absolute URLs
- Test implementation
- Monitor for errors in Search Console

### ccTLD vs Subdomain vs Subdirectory

**ccTLD (example.co.uk):**
- Strong geo-targeting signal
- More expensive
- Harder to manage
- Good for country-specific sites

**Subdomain (uk.example.com):**
- Easy to set up
- Can be hosted separately
- Moderate geo-targeting signal
- Good for large multinational sites

**Subdirectory (example.com/uk/):**
- Easy to manage
- Shares domain authority
- Moderate geo-targeting signal
- Good for most international sites

---

## Technical SEO Tools

### Essential Tools

**Crawl & Indexation:**
- Google Search Console (free)
- Bing Webmaster Tools (free)
- Screaming Frog SEO Spider (free up to 500 URLs)
- Sitebulb
- DeepCrawl
- Botify

**Page Speed:**
- Google PageSpeed Insights (free)
- GTmetrix (free)
- WebPageTest (free)
- Lighthouse (free, in Chrome DevTools)
- Core Web Vitals report in GSC

**Mobile:**
- Google Mobile-Friendly Test (free)
- BrowserStack
- Responsinator

**Structured Data:**
- Google Rich Results Test (free)
- Schema.org Validator (free)
- Schema Markup Generator

**Security:**
- SSL Labs SSL Test (free)
- SecurityHeaders.com (free)

**Performance:**
- WebPageTest (free)
- Pingdom
- New Relic
- Datadog

---

## Common Technical SEO Issues

### Crawl Errors

**404 Not Found:**
- Fix broken internal links
- Set up 301 redirects for moved pages
- Create custom 404 page
- Monitor in Search Console

**5xx Server Errors:**
- Fix server issues
- Improve server capacity
- Optimize database queries
- Contact hosting provider

**Robots.txt Blocking:**
- Review robots.txt
- Unblock important resources
- Test with Robots.txt Tester

### Duplicate Content

**Causes:**
- URL parameters
- HTTP vs HTTPS
- www vs non-www
- Trailing slashes
- Printer-friendly versions
- Session IDs
- Duplicate product descriptions

**Solutions:**
- Implement canonical tags
- Use 301 redirects
- Remove duplicate content
- Use noindex where appropriate
- Consolidate duplicate pages

### Thin Content

**Issue:** Pages with little or no original content

**Solutions:**
- Add valuable content
- Remove thin pages
- Consolidate similar pages
- Add unique product descriptions
- Create comprehensive content

### Slow Page Speed

**Causes:**
- Large images
- Unoptimized code
- Too many HTTP requests
- No caching
- Slow hosting
- Render-blocking resources

**Solutions:**
- Optimize images
- Minify code
- Implement caching
- Use CDN
- Improve hosting
- Remove render-blocking resources

### Mobile Issues

**Common Problems:**
- Not mobile-friendly
- Slow mobile speed
- Intrusive interstitials
- Unplayable content
- Incorrect viewport

**Solutions:**
- Implement responsive design
- Optimize mobile speed
- Remove intrusive interstitials
- Ensure content is playable
- Set correct viewport

### Security Issues

**Common Problems:**
- Not using HTTPS
- Mixed content
- Expired SSL certificate
- Security vulnerabilities

**Solutions:**
- Implement HTTPS
- Fix mixed content
- Renew SSL certificate
- Regular security audits

---

## Technical SEO Checklist

### On-Page Technical SEO

- [ ] HTTPS implemented
- [ ] SSL certificate valid
- [ ] No mixed content
- [ ] Robots.txt properly configured
- [ ] XML sitemap created and submitted
- [ ] Meta robots tags correct
- [ ] Canonical tags implemented
- [ ] No duplicate content
- [ ] URL structure optimized
- [ ] 404 page created
- [ ] 301 redirects for changed URLs
- [ ] No redirect chains
- [ ] Structured data implemented
- [ ] Schema validated

### Performance

- [ ] Page speed optimized
- [ ] Images optimized
- [ ] Code minified
- [ ] Caching implemented
- [ ] CDN used
- [ ] Gzip/Brotli compression enabled
- [ ] Core Web Vitals passing
- [ ] Mobile speed optimized

### Mobile

- [ ] Responsive design implemented
- [ ] Mobile-friendly test passed
- [ ] Viewport set correctly
- [ ] Touch targets adequate size
- [ ] Font size readable
- [ ] No horizontal scrolling
- [ ] Mobile usability issues fixed

### Indexation

- [ ] Important pages indexed
- [ ] No unwanted pages indexed
- [ ] Crawl errors fixed
- [ ] Crawl budget optimized
- [ ] Internal linking optimized
- [ ] Orphan pages fixed
- [ ] XML sitemap accurate

### International (if applicable)

- [ ] Hreflang implemented
- [ ] Language/region targeting set
- [ ] ccTLD/subdomain/subdirectory chosen
- [ ] Hreflang tags validated
- [ ] No hreflang errors

---

## Technical SEO Best Practices

### General Principles

1. **Crawl First:** Ensure search engines can crawl your site
2. **Index Second:** Ensure important pages are indexed
3. **Rank Third:** Optimize for ranking factors
4. **User Experience:** Always prioritize users
5. **Performance:** Speed matters
6. **Mobile:** Mobile-first is mandatory
7. **Security:** HTTPS is required
8. **Standards:** Follow web standards
9. **Monitoring:** Continuously monitor
10. **Continuous Improvement:** Always optimize

### Implementation Priority

**High Priority:**
- HTTPS implementation
- Fix crawl errors
- Fix indexation issues
- Implement XML sitemap
- Fix mobile usability issues
- Improve page speed

**Medium Priority:**
- Implement structured data
- Optimize URL structure
- Implement canonical tags
- Fix duplicate content
- Optimize internal linking

**Ongoing:**
- Monitor Search Console
- Regular technical audits
- Performance optimization
- Security updates
- Stay current with best practices

---

## Notes

- Technical SEO is the foundation of all SEO
- Without technical SEO, other SEO efforts are wasted
- Regular technical audits are essential
- Monitor Search Console for issues
- Stay current with Google's guidelines
- Test all changes before implementing
- Document all technical changes
- Technical SEO is ongoing, not one-time
- Performance directly impacts rankings
- Mobile optimization is mandatory
- Security is non-negotiable
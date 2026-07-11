import { CalendarIcon, ClockIcon, VideoCameraIcon } from '@heroicons/react/24/outline'

export const metadata = {
  title: 'Book Strategy Call | Nexora Digital Marketing',
  description: 'Schedule a free 30-minute SEO strategy call. We\'ll analyze your website and create a custom action plan.',
}

export default function BookStrategyCallPage() {
  return (
    <div className="pt-24">
      <section className="py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
              Book Your Free Strategy Call
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Get a 30-minute consultation to discuss your SEO goals and create a custom strategy.
            </p>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="max-w-2xl mx-auto">
            <div className="card">
              <div className="space-y-6">
                <div className="flex items-center gap-4">
                  <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary">
                    <CalendarIcon className="h-6 w-6 text-white" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">Pick a Date</h3>
                    <p className="text-gray-600">Select a time that works for you</p>
                  </div>
                </div>
                
                <div className="flex items-center gap-4">
                  <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary">
                    <ClockIcon className="h-6 w-6 text-white" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">30 Minutes</h3>
                    <p className="text-gray-600">Focused SEO consultation</p>
                  </div>
                </div>

                <div className="flex items-center gap-4">
                  <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary">
                    <VideoCameraIcon className="h-6 w-6 text-white" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">Video Call</h3>
                    <p className="text-gray-600">Connect via Zoom or Google Meet</p>
                  </div>
                </div>

                <form className="mt-8 space-y-6">
                  <div>
                    <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                      Full Name
                    </label>
                    <input
                      type="text"
                      id="name"
                      required
                      className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
                    />
                  </div>
                  
                  <div>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                      Work Email
                    </label>
                    <input
                      type="email"
                      id="email"
                      required
                      className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
                    />
                  </div>

                  <div>
                    <label htmlFor="website" className="block text-sm font-medium text-gray-700">
                      Website URL
                    </label>
                    <input
                      type="url"
                      id="website"
                      required
                      placeholder="https://example.com"
                      className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
                    />
                  </div>

                  <div>
                    <label htmlFor="service" className="block text-sm font-medium text-gray-700">
                      Service Interest
                    </label>
                    <select
                      id="service"
                      className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
                    >
                      <option>SEO Audit</option>
                      <option>Monthly SEO</option>
                      <option>Technical SEO</option>
                      <option>Keyword Research</option>
                      <option>Local SEO</option>
                      <option>Content Strategy</option>
                    </select>
                  </div>

                  <button type="submit" className="btn-primary w-full">
                    Book Free Consultation
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
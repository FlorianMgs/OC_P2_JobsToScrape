import scrapy


class PythonOrgPostsSpider(scrapy.Spider):
    name = "python_org_posts"
    start_urls = [
        'https://www.python.org/jobs/'
    ]

    def format_locations(self, element):
        formatted = element.replace('Remote', '').replace('/', '').replace('virtual', '')
        words = formatted.split(' ')
        formatted = ' '.join(x for x in words if x != 'or' and x != ' ')
        return formatted

    def parse(self, response):
        for post in response.xpath('//*[@id="content"]/div/section/div/ol/li'):
            yield {
                'title': post.css('.listing-company-name a::text').get(),
                'link': 'https://www.python.org' + post.css('.listing-company-name a::attr(href)').get(),
                'city': self.format_locations(post.css('.listing-location a::text').get().split(', ')[0]),
                'state': self.format_locations(post.css('.listing-location a::text').get().split(', ')[1]),
                'country': self.format_locations(post.css('.listing-location a::text').get().split(', ')[-1]),
                'job type': ', '.join(post.css('.listing-job-type a::text').getall()),
                'put date': post.css('time::text').get(),
                'categories': post.css('.listing-company-category a::text').get(),
                'remote': 'Yes' if 'Remote' in post.css('.listing-location a::text').get() else 'No',
                'relocation': ''
            }
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

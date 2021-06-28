import scrapy
import re


class DjangojobsPostsSpider(scrapy.Spider):
    name = "djangojobs_posts"
    start_urls = [
        'https://djangojobs.net/jobs/'
    ]

    def format_html(self, data):
        pattern = re.compile(r'<.*?>')
        return pattern.sub('', data)

    def parse(self, response):
        titles = response.css('blockquote h4 a').getall()
        links = response.css('blockquote h4 a::attr(href)').getall()

        #Locations & put date
        locations_put_dates = response.css('.clearfix div::text').getall()
        put_dates = []
        cities = []
        states = []
        countries = []
        for elmt in locations_put_dates:
            locations = elmt.split(' | ')[0].split(',')
            put_dates.append(elmt.split(' | ')[-1])
            cities.append(locations[0])
            if 'United States' in locations:
                states.append(locations[1])
            else:
                states.append('')
            countries.append(locations[-1])

        #Remote and Relocation
        remote_relocation = response.css('.clearfix').getall()
        remote = []
        relocation = []
        for elmt in remote_relocation:
            formatted = self.format_html(elmt)
            check = formatted.split('|')
            if 'Yes' in check[0]:
                remote.append('Yes')
            else:
                remote.append('No')
            if 'Yes' in check[1]:
                relocation.append('Yes')
            else:
                relocation.append('No')

        for i, title in enumerate(titles):
            yield {
                'title': self.format_html(str(title)),
                'link': 'https://djangojobs.net' + links[i],
                'city': cities[i],
                'state': states[i],
                'country': countries[i],
                'job type': '',
                'put date': put_dates[i],
                'categories': '',
                'remote': remote[i],
                'relocation': relocation[i]
            }

        next_page = response.xpath('/html/body/div[1]/div[4]/div/div[22]/ul/li[7]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

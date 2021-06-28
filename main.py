from JobsToScrape.JobsToScrape.spiders.pythonorg_posts_spider import *
from JobsToScrape.JobsToScrape.spiders.djangojobs_posts_spider import *

from link_scraper import *

from twisted.internet import defer, reactor
from scrapy.crawler import CrawlerRunner


python_org_url = 'https://www.python.org/jobs/'
python_org_types_links = LinkScraper().get_links(python_org_url, type='types')
python_org_categories_links = LinkScraper().get_links(python_org_url, type='categories')

#Python.org: All posts

allpost_settings = {
    "FEEDS": {
        "data/python_org/all_posts.csv": {"format": "csv"},
    },
}
process_all_posts = CrawlerRunner(settings=allpost_settings)


#Python.org: posts by Types:
i = 0
for type, url in python_org_types_links.items():
    types_posts_settings = {
        "FEEDS": {
            "data/python_org/types_posts/" + type + ".csv": {"format": "csv"},
        },
    }
    process_type_posts = CrawlerRunner(settings=types_posts_settings)
    process_type_posts.crawl(PythonOrgPostsSpider, start_urls=[url])


#Python.org: posts by Categories:
i = 0
for type, url in python_org_categories_links.items():
    types_categories_settings = {
        "FEEDS": {
            "data/python_org/categories_posts/" + type + ".csv": {"format": "csv"},
        },
    }
    process_categories_posts = CrawlerRunner(settings=types_categories_settings)
    process_categories_posts.crawl(PythonOrgPostsSpider, start_urls=[url])


#Djangojobs: all posts
allpost_settings = {
    "FEEDS": {
        "data/djangojobs/all_posts.csv": {"format": "csv"},
    },
}
process_djangojobs = CrawlerRunner(settings=allpost_settings)


@defer.inlineCallbacks
def crawl():
    yield process_all_posts.crawl(PythonOrgPostsSpider)
    yield process_type_posts.crawl(PythonOrgPostsSpider)
    yield process_categories_posts.crawl(PythonOrgPostsSpider)
    yield process_djangojobs.crawl(DjangojobsPostsSpider)
    reactor.stop()


crawl()
reactor.run()

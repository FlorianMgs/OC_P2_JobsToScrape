import requests
from bs4 import BeautifulSoup


class LinkScraper:

    def get_soup(self, link):
        soup = BeautifulSoup(requests.get(link).text, 'lxml')

        return soup

    def get_links(self, link, type):
        if type == "types":
            li_class = 'tier-1 element-2'
        else:
            li_class = 'tier-1 element-3'
        soup = self.get_soup(link)
        menu = soup.find('nav', {'id': 'mainnav'})
        links_type = menu.ul.find('li', {'class': li_class}).ul
        link_items = links_type.find_all('li')
        links = {}
        for link in link_items:
            links[link.a.text.replace('/', '-')] = 'https://www.python.org' + link.a.get('href')

        return links

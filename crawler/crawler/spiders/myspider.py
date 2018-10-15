import scrapy
from scrapy.spiders import Spider as BS
from crawler.items import CrawlerItem
from scrapy.http import Request

class MySpider(BS):
    name = "crawler"
    '''
    def __init__(self, name=name, allowed_domains=[], start_urls=[]):
       BS.__init__(self, name=name, allowed_domains=allowed_domains, start_urls=start_urls)
       #self.name = name
       #self.allowed_domains = allowed_domains
       #self.start_urls = start_urls
    '''
    name = 'crawler'
    allowed_domains = ['bbs.hupu.com']
    start_urls = [
        'https://bbs.hupu.com/23925679.html',
    ]

    def start_requests(self):
        print('Start requests')
        for url in self.start_urls:
            print(url)
            yield Request(url, self.parse)

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
        print(response.text)

if __name__ == '__main__':
    sp = MySpider(name='crawler', allowed_domains=['hupu.com'], start_urls=['https://bbs.hupu.com/23925679-2.html'])
    print(sp.start_urls)
    sp.start_requests()
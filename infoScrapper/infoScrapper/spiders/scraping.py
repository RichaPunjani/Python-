#  To run this file in pycharm in edit configuration name your module as "scrapy.cmdline"
#  and parameter as "crawl scrapper" since scrapper is the name of this spider

import scrapy
import text2emotion as te

class QuotesSpider(scrapy.Spider):                  #class of the spider
    name = "scrapper"                               #name of the spider
    start_urls = [
        'https://www.amazon.in/'
        ]                                           #initializing starting urls for spider

    def parse(self, response):
        page = response.url.split('.')[1]
        filename = f'{page}.html'                   #creating html file
        with open(filename, 'wb') as f:
            f.write(response.body)                  #writing html response scrapped from urls


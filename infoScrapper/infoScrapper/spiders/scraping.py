#  To run this file in pycharm in edit configuration name your module as "scrapy.cmdline"
#  and parameter as "crawl scrapper" since scrapper is the name of this spider
import os

import scrapy
from scrapy.selector import Selector
import text2emotion as te
import csv

class QuotesSpider(scrapy.Spider):                  #class of the spider
    name = "scrapper"                               #name of the spider
    start_urls = [
        'https://www.bbc.com/'
        ]                                           #initializing starting urls for spider

    def parse(self, response):
        page = response.url.split('.')[1]
        filename = f'{page}.html'                   #creating html file
        with open(filename, 'wb') as f:
            f.write(response.body)                  #writing html response scrapped from urls
        self.res=response

        self.storeResponse();

    def storeResponse(self):
            titles = Selector(response=self.res).xpath('//li/div/@data-bbc-title').getall()
            filename=f'{self.res.url.split(".")[1]}.csv'
            with open(filename, mode='w') as csv_file:
                fieldnames = ['Headline', 'Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()

                for item in titles:
                    print (te.get_emotion(item))
                    emotion=te.get_emotion(item)
                    writer.writerow({'Headline':item,
                                     'Happy':emotion['Happy'],
                                     'Angry':emotion['Angry'],
                                     'Surprise':emotion['Surprise'],
                                     'Sad':emotion['Sad'],
                                     'Fear':emotion['Fear']})




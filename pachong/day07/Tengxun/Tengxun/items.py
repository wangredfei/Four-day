# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    zhName = scrapy.Field()
    zhLink = scrapy.Field()
    zhType = scrapy.Field()
    zhNum = scrapy.Field()
    zhAddress = scrapy.Field()
    zhTime = scrapy.Field()

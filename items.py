# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class BookItem(scrapy.Item):
      # define the fields for your item here like:
      ID=scrapy.Field()
      bTitle = scrapy.Field()
      bAuthor = scrapy.Field()
      bPublisher = scrapy.Field()
      bDate = scrapy.Field()
      bPrice = scrapy.Field()
      bDetail = scrapy.Field()
      bImage = scrapy.Field()


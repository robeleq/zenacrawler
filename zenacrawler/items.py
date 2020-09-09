# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitspaces(value):
    return value.strip()

class ZenaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    headline = scrapy.Field()
    text = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitspaces),
        output_processor=TakeFirst(),
    )
    pass

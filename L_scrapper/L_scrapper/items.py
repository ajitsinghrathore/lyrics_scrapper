# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class lyrics_item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    lyrics  = scrapy.Field()
    song_id = scrapy.Field()
    genere = scrapy.Field()
    title = scrapy.Field()
    


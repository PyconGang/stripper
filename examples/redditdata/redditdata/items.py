"""
This represents the collection of items around the reddit scraper
"""

from scrapy.Item import Item, Field


class RedditPost(Item):
    title = Field()
    votes = Field()
    link = Field()

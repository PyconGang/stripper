"""
This represents the collection of items around the reddit scraper
"""

from scrapy.item import Item, Field


class RedditPost(Item):
    title = Field()
    votes = Field()
    url = Field()

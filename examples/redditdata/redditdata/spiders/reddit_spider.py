"""
This is a spider for /r/Python reddit posts
"""
from scrapy.spider import Spider
from scrapy.selector import Selector
from redditdata.items import RedditPost


class RedditSpider(Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = [
        'http://www.reddit.com/r/python'
    ]

    def parse(self, response):
        """

        @url http://www.reddit.com/r/python
        :param response: the object that represents the data returned from the scraper's access to the site
        :return: list of data scraped by the scraper
        """
        sel = Selector(response)
        sites = sel.xpath(""" TODO: get xpath for post""")
        posts = []

        for site in sites:
            post = RedditPost()
            post['title'] = site.xpath(' TODO: get xpath for title /text()').extract()
            post['upvotes'] = site.xpath(' TODO: get xpath for upvote').text()
            post['url'] = site.xpath('TODO: get xpath for url /@href').extract()
            posts.append(post)

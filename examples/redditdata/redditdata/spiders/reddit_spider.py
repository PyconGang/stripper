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
        sites = sel.xpath('//*[@id="siteTable"]/div')
        posts = []

        # TODO: test this shit
        for site in sites:
            post = RedditPost()
            post['title'] = site.xpath('/div[2]/p[1]/a/text()').extract()
            post['votes'] = site.xpath('/div[1]/div[3]').text()
            post['url'] = site.xpath('/div[2]/p[1]/a/@href').extract()
            posts.append(post)

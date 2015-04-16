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
        posts = sel.xpath('//*[@id="siteTable"]/div[contains(@class, "thing")]')
        parsed_posts = []

        # TODO: test this shit
        for post in posts:
            parsed_post = RedditPost()
            parsed_post['votes'] = post.xpath('div[1]/div[@class="score unvoted"]/text()').extract()
            parsed_post['title'] = post.xpath('div[2]/p/a[contains(@class, "title")]/text()').extract()
            parsed_post['url'] = post.xpath('div[2]/p/a[contains(@class, "title")]/@href').extract()
            parsed_posts.append(parsed_post)
        return parsed_posts
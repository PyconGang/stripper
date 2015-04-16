# -*- coding: utf-8 -*-

# Scrapy settings for redditdata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'redditdata'

SPIDER_MODULES = ['redditdata.spiders']
NEWSPIDER_MODULE = 'redditdata.spiders'
DEFAULT_ITEM_CLASS = 'redditdata.items.RedditPost'
ITEM_PIPELINES = {'redditdata.pipelines.PostPipeline'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'stripper (+http://stripperspider.org)'

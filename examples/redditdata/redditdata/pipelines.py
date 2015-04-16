# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PostPipeline(object):
    """
    A pipeline for changing those posts with no votes that are represented by
    \u2022 (HTML for dot) with 0
    """
    null_score = u'\u2022'

    def process_item(self, item, spider):
        if self.null_score in item['votes']:
            item['votes'] = u'0'
        return item

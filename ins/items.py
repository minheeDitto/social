# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class UniformItem(Item):
    """
    统一格式的Item

    为了返回同意的格式，同
    时保留最初的信息多样性
    """
    resource_account_id = Field()  # 账号Id
    text = Field()  # 朋友圈内容
    publish_time = Field()  # 推送时间
    crawler_time = Field()  # 爬取时间
    hash = Field()  # ID + 账号哈希值
    image = Field()  # 图片
    last_publish_time = Field()  # 存储Java传过来的最后发布时间参数

class FB(Item):
    name = Field()
    home_page = Field()

class FB_group(Item):
    name = Field()
    home_page = Field()
    property = Field()
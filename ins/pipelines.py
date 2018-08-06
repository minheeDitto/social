# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class InsPipeline(object):
    d = set()
    def process_item(self, item, spider):
        if spider.name == 'FB':
            with open('FB.txt', 'a',encoding='utf-8') as f:
                f.write("name is "+ item["name"] +'    home page is  '+ item["home_page"] + '\n' )
            return item
        if spider.name == 'member_FB':
            with open('member_FB.txt', 'a', encoding='utf-8') as f:
                f.write("name is " + item["name"] + '    home page is  ' + item["home_page"] + '\n')
            return item
        if spider.name == 'FB_group':
            with open('group.txt', 'a', encoding='utf-8') as f:
                f.write("name is " + item["name"] + '    home page is  ' + item["home_page"] + '\n')
            return item
        if spider.name == 'inst':
            with open('ins.txt', 'a', encoding='utf-8') as f:
                f.write("name is " + item["username"] + '\n')
            return item
        if spider.name == 'twi':
            with open('twi.txt', 'a', encoding='utf-8') as f:
                f.write("name is " + item["username"] + '\n')
            return item
        if spider.name == 'fb_fans':
             # with open('fb_fans.txt', 'a', encoding='utf-8') as f:
             #     f.write("name is " + item["name"] + "  home page is  "+item["home_page"] + '\n')
             client = pymongo.MongoClient(host='localhost', port=27017)
             table = client["zhangzhen"]["zhang"]
             table.insert(item)
             return item


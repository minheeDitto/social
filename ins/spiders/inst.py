# -*- coding: utf-8 -*-
import json
import re
import scrapy
from copy import deepcopy
from ins.items import UniformItem
import datetime
import time
from ins.function.get_hash import gen_hash

class InstSpider(scrapy.Spider):
    name = 'inst'
    allowed_domains = ['instagram.com']
    # start_urls = ['https://www.instagram.com/jiang.ly/']
    follow_hash =  '149bef52a3b2af88c0fec37913fe1cbc'
    info_hash = 'c6809c9c025875ac6f02619eae97a80e'
    base_url = 'https://www.instagram.com/graphql/query/?'

    def __init__(self):
        self.crawl =set()


    def start_requests(self):
        a = ['jiang.ly', 'seojuhyun_s', 'yoona__lim']
        """
            request the user home_page for user_id
        """
        for i in a:
            yield scrapy.Request(
                url='https://www.instagram.com/{}/'.format(i),
                callback=self.user_id,
                dont_filter=True,
            )

    def user_id(self, response):
        """
        get user_id and follows_id , callback for follows_info
        :param response:
        """
        user_id = deepcopy(re.findall('profilePage\_(\d+)', response.body.decode()))
        print(user_id)
        if len(user_id) != 0:
            # yield scrapy.Request(
            #     self.base_url+"query_hash="+self.info_hash+'&variables={"id": %d,"first":12}' % (int(user_id[0])),
            #     callback=self.user_info,
            #     dont_filter=True,
            #
            #     meta={"user_id": user_id[0]},
            #     priority=10
            #     )
            follows_query_hash = self.follow_hash
            follows_base_url = self.base_url
            id = "id"
            url =  '%squery_hash=%s&variables={"%s":"%s","first":24}' %(follows_base_url, follows_query_hash, id, user_id[0])
            yield scrapy.Request(
               url,
                callback=self.follows_info,
                dont_filter=True,
                meta={"user_id":user_id[0]},
                priority=5
            )

    def follows_info(self, response):
        """
        get the follows's username
        :param response:
        :return: username
        """
        user_id = deepcopy(response.meta["user_id"])
        follows_user_info = json.loads(response.body.decode())
        follows_user_id = follows_user_info["data"]["user"]["edge_followed_by"]["edges"]

        if len(follows_user_id) == 0:
            return


        next_cursor = follows_user_info["data"]["user"]["edge_followed_by"]["page_info"]["has_next_page"]
        if next_cursor:
            after = follows_user_info["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
            id = "id"
            query_hash = self.follow_hash
            base_url = self.base_url
            yield scrapy.Request(
                '%squery_hash=%s&variables={"%s":"%s", "first": 12, "after":"%s" }' % (base_url, query_hash, id, user_id, after),
                callback=self.follows_info,
                meta={"user_id":user_id},
                priority=9
            )

        for follow_user_id in follows_user_id:
            username = follow_user_id["node"]["username"]
            if user_id == '6434246318':
                # print(username)
                yield {"username": username}
            # if username not in self.crawl:
            #     yield scrapy.Request(
            #         url='https://www.instagram.com/{}/'.format(username),
            #         callback=self.user_id,
            #         dont_filter=True,
            #         priority=4
            #     )

    # def user_info(self, response):
    #     """
    #     get the user data
    #     :param response:
    #     :return:detail user infomation
    #     """
    #     user_id = deepcopy(response.meta["user_id"])
    #
    #     """deepcopy for preventing data cover"""
    #
    #     data = deepcopy(json.loads(response.body.decode()))
    #     edges = data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
    #     if len(data) != 0:
    #         if len(edges) == 0:
    #             return
    #         for photo in edges:
    #             photo = photo["node"]
    #             url = photo["display_url"]
    #             twetts_id = photo["id"]
    #
    #             item = UniformItem()
    #             item["resource_account_id"] = user_id
    #             text = ''
    #             example = photo["edge_media_to_caption"]["edges"]
    #             if example:
    #                 text = example[0]["node"].get("text", None)
    #             item["text"] = text
    #             publish_time = photo["taken_at_timestamp"]
    #             publish_time = datetime.datetime.fromtimestamp(int(publish_time))
    #             item["publish_time"] = publish_time
    #             item["crawler_time"] = int(time.time())
    #             item["hash"] = gen_hash(twetts_id, publish_time, user_id)
    #             item["image"] = url
    #             print(item)
    #
    #
    #         next_cursor = data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
    #         if next_cursor:
    #             after = data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
    #             id = "id"
    #             query_hash = self.info_hash
    #             base_url = self.base_url
    #             yield scrapy.Request(
    #                 '%squery_hash=%s&variables={"%s":"%s","first":12,"after":"%s"}' % (base_url, query_hash, id, user_id, after),
    #                 callback=self.user_info,
    #                 dont_filter=True,
    #                 meta={"user_id": user_id},
    #                       priority=9
    #             )




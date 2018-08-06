# -*- coding: utf-8 -*-
import json

import scrapy
import re
from copy import deepcopy
from ins.twitter_get_userid import get_user_id
from urllib.parse import quote
from ins.items import UniformItem
from ins.function.get_hash import gen_hash
from ins.items import FB


class TwiSpider(scrapy.Spider):
    name = 'twi'
    allowed_domains = ['twitter.com']
    # start_urls = ['https://mobile.twitter.com/koko_villal_']
    home_url = 'https://twitter.com/{}'
    auth =  "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    article_url = 'https://api.twitter.com/2/timeline/profile/{}.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&send_error_codes=true&include_tweet_replies=false&userId={}&count=20&ext=mediaStats%2ChighlightedLabel'
    article_cursor_url = 'https://api.twitter.com/2/timeline/profile/{}.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&send_error_codes=true&include_tweet_replies=false&userId={}&count=20&cursor={}&ext=mediaStats%2ChighlightedLabel'
    follow_url = 'https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor=-1&user_id={}&count=20'
    follow_cursor_url = 'https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor={}&user_id={}&count=20'
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
}
    def __init__(self):
        self.crawl = set()

    def start_requests(self):
        # self.crawl.add('938326738353844224')
        a = ["koko_villal_", "Hyoyeon_djhyo", "chelsietrillo", "heyitsmechexsy_"]
        # b = ["koko_villal_"]

        for i in a:
            user_id = get_user_id(i)
            yield scrapy.Request(
                url=self.home_url.format(i),
                callback=self.parse,
                headers=self.headers,
                meta={"user_id": user_id}
            )

    def parse(self, response):
        user_id = deepcopy(response.meta["user_id"])
        cookie = response.request.headers.getlist('Cookie')[0].decode()
        ct0 = re.findall('ct0\=(.*?)\;', cookie)
        if len(ct0) != 0:
            ct0 = ct0[0]
        else:
            ct0 = re.findall('ct0\=(.*)', cookie)[0]

        headers = {

            "authorization": self.auth,
            "x-csrf-token": ct0,
            "user-agent":self.headers["user-agent"]

        }
        # url = self.article_url.format(user_id, user_id)
        # yield scrapy.Request(
        #     url,
        #     callback=self.detail_article,
        #     headers=headers,
        #     meta={"user_id": user_id, "ct0": ct0},
        #     priority=10,
        #     dont_filter=True,
        # )
        yield scrapy.Request(
            url = self.follow_url.format(user_id),
            callback=self.follow_info,
            meta={"user_id": deepcopy(user_id)},
            headers=headers,
            priority=7,
            dont_filter=True,


        )

    def follow_info(self, response):
        cookie = response.request.headers.getlist('Cookie')[0].decode()
        ct0 = re.findall('ct0\=(.*?)\;', cookie)

        if len(ct0) != 0:
            ct0 = ct0[0]
        else:
            ct0 = re.findall('ct0\=(.*)', cookie)[0]
        print(ct0)
        headers = {

            "authorization": self.auth,
            "x-csrf-token": ct0,


        }
        user_id = deepcopy(response.meta["user_id"])
        users = json.loads(response.body.decode())
        for user in users["users"]:
            id_str = user["id_str"]
            print(user["screen_name"])
            yield {"username":user["screen_name"]}
            # if id_str not in  self.crawl:
                #  self.crawl.add(id_str)
                # yield scrapy.Request(
                #     self.home_url.format(user["screen_name"]),
                #     callback=self.parse,
                #     meta={"user_id": deepcopy(id_str)},
                #     dont_filter=True
                #
                #
                # )
        next_cursor_str = users["next_cursor_str"]
        if next_cursor_str != '0':
            yield scrapy.Request(
                url=self.follow_cursor_url.format(next_cursor_str, user_id),
                callback=self.follow_info,

                headers=headers,
                dont_filter=True,
                meta={"user_id": deepcopy(user_id)}
            )

    # def other_follow_info(self, response):
    #     cookie = response.request.headers.getlist('Cookie')[0].decode()
    #     ct0 = re.findall('ct0\=(.*?)\;', cookie)
    #     if len(ct0) != 0:
    #         ct0 = ct0[0]
    #     else:
    #         ct0 = re.findall('ct0\=(.*)', cookie)[0]
    #     user_id = deepcopy(response.meta["user_id"])
    #     users = json.loads(response.body.decode())
    #     for user in users["users"]:
    #         id_str = user["id_str"]
    #         print(user["screen_name"])
    #     headers = {
    #
    #         "authorization": self.auth,
    #         "x-csrf-token": ct0,
    #     }
    #     next_cursor_str = users["next_cursor_str"]
    #     if next_cursor_str != '0':
    #         yield scrapy.Request(
    #             url=self.follow_cursor_url.format(next_cursor_str, user_id),
    #             callback=self.other_follow_info,
    #
    #             headers=headers,
    #             dont_filter=True,
    #             meta={"user_id": deepcopy(user_id)}
    #         )

    # def detail_article(self, response):
    #     cookie = response.request.headers.getlist('Cookie')[0].decode()
    #     ct0 = re.findall('ct0\=(.*?)\;', cookie)
    #     if len(ct0) != 0:
    #         ct0 = ct0[0]
    #     else:
    #         ct0 = re.findall('ct0\=(.*)', cookie)[0]
    #     user_id = deepcopy(response.meta["user_id"])
    #     headers = {
    #
    #         "authorization": self.auth,
    #         "x-csrf-token": ct0,
    #
    #     }
    #     datas = deepcopy(json.loads(response.body.decode())["globalObjects"]["tweets"])
    #     if len(datas) == 0:
    #         return
    #     img_list = []
    #     for data in datas.values():
    #         item = UniformItem()
    #         twitter_img = data["entities"].get("media", None)
    #         if twitter_img:
    #             for img in twitter_img:
    #                 media_url = img["media_url"]
    #                 img_list.append(media_url)
    #
    #         item["image"] = img_list
    #         item["text"] = data["full_text"]
    #         item["publish_time"] = data["created_at"]
    #         item["crawler_time"] = int(time.time())
    #         item["resource_account_id"] = user_id
    #         print(item)
    #     cursor = json.loads(response.body.decode())["timeline"]["instructions"][0]["addEntries"]["entries"][-1]["content"]["operation"]["cursor"]["value"]
    #     cursor = quote(cursor)
    #     yield scrapy.Request(
    #         self.article_cursor_url.format(user_id, user_id, cursor),
    #         callback=self.detail_article,
    #         meta={"user_id": user_id,},
    #         headers=headers,
    #         dont_filter=True,
    #         priority=8
    #
    #         )



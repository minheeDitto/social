# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
# from ins.cookies import cookies
# from ins.user_agents import agents
import logging
import time
# from ins.twitter_cookie import Cookies
import asyncio

import time
from ins.FB_get_cookies import get_cookies, get




logger = logging.getLogger(__name__)
logging.getLogger('selenium').setLevel(logging.DEBUG)



class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = "https://127.0.0.1:1080"


class InstUserAgentMiddleware(object):

    def process_request(self, request, spider):
        request.meta['User-Agent'] = random.choice(agents)


class InsMiddleWare(object):
    # def process_request(self, request, spider):
    #     if spider.name == 'inst':
    #         cookie = random.choice(cookies)
    #         request.cookies = cookie

    def process_response(self, request, response, spider):
        if spider.name == 'twi':
            response_status = response.status

            if response_status == 200:
                logger.debug("爬取成功")
                return response
            else:
                logging.warning("{}遭遇爬虫,休息十秒,状态码{}".format(spider.name, response.status))
                clock = 0
                sleep_time = 10
                while clock < sleep_time:
                    rest_clock = sleep_time - clock
                    time.sleep(1)
                    clock += 1
                logger.debug("爬虫重新启动中，正在爬取{}".format(request))
                return request
        else:
            return response


class TwitterMiddle(object):
    def process_request(self, request, spider):
        if spider.name == "twi":
            cookie = random.choice(Cookies)
            request.cookies = cookie


class FacebookMiddle(object):
    def process_request(self, request, spider):
        if spider.name == 'FB' or spider.name == 'member_FB' or spider.name == 'FB_group' or spider.name == 'fb_fans':
            cookies = get()
            request.cookies = cookies






























# -*- coding: utf-8 -*-
import scrapy
from ins.items import FB
import time
import re
from lxml import etree
from html.parser import HTMLParser

class MemberFbSpider(scrapy.Spider):
    name = 'member_FB'
    allowed_domains = ['facebook.com']
    Time = int(time.time())
    # start_urls = ['http://facebook.com/']
    base_url = "https://m.facebook.com"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1", }

    def start_requests(self):
        Time = int(time.time())
        url = 'https://m.facebook.com/groups/453117594700340?group_view_referrer=unknown'

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            headers=self.headers,
        )


    def parse(self, response):
        ajax = re.findall('\"encrypted\":\"(.*?)\"', response.body.decode())[0]
        fb_dtsg = re.findall(r'fb_dtsg\\\" value=\\\"(.*?)\\', response.body.decode())[0]
        url = 'https://m.facebook.com/browse/group/members/?id=453117594700340&start=0&listType=list_nonfriend_nonadmin&refid=18&__m_async_page__=&m_sess=&__dyn=&__req=&__ajax__={}&__user=100024814180169'.format(ajax)
        yield scrapy.Request(
            url=url,
            headers=self.headers,
            callback=self.member_info,
            meta={"fb_dtsg": fb_dtsg, "ajax": ajax},
            dont_filter=False,

        )

    def member_info(self, response):
        fb_dtsg = response.meta["fb_dtsg"]
        ajax = response.meta["ajax"]
        html = HTMLParser().unescape(re.sub(r'\\','',re.sub(r"\\u003C",'<', response.body.decode())))
        next_cursor = re.findall(r'm_more_item\",\"href\"\:\"(/browse.*?)\",',html)[0]
        member_info = re.findall(r'html\"\:\"(.*?)\",\"replaceifexists',html)[0]
        real_member_info = etree.HTML(member_info).xpath("//div[@class='_55x2']/div")
        for i in real_member_info:
            if len(i.xpath("./div[2]/div/div/h3/text()")) != 0:
                person_info = FB()
                person_info["name"] = i.xpath("./div[2]/div/div/h3/text()")[0]
                person_info["home_page"] = i.xpath("./div[last()]/div/a/@href")[0]
                print(person_info)
                yield person_info
        data = {
            "m_sess": "",
            "fb_dtsg":fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax,
            "__user": "100024814180169",

        }
        real_friend_url = self.base_url + next_cursor
        yield scrapy.FormRequest(
            url=real_friend_url,
            formdata=data,
            callback=self.other_member_info,
            meta={"ajax": ajax, "fb_dtsg": fb_dtsg},
            headers=self.headers,
        )

    def other_member_info(self, response):
        ajax = response.meta["ajax"]
        fb_dtsg = response.meta["fb_dtsg"]
        data = {
            "m_sess": "",
            "fb_dtsg": fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax,
            "__user": "100024814180169",

        }

        html = HTMLParser().unescape(re.sub(r'\\','',re.sub(r"\\u003C",'<', response.body.decode())))
        next_cursor = re.findall(r'href\"\:\"(/browse.*?)\"', html)
        real_info = re.findall(r'\"html\":\"(.*?)\",\"replaceifexists', html)[0]
        member_info = etree.HTML(real_info).xpath("//div[@class='_55x2']/div")
        print(html)

        for i in member_info:
            if len(i.xpath(".//div[@class='_5xu4']//h1[1]/text()")) != 0:
                person_info = FB()
                person_info["name"] = i.xpath(".//div[@class='_5xu4']//h1[1]/text()")[0]
                person_info["home_page"] = i.xpath("./div[last()]/div/a/@href")[0]
                print(person_info)
                yield person_info
        if len(next_cursor):
            yield scrapy.FormRequest(
                    url=self.base_url + next_cursor[0],
                    formdata=data,
                    callback=self.other_member_info,
                    meta={"ajax": ajax, "fb_dtsg": fb_dtsg},
                headers=self.headers,
                )






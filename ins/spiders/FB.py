# -*- coding: utf-8 -*-
import scrapy
import time
from copy import deepcopy
from ins.items import FB
import re
from html.parser import HTMLParser
from lxml import etree


class FbSpider(scrapy.Spider):
    name = 'FB'
    allowed_domains = ['facebook.com']

    def __init__(self, *args, **kwargs):
        super(FbSpider, self).__init__(*args, **kwargs)
    # start_urls = ['http://facebook.com/'
        self.fans_homepage1 = "https://m.facebook.com{}/friends?lst=100024814180169%3A{}%3A{}&refid=17&ref=page_internal"
        self.fans_homepage2 = "https://m.facebook.com/profile.php?v=friends&lst=100024814180169%3A{}%3A{}&id={}&ref=page_internal"
        # self.more_base_url = "https://m.facebook.com/profile.php?v=friends&unit_cursor={}&lst=100024814180169%100024814180169%3A{}&id=100024814180169"
        self.headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1", }
        self.base_url = "https://m.facebook.com"

    def start_requests(self):
        Time = int(time.time())
        url = f'https://m.facebook.com/profile.php?v=friends&lst=100024814180169%3A100015142061592%3A{self.Time}&id=100024814180169'

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            headers=self.headers,
        )

    def parse(self, response):
        friend_name = response.xpath("//div[@class='_55wo _55x2']//h3[@class='_52jh _5pxc']")
        for i in friend_name:
            if len(i.xpath('./a/@href').extract()) != 0:
                home_page = i.xpath("./a/@href").extract_first()
            else:
                home_page = ''
            person_info = FB()
            person_info["name"] = i.xpath("./a/text()").extract_first()
            person_info["home_page"] = home_page
            yield person_info
        fb_dtsg = response.xpath("//input[@name='fb_dtsg']/@value").extract_first()
        ajax = re.findall('\"encrypted\":\"(.*?)\"', response.body.decode())[0]

        more_friends_url = re.findall(r'\"m_more_friends\",\"href\":\"\\(.*?)\",', response.body.decode())
        if len(more_friends_url) != 0:
            real_friend_url =  re.sub(r'\\','',self.base_url + re.sub(r"\\u0025", "%",more_friends_url[0],2))


            data = {
                "m_sess": "",
                "fb_dtsg": fb_dtsg,
                "__dyn": " ",
                "__req": " ",
                "__ajax__": ajax,
                "__user": "100024814180169"
                }
            yield scrapy.FormRequest(
                url=real_friend_url,
                formdata=data,
                callback=self.follows_info,
                meta={"fb_dtsg":fb_dtsg, "ajax": ajax},
                headers=self.headers,
            )

    def follows_info(self, response):
        fb_dtsg = response.meta["fb_dtsg"]
        ajax = response.meta["ajax"]
        data = {
            "m_sess": "",
            "fb_dtsg": fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax,
            "__user": "100024814180169"
        }

        html = deepcopy(response.body.decode())
        next_cursor = re.findall(r'm_more_friends.*?href\\\":\\\"\\\\\\(.*?)\"', html)
        if len(next_cursor) !=0 :
            real_cursor = self.base_url + re.sub(r'\\', '', re.sub(r"\\u0025", "%", next_cursor[0], 2))
        # print(next_cursor)
        r_html = re.sub(r'\\','',re.sub(r'\\u003C','<',re.findall(r'\"html\":\"(.*?)\",\"replaceifexists\"', html)[0]))
        # print(r_html)
        real_html =  etree.HTML(HTMLParser().unescape(r_html)).xpath("//div[@class='_55wo _55x2']//div[@class='_55wp _4g33 _5pxa']")
        for i in real_html:
            person_info = FB()
            home_page = i.xpath("./div[@class='_5s61 _2b4m']/a/@href")
            if len(home_page) == 0:
                home_page = ''
            else:
                home_page = home_page[0]
            name = i.xpath("./div[@class='_5s61 _2b4m']/a/i/@aria-label")[0]
            person_info["name"] = name
            person_info["home_page"] = home_page
            print(person_info)
            yield person_info

        if len(next_cursor) != 0:
            yield scrapy.FormRequest(
                url = real_cursor,
                formdata=data,
                callback=self.follows_info,
                meta={"fb_dtsg": fb_dtsg, "ajax": ajax},
                headers=self.headers

            )








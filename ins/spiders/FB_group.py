# -*- coding: utf-8 -*-
import re
from copy import deepcopy
from html.parser import HTMLParser
from ins.items import FB_group
import scrapy
from lxml import etree


class FbGroupSpider(scrapy.Spider):
    name = 'FB_group'
    allowed_domains = ['facebook.com']
    # start_urls = ['http://facebook.com/]
    base_url = "https://www.facebook.com/pages_reaction_units/more/?"
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def start_requests(self):
        url = 'https://www.facebook.com/groups/Scifiandbooklovers/members/'
        yield scrapy.Request(
            url=url,
            headers=self.headers,
            meta={"property":"book"},
            callback=self.parse
        )

    def parse(self, response):
        """
        get first page member_info
        :param response:
        """
        property = deepcopy(response.meta["property"])
        html = response.body.decode()
        members_info = re.findall(r'\"hidden_elem\"\>\<code id="u_0_1.*?"\>\<\!\-\-(.*?)\-\-\>\<\/code\>', html)[0]
        real_members = etree.HTML(members_info).xpath("//div[@id='groupsMemberBrowserContent']/div[2]//ul/div")
        master = etree.HTML(members_info).xpath("//div[@class='fbProfileBrowser']//div[@class='_60ri fsl fwb fcb']/a[1]")[0]
        person_info = FB_group()
        person_info["name"] = master.xpath('./text()')[0]
        person_info["home_page"] = master.xpath("./@href")[0]
        person_info["property"] = property
        for member in real_members:
            person_info = FB_group()
            name = member.xpath("./div/div[2]/div/div[2]/div/a/text()")[0]
            person_info["name"] = name
            home_page = member.xpath("./div/div[2]/div/div[2]/div/a/@href")[0]
            person_info["home_page"] = home_page
            person_info["property"] = property
            yield person_info
        next_cursor_url = self.base_url + re.findall(r'(\/ajax\/browser.*?)\"',HTMLParser().unescape(members_info))[0]

        yield scrapy.Request(
            url=next_cursor_url + '&__a=1',
            callback=self.next_member_info,
            headers=self.headers
        )

    def next_member_info(self, response):
        """
        until cursor is empty, repeat crawl next member_information
        :param response:
        """
        next_html = deepcopy(response.body.decode())
        next_member_info = re.findall(r'__html\"\:\"(.*?)\"\}', next_html)[0]
        real_member_info = re.sub(r'\\', '', HTMLParser().unescape(re.sub(r'\\u003C', '<', next_member_info)))
        """
        continous to native html code
        """
        take_members = etree.HTML(real_member_info).xpath("//ul//div[@class='clearfix _60rh _gse']")
        for member in take_members:
            person_info = FB_group()
            name = member.xpath("./a[1]/img/@aria-label")[0]
            person_info["name"] = name
            home_page = member.xpath("./a[1]/@href")[0]
            person_info["home_page"] = home_page
            person_info["property"] = property
            yield person_info
        next_curosr = etree.HTML(real_member_info).xpath("//div[@class='clearfix mam uiMorePager stat_elem morePager _52jv']/div[1]/a[1]/@href")
        if len(next_curosr) != 0 :
            yield scrapy.Request(
                url=self.base_url + next_curosr[0] + '&__a=1',
                callback=self.next_member_info,
                headers=self.headers
            )








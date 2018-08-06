# -*- coding: utf-8 -*-
from scrapy import Spider as BaseSpider
from scrapy import Request, FormRequest
from html.parser import HTMLParser
import lxml
import re
import copy
import time



class FbFansSpider(BaseSpider):
    name = 'fb_fans'
    allowed_domains = ['facebook.com']
    # start_urls = ['http://facebook.com/']
    fans_friend = set()


    def __init__(self, *args, **kwargs):
        super(FbFansSpider, self).__init__(*args, **kwargs)
        self.fans_homepage1 = "https://m.facebook.com{}/friends?lst=100024814180169%3A{}%3A{}&refid=17&ref=page_internal"
        self.fans_homepage2 = "https://m.facebook.com/profile.php?v=friends&lst=100024814180169%3A{}%3A{}&id={}&ref=page_internal"
        self.base_url = "https://m.facebook.com"
        self.fans_list = ["chineseog"]
        self.home_page = 'https://m.facebook.com/{}/posts/?ref =page_internal&mt_nav=1&__nodl&_rdr'
        self.fans_page = 'https://m.facebook.com/ufi/reaction/profile/browser/?__m_async_page__=&__ajax__={}&ft_ent_identifier={}'
        self.base_url = 'https://m.facebook.com'
        self.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Mobile Safari/537.36"}

    def start_requests(self):
        for url in self.fans_list:
            yield Request(
                url=self.home_page.format(url),
                headers=self.headers,
                meta={"remove_id": url}
             )

    def parse(self, response):
        """
        第一部分获取第一页动态的点赞人数页面的关键参数fbid，然后回调get_fans_page
        第二部分找到下一页地址进行回调到next_page
        :param response:
        """
        remove_id = response.meta["remove_id"]
        html = HTMLParser().unescape(response.body.decode())
        html_str = lxml.etree.HTML(html)
        fb_dtsg = re.findall(r'\"dtsg\":{\"token\"\:\"(.*?)\"',html)[0]
        ajax = re.findall('\"encrypted\":\"(.*?)\"', html)[0]
        text = html_str.xpath("//div[@id='pages_msite_body_contents']//div[@class='_55wo _gui']")

        for i in text[1:2]:
            id = re.findall(r'fbid\=(\d+)',i.xpath(".//div[@class='_4g33 _52we _34qc _3hxn _3myz _4b45']/div/a/@href")[0])[0]
            yield Request(
                url=self.fans_page.format(ajax, id),
                headers=self.headers,
                callback=self.get_fans_page,
                meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": ajax, "remove_id": remove_id})

            )

        data1 = {
            "m_sess":"",
            "fb_dtsg": fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax
        }
        cursor = re.findall(r'm_pages_reaction_see_more_unit\",\"href\"\:\"(.*?)\"', html)
        # if len(cursor) != 0:
        #     real_cursor = re.sub(r'\\', '', eval("u\"" + cursor[0] + "\""))
        #     yield FormRequest(
        #         url=self.base_url+real_cursor,
        #         headers=self.headers,
        #         formdata=data1,
        #         callback=self.next_page,
        #         meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": ajax, "remove_id": remove_id})
        #
        #     )

    def next_page(self, response):
        """
        第一部分同上获取fbid（若版主更新头像以及其他动态需要重新获取适当的参数）然后进行回调获取点赞的人的昵称和主页信息
        第二部分不断访问下一页进行回调，直到为空。
        :param response:
        """
        remove_id = response.meta["remove_id"]

        fb_dtsg = response.meta["fb_dtsg"]
        ajax = response.meta["ajax"]
        data1 = {
            "m_sess": "",
            "fb_dtsg": fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax
        }
        html= copy.deepcopy(re.findall(r'm_pages_reaction_see_more_unit\",\"html\":\"(.*?)\",\"replaceifexists\"', response.body.decode())[0])
        real_html = re.sub(r'\\', '', re.sub(r'\\u003C', '<', HTMLParser().unescape(html)))
        # print(real_html)
        get_fbid = lxml.etree.HTML(real_html).xpath("//div[@class='_3-8x']//div[@class='_55wo _gui']")
        if len(get_fbid) != 0:
            for i in get_fbid:
                first_id = i.xpath(".//div[@class='_4g33 _52we _34qc _3hxn _3myz _4b45']/div/a/@href")

                if len(first_id) != 0:
                    id = re.findall(r'fbid\=(\d+)', first_id[0])
                    if len(id) == 0:
                        id = re.findall(r'\/(\d+)\/\?', first_id[0])
                    yield Request(
                        url=self.fans_page.format(ajax, id[0]),
                        headers=self.headers,
                        callback=self.get_fans_page,
                        meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": "ajax", "remove_id": remove_id})
                    )


        cursor = re.findall(r'm_pages_reaction_see_more_unit\\",\\"href\\"\:\\"(.*?)\\",\\"proximity_pages', response.body.decode())
        if len(cursor) !=0 :
            cursor = re.sub(r'\\\\u0025', '%', re.sub(r'\\\\\\','', cursor[0]))
            yield FormRequest(
                url=self.base_url + cursor,
                headers=self.headers,
                callback=self.next_page,
                formdata=data1,
                meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": "ajax", "remove_id": remove_id})
            )

    def get_fans_page(self, response):
        """
        获取点赞的人的昵称以及主页信(若有下一页的cursor，则回调进行访问)
        :param response:
        """
        remove_id = response.meta["remove_id"]
        ajax = response.meta["ajax"]
        fb_dtsg = response.meta["fb_dtsg"]
        html = copy.deepcopy(re.findall(r'html"\:\"(.*?)\","replaceifexists', response.body.decode()))

        click_person = HTMLParser().unescape(re.sub(r'\\', '', re.sub(r'\\u0025', '%', re.sub(r"\\u003C", '<', html[0]))))
        if len(click_person) != 0:
            get_person_homepage = lxml.etree.HTML(click_person).xpath("//div[contains(@class,'_1uja')]")
            if len(get_person_homepage) != 0:
                for i in get_person_homepage:
                    person_info = {}
                    person_info["name"] = i.xpath(".//a[@class='darkTouch _1aj5 l']/i/@aria-label")[0]
                    home_page = i.xpath(".//a[@class='darkTouch _1aj5 l']/@href")[0]
                    person_info["home_page"] = home_page
                    if remove_id not in home_page:
                        if 'profile.php' in home_page:
                            person_id = home_page.split("=")[-1]
                            yield Request(
                                url=self.fans_homepage2.format(person_id, str(int(time.time())), person_id),
                                callback=self.get_fans_friends,
                                headers=self.headers,
                                dont_filter=False,
                            )
                        else:
                            yield Request(
                                url=self.base_url+home_page,
                                headers=self.headers,
                                callback=self.get_fans_id,
                                dont_filter=False,
                                meta={"home_page": copy.deepcopy(home_page)}
                            )


        data1 = {
            "m_sess": "",
            "fb_dtsg": fb_dtsg,
            "__dyn": " ",
            "__req": " ",
            "__ajax__": ajax
        }
        if len(click_person) != 0:
            next_fans_page = lxml.etree.HTML(click_person).xpath("//div[@id='reaction_profile_pager']/a/@href")
            if len(next_fans_page) != 0:
                yield FormRequest(
                    url=self.base_url+next_fans_page[0],
                    callback=self.get_fans_page,
                    headers=self.headers,
                    formdata=data1,
                    meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": "ajax", "remove_id": remove_id})

                )
            else:
                html = copy.deepcopy(re.findall(r'reaction_profile_pager\",\"html\"\:\"(.*?)\","replaceifexists',response.body.decode()))
                if len(html) != 0 :
                    get_next = HTMLParser().unescape(re.sub(r'\\', '', re.sub(r'\\u0025', '%', re.sub(r"\\u003C", '<', html[0]))))
                    next_page = lxml.etree.HTML(get_next).xpath("//div[@id='reaction_profile_pager']/a[1]/@href")
                    if len(next_page) !=0 :
                        yield FormRequest(
                            url=self.base_url+next_page[0],
                            callback=self.get_fans_page,
                            headers=self.headers,
                            formdata=data1,
                            meta=copy.deepcopy({"fb_dtsg": fb_dtsg, "ajax": "ajax", "remove_id": remove_id})
                        )

    def get_fans_id(self, response):
        home_page = response.meta["home_page"]
        fans_id = re.findall(r'"entity_id":(\d+)', response.body.decode())[0]
        yield Request(
            url=self.fans_homepage1.format(home_page, fans_id, str(int(time.time()))),
            callback=self.get_fans_friends,
            headers=self.headers,
        )



    def get_fans_friends(self, response):
        print(response.url)
        friend_name = response.xpath("//div[@class='_55wo _55x2']//h3[@class='_52jh _5pxc']")
        if len(friend_name) !=0:
            for i in friend_name:
                if len(i.xpath('./a/@href').extract()) != 0:
                    home_page = i.xpath("./a/@href").extract_first()
                else:
                    home_page = ''
                person_info = {}
                person_info["name"] = i.xpath("./a/text()").extract_first()
                person_info["home_page"] = home_page
                yield person_info
            fb_dtsg = response.xpath("//input[@name='fb_dtsg']/@value").extract_first()
            ajax = re.findall('\"encrypted\":\"(.*?)\"', response.body.decode())[0]

            more_friends_url = re.findall(r'\"m_more_friends\",\"href\":\"\\(.*?)\",', response.body.decode())
            if len(more_friends_url) != 0:
                real_friend_url = re.sub(r'\\', '', self.base_url + re.sub(r"\\u0025", "%", more_friends_url[0], 2))

                data = {
                    "m_sess": "",
                    "fb_dtsg": fb_dtsg,
                    "__dyn": " ",
                    "__req": " ",
                    "__ajax__": ajax,
                    "__user": "100024814180169"
                }
                yield FormRequest(
                    url=real_friend_url,
                    formdata=data,
                    callback=self.follows_info,
                    meta={"fb_dtsg": fb_dtsg, "ajax": ajax},
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

        html = copy.deepcopy(response.body.decode())
        next_cursor = re.findall(r'm_more_friends.*?href\\\":\\\"\\\\\\(.*?)\"', html)
        if len(next_cursor) !=0 :
            real_cursor = self.base_url + re.sub(r'\\', '', re.sub(r"\\u0025", "%", next_cursor[0], 2))
        # print(next_cursor)
        r_html = re.sub(r'\\','',re.sub(r'\\u003C','<',re.findall(r'\"html\":\"(.*?)\",\"replaceifexists\"', html)[0]))
        # print(r_html)
        real_html =  lxml.etree.HTML(HTMLParser().unescape(r_html)).xpath("//div[@class='_55wo _55x2']//div[@class='_55wp _4g33 _5pxa']")
        for i in real_html:
            person_info = {}
            home_page = i.xpath("./div[@class='_5s61 _2b4m']/a/@href")
            if len(home_page) == 0:
                home_page = ''
            else:
                home_page = home_page[0]
            name = i.xpath("./div[@class='_5s61 _2b4m']/a/i/@aria-label")[0]
            person_info["name"] = name
            person_info["home_page"] = home_page
            yield person_info

        if len(next_cursor) != 0:
            yield FormRequest(
                url=real_cursor,
                formdata=data,
                callback=self.follows_info,
                meta={"fb_dtsg": fb_dtsg, "ajax": ajax},
                headers=self.headers

            )














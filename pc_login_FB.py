import requests
import re
from lxml import etree
from html.parser import HTMLParser
import time


headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "cookie": "datr=K_lPWxKhMWOaYgIpPTFRDrWb; sb=MPlPW4pcqPKXs9vFvX75ZvVx; c_user=100024814180169; pl=n; xs=6%3AB4fSD6f49NtjfA%3A2%3A1531969874%3A13962%3A10366; wd=1920x974; spin=r.4138344_b.trunk_t.1532513968_s.1_v.2_; fr=0hUXnouZ7jgsv7xxU.AWU-TF1JHoUoyRCae4u-hJrthKM.BbT_kr.eo.FtP.0.0.BbWT5j.AWViFHco; presence=EDvF3EtimeF1532577336EuserFA21B24814180169A2EstateFDt3F_5b_5dG532577336093CEchFDp_5f1B24814180169F2CC"
}
url = 'https://www.facebook.com/groups/Scifiandbooklovers/members/'
proxy = {
    "https": "https://127.0.0.1:1080"
}
a = requests.get(url ,headers=headers, proxies=proxy).text
print(a)
members_info = re.findall(r'\"hidden_elem\"\>\<code id="u_0_1.*?"\>\<\!\-\-(.*?)\-\-\>\<\/code\>',a)[0]
print(members_info)
real_members = etree.HTML(members_info).xpath("//div[@id='groupsMemberBrowserContent']/div[2]//ul/div")

# for i in real_members:
#     person_info = {}
#     name = i.xpath("./div/div[2]/div/div[2]/div/a/text()")[0]
#     person_info["name"] = name
#     home_page = i.xpath("./div/div[2]/div/div[2]/div/a/@href")[0]
#     person_info["home_page"] = home_page
#     # print(person_info)
# next_cursor_url = "https://www.facebook.com" + etree.HTML(HTMLParser().unescape(members_info)).xpath("//div[@id='u_0_1a']/div/a/@href")[0]
# print(next_cursor_url)



params = {
# "dpr": "1",
# "__user": "100024814180169",
"__a": "1",
# "__dyn": "",

# "__req": "q",
# "__be": "1",
# "__pc": "PHASED:DEFAULT",
# "__rev": "4133497",
# "__spin_r": "4133497",
# "__spin_b": "trunk",
# "__spin_t": int(time.time())
}
# next_html = requests.get(next_cursor_url,params=params, headers=headers, proxies=proxy).text
# next_member_info = re.findall(r'__html\"\:\"(.*?)\"\}',next_html)[0]
# real_member_info = re.sub(r'\\','',HTMLParser().unescape(re.sub(r'\\u003C','<',next_member_info)))
#
# take_members = etree.HTML(real_member_info).xpath("//ul//div[@class='clearfix _60rh _gse']")
# print(real_member_info)
#
#
# for i in take_members:
#     person_info = {}
#     name = i.xpath("./a[1]/img/@aria-label")[0]
#     person_info["name"] = name
#     home_page = i.xpath("./a[1]/@href")[0]
#     person_info["home_page"] = home_page
#     print(person_info)
#
# next_cursor2 = etree.HTML(real_member_info).xpath("//div[@class='clearfix mam uiMorePager stat_elem morePager _52jv']/div[1]/a[1]/@href")
# print(next_cursor2[0])
#

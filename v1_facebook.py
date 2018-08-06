# from html.parser import HTMLParser
# print(HTMLParser().unescape('&#039;&#xe15;&#xe31;&#xe2a;&#xe44;&#xe07;&#039; &#039;&#xe08;&#xe33;&#xe44;&#xe14;&#xe49;&#xe1b;&#xe48;&#xe32;&#xe27;&#039'))
# 

# a = '\u015f'
# print(a.encode().decode())
# one = a.split(' ')[0].split('u')
# two = a.split(' ')[1].split('u')
#
# real = eval("u\"" + '\\u'.join(one) + "\"") + ' '+ eval("u\"" + '\\u'.join(two) + "\"")
# print(real)
from lxml import etree
import requests
import re
proxy ={
    "https":"https://127.0.0.1:1080"
}
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
"cookie": "datr=K_lPWxKhMWOaYgIpPTFRDrWb; sb=MPlPW4pcqPKXs9vFvX75ZvVx; c_user=100024814180169; pl=n; xs=6%3AB4fSD6f49NtjfA%3A2%3A1531969874%3A13962%3A10366; spin=r.4170030_b.trunk_t.1533258147_s.1_v.2_; fr=0hUXnouZ7jgsv7xxU.AWX3P6R2xADBUzwsYbFT7gTKGnk.BbT_kr.eo.Fte.0.0.BbY6ms.AWVtSG2K; m_pixel_ratio=1; act=1533262616603%2F5; presence=EDvF3EtimeF1533262636EuserFA21B24814180169A2EstateFDt3F_5b_5dG533262636104CEchFDp_5f1B24814180169F2CC; wd=1903x943referer: https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=1301105196572289&av=100024814180169"
}
# data1 = {
#             "m_sess": "",
#             "fb_dtsg": "AQHOqD2lU6vk:AQG2StcWrJqQ",
#             "__dyn": " ",
#             "__req": " ",
#             "__ajax__": "AYmqD_eAwM2rSVC0RnR45BrVjSgHIcUP1475AAsUK82oK-nYRKF-_PO61VzofPvWcN4-y0N5Juo9d6BQM3L97Xwaty9lVP8cJF1ageD250FJjQ"
#         }
a = 'https://m.facebook.com/profile.php?v=friends&lst=100024814180169%3A100006794856940%3A1533264020&id=100006794856940'
url = requests.get( url=a,headers=headers, proxies=proxy).text
# id = re.findall(r'"entity_id":(\d+)', url)[0]
friend_name = etree.HTML(url).xpath("//div[@class='_55wo _55x2']//h3[@class='_52jh _5pxc']")
print(friend_name)







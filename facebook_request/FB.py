import requests
from lxml import etree
import re
from html.parser import HTMLParser
import time
from real_url import change, change_code

proxy = {"http":"http://127.0.0.1:1080",
         "https":"https://127.0.0.1:1080"
         }
cookie = [{'name': 'xs', 'value': '2%3AXCy2pFDEJuVT1g%3A2%3A1531970057%3A13962%3A11803', 'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680849, 'size': 53, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'c_user', 'value': '100024814180169', 'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680825, 'size': 21, 'httpOnly': False, 'secure': True, 'session': False}, {'name': 'datr', 'value': 'BQJQW4kLZcQqdK1n7YrpKRPm', 'domain': '.facebook.com', 'path': '/', 'expires': 1595042054.156114, 'size': 28, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'sb', 'value': 'BQJQW6GMSaxKo2q8WAH06jFC', 'domain': '.facebook.com', 'path': '/', 'expires': 1595042056.680747, 'size': 26, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'm_pixel_ratio', 'value': '1', 'domain': '.facebook.com', 'path': '/', 'expires': -1, 'size': 14, 'httpOnly': False, 'secure': True, 'session': True}, {'name': 'wd', 'value': '800x600', 'domain': '.facebook.com', 'path': '/', 'expires': 1532574859, 'size': 9, 'httpOnly': False, 'secure': True, 'session': False}, {'name': 'pl', 'value': 'n', 'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680871, 'size': 3, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'fr', 'value': '0tsbUP1ljZOqQ6OdP.AWU340UEdrN18v-OqGECvWG7HKU.BbUAIF.yr.AAA.0.0.BbUAII.AWWnE0Cq', 'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680704, 'size': 81, 'httpOnly': True, 'secure': True, 'session': False}]
cookies = ''
for i in cookie:
    cookies += i["name"] + "=" + i["value"] + "; "
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "cookie":cookies
    }


ti = int(time.time())
url = 'https://m.facebook.com/profile.php?v=friends&lst=100024814180169%3A100023605576334%3A{}&id=100023605576334'.format(ti)
html = requests.get(url, headers=headers, proxies=proxy).text
friends_str = etree.HTML(html)
friend_name = friends_str.xpath("//h3[@class='_52jh _5pxc']/a/text()")
friend_home_page = friends_str.xpath("//h3[@class='_52jh _5pxc']/a/@href")
friend = {}
for i in range(len(friend_name)):
    friend[friend_name[i]] = friend_home_page[i].split("&")[0]
# print(friend)
fb_dtsg = friends_str.xpath("//input[@name='fb_dtsg']/@value")[0]
ajax = re.findall('\"encrypted\":\"(.*?)\"', html)[0]
base_url = "https://m.facebook.com/"
more_friends_url = re.findall(r'\"m_more_friends\",\"href\":\"(.*?)\"',html)[0].split("/")[1]
real_friend_url = base_url + re.sub(r"\\u0025", "%",more_friends_url,2)

url2 = real_friend_url
data = {
"m_sess":"",
"fb_dtsg": fb_dtsg,
"__dyn": " ",
"__req": " ",
"__ajax__": ajax,
"__user": "100024814180169"
}
#
more_base_url = "https://m.facebook.com/profile.php?v=friends&unit_cursor={}&lst=100024814180169%3A100023605576334%3A{}&id=100023605576334"
t2 = requests.post(url2, headers=headers, data=data, proxies=proxy).text
ajax2_friends_html = re.findall(r'\"html\":\"(.*?)\",\"replaceifexists\"',t2)[0]
next_cursor = re.findall(r'cursor=(.*?)\&.*\",', t2)[0]
real2 = HTMLParser().unescape(ajax2_friends_html)
h2 =[]
profile = re.findall(r'darkTouch\\\" href\=\\\"\\(.*?=17)', real2)
for m in profile:
    if m not in h2:
        h2.append(m)
friend_name = re.findall(r'profpic\\\" aria-label=\\\"(.*?)\\\"', real2)
d2 = []
for i in friend_name:
    if i not in d2:
        d2.append(i)
next_friend2 = {}
for i in range(len(d2)):
    next_friend2[d2[i]] = h2[i]
print(next_friend2)

three_friend_url = more_base_url.format(next_cursor,ti)
t3 = requests.post(three_friend_url, headers=headers, data=data, proxies=proxy).text
ajax3_friends_html = re.findall(r'\"html\":\"(.*?)\",\"replaceifexists\"',t3)[0]
next_cursor = re.findall(r'cursor=(.*?)\&.*\",', t3)
real3 = HTMLParser().unescape(ajax3_friends_html)
h3 =[]
profile = re.findall(r'darkTouch\\\" href\=\\\"\\(.*?=17)', real3)
for m in profile:
    if m not in h3:
        h3.append(m)
friend_name = re.findall(r'profpic\\\" aria-label=\\\"(.*?)\\\"', real3)
d3 = []
for i in friend_name:
    if i not in d3:
        d3.append(i)
next_friend3 = {}
for i in range(len(d3)):
    next_friend3[d3[i]] = h3[i]

print(next_friend3)

#文章数据
home_page_url = 'https://m.facebook.com/profile.php?id=100023605576334'

html = requests.get(home_page_url, headers=headers, proxies=proxy).text
next_cursor = '%'.join(re.findall(r'cursor=(.*?)\"', html)[0].split('\\u0025'))
# print(next_cursor)
aticle_html = HTMLParser().unescape(re.findall(r'\"normalResources\".*?\"content\".*?\"__html\":\"(.*?)\"\}', html)[-2])
# print(aticle_html)
user_id = re.findall(r'entity_id\"\:(\d+)', html)[0]
# print(aticle_html)
story = re.findall(r'href\=\\\"\\(/story.*?\&id=\d+)\&', aticle_html)
real_story_page = []
for i in story:
    id = i.split("&id=")[1]
    if id == '100023605576334':
        url = 'https://m.facebook.com' + i
        if url not in real_story_page:
            real_story_page.append(url)
# for m in real_story_page:
#     print(m)




base_story_url = 'https://m.facebook.com/profile/timeline/stream/?cursor={}'
next2_url = base_story_url.format(next_cursor)
next2_story = HTMLParser().unescape(requests.post(next2_url, headers=headers, data=data, proxies=proxy).text)
# print(next2_story)
story2 =  re.findall(r'href\=\\\"\\(/story.*?\&id=\d+)\&', next2_story)
real_story_page2 = []
for i in story2:
    id = i.split("&id=")[1]
    if id == '100023605576334':
        url1 = 'https://m.facebook.com'+i
        if url1 not in real_story_page2:
            real_story_page2.append(url1)
for i in real_story_page2:
    print(i)
#5C1194DA,5BE673CD

#文章图片以及说说
real_arictle_text = re.sub(r'\\u003C','<',requests.get(real_story_page2[2], headers=headers, proxies=proxy).text)
text = re.findall('_5rgt _5nk5.*?\<p\>(.*?)\<', real_arictle_text)
print(eval("u\"" + text[0] + "\""))
















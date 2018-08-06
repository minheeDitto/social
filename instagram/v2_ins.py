import requests
import re
import json


class other(Exception):
    def __init__(self, problem):
        problem_data = "There is no data, the reason is {}".format(problem)
        self.problem = problem_data

    def __str__(self):
        return self.problem

proxy = {
    "https": "https://127.0.0.1:19180",
    "http": "http://127.0.0.1:19180",

}


headers = {
"referer":"https://www.instagram.com/accounts/login/",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"x-csrftoken":"0Qo7HqoqGvWFMYCabCqSg45f0WhgBwN8",
"x-instagram-ajax":"db5f166b6f7a",
}
url = 'https://www.instagram.com/accounts/login/ajax/'
data = {
    "username": "460020889@qq.com",
    "password": "siguma777x",
    "queryParams": "{}"
}
html = requests.post(url, headers=headers,data=data, proxies=proxy)
a = html.cookies.get_dict()
cookie = ''
for key, value in a.items():
    cookie += key + '=' + value + '; '
print(cookie)
headers_follow_home = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
'cookie': cookie,
}
follow_page_url = 'https://www.instagram.com/taeyeon_ss/'
follow_home = requests.get(follow_page_url, headers=headers_follow_home, proxies=proxy)
user_id = re.findall('\"owner.*?\:\"(\d+)\"',follow_home.text)[0]

headers1 = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"referer":"https://www.instagram.com/jiang.ly/followers/",
# "x-instagram-gis":"a8a9fe5d0d8363fa421f08e9befb3b0e",
    'cookie': cookie
    }


# 获取粉丝的id及其其他数据
url = 'https://www.instagram.com/graphql/query/?query_hash=149bef52a3b2af88c0fec37913fe1cbc&variables={"id": %d,"first":24}' % int(user_id)
html = requests.get(url, headers=headers1, proxies=proxy)
edg = html.json()["data"]["user"]["edge_followed_by"]["edges"]



#获取个人的推文

# url_for_data = 'https://www.instagram.com/graphql/query/?query_hash=c6809c9c025875ac6f02619eae97a80e&variables={"id":%d,"first":12}' % int(329452045)
# html2 = requests.get(url_for_data,headers=headers1,proxies=proxy)
# # print(html2.json()["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"])
# edg = html2.json()["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
# for i in edg:
#     print(i)

import requests
import re

def get_user_id(name):
    proxy = {
    "https":"https://127.0.0.1:1080"
    }
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
     }
    url = 'https://twitter.com/{}'.format(name)
    a = requests.get(url,headers=headers, proxies=proxy).text
    user_id = re.findall(r'profile_banners\/(\d+)',a)[0]
    return user_id

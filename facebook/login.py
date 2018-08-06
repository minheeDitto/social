import  requests


proxy = {
    "https":"https://127.0.0.1:19180"
}

headers = {
    "cookie": "c_user=100014678298769; xs=40%3AvGIUTM3WVvnaag%3A2%3A1531119200",
    "referer": "https://m.facebook.com/login/save-device/?login_source=login",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

url ='https://m.facebook.com/profile.php?ref=bookmarks'
html = requests.get(url, headers=headers,proxies=proxy).text
print(html)
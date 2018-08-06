import requests

def get_token():
    proxy = {
            "https": "https://127.0.0.1:1080",
            "http": "http://127.0.0.1:1080",

        }


    headers = {
        "referer":"https://www.instagram.com/accounts/login/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        # "x-csrftoken":"gBEMruMkcG2T7KfHzHltDvhcjq9IJl5T",
        # "x-instagram-ajax":"555f906fdf5f",
        }
    url = 'https://www.instagram.com/accounts/login/ajax/'
    data = {
            "username": "460020889@qq.com",
            "password": "zhangzhen2",
            "queryParams": "{}"
        }
    text_str = requests.post(url,headers=headers,data=data,proxies=proxy)
    csrf_token = text_str.cookies.get("csrftoken")
    return csrf_token

if __name__ == '__main__':
    print(get_token())


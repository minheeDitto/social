import requests
from ins.get_ins_csrftoken import get_token

def get_cookies(username, password):
    proxy = {
        "https": "https://127.0.0.1:1080",
        "http": "http://127.0.0.1:1080",

    }


    headers = {
    "referer":"https://www.instagram.com/accounts/login/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "x-csrftoken":get_token(),
    # "x-instagram-ajax":"555f906fdf5f",
    }
    url = 'https://www.instagram.com/accounts/login/ajax/'
    data = {
        "username": username,
        "password": password,
        "queryParams": "{}"
    }
    try:
        html = requests.post(url, headers=headers,data=data, proxies=proxy)

        a = html.cookies.get_dict()
        return a
        # cookie = {}
        # for key in a.items():
        #     # cookie += key + '=' + value + '; '
        #     cookie["key.name"] = key.value

    except Exception as e:
        print("the problem is{}".format(e))




# if __name__ == '__main__':
#     print(get_cookies())
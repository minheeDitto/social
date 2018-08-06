from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
from selenium.webdriver.common.proxy import ProxyType

proxy = {
    "https":"https://127.0.0.1:19180"
}
data = {"username": "zhangzhen87",
        "password": "zhangzhen2517651",
        "queryParms": "{}"}
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
           "x-csrftoken": "mlqsrOldefvNst3qJ0sSWTy3vNVd7OUT",
           "x-instagram-ajax": "555f906fdf5f",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/login/"

}
# he = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
html = requests.post("https://www.instagram.com/accounts/login/ajax/", headers=headers, data=data, proxies=proxy)
# cookies = html.cookies.get_dict()
print(html.headers['set-cookie'])
print(html.cookies.get_dict())
# for cookie1, cookie2 in cookies.items():
#     total_cookie += cookie1 + '=' + cookie2 + '; '

# print(total_cookie)
# print(requests.get("https://www.instagram.com/jiang.ly/",headers=headers,proxies=proxy,cookies={"Cookie": total_cookie}).text)

# proxy = webdriver.Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = '127.0.0.1:19180'
# proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
# desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
# headers = {
    # "cookie": total_cookie,
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "accept-encoding": "gzip, deflate, br"
# }
# for key, value in headers.items():
#     desired_capabilities['phantomjs.page.customHeaders.{}'.format(key)] = value

# driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)
#
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=options)
# # for name,value in cookies.items():
# #     driver.add_cookie({"name": name, "value": value})
# driver.get("https://www.instagram.com/jiang.ly")


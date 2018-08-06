import time

from selenium import webdriver
from retrying import retry
import logging


# logger = logging.getLogger(__name__)
# logging.getLogger('selenium').setLevel(logging.WARNING)


# @retry(stop_max_attempt_number=3)
def get_auth_token():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(15)
    driver.get("https://mobile.twitter.com/login")
    try:
        driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys("zhangzhen871")
        driver.find_element_by_xpath("//input[@name='session[password]']").send_keys("zhangzhen")
        driver.find_element_by_xpath('//*[@id="react-root"]/div[1]/main/div/div/form/div/div[3]/div').click()


        # for i in ad:
        #     c[i["name"]] = i["value"]
        # return c

        auth_cookie = driver.get_cookie("auth_token")["value"]
        ct0 = driver.get_cookie("ct0")["value"]
        twitter_sess = driver.get_cookie("_twitter_sess")["value"]
        cookie = "auth_token=" + auth_cookie + "; " + "ct0=" + ct0 + '; ' + " _twitter_sess=" + twitter_sess
        return cookie,ct0

    except Exception as e:
        print(e)
    driver.close()
    driver.quit()



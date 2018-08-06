from selenium import webdriver
import logging


logger = logging.getLogger(__name__)
logging.getLogger('selenium').setLevel(logging.WARNING)


# @retry(stop_max_attempt_number=3)
def get_auth_token():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    # options.add_argument("user-agent='Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'")
    driver = webdriver.Chrome(chrome_options=options)

    driver.implicitly_wait(10)
    driver.get("https://m.facebook.com/login/?ref=dbl&fl&refid=8")
    driver.find_element_by_xpath("//input[@name='email']").send_keys("yangxustrong@gamil.com")
    driver.find_element_by_xpath("//input[@name='pass']").send_keys("siguma777x")
    driver.find_element_by_id("u_0_5").click()
    driver.get("https://m.facebook.com/home.php")
    return driver.get_cookies()
    # driver.close()
    # driver.quit()


print(get_auth_token())
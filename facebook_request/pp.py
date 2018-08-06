import asyncio
from pyppeteer import launch
import time
from lxml import etree
from cookie import cookies
async def main():
    co = [{'name': 'personalization_id', 'value': '"v1_MvZAh3drPpExES5YTDtqTA=="', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042934.72119, 'size': 47, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'dnt', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.023844, 'size': 4, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'guest_id', 'value': 'v1%3A153197093452247637', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042934.721397, 'size': 31, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_ga', 'value': 'GA1.2.1995012684.1531970938', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042940, 'size': 30, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_gat', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1531970998, 'size': 5, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'twid', 'value': '"u=1014394235133444097"', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024145, 'size': 27, 'httpOnly': False, 'secure': True, 'session': False}, {'name': '_gid', 'value': 'GA1.2.142880073.1531970938', 'domain': '.twitter.com', 'path': '/', 'expires': 1532057340, 'size': 30, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'gt', 'value': '1019786129065893889', 'domain': '.twitter.com', 'path': '/', 'expires': 1531981734.826326, 'size': 21, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'ads_prefs', 'value': '"HBESAAA="', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.023952, 'size': 19, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'kdt', 'value': 'OLu35HEpvEzXMnz5JeTCmgByl2n68HnjHTkPOD4p', 'domain': '.twitter.com', 'path': '/', 'expires': 1579231739.023999, 'size': 43, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'remember_checked_on', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024044, 'size': 20, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_twitter_sess', 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNJmlbBkAToJdXNlcmwr%250ACQFAVa8u2hMOOgxjc3JmX2lkIiU0N2YzODIxOGUyNmIzYzAzNTBiYTUwNWYw%250ANmY3MjRjMToHaWQiJTRmNDA1YjdjMmNkOGM3NWNhN2RjZjBhZjM1NzA5YzQw--c2f1da8994dc1d286ee21881e99a05bc40d91daf', 'domain': '.twitter.com', 'path': '/', 'expires': -1, 'size': 310, 'httpOnly': True, 'secure': True, 'session': True}, {'name': 'u', 'value': '23bdb1e747a09c7270fd494be3ca7ab3', 'domain': '.twitter.com', 'path': '/', 'expires': 1563506939.024191, 'size': 33, 'httpOnly': False, 'secure': True, 'session': False}, {'name': 'auth_token', 'value': '6de037871e547b21b6928888aaac8fba2aecfdad', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024296, 'size': 50, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'ct0', 'value': '169c14574bb402c28ed048be872e1361', 'domain': '.twitter.com', 'path': '/', 'expires': 1531992539.388026, 'size': 35, 'httpOnly': False, 'secure': True, 'session': False}]
    browser = await launch()
    page = await browser.newPage()
    await page.setCookie(*co)
    # await page.goto('https://mobile.twitter.com/login')
    # await page.waitFor('form.rn-13qz1uu')
    # await page.type("input[type=text]",'zhangzhen871')
    # await  page.type("input[type='password']",'zhangzhen')
    # await  page.click("div[role='button']")
    time.sleep(4)
    await page.goto("https://mobile.twitter.com/ThawTha97167658")
    time.sleep(4)
    await page.screenshot({"path": "ex.png"})
    # cookie = await page.cookies()
    text = await page.content()
    print(text)

    # a = await page.content()
    # print(a)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
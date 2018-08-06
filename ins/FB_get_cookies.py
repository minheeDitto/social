import asyncio
from pyppeteer import launch
import time
import requests

def get_cookies():
    async def main():
        browser = await launch()
        page = await browser.newPage()
        # cookie = [{'name': 'personalization_id', 'value': '"v1_MvZAh3drPpExES5YTDtqTA=="', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042934.72119, 'size': 47, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'dnt', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.023844, 'size': 4, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'guest_id', 'value': 'v1%3A153197093452247637', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042934.721397, 'size': 31, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_ga', 'value': 'GA1.2.1995012684.1531970938', 'domain': '.twitter.com', 'path': '/', 'expires': 1595042940, 'size': 30, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_gat', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1531970998, 'size': 5, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'twid', 'value': '"u=1014394235133444097"', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024145, 'size': 27, 'httpOnly': False, 'secure': True, 'session': False}, {'name': '_gid', 'value': 'GA1.2.142880073.1531970938', 'domain': '.twitter.com', 'path': '/', 'expires': 1532057340, 'size': 30, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'gt', 'value': '1019786129065893889', 'domain': '.twitter.com', 'path': '/', 'expires': 1531981734.826326, 'size': 21, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'ads_prefs', 'value': '"HBESAAA="', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.023952, 'size': 19, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'kdt', 'value': 'OLu35HEpvEzXMnz5JeTCmgByl2n68HnjHTkPOD4p', 'domain': '.twitter.com', 'path': '/', 'expires': 1579231739.023999, 'size': 43, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'remember_checked_on', 'value': '1', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024044, 'size': 20, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_twitter_sess', 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNJmlbBkAToJdXNlcmwr%250ACQFAVa8u2hMOOgxjc3JmX2lkIiU0N2YzODIxOGUyNmIzYzAzNTBiYTUwNWYw%250ANmY3MjRjMToHaWQiJTRmNDA1YjdjMmNkOGM3NWNhN2RjZjBhZjM1NzA5YzQw--c2f1da8994dc1d286ee21881e99a05bc40d91daf', 'domain': '.twitter.com', 'path': '/', 'expires': -1, 'size': 310, 'httpOnly': True, 'secure': True, 'session': True}, {'name': 'u', 'value': '23bdb1e747a09c7270fd494be3ca7ab3', 'domain': '.twitter.com', 'path': '/', 'expires': 1563506939.024191, 'size': 33, 'httpOnly': False, 'secure': True, 'session': False}, {'name': 'auth_token', 'value': '6de037871e547b21b6928888aaac8fba2aecfdad', 'domain': '.twitter.com', 'path': '/', 'expires': 1847330939.024296, 'size': 50, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'ct0', 'value': '169c14574bb402c28ed048be872e1361', 'domain': '.twitter.com', 'path': '/', 'expires': 1531992539.388026, 'size': 35, 'httpOnly': False, 'secure': True, 'session': False}]
        # await page.setCookie(*cookie)
        await page.goto('https://m.facebook.com/home.php')
        await page.waitFor('form#login_form')
        await page.type("input#m_login_email",'17512565816')
        await  page.type("input#m_login_password",'lua12378900')
        await  page.click("button[type=button]")
        time.sleep(4)
        cookie = await page.cookies()
        cookies = {}
        for i in cookie:
            cookies[i["name"]] = i["value"]
        return cookies

    return asyncio.get_event_loop().run_until_complete(main())

def get():
    # cookie = [{'name': 'xs', 'value': '2%3AXCy2pFDEJuVT1g%3A2%3A1531970057%3A13962%3A11803', 'domain': '.facebook.com',
    #            'path': '/', 'expires': 1539746056.680849, 'size': 53, 'httpOnly': True, 'secure': True,
    #            'session': False}, {'name': 'c_user', 'value': '100024814180169', 'domain': '.facebook.com', 'path': '/',
    #                                'expires': 1539746056.680825, 'size': 21, 'httpOnly': False, 'secure': True,
    #                                'session': False},
    #           {'name': 'datr', 'value': 'BQJQW4kLZcQqdK1n7YrpKRPm', 'domain': '.facebook.com', 'path': '/',
    #            'expires': 1595042054.156114, 'size': 28, 'httpOnly': True, 'secure': True, 'session': False},
    #           {'name': 'sb', 'value': 'BQJQW6GMSaxKo2q8WAH06jFC', 'domain': '.facebook.com', 'path': '/',
    #            'expires': 1595042056.680747, 'size': 26, 'httpOnly': True, 'secure': True, 'session': False},
    #           {'name': 'm_pixel_ratio', 'value': '1', 'domain': '.facebook.com', 'path': '/', 'expires': -1, 'size': 14,
    #            'httpOnly': False, 'secure': True, 'session': True},
    #           {'name': 'wd', 'value': '800x600', 'domain': '.facebook.com', 'path': '/', 'expires': 1532574859,
    #            'size': 9, 'httpOnly': False, 'secure': True, 'session': False},
    #           {'name': 'pl', 'value': 'n', 'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680871,
    #            'size': 3, 'httpOnly': True, 'secure': True, 'session': False},
    #           {'name': 'fr', 'value': '0tsbUP1ljZOqQ6OdP.AWU340UEdrN18v-OqGECvWG7HKU.BbUAIF.yr.AAA.0.0.BbUAII.AWWnE0Cq',
    #            'domain': '.facebook.com', 'path': '/', 'expires': 1539746056.680704, 'size': 81, 'httpOnly': True,
    #            'secure': True, 'session': False}]
    # cookies = {}
    #
    # for i in cookie:
    #     cookies[i["name"]] = i["value"]
    # return cookies
    cookies = {}
    cookie = 'datr=K_lPWxKhMWOaYgIpPTFRDrWb; sb=MPlPW4pcqPKXs9vFvX75ZvVx; c_user=100024814180169; pl=n; xs=6%3AB4fSD6f49NtjfA%3A2%3A1531969874%3A13962%3A10366; spin=r.4153383_b.trunk_t.1532913139_s.1_v.2_; m_pixel_ratio=1; act=1532928393905%2F147; presence=EDvF3EtimeF1532929286EuserFA21B24814180169A2EstateFDsb2F1532927562420EatF1532929286804Et3F_5b_5dEutc3F1532928394442G532929286809CEchFDp_5f1B24814180169F44CC; fr=0hUXnouZ7jgsv7xxU.AWUkBoclM5xcZaSwuKzhJRb4szw.BbT_kr.eo.Fte.0.0.BbXrsh.AWWMrDFd; x-referer=eyJyIjoiL3N0b3J5LnBocD9zdG9yeV9mYmlkPTE3ODAzNDYyODU1OTk1MjImaWQ9MTc3OTYyOTgzNTY3MTE2NyZhbmNob3JfY29tcG9zZXI9ZmFsc2UmcmVmPXBhZ2VfaW50ZXJuYWwiLCJoIjoiL3N0b3J5LnBocD9zdG9yeV9mYmlkPTE3ODAzNDYyODU1OTk1MjImaWQ9MTc3OTYyOTgzNTY3MTE2NyZhbmNob3JfY29tcG9zZXI9ZmFsc2UmcmVmPXBhZ2VfaW50ZXJuYWwiLCJzIjoibSJ9; wd=1903x943'
    other_cookie = cookie.split('; ')
    for i in other_cookie:
        cookies[i.split("=")[0]] = i.split("=")[1]
    return cookies






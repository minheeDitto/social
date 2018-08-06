import requests


headers = {
"Content-Type": "application/x-www-form-urlencoded",
    "origin": "https://mobile.twitter.com",
    "referer": "https://mobile.twitter.com/login",
"Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
"X-DevTools-Emulate-Network-Conditions-Client-Id": "9539DED70AA4D1197C0B3E1E7937E140"


    }
proxy = {
    "https": "https://127.0.0.1:19180"
}

session = requests.session()
data = {
    "session[username_or_email]": "+8618755591503",
    "session[password]": 'zhangzhen',
    "authenticity_token": "5830aa88336c66d02e610c1af15f4c8f6b032155",
    "ui_metrics": '{"rf":{"f487b3ef9130051180504cba4659da856ae3a8ad6b39210ec2197c44f827a68b":-32,"a1041138ca012a3aba6210f6f1ced2df7a132e3e25110d9e5a672e4179572b98":38,"aed3fb7f8e0f1cb85c202e69e964a0464b87571316690af3e58991f60d59d909":106,"a72beaafc638edb4666a7f9697217533f4590ce6b193353146b0890bf00ee8db":125},"s":"mDMR_wB-j3MGXHltV7IuyIJXiekWBAehRptW3eBAudX7tcYlwHgfXDDr617wWDhIN4iwN8Aj4OX9S9iPQnUHZ5Y0FEZFW8a9UkfnkCs5pMasaG7Rd58l0f7yv0xE5ZXgFQ6HpndpW7JJY-Isu8vla47NfLnutug08RW52Lx0YZ2_FsxZSfnH1kptptsS_5sVggVa4oPKKZNJjXOe3MPOXhFjo_Ue2xkB60MqZSCcJ89Mbz1vqK4IkJYe3Moa6hci1EJo0d2BkmB1cw3OCqyLgrD35CR5mhZBKkB4dpvfsbO2mp8S1AbxBdnTQu7ocP777ml7i9RMTVFiIuCqRS9LegAAAWRkDptA"}',
    "scribe_log":"",
    "redirect_after_login":"",
    "authenticity_token": "5830aa88336c66d02e610c1af15f4c8f6b032155",
    "remember_me": "1"

}
headers2 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "referer": "https://twitter.com/account/access?lang=en",
"upgrade-insecure-requests": "1",

"cookie": '__utmc=43838368; __utmz=43838368.1530685322.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct0=bd67fa5a78bff7a13518533b10c15c8a; _ga=GA1.2.284804244.1530685322; _gid=GA1.2.1685148992.1530685366; kdt=xHdWcr2ZZSv2sVcuytGoXkMNvOZ0LsaVUXEC1M3t; dnt=1; lang=en; csrf_same_site_set=1; csrf_same_site=1; gt=1014402772345618432; remember_checked_on=1; _twitter_sess=BAh7EiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMoW9WNkAToMY3NyZl9p%250AZCIlYjMyNDM5NDBhNGRjYWIzMzBiOGRhMDc2ZWFmNDg5Mzk6B2lkIiU2MDQ0%250AOGI1ZDg5YTg5NzNjMDZkYjUyNTcyMGViZmZhOToSZ2V0X3RpbWVzdGFtcGwr%250ACD449WNkAToQZ3Vlc3RfdG9rZW4iGDEwMTQzOTQwOTEwMTcxNDIyNzI6Gmd1%250AZXN0X3Rva2VuX3RpbWVzdGFtcGwrCEk49WNkASIJcHJycCIAOghwcnNpCToI%250AcHJ1aQTUaf0POghwcmlpBjoIcHJlafo6CXVzZXJsKwkBQFWvLtoTDg%253D%253D--60f5a055a52aa2d2ec46b105bce0edd21d299d76; personalization_id="v1_mqH36X4w+LZDr+w84O1rRA=="; guest_id=v1%3A153068750716996899; ads_prefs="HBESAAA="; twid="u=1014394235133444097"; auth_token=012ef7fc641d7eaa2c5c5d63b5c680069a617268; __utma=43838368.284804244.1530685322.1530685322.1530687832.2; __utmb=43838368.2.9.1530687854681'
}
html = requests.post("https://twitter.com/sessions", headers=headers, data=data, proxies=proxy)
print(html.cookies)

# print(session.get("https://twitter.com/IamJiangLY/followers",headers=headers2,proxies=proxy).text)
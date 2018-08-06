import requests
from requests_oauthlib import OAuth1
import time
from threading import Thread
from retrying import  retry


# @retry(stop_max_attempt_number=3)
def run():
    headers = {
        # "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "zh-CN,zh;q=0.9",
    # "access-control-request-headers": "authorization,x-csrf-token,x-twitter-active-user,x-twitter-auth-type,x-twitter-client-language",
    # "access-control-request-method":"GET",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    # "origin": "https://mobile.twitter.com",
    # "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
               # 'cookie':'personalization_id="v1_ph0qBIyV/PbKjtio3Z9aiw=="; guest_id=v1%3A153075497793296514; gt=1014686037476454400; _gat=1; dnt=1; ads_prefs="HBESAAA="; kdt=Wr6BoFpmNYDzWAx6AHQHMMnUf9ZiftjBmu2P44tN; remember_checked_on=1; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLdoHGhkAToMY3NyZl9p%250AZCIlOGY5OTJiOTcyNzBlNzQwMTc3MzE5ZDU0MTA5NDVhNDU6B2lkIiVmM2Yy%250AM2NlMDc3NDNhMmJmMGQwZWQ5MTY2NmRkYWNjNjoJdXNlcmwrCQFAVa8u2hMO--358b9480ebcd061d258d8bf1a6cc3b96ba2d9f84; twid="u=1014394235133444097"; u=dbd4ebcc87eedd021f06ddf895cbe345; auth_token=1ec6d112d08b38560b3033644da1921b43a59b9e; ct0=aaf87707f9292a4a60e5b251bc4c0afd; lang=en; _ga=GA1.2.1826744597.1530754981; _gid=GA1.2.1751762114.1530754981',
    "x-csrf-token":"37e160866abadb98bfb8a75d026fee20",
    # "Referer":"https://mobile.twitter.com/IamJiangLY",
               # "x-twitter-active-user":'yes',
               # "x-twitter-auth-type":"OAuth2Session",
               # "x-twitter-client-language": "zh",
        # 'cookie': '__utmz=43838368.1530685322.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.284804244.1530685322; kdt=xHdWcr2ZZSv2sVcuytGoXkMNvOZ0LsaVUXEC1M3t; dnt=1; csrf_same_site_set=1; csrf_same_site=1; __utma=43838368.284804244.1530685322.1530685322.1530687832.2; eu_cn=1; tfw_exp=0; __utmz=191792890.1530940262.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); remember_checked_on=1; _gid=GA1.2.418549625.1531366569; personalization_id="v1_2U3WcIgDqfcD603xYl5wtQ=="; guest_id=v1%3A153139111838966063; ads_prefs="HBESAAA="; twid="u=1014394235133444097"; u=6bf02a6be968793d13c03fab8f7caa97; auth_token=3ae9a2eba2cf537f5fa811ab820bfb10a1dd55ad; ct0=37e160866abadb98bfb8a75d026fee20; lang=zh-cn; _gat=1'
}



    proxy = {
        "https": "https://127.0.0.1:1080"
    }
    url ='https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor=1603480169055186454&user_id=2211068115&count=20'
    html = requests.get(url, headers=headers, proxies=proxy)
    return html.text

print(run())

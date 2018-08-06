import requests

from twitter.vir_login import get_auth_token



cookie,ct0 = get_auth_token()
proxy = {
  "https":"https://127.0.0.1:19180"
}

headers = {

    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",

    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
      "x-csrf-token": ct0,
# 'cookie': 'ct0=7c72ad1e16db37b5659b1ca13b558a0b; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJoEqnJkAToMY3NyZl9p%250AZCIlYWMxY2JlMzIyOTQwOWYxZWYyYzE3MDMyNTQ4MjQ2NWI6B2lkIiVmZDkw%250AZjg4MTMzZTQxNjMyMTQ0NDQ4NzExZDI1N2FjMDoJdXNlcmwrCQFAVa8u2hMO--1d42867a192d4a575628a7bf7c56c3cdcf976661; auth_token=14aed77daad438039a9ff3e71a8208438bd95e38'

"cookie": cookie
    }

# url = 'https://api.twitter.com/2/timeline/media/2211068115.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&send_error_codes=true&count=20&ext=mediaStats%2ChighlightedLabel'
url2 = 'https://api.twitter.com/2/timeline/profile/2211068115.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&send_error_codes=true&include_tweet_replies=false&userId=2211068115&count=20&ext=mediaStats%2ChighlightedLabel'
url = ' https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor=-1&user_id=752709590609952768&count=20'
html = requests.get(url, headers=headers, proxies=proxy).json()
# datas = html["globalObjects"]["tweets"]
print(html)
# for data in datas.values():
#     twitter_img = data["entities"].get("media", None)
#     if twitter_img:
#         print(twitter_img)

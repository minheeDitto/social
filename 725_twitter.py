import requests

url = 'https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor=-1&user_id=938326738353844224&count=20'
proxy = {
    "https":"https://127.0.0.1:1080"
}

headers = {
"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    'x-csrf-token': "e4722633d24162d367d95ea6aaf45a6e"


}
url2 = ' https://api.twitter.com/1.1/followers/list.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&skip_status=1&cursor=1599741126944116661&user_id=2211068115&count=20'
a = requests.get(url2, headers=headers,proxies=proxy).text
print(a)
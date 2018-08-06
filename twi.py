import time
import tweepy
from tweepy import OAuthHandler


consumer_key = 'EKMnf1HSdiR8sBCQpkTycQFI7'
consumer_secret = '2MsyqwzG9cEc9g42CiBrEX168TcIAyRmBAQ3vnnpYKJK7aCQa9'
access_token = '1014394235133444097-E5ZGY6noMbVtO8m6QpgkjIJLE1hNpE'
access_secret = '6xagGJ1qKNIrEkQAACMo6pKjVTtInIGuraZRhbbquWqtH'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,proxy='127.0.0.1:19180')


user = tweepy.Cursor(api.followers, screen_name='IamJiangLY').items()

flag = 0

list1 = []
while flag<100:
    try:
        u = next(user)
        list1.append(u)
        print(u)
        flag = flag + 1
    except:
        time.sleep(15*60)



import random
import sys
from time import sleep

from tweepy import API, OAuthHandler

from manverbing import manverbing
from secrets import (
    consumer_key, consumer_secret, access_token, access_token_secret,
)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def post():
    api.update_status(manverbing())


if __name__ == '__main__':
    if '-wait' in sys.argv:
        sleep(60 * 60 * random.random())

    post()

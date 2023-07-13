#!/usr/bin/python3

'''
Queries REDDIT API and returns number of
subscribers for a given subreddit
'''


import json
import requests



def number_of_subscribers(subreddit):
    '''
    returns number of subcribers if subreddit
    is valid
    '''

    subredditURL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    subreddit_info = requests.get(
        subredditURL,
        headers={'user-agent': 'user'},
        allow_redirects=False
    ).json()

    if "data" not in subreddit_info:
        return 0
    subscriber_count = subreddit_info.get('data').get('subscribers')
    return subscriber_count

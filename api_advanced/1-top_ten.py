#!/usr/bin/python3

'''
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
'''


import requests


def top_ten(subreddit):
    '''
    prints first 10 hot posts
    listed for a subreddit
    '''
    subreddit_URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit
    )
    subreddit_info = requests.get(
        subreddit_URL,
        headers={'user-agent': 'user'},
        allow_redirects=False
    ).json()

    if 'data' not in subreddit_info:
        print(None)
        return
    children = subreddit_info.get('data').get('children')
    for child in children:
        print(child.get('data').get('title'))

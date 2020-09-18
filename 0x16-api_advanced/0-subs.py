#!/usr/bin/python3
""" subs """

import requests


def number_of_subscribers(subreddit):
    ''' get subreddit subscriber count '''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    hdrs = {'User-Agent': ''}
    resp = requests.get(url, headers=hdrs, allow_redirects=False).\
        json().get('data')
    if resp:
        return resp.get('subscribers')
    return 0

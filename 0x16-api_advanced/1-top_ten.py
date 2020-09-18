#!/usr/bin/python3
""" task 1 """

import requests


def top_ten(subreddit):
    ''' return top ten of subreddit '''

    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    hdrs = {'User-Agent': ''}

    try:
        resp = requests.get(url, headers=hdrs, allow_redirects=False).\
            json().get('data')
        [print(c['data']['title']) for c in resp.get('children')]
    except:
        print(None)

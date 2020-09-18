#!/usr/bin/python3
""" task 1 """

import requests


def recurse(subreddit, hot_list=[]):
    ''' return top ten of subreddit '''

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after=after'.format(subreddit)
    hdrs = {'User-Agent': ''}

    try:
        response = requests.get(url, headers=hdrs, allow_redirects=False).\
            json().get('data') 
        if response.get('after'):
            hot_list += [resp.get('title') for resp in response.get('children')]
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return (None)

#!/usr/bin/python3
"""recurse to subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the reddit API"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    data = {}
    if after is not None:
        data = {"after": after}
    response = requests.get(url, headers=user_agent, params=data)
    result = response.json()
    after = result['data']["after"]
    try:
        children = result["data"]["children"]
    except:
        print("None")
        return(None)
    for child in children:
        hot_list.append(child["data"]['title'])
    if after is None:
        return(hot_list)
    return(recurse(subreddit, hot_list, after))

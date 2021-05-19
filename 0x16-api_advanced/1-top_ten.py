#!/usr/bin/python3
"""top ten"""
import requests


def top_ten(subreddit):
    """subreddit top ten"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)
    result = response.json()
    try:
        children = result["data"]["children"]
    except:
        print("None")
        return(None)
    count = 0
    for child in children:
        print(child["data"]['title'])
        count += 1
        if count > 9:
            break

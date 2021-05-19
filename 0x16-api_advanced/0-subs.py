#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)
    result = response.json()

    return (result["data"]["subscribers"])
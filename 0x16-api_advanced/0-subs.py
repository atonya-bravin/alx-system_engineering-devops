#!/usr/bin/python3
""" script to display the number of subscriber in subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ return the total number of subscribers in subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'api-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        no_of_subs = data.get("data").get("subscribers")
        return no_of_subs
    else:
        return 0

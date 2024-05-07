#!/usr/bin/python3
""" this areas is for the file description"""
import requests


def number_of_subscribers(subreddit):
    """ this function return the
    numebr of subscribers on Redit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = request.get(url,
                           headers={'User-Agent': 'Mozilla/5.0'},
                           allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

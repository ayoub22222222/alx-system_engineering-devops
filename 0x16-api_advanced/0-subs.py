#!/usr/bin/python3
""" this areas is for the file description"""
import requests
import re

EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[\[({] | [)}\],;:]')


def number_of_subscribers(subreddit):
    """ this function return the
    numebr of subscribers on Redit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    var = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=var, allow_redirects=False)
    if response.status_code == 200:
        df = response.json()
        sub = df['data']['subscribers']
        return sub
    else:
        return 0

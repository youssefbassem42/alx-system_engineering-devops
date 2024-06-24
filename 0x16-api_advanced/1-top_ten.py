#!/usr/bin/python3
""" get latest 10 hot posts"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {"User-Agent": "Custom"}
    params = {"limit" : 10}
    response = requests.get(url, headers= header, params=params)
    if response.status_code == 200:
        for post in response.json().get("data").get('children'):
            data = post.get('data')
            title = data.get('title')
            print(title)
    else:
        print(None) 

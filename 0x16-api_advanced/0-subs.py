#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditClient/1.0)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

# Example usage
subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")

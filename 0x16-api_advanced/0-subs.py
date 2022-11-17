#!/usr/bin/python3
""" returns number of subscribers on an subreddit """
import requests

def number_of_subscribers(subreddit):
    url = ("GET [/r/{}]/about/where".format(subbreddit))
    r = requests.get("GET [/r/subreddit]/about/contributors")

    return(r.json())

#!/usr/bin/python3
""" This scirpt calls a REST API """
import requests
from sys import argv

if __name__ == "__main__":
    theid = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(url)
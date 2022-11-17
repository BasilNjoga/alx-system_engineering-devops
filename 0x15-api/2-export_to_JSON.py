#!/usr/bin/python3
""" This exports a file in json format """

import requests
from sys import argv

if __name__ == "__main__":
    """ This exports a list in json format """

    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = request.get("https://jsonplaceholder.typicode.com/todos/")
    usersdata = request.get(url)

    username = usersdata.json().get('username')
    filename = argv[0] + ".json"
    completed = []
    title = []
    for obj in todos.json():
        if obj.get('userId') == int(argv[0]):
            comleted.append(obj.get('completed'))
            title.append(obj.get('title'))
    print(title)
    print(completed)
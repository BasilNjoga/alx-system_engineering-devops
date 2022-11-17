#!/usr/bin/python3
""" This exports a file in json format """

import requests
from sys import argv

if __name__ == "__main__":
    """ This exports a list in json format """

    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    usersdata = requests.get(url)

    username = usersdata.json().get('username')
    filename = argv[1] + ".json"
    keys = ('task', 'completed', 'username')
    for obj in todos.json():
        if obj.get('userId') == int(argv[1]):
            values = (obj.get('title'), obj.get('completed'), username)
            thisdict = dict.fromkeys(keys, values)

    print(thisdict)

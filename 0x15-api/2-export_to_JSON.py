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
    keys = ['tasks', 'completed', 'username']
    completed = []
    title = []
    taskslist = []
    for obj in todos.json():
        if obj.get('userId') == int(argv[1]):
            completed.append(obj.get('completed'))
            title.append(obj.get('title'))
    print(title)
    print(completed)
    for count in range(len(title)):
        tasklist[count] = dict(zip(keys, title

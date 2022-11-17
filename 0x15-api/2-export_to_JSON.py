#!/usr/bin/python3
""" This exports a file in json format """

import json
import requests
from sys import argv

if __name__ == "__main__":
    """ This exports a list in json format """

    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    usersdata = requests.get(url)

    username = usersdata.json().get('username')
    filename = argv[1] + ".json"
    keys = ['task', 'completed', 'username']
    completed = []
    title = []
    taskslist = []
    for obj in todos.json():
        if obj.get('userId') == int(argv[1]):
            completed.append(obj.get('completed'))
            title.append(obj.get('title'))
    values = []
    for count in range(len(title)):
        for i in range(3):
            values.append(title[count])
            values.append(completed[count])
            values.append(username)
        taskslist.append(dict(zip(keys, values)))
        values.clear()

    out = dict.fromkeys(argv[1], taskslist)
    json_object = json.dumps(out, indent=4)

    with open(filename, "w") as outfile:
        outfile.write(json_object)

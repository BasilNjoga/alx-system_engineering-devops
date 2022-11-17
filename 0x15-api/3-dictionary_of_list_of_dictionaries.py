#!/usr/bin/python3
""" This exports a file in json format """

import json
import requests

if __name__ == "__main__":
    """ This exports a list in json format """

    url = "https://jsonplaceholder.typicode.com/users/"
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    usersdata = requests.get(url)

    filename = "todo_all_employess.json"
    keys = ['task', 'completed', 'username']
    names = []
    completed = []
    title = []
    taskslist = []
    alllist = []

    for full in range(10):
        for obj in todos.json():
            if obj.get('userId') == full:
                completed.append(obj.get('completed'))
                title.append(obj.get('title'))
        for new in usersdata.json():
            if new.get('id') == full:
                names.append(new.get('username'))
        values = []
        for count in range(len(title)):
            for i in range(3):
                values.append(title[count])
                values.append(completed[count])
                values.append(names[count])
            taskslist.append(dict(zip(keys, values)))
            values.clear()
        allist.append(taskslist)
    count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    out = dict(zip(nums, allist))
    json_object = json.dumps()

    with open(filename, "w") as outfile:
        outfile.write(json_object)

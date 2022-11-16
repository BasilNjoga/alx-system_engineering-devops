#!/usr/bin/python3
""" This scirpt calls a REST API """
import requests
from sys import argv

if __name__ == "__main__":
    theid = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(url)
    tasks = 0
    complete = 0
    data = users.json()
    numbers = todos.json()
    for obj in numbers:
        if obj['userId'] == theid:
            tasks = tasks + 1
            if obj['completed'] is True:
                complete = complete + 1
    out = (f"Employee {data['name']} is done with tasks")
    #print(out + "({}/{}):".format(complete, tasks))

#!/usr/bin/python3
""" This is a file on calling data from a rest api """
import requests
from sys import argv

if __name__ == "__main__":
    """This calls from a rest api"""
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
    out = f"Employee {data['name']} is done with tasks "
    print(out + "({}/{}):".format(complete, tasks))
    for obj in numbers:
        if ((obj['userId'] == theid) & (obj['completed'] is True)):
            print("\t {}".format(obj['title']))

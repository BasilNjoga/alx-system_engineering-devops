#!/usr/bin/python3
""" This is a file on calling data from a rest api """
import requests
from sys import argv

theid = argv[1]
url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
users = requests.get(url)
tasks = 0
complete = 0

data = users.json()
numbers = todos.json()
for obj in numbers:
    if obj['userId'] == 1:
        tasks = tasks + 1
        if obj['completed'] == True:
            complete = complete + 1
print(theid)
print("Employee {} is done with tasks ({}/{}):".format(data['name'], complete, tasks))
for obj in numbers:
    if ((obj['userId'] == 1) & (obj['completed'] == True)):
            print("\t {}".format(obj['title']))

#!/usr/bin/python3
""" This is a file on calling data from a rest api """
import requests
from sys import argv

users = "https://jsonplaceholder.typicode.com/users"
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
users = requests.get(f"https://jsonplaceholder.typicode.com/users/1")

data = users.json()
print(data)
print(users)
print(data["name"])
#print("Employee {} is done with".format(data['name']))

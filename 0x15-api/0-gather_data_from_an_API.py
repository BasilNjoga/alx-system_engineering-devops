#!/usr/bin/python3
""" This is a file on calling data from a rest api """
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json)

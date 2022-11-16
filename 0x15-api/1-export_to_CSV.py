#!/usr/bin/python3
""" This scirpt exports data in csv format"""
from flatten_json import flatten
import json, pandas
import requests
from sys import argv

if __name__ == "__main__":
    """ runs only when function is called """
    theid = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(url)
    data = users.json()
    numbers = todos.json()

    fname = argv[1] + ".csv"
    key_list = ['userId', 'completed', 'title']
    numbers = [{k:d[k] for k in key_list} for d in numbers]
    
    # Flatten and convert to a data frame
    json_list_flattened = (flatten(d, '.') for d in json_list)
    df = pandas.DataFrame(json_list_flattened)
    
    # Export to CSV in the same directory with the original file name
    export_csv = df.to_csv (fname, sep=',', encoding='utf-8', index=None, header=True)

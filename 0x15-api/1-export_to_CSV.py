#!/usr/bin/python3
""" This scirpt exports data in csv format"""
import csv
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

    fname = theid + ".csv"
    data_file = open(fname, 'w', newline='')
    csv_writer = csv.writer(data_file)

    for obj in numbers:
        if count == 0:
            header = obj.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close
        

    

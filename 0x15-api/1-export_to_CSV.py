#!/usr/bin/python3
""" module writes response to a CSV file """
import csv
import requests
import sys


if __name__ == "__main__":
    """ This file exports a csv file """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    user_response = requests.get(url)
    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/")

    employee_name = user_response.json().get('username')
    filename = employee_id + '.csv'
    with open(filename, 'a') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos_response.json():
            if task.get('userId') == int(employee_id):
                csv_writer.writerow([
                    employee_id, employee_name, str(task.get('completed')),
                    task.get('title')])

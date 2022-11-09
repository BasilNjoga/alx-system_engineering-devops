#!/usr/bin/python3
""" This script fetches a RESTapi and gets a response """

import requests

fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))

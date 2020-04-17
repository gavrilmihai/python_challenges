'''Day 6 : GET
Write some code to GET content from the following URL: https://jsonplaceholder.typicode.com/posts/1
The above should return a single record. Load the returned record into a dictionary and print to STDOUT in a nicely formatted string.
Extend your code to GET all the records from https://jsonplaceholder.typicode.com/posts , formatting as before and printing to STDOUT.'''
import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url).json()
for entry in response:
    print('Title: {}\n'.format(entry['title']))
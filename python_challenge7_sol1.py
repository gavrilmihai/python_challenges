'''Day 7:
Following on from yesterday's challenge ...
Write a script to POST data to following URL: https://jsonplaceholder.typicode.com/posts
The data will need to be in JSON format with following schema;
{
  "title": "My Fancy Title",
  "body": "This API should echo back my JSON as the response",
  "userId": "9"
}'''
import requests
import json

data_dict = {
  "userId": "1",
  "title": "my fancy title",
  "body": "echo back",

}

data_dict['title'] = input('Whats the title? ')
data_dict['body'] = input('Whats the body? ')
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
json_data = json.dumps(data_dict)

r = requests.post('https://jsonplaceholder.typicode.com/posts/', data=json_data , headers=headers)

print(f'you sent {json_data}')
print(f'we got back {r.text}')
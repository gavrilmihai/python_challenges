import requests
import json

#The below block retrued a dictionary from the url, so can unopack it
url = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
print(f'the url var is a {type(url)} \n')
for key,value in url.items():
    print(f'{key}: {value:} \n')

#The below block retrued a list of dictinaries though from the url 
urls = requests.get('https://jsonplaceholder.typicode.com/posts/').json()
print(f'the urls var is a {type(urls)} \n')
for new_item in urls:
    for keys,values in new_item.items():
        print(f'{keys}: {values:} \n')
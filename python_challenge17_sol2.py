'''
Challenge: read data and list comprehension:
Create a text file with the following string MY_device,IOS-XE,192.66.66.1,cisco,paddlepass
Read this text file into python
Using only one line (list comprehension) put each element of this data into a new list
example [list(range(x,x+10)) for x in [1,11,21] ]  
'''
print([[word for word in str_list.split(',')] for str_list in open('day17.txt')])

'''Day 8 Challenge
Using the csv_for_day8.csv:
Create a dictionary of the data, where column A will be the keys & the remaining columns will be the items.
You may need to look at open('csv_for_day8.csv’) to read the data in the file.
Print out the dictionary
Think about getting data from a file and into python so we can use it.. Can you suggest other ways to lay out the XLS,CSV data that would ease the imports..
What about how to keep the data in python, whats best? lists, lists of dictionaries, strings, other…
This data may be used tomorrow for jinja2 templates…'''
import csv 
mydict={}
with open('csv_for_day8.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    for line in csv_reader:
        key=line[0]
        value=line[1:]
        mydict.update({key:value})
print(mydict)
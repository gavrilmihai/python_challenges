from fbchat import Client
from fbchat.models import *
import openpyxl
import json
wb = openpyxl.Workbook() 
wb.create_sheet('FB-Users')
sheet=wb['FB-Users']
client = Client("gavrilmihai@gmail.com", "^&Tytan76")
print("Own id: {}".format(client.uid))
users = client.fetchAllUsers()
key_columns='A'
sheet[key_columns+str(1)]= "Index"
for i in range(0,len(users)):
    value_columns='A'
    sheet[value_columns+str(i+2)]= i+2
    user=users[i].__dict__
    for k,v in user.items():
        if i==0: #Write columns headers from first entry with dictionary keys then values on next row
            value_columns=chr(ord(value_columns)+1)  #Move Column to right stay in same row 
            sheet[value_columns+str(i+1)]= k
            sheet[value_columns+str(i+2)]= str(v)

        else:
            value_columns=chr(ord(value_columns)+1)  #Move Column to right stay in same row 
            sheet[value_columns+str(i+2)]= str(v)

wb.save('facebook_users.xlsx')
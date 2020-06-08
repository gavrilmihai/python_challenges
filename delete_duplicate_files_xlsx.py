import hashlib 
import os
import openpyxl
import json
import sys
unique = dict()
duplicates =dict()
wb = openpyxl.load_workbook('files_duplicates.xlsx')
sheet=wb.active
key_columns='B'
key_row=2 
while sheet[key_columns+str(key_row)].value != None :
    print(sheet[key_columns+str(key_row)].value)
    os.remove(sheet[key_columns+str(key_row)].value)
    key_row+=1



#!/usr/local/bin/python3                                                                         
# Copyright © 2020 Gavril Mihai Rusu <grusu@cisco.com>                                                                                                      
# Distributed under terms of the Cisco Evaluation Purposes license. 
'''This script check a path and propose for deletion found duplicate files '''
import hashlib, os, openpyxl ,json
unique = dict()
duplicates =dict()
wb = openpyxl.load_workbook('files_duplicates.xlsx')
sheet=wb.active
wb.create_sheet('Duplicates') #create a new Sheet for inserting Dictionary data 
sheet=wb['Duplicates']
key_columns='A'  #Start in Column B row 4
row_index=2
for root, dirs, files in os.walk('/media/pi/TM', topdown=False):
    for file in files:
        filehash = hashlib.md5(open(os.path.join(root,file),'rb').read()).hexdigest()
        if filehash not in unique: 
            unique[filehash] = file
            print( file, 'unique') 
        else:
            print( file , 'is a duplicate')
            duplicates[filehash]= os.path.join(root,file)
for k,v in duplicates.items():
    sheet[key_columns+str(row_index)]= k   #Update Cell Value with Key
    value_columns=chr(ord(key_columns)+1)  #Move Column to right stay in same row 
    sheet[value_columns+str(row_index)]= v #Update Cell Value with FileName
    row_index+=1                          #Move to row bellow
wb.save('files_duplicates.xlsx')

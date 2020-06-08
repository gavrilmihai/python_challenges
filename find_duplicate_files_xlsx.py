import hashlib 
import os
import openpyxl
import json
import sys
unique = dict()
duplicates =dict()
wb = openpyxl.load_workbook('files_duplicates.xlsx')
sheet=wb.active
sheet['A1']= "File Name"
sheet['B1']= "Full File Name "
sheet['C1']= "Duplicate of "
key_columns='A'  #Start in Column A row 2
row_index=2
for root, dirs, files in os.walk( sys.argv[1], topdown=False):
    for file in files:
        filehash = hashlib.md5(open(os.path.join(root,file),'rb').read()).hexdigest()
        if filehash not in unique: 
            unique[filehash] = os.path.join(root,file)
            print( file, 'unique') 
        else:
            print( file , 'is a duplicate of ' , unique[filehash])
            duplicates[file]= [os.path.join(root,file), unique[filehash]]

for k,v in duplicates.items():
    #print(k,v[0],v[1])
    sheet[key_columns+str(row_index)]= k   #Update Cell Value with Key
    value_columns=chr(ord(key_columns)+1)  #Move Column to right stay in same row 
    sheet[value_columns+str(row_index)]= v[0] #Update Cell Value with FileName
    value_columns=chr(ord(key_columns)+2)  #Move Column to right stay in same row 
    sheet[value_columns+str(row_index)]= v[1] #Update Cell Value with FileName
    row_index+=1                          #Move to row bellow
wb.save('files_duplicates.xlsx')

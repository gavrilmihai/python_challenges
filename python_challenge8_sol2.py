#First create an empty dictinary
device_dictinary = {}

#A for loop to look over each line and do something.
for line in open('csv_for_day8.csv'):
    #Create a list of data from each line, strip of the /n and split on , as its CSV
    read_in_line = line.strip().split(',')
    
    #Look at the length of the list, use this value to add the list data to the keys 
    data_lenth = len(read_in_line)
    
    #From list item 0 create the keys, where the remaining items will be the values of this.
    device_dictinary[read_in_line[0]] = read_in_line[1:data_lenth]

#itterate over the data to check its ok.
for item,data in device_dictinary.items():
    print(f'{item}  {data}')
odd_list = []
even_list = []
dictinary_with_lists = {'ODD':[],'EVEN':[]}

for number in range(int(input('What range: '))):
       even_list.append(number) if number%2==0 else odd_list.append(number) 
dictinary_with_lists['ODD'],dictinary_with_lists['EVEN'] = sorted(odd_list),sorted(even_list)



for key, item in dictinary_with_lists.items():
    print(f'{key}: {item} \n')
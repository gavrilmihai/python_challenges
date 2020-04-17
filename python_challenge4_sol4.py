import random
num_list = range(1, random.randint(10,500))

odd, even = [x for x in num_list if x%2], [x for x in num_list if not x%2]

print(f'{odd} \n\n {even}')

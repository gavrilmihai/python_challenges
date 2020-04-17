OddNumbers = []
EvenNumbers = []
n = input("enter Upper limit: ")
for i in range(1, int(n)):
    if (i % 2) == 0:
        EvenNumbers.append(i)
    else:
        OddNumbers.append(i)

print (f'EvenNumbers')
print (EvenNumbers)
print (f'OddNumbers')
print (OddNumbers)
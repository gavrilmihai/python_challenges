import random

odd = []
even = []
for x in range(1, random.randint(10,500)):
    if x % 2:
        even.append(x)
    else:
        odd.append(x)

print(odd)
print(even)
'''
Day 15: fizzbuzz
This is quite a common interview type question, and a bit of fun to start the week.
FizzBuzz Problem Statement
Based on a traditional English children's game
Print the numbers 1..50
For multiples of 3, print "Fizz" instead of the number
For multiples of 5, print "Buzz" instead of the number
For multiples of 3 and 5, print "FizzBuzz" instead of the number
'''

for n in range(1,51):
    if n%15 == 0 :
        print(f'{n} ---> FizzBuzz')
    elif n%3 == 0 :
        print(f'{n} ---> Fizz')
    elif n%5 == 0:
        print(f'{n} ---> Buzz')
    else:
        print(n)

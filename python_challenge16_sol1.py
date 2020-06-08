'''
Day 16: Batman:
Gotham city is being invaded by evil goons, it’s up to you and batman to save the citizens. You need to use your python powers to decide how to save the day.
If there are 4 of less evil goons out there then you can go it alone, you should print out “Hey man, i got this!!!”
If there are 5 to 10 evil goons out there you need to call for help so call out “Help me Batman!!”
But if there are more than 10, you don’t want to risk yourself, just wish batman luck “Good luck out there dark night”
Use the ```goons = random.randint(1,14)`` for the seed data.
'''
import random
def goons(n):
    for i in range(int(n)):
        goons = random.randint(1,14) 
        print(f'This is the checked goons: { goons }')
        if goons <= 4 :
            print('Hey man, i got this!!!')
        elif 5 <= goons <= 10 :
            print('Help me Batman!!')
        else:
            print('Good luck out there dark night')
nr=input('Enter number of goons to check')
goons(nr)

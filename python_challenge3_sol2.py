import statistics
from colorama import Fore
from colorama import Style
items = []
def times():   
    i=0
    while 1:
        i+=1
        item= input('\n\nPlease enter your 10Km time in minutes(Enter "q" to quit): \n\n\n %d: '%i)
        if item == "q":
            break
        if item == "":
            print(f'{Fore.RED}\n\nInvalid format, please enter numbers only !!{Style.RESET_ALL}')
        elif item.isalpha():
            print(f'{Fore.RED}\n\nInvalid format, please enter numbers only !!{Style.RESET_ALL}')
        else:
            items.append(float(item))

if len(items) != 0:
    averagetimes = statistics.mean(items)
    print ("\n\nYour average time was: \n\n")
    print (averagetimes)
times()
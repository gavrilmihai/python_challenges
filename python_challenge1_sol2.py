objects = [12, "python", "6.7", 9.9, 13.0, 'cobra', 3, "pascal", 99.99, "45"]
#
def object_math(list_in):
    total = 0
    for item in list_in:
        if type(item) == int or type(item) == float:
            total += int(item)
            print(f'Adding {int(item)} to the total, new total of {total} \n')
            #
        elif item.isnumeric():
            total += int(item)
            print(f'Adding {int(item)} to the total, new total of {total} \n')
            #
        elif item.split('.')[0].isnumeric():
            total += int(item.split('.')[0])
            print(f'Adding {item.split(".")[0]} to the total, new total of {total} \n')
            #
        else:
            print(f'Discarded string of {item} \n')
            #
    return total
#
print(f'\n Total is {object_math(objects)}')
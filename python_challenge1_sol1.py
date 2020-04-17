'''Day 1:
Write a function that takes a list of objects.
Sum the objects that either are integers or can be turned into integers
Ignore other values in the list'''
objects = [12, "python", "6.7", 9.9, 13.0, 'cobra', 3, "pascal", 99.99, "45"]
objects2 = [] # null list
sum = 0
print(objects)
for object in objects:
    print (type(object))
    if type(object) == int or type(object) == float: #loop through the values in the objects list if an integer or float add to objects2 list
        objects2.append(int(object)) #turn each value in objects2 list into an integer
        print(objects2)
for object2 in objects2:
    sum += object2 #for each value in the objects2 list add to the variable sum
    print (sum)
print("\nthe total sum is: ", sum,)
input("\n\nPress the enter key to exit\n\n")
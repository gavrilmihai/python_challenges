'''DAY 3: Maths & files:
Base
Write a program that asks the user long it took to run 10 km today.
The program continues to ask how long (in minutes) it took for previous runs.
When the user enters q, the program exits after calculating and displaying the average time that the 10 km run took.
Numeric inputs and outputs should all be floating-point values
Level 2
Have the users data saved to a file
Subsequent running of the program should append this saved data
When the user enters q, the program exits after calculating and displaying the average time that the 10 km run took across all data in the file.
Level 3
Store the run data in a list & when saving to the file, save it as JSON format
Run the calculation from the file data, but you should also show how many runs had duplicate times (allow for a variance of 1 minute) '''
def userin():
    runlist = []
    runtime = 'bogus'
    while runtime == input('What was your 10km runtime? '):
        if runtime == 'q':
            break
        elif runtime.isalpha():
            print('Decimal values only!')
        else:
            runlist.append(float(runtime))
            runcalc(runlist)
            
#Function to calulate the average, slopwest and fastest times
def runcalc(rundata):
    total_time = sum(rundata)
    average_time = sum(rundata)/len(rundata)
    slowest_time = sorted(rundata)[-1]
    Fastest_time = sorted(rundata)[0]
    print(f'{total_time} {average_time} {slowest_time} {Fastest_time}')    
userin()

#Day2

# imports
import random

RANDOM_WORDS = ("CISCO", "GARAGE", "SCOTLAND", "MOUSE", "PYTHON", "PLATE", "BRICK", "DOOR", "CHAIR", "PICTURE", "SKY", "ROOF", "GRASS", "FOOTBALL") #set a list of random words

# initialize variables
word = random.choice(RANDOM_WORDS)   # the word to be guessed
used = []   # words already guessed
wrong = 0   # set the number of wrong attempts to zero
count = 5   # set thenumber of guesses count to 5
guess = ""  # set the guess string to null
new_list = []
wordsposition = RANDOM_WORDS.index(word)
print(wordsposition)

print("\n\nWelcome to the word guessing game! You have five guesses to guess what the word is\n")
print("The word is: ", word) # Debug to show what the random word is
print("The words that you can use are: ")
WORDS = sorted(RANDOM_WORDS) #sort the list into alphabetical order
for string in WORDS:
    print(string)
new_list = WORDS #create a new list that can be used for giving the user a list of the words that are available to guess from
while wrong < 5 and guess != word:
    wrong +=1
    if count > 1:
        print("You have ", count, " guesses left\n")
    else:
        print("This is your last guess")
    guess = input("\nPlease input the word that you think it will be: ")
    guess = guess.upper() #change guess input to all upper case
    count -=1
    while guess not in new_list: #add some error checking so that only valid words in the list can be input
        guess = input("Please try again. The word is not in the list! This does not count as a guess\n\nWhat do you think the word will be: ")
        guess = guess.upper() #change guess input to all upper case
    if guess == word:
	    print("\n\nCONGRATULATIONS! You've found the correct word\n\n")
    else:
        print("That's the wrong guess!\n\n")
        used.append(guess)
        print(used, " \n") #print the guesses that have been used - mainly here for debugging
        if guess < word:
            guessposition = new_list.index(guess)
            new_list = new_list[guessposition+1:] #create a new list from the base words/new list that discount words from the guessed word and lower
            print("The word is higher in the dictionary than your guess\n")
            print("The words which are now available to guess are: \n")
            for string in new_list:
                print(string) #print the words that can now be used as guesses
        if guess > word:
            print("The word is lower in the dictionary than your guess\n")
            guessposition = new_list.index(guess)
            new_list = new_list[:guessposition] #create a new list from the base words/new list that discount words from the guessed word and higher 
            print("The words which are now available to guess are: \n")
            for string in new_list:
                print(string) #print the words that can now be used as guesses
input("\n\nPress the enter key to exit\n\n")
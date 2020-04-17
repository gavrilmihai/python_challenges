'''#Day 2:
Have a program choose a random word from the dictionary, and then ask the user to guess the word. (You might want to limit yourself to 5 letter of less words.
If incorrect guess, prompt them to choose an earlier or later word in the dictionary.'''

from PyDictionary import PyDictionary as dictionary
from random_words import RandomWords

# setup the enchant spellchecker with en_US
d = enchant.Dict("en_US")

# Get us a random word
random_word = RandomWords().random_word()

print("Please try and guess the secret word, up to 5 chars")

# You may want to comment this out if you want to play fow-real
print(random_word)

# Start the guessing game
while True:
    # Create a list and add our random word
    comparison_list = [random_word]
    
    # Ask the user for input with prompt 'guess:'
    guess = input('guess: ')
    
    # Use the enchant module to verify this is a word in the en_US dictionary
    # If it is not ...
    if not d.check(guess):
        print("that is not a real word!")
        # Start the while loop again
        continue
        
    # If we got here the spellcheck passed OK, so check if the guess matches the random_word
    if guess == random_word:
       print("Well done!")
       # Do a dictionary lookup on the random_word
       lookup = dictionary.meaning(random_word)
       print (lookup)
       # End the game
       break
    # If the word doesn't match, append it to the list with the random_word and sort them
    else:
        comparison_list.append(guess)
        comparison_list.sort()
        # After sorting, check which word comes first in the list
        if comparison_list.index(guess) > comparison_list.index(random_word):
            print("Not quite.  The secret word comes BEFORE that in the dictionary")
        else:
            print("Not quite.  The secret word comes AFTER that in the dictionary")


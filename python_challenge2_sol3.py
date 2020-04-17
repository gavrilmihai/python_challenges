#Import module to check the work & do a lookup on the meaning(s)
from PyDictionary import PyDictionary
#Import module to generate a random word
from random_word import RandomWords
#Createa and print the random word to the console 
random_word = RandomWords().get_random_word(hasDictionaryDef="true")
print(f'The word we seek if {random_word}')


#A function that check the word, if its a non word it tells you so,
#Else will say higher or lower in the dicatanry 9-0,A-Z,a-z
#If correct it will tell you the verbs and nouns from PyDictionary
def word_guess(userguess_in, random_word_in):
    result = (PyDictionary(userguess_in).meaning(userguess_in))
    if not result:
        print(f'As there is no such word {userguess_in}')
    elif userguess_in > random_word_in:
        print('Lower in the dictinary')
    elif userguess_in < random_word_in:
        print('Higher in the dictinary')
    else:
        print('You guessed it!')
        for key, item in result.items():
            print(f'\n{key}:')
            for entry in item:
                print(f'* {entry}') 
        return exit
                
#While loop using the walrus to keep asking the user for input
#Then passing that with the work to the function.
while userguess := input('What is your word guess? '):
        word_guess(userguess, random_word)
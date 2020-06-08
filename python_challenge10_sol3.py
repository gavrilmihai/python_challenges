from collections import Counter
import re

#Open my file base if needed
#%cd /Users/sabibby/Documents/GitHub/programability/Python_codes/Python Course/regexp-slides/regexp-exercise-files
    
    
def create_word_list(min=24, max=99):
    """This function is to create a word list based on the spefied inout lenht value, so you pass to it
    create_word_list(min,max), where if not passed the min and max will be 22 and 99 respectivly"""
    #Create a empty list
    word_list = []
    
    #Take 22+ letter words out of the local words file, needs doube {{}} bracktes to escpe them in regexp.
    ro = re.compile(rf'\w{{{min},{max}}}')
    for lines in open('words.txt'):
        m = ro.search(lines)
        if m:
            word_list.append(m.group(0))
    return word_list
        


#Find the most common letters in the list:
def what_word_wins(check_list):
    """This function compares a list of data, it looks at each word and finds out which word has
    the most occurances of the same letter"""
    #Counter to check the current words occurances.
    counter_check = 0
    #Placeholder for the current winning word
    winning_word = ''
    #For loop to check all words
    for word in check_list:
        #most_common returns a list of tuples with the most common elements and their counts e.g ['i','6']
        #In our case we take the (1) most common letter and look ath the firs [0] list entry.
        #We take this data and pass it to the varibles called letters and occurance to use for comaprison.
        letters, occurance = Counter(word).most_common(1)[0]
        #Now we check if the current is better than previous, if so we make this the new leader item and set the 
        #word_match to this word (What if a a draw, we will hit only use the first match only.)
        if occurance > counter_check:
            counter_check = occurance
            word_match = word
    return word_match


def what_word_came_second(check_list):
    """This function compares a list of data, it looks at each word and finds out which word has
    the 2nd mose occurances of the same letter, to show how the most_common works
    There are no notes as they are a duplicate of the what_word_wins function"""
    counter_check = 0
    winning_word = ''
    
    for word in check_list:
        #Here we look at the top 2 common letters and pass back the 2nd [1] entry to the occurance variable.
        #Note if there are words of just one letter type this will fail, so i built in a excetipn check for 
        #the IndexError: list index out of range
        try:
            letters, occurance = Counter(word).most_common(2)[1]
            if occurance > counter_check:
                counter_check = occurance
                word_match = word
        except (IndexError):
            continue
    try:
        if word_match:
            return word_match
    except (UnboundLocalError):
        return ('There is no 2nd letter')
    
#Create a list for the words and pass it to the comparison function 
#I could have called the create_word_list function within each othe r fucntion call, 
#But that would need to rin the finction twice and seemed illoical, so its called once first 
#To get the list of words & the re-used.
list_of_words = create_word_list(1,1)
print(f'The most common letters occurance is in {what_word_wins(list_of_words)}')
print()
print(f'The second common letter occurance is in {what_word_came_second(list_of_words)}')
print()
print(f'the list of words was \n\n{list_of_words}')
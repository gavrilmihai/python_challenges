'''Day 10 find data:
Write a function that takes a sequence of strings as input (you can use a pre-canned list, 
or some dictionary lookup for initial testing). The function should return the string that contains 
the greatest number of repeated letters. In other words:
For each word, find the letter that appears the most times
Find the word whose most-repeated letter appears more than any other
E.g, if words = ['this', 'is', 'an', 'elementary', 'test', 'example'] then your function should return elementary.
Functions def name(input_list): and lists list_is_in_square_brackets = ['this', 'is', ‘list’] are used here.
'''
input_list= ['csr1kv1', 'asav','vios','elementary'] 
letter_in_words={}
result=""
def word_char_repetition(list):
    """This function take the list of words,looks at each word and finds out which word has
    the most occurances of the same letter .Returns the word and biggest number of occurences"""
    for word in list :
        letter_repetition=[]
        for s in word:   
           letter_repetition.append(word.count(s))
        letter_in_words.update({word:max(letter_repetition)})
    return max(letter_in_words,key=letter_in_words.get)
def word_max_count(word,nr):
    """This function take the word and number of letter occurence and return the letter that match the number of occurences  """
    for c in word:
        if word.count(c)== nr :
            letter=c
            break
        else:
            continue
    return letter
result=word_char_repetition(input_list)
m=letter_in_words[result]
print(letter_in_words)
letter=word_max_count(result,m)
print(f'The word "{ result }" is having most letter repetitions { m } for "{ letter }" ')

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
    for word in list :
        letter_count=[]
        letter_repetition={}
        for s in word:   
           letter_repetition.update({s:word.count(s)})
        letter=max(letter_repetition,key=letter_repetition.get)
        letter_count.append(letter)
        letter_count.append(letter_repetition[letter])
        letter_in_words.update({word:letter_count})
    
    return max(letter_in_words,key=letter_in_words.get)
result=word_char_repetition(input_list)
print(letter_in_words)
print(f'The word "{ result }" is having the most letters repetitions ')
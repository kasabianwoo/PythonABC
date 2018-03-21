# -*- coding:utf-8 -*-




'''

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );
print str.split('\n', 2 );

'''

'''
a = [5,7,6,3,4,1,2]
print sorted(a)
print sorted(a,reverse=True)
'''

'''

L=[('b',2),('a',1),('c',3),('d',4)]
M=[('b',2),('f',1),('c',3),('d',4)]
print sorted(L)   
print sorted(M)   
print sorted(M,key=lambda x:x[0])   
print sorted(M,key=lambda x:x[1])   
print sorted(M,cmp=lambda x,y:cmp(x[1],y[0]))  
''' 



'''

alist = ['a','b','c','d']
pop_list = alist.pop(-1)
print pop_list
print alist

'''



def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


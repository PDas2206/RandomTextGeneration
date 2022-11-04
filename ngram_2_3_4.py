# -*- coding: utf-8 -*-
"""
RANDOM TEXT GENERATION

This program creates 2/3/4-gram models of text2 from nltk.book 
(Sense and Sensibility, by Jane Asuten). Random texts of 100 words 
are then generated based on these n-gram models.
"""
import nltk
import random
from nltk.book import *
from nltk.tokenize import word_tokenize
from ngram import BasicNgram


token_list=[]
for line in text2:
    tokens = nltk.word_tokenize(line)
    token_list.extend(tokens)

n=input("What n-gram do you want to generate between 2 and 4 (default is 4)?") 
int_n=int(n)   
ngram=BasicNgram(int_n,token_list)


"""
 This section checks the user input and accordingly creates the n-gram model.
 It then generates random texts of 100 words according to this n-gram model.
 
"""
if int_n==2:
    start_context=random.choice(ngram.contexts())
    print(start_context)
    #creating context for next word
    a=start_context[0]
    word=""
    random_text=[]
    
    for i in range(1,101):
        p_b=ngram[(a,)]
        word=p_b.generate()
        a=word
        random_text.append(word)
    print(" ".join(random_text))
    
elif int_n==3:
    start_context=random.choice(ngram.contexts())
    print(start_context)
    #creating context for next word
    a=start_context[0]
    b=start_context[1]
    word=""
    random_text=[]

    for i in range(1,101):
        p_b=ngram[(a,b)]
        word=p_b.generate()
        a=b
        b=word
        random_text.append(word)
    print(" ".join(random_text))
    
        
else:
    start_context=random.choice(ngram.contexts())
    print(start_context)
    #creating context for next word
    a=start_context[0]
    b=start_context[1]
    c=start_context[2]
    word=""
    random_text=[]
    for i in range(1,101):
        p_b=ngram[(a,b,c)]
        word=p_b.generate()
        a=b
        b=c
        c=word
        random_text.append(word)
    print(" ".join(random_text))
    
   


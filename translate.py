from itertools import permutations
from random import randint
from math import factorial

words=open("text.txt").read()
alien_words = ""

for word in words.split(' '):
    if len(word) > 3:
       pickone = randint(1,factorial(len(word)-4))
       middle = list(permutations(word[1:-1]))[pickone]
       middle = "{}{}{}".format(word[0],''.join(middle),word[-1])
    else:
       middle=word[::-1]

    alien_words += middle + " "

print(alien_words)

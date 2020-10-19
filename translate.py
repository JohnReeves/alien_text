from itertools import permutations
from random import randint
from math import factorial

words = ""
alien_words = ""

with open('text.txt', 'r') as f:
   words = f.read()

for word in words.split(' '):
    middle=""
    # 13! is about 6 billion and breaks the vm
    if len(word) > 3 and len(word) < 10:
       pickone = randint(1,factorial(len(word)-4))
       middle = list(permutations(word[1:-1]))[pickone]
       middle = "{}{}{}".format(word[0],''.join(middle),word[-1])
    else:
       middle = word

    alien_words += middle + " "

print(alien_words)

with open('alien_output.txt','w') as f:
  f.write(alien_words)

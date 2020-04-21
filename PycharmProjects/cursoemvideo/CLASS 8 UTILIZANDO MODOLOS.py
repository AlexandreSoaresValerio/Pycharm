# import math
from math import sqrt, floor
num = int(input('digite um numero?'))
raiz = sqrt(num)
print(' A raiz de {} e igual a {}'.format(num, floor(raiz)))
#raiz = math.sqrt(num)
#print('A raiz de {} e igual a {} '.format(num,math.floor(raiz)))

import random
num= random.randint(1,100)
print(num)

import emoji
print(emoji.emojize('hello love :heart:',use_aliases = True))

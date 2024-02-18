from random import *
import json

lst = ['py', 'js', 'cs']

dct = { }

for _ in range(6):
    x = choice(lst)

    if dct.get(x) == None:
        dct[x] = 1
    else:
        dct[x] += 1

    print(dct)

print(json.dumps(dct, indent=4))

from random import random as rnd


with open('./data/nums.csv', 'w') as f:
    count = 10
    for i in range(1, count+1):
        x = 100 + 900*rnd()
        f.write(f"{i} {x}\n")
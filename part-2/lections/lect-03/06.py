from random import random as rnd


with open('./data/nums.csv', 'w') as f:
    count = 10
    for i in range(count):
        f.write(f"{100 + 900*rnd()}\n")
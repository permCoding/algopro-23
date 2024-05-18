from random import randint
from timeit import timeit

cols, rows = 100, 2
tab = [ [randint(100, 999) for col in range(cols)] for row in range(rows)]
# print(tab)

def f1():
    sm = 0
    for cl in range(cols):
        for rw in range(rows):
            sm += tab[rw][cl]

def f2():
    sm = 0
    for rw in range(rows):
        for cl in range(cols):
            sm += tab[rw][cl]

r1 = round(timeit(f1, number=10_000), 3)
r2 = round(timeit(f2, number=10_000), 3)

print(r1, r2)

from random import randint
from timeit import timeit

cols, rows = 100, 2
tab = [ [randint(100, 999) for col in range(cols)] for row in range(rows)]
# print(tab)

def f1():
    cnt = 0
    sm = 0
    for cl in range(cols):
        cnt += 1
        for rw in range(rows):
            cnt += 1
            sm += tab[rw][cl]
    print(f'f1 => {cnt}')

def f2():
    cnt = 0
    sm = 0
    for rw in range(rows):
        cnt += 1
        for cl in range(cols):
            cnt += 1
            sm += tab[rw][cl]
    print(f'f2 => {cnt}')

f1()
f2()
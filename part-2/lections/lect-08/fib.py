# break point
# step recurse 
from functools import lru_cache


def fib(n):
    if n < 3: return 1
    return fib(n-2) + fib(n-1)


@lru_cache()
def fib_lru(n):
    if n < 3: return 1
    return fib_lru(n-2) + fib_lru(n-1)


def fib_cache(n):  # вручную
    if n < 3: return 1
    if cache[n-2] == 0: cache[n-2] = fib_cache(n-2)
    if cache[n-1] == 0: cache[n-1] = fib_cache(n-1)
    return cache[n-2] + cache[n-1]


def fib_for():  # решить кролика
    pass

n = 138
cache = [0,1,1] + [0] * n
print(fib_cache(n))
print(cache)
"""
0 1 2 3 4 5 6 7  8  9  10 
0 1 1 2 3 5 8 13 21 34 55
0 1 1 0 0 5 0 0  0  0  0  <== cache
"""
from timeit import default_timer as dt
from random import randint as rnd

def get_merge(lst_a, lst_b):
    lst_ab, a, b = [], 0, 0
    while a < len(lst_a) and b < len(lst_b):
        if lst_a[a] < lst_b[b]:
            lst_ab.append( lst_a[a] )
            a += 1
        else:
            lst_ab.append( lst_b[b] )
            b += 1
    return lst_ab + lst_a[a:] + lst_b[b:]

def sort_merge(lst):    
    if len(lst) < 2: return lst
    mid = len(lst) // 2
    lt, rt = sort_merge(lst[:mid]), sort_merge(lst[mid:])
    return get_merge(lt, rt)

nums = [rnd(1, 10_000) for _ in range(20_000)]  # asc 20_000 -> .1 sec

start = dt()
srtd = sort_merge(nums)
finish = dt()
print(round(finish-start, 2))
# print(srtd)
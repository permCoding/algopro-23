from random import randint as rnd
from timeit import default_timer as dt


def merge(lt, rt):
    a, b, lst = 0, 0, []
    while a < len(lt) and b < len(rt):
        if lt[a] < rt[b]:
            lst.append(lt[a])
            a += 1
        else:
            lst.append(rt[b])
            b += 1
    return lst + lt[a:] + rt[b:]


def sort_merge(lst):  # log(n)
    n = len(lst)
    if n < 2: return lst
    lt, rt = lst[:n//2], lst[n//2:]
    return merge( sort_merge(lt), sort_merge(rt) )  # n


nums = [rnd(1, 10_000) for _ in range(10_000)]
start = dt()
sort_merge(nums)
finish = dt()
print(round(finish-start, 3))

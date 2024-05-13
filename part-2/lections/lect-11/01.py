from random import randint as rnd


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


nums = [rnd(1, 10_000) for _ in range(100)]
# nums = [6, 1, 2, 5, 4, 2, 6]
print(sort_merge(nums))

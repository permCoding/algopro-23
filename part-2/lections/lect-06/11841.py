def get(n, end):
    if n < end or n == 20: return 0
    if n == end: return 1
    return get(n-2, end) + get(n-3, end) + get(n//5, end)


print(get(41, 10) * get(10, 5))
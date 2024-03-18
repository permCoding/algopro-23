def get(n, end):
    if n > end or n == 11: return 0
    if n == end: return 1
    return get(n+1, end) + get(n*2, end) + get(n**2, end)


print(get(2, 10) * get(10, 40))

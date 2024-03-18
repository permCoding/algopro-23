def get(n, end, step=''):
    if n > end+1: return 0
    if n == end: return 1
    d1 = 0 if step == 'a' else get(n-1, end, 'a')
    # d1 = 0
    # if step != 'a':
    #     d1 = get(n-1, end, 'a')
    d2 = get(n*2, end, 'b')
    d3 = get(n*3, end, 'c')
    return d1 + d2 + d3


print(get(3, 15))
# при этом не содержат двух команд A подряд

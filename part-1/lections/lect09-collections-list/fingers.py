def get1(n):
    n %= 8  # 0 1 2 3 4 5 6 7
    if n == 0: return 2
    if n < 6: return n
    if n == 6: return 4
    return 3

def get2(n):
    n %= 8  # 0 1 2 3 4 5 6 7
    if n == 0: return 2
    if n < 6: return n
    return 10 - n

def get3(n):
    t = (2,1,2,3,4,5,4,3)
    n %= 8
    return t[n]

def get4(n):
    return (2,1,2,3,4,5,4,3)[n%8]

def get5(n):
    p, d = 0, +1
    for _ in range(n):
        if p == 5: d = -1
        if p == 1: d = +1
        p += d
    return p

for n in 1,2,6,7,8,80,81,86,1000:
    print(get1(n), get2(n), get3(n), get4(n), get5(n))


# r = list(range(5))
# print(r)

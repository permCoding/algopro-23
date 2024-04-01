def fib_for(n):  # решить кролика
    cache = [0, 1, 1]
    for n in range(3, n+1):
        cache.append(cache[n-2] + cache[n-1])
    return cache


n = 10
result = fib_for(n)
print(result)
print(f"fib({n}) = {result[-1]}")

'''
0 1 2 3 4 5 6 7  8  9  10 
0 1 1 2 3 5 8 13 21 34 55
0 1 1 0 0 5 0 0  0  0  0  <== cache
'''
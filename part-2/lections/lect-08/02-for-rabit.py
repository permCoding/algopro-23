def getRouter12(n):  # решить кролика
    cache = [1] + [0] * (n + 1 + 2)
    for i in range(n+1):
        cache[i+1] += cache[i]
        cache[i+2] += cache[i]
    return cache


def getRouter(k, n):  # решить кролика
    cache = [1] + [0] * (n + 1 + k)
    for i in range(n+1):
        for j in range(1, k+1):
            cache[i+j] += cache[i]
    return cache


k, n = 2, 7
result = getRouter(k, n)
print(result[0:n+1])
print(result[n])

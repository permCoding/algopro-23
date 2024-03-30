k, n = map(int, input().split())
t = [1] + [0] * (k+n)
for i in range(n):
    for j in range(i+1, i+k+1):
        t[j] += t[i]
print(t[n])

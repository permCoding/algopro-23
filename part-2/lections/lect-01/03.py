import random as rnd


t = (23, 34, 33, 12, 55)
r = [0] * len(t)
# r = [0 for _ in range(len(t))]

for _ in range(10_000):  # 100 -> 20%  1000 -> 6%  10000 -> 2%
    st = rnd.choice(t)
    pos = t.index(st)
    r[pos] += 1

print(r)

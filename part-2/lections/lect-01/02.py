import random as rnd


t = (23, 34, 33, 45, 12, 55)  # tuple

for _ in range(10):
    st = rnd.choice(t)
    print(st)

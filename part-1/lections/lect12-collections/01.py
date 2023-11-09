from random import shuffle

t = list(range(10))
shuffle(t)
print(t)

t.sort()
print(t)

new_t = sorted(t, reverse=True)
print(new_t)

from random import randint

s = ''
for _ in range(10):
    n = randint(100, 999)
    s += str(n) + ' '

f = open('./gen.txt', 'w')
f.write(s)
f.close()

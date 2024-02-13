from random import randint as rnd

filename = 'gen.txt'
cnt = 10
with open(filename, 'w') as f:
    f.write(' '.join(str(rnd(100,999)) for _ in range(cnt)))

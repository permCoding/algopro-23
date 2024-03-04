from random import shuffle

s = '1 2 3 4 5 6'

m = map(int, s.split(' '))

# tpl = tuple(m)
# tpl = (int(elm)*.1 for elm in m)
# print(tpl)

# lst = list(m)

def get_str(lst, sep=' '):
    shuffle(lst)
    return sep.join(map(str, lst))
    

lst = [int(elm)**2 for elm in m]
# s = get_str(lst, ';')
s = get_str(lst)
print(s)


# t = map(lambda elm: int(elm), s.split(' '))
# for elm in t: print(elm)


# print(t)
# print(sum(t))


from random import randint as r


# lst = [i**2 for i in range(11, 16)]
# print(lst)

s = ' '.join(str(r(10,99)) for _ in range(5))
print(s)

# msg['text'] = s




# print(lst)
# print(*lst)

# s = ''
# for elm in lst:
#     s += str(elm) + ' '
# print(s)



# s = ''
# for _ in range(5):
#     s += str(randint(10, 99)) + ' '
# print(s)

# s = ''
# i = 0
# while i < 5:
#     s += str(randint(10, 99)) + ' '
#     i += 1
# print(s)

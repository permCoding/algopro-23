# бинарный поиск
# найти позицию элемента 

t = [elm*3 for elm in range(10)]
print(t)
n = 12

pos, lt, rt = -1, 0, len(t)-1
while rt >= lt:
    md = (rt + lt) // 2
    if n == t[md]:
        pos = md
        break
    if n > t[md]:
        lt = md + 1
    if n < t[md]:
        rt = md - 1

print(pos)  # для числа 15 ответ 5

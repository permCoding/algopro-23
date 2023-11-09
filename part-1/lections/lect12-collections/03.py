s = "12345266783002"
t = list(s)

print(s)
print(t)

print(type(s), type(t))

print(len(s), len(t))

print(s.index('2'))
print(t.index('2'))

print(s.index('2', 2))
print(t.index('2', 2))

x,y = 12,0
try:  # обработка исключений
    print(x/y)
except:
    print("не удалось")
finally:
    print("==> the end <==")

try:
    print(s.index('2', 6, 12))
    print(t.index('2', 6, 12))
except:
    print("не найден")

print(s.find("A"))
print(s.find("2"))

print("A" in s)
print("2" in s)

t = list(range(10))

print(t)
print(*t)
print(";".join(["1","3","8"]))
# print(";".join(t))  # так не работает

print(";".join(map(str, t)))
print(";".join([str(elm) for elm in t]))

for i, elm in enumerate(t[::-1]):
    print(i, elm)
    
for i in range(len(t)):
    print(i, list(reversed(t))[i])

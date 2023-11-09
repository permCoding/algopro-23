t = [1,2,3]

t.append(4)
t.append(5)

t += [6]
t += [7]

print(t)

q = [99,88,77]
# for elm in q: t.append(elm)
# print(t)

t.extend(q)
print(t)
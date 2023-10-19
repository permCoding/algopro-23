line = open("./data/01.txt").readline()

lst = line.split(" ")

nums = list(map(int, lst))

filtered = list(filter(lambda elm: elm%2 != 0, nums))

print(filtered)
print(sum(filtered))

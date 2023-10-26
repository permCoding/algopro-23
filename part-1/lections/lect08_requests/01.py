filename = "./txt/01.txt"

f = open(filename, "r", encoding="utf8")
line = f.readline()
f.close()

lst = line.split(" ")

nums = []
for elm in lst: nums.append(int(elm))
print(nums)

nums = [int(elm) for elm in lst]
print(nums)

nums = list(map(int, lst))
print(nums)

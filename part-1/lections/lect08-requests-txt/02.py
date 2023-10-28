filename = "./txt/01.txt"

f = open(filename, "r", encoding="utf8")
line = f.readline()
f.close()

lst = line.split(" ")

nums = [int(elm) for elm in lst if int(elm)%2 != 0]
print(nums)


line = open("./data/01.txt").readline()
lst = line.split(" ")

nums = [int(item) for item in lst]
print(nums)

nums = list(map(int, lst))
print(nums)

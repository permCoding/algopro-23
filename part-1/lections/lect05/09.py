s = "12 34 56 99"
obj = map(int, s.split())
print(obj)

nums = list(obj)
print(nums)  # v1

obj = map(int, s.split())
nums = []
for elm in obj:  # забираем из итератора
    nums.append(elm)  # размещаем в список
print(nums)  # 2
from os import system


s = "13 34 45 78 99 1 12345"  # input()

system("cls")  # clear

lst = s.split(' ')
nums = []
for elm in lst:
    nums.append(int(elm))

print(nums)

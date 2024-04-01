nums = [8,1,2,5,4,6,0,0,0,99]
n = len(nums)

for i in range(n):
    pos_min = i
    for j in range(i, n):
        pass
    nums[pos_min], nums[i] = nums[i], nums[pos_min]
    
print(nums)

nums = [3,2,1,5,4,6,0,7,0,99]  # asc
print(nums)

# всплытие один раз
n = len(nums)
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)

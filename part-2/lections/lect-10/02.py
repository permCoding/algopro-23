def sort_bubble(nums):
    for j in range(0, len(nums)-1):
        for i in range(0, len(nums)-1 -j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


nums = [3,2,1,5,4,6,0,7,0,99,-3]  # asc
print(sort_bubble(nums))

nums = [8,2,1,5,4,6,0,0,0,99]  # asc
print(nums)





for left in range(0, len(nums)-1):

    pos_min = left
    for pos_cur in range(left, len(nums)):
        if nums[pos_cur] < nums[pos_min]:
            pos_min = pos_cur
    
    nums[pos_min], nums[left] = nums[left], nums[pos_min]  # swap
    
    print(nums)

def get_sorted_list(nums):
    """  
    вернуть отсортированный список (методом выбора)   
    сложность n**2 
    """
    for left in range(0, len(nums)-1):
        pos_min = left
        for pos_cur in range(left, len(nums)):
            if nums[pos_cur] < nums[pos_min]:
                pos_min = pos_cur
        
        nums[pos_min], nums[left] = nums[left], nums[pos_min]
        
    return nums


def get_sorted_list_opt(nums):
    """
    вернуть отсортированный список (методом выбора)  
    с оптимизацией - если не было ни однойзамены  
    то дальше прекратить сортировку  
    """
    for left in range(0, len(nums)-1):
        # b = True
        pos_min = left
        for pos_cur in range(left, len(nums)):
            # if nums[pos_cur] < nums[pos_cur-1]: b = False
            if nums[pos_cur] < nums[pos_min]:
                pos_min = pos_cur
        
        nums[pos_min], nums[left] = nums[left], nums[pos_min]
        # if b == True: return nums
        print(nums)

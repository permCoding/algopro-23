from functools import reduce

def get_data(filename):
    data = []
    for line in open(filename, 'r'):
        try:
            data.append(float(line.replace(',', '.')))
        except:
            pass
    return data


nums = get_data('./data/nums.csv')

# sm = sum(nums)  # 1
# sm, i = 0, 0
# while i < len(nums):  # 2
#     sm += nums[i]
#     i += 1
# 3 - reduce (map, filter)

lst = [1,2,3,4,5]
acc = reduce(lambda acc, cur: acc+cur, lst, 0)
print(acc)

# arg = sm / len(nums)
# print(f'{arg:.4f}')

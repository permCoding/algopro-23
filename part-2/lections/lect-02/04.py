def get_numbers(lines):
    numbers = []
    i = 0
    while i < len(lines):
        x = lines[i]
        try:
            num = int(x)
            numbers.append(num)
        except:
            pass
        i += 1
    return numbers

lines = open('./data/data.txt').readlines()
numbers = get_numbers(lines)

print(sum(num for num in numbers if num%2))

def odd(num):
    return num%2 != 0

# print(sum(filter(odd, numbers)))
print(sum(filter(lambda num: num%2!=0, numbers)))
print(sum(filter(lambda num: num%2, numbers)))

# map filter
# [ for ]
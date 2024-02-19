lines = open('./data/data.txt').readlines()

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

print(numbers)
sm = 0
for num in numbers:
    if num % 2 != 0:
        sm += num
    
print(numbers)
print(sm)

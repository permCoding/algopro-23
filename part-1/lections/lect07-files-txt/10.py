lines = open("./data/02.txt").readlines()

lst = [sum(map(float, line.split(';'))) for line in lines]

print(lst)

index = 2
print(lines[index])

"""
вывести на экран одну строку из файла
такую которая содержит максимальную сумму

"""

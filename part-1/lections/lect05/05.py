from os import system


s = "13 34 45 78"  # input()

system("cls")  # clear

lst = s.split(' ')
print(int(lst[0]) + int(lst[1]))

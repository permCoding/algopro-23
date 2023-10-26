from os import system
import utils


system("clear")
b = input("Введите двоичное число - ")
print(utils.to_int(b))
print(utils.to_int_(b))
print(utils.to_int__(b))

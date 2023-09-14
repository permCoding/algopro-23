"""
деление программы на 
- бизнес-логику
- интерфейс пользователя
"""


class Track():
    pass


def get_double(num):
    """ увеличить в два раза """
    return num + num 


def get_pow(num, p):  # comment
    pass
    x = 0
    return num**p


num = int(input("Введите число - "))
print(f'"num" = {get_double(num)}')


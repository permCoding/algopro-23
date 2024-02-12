from random import randint


wins = [0, 0]
while wins[0] < 3 and wins[1] < 3:
    cm = randint(0, 2)
    
    print('0 - камень\n1 - ножницы\n2 - бумага')
    while True:
        hm = input("Сделайте свой ход - ")
        if True: break


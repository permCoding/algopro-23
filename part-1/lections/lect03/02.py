import os

os.system('clear')

def ex01(binary):
    pos = 0
    while pos < len(binary):
        print(binary[pos])
        pos += 1


def ex02(binary):
    pos = 0
    while True:
        print(binary[pos])
        pos += 1
        if pos == len(binary):
            break


def ex03(binary):
    for i in range(len(binary)):
        print(binary[i])


def ex04(binary):
    for i in range(len(binary)-1, -1, -1):
        print(binary[i])


def ex05(line):
    # for smb in line:
    #     print(smb)
    for smb in line[::-1]:
        print(smb)


def ex06(line):
    if line == "":
        return None
    print(line[0])
    ex06(line[1:])  # шаг рекурсии

# ex01("11001")
# ex02("100")
# ex03("1011")
# ex04("0123456789")
# ex05("0123456789")
ex06("01234")

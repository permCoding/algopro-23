filename = "./docs/Блок.txt"

fr = open(filename, "r", encoding="utf8")
lines = fr.readlines()

for i in range(len(lines)):
    print(lines[i], end='')

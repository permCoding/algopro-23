filename = "./docs/Блок.txt"

fr = open(filename, "r", encoding="utf8")
lines = fr.readlines()
# print(lines)

fw = open("./copy.txt", "w", encoding="utf8")
fw.writelines(lines[0:4])

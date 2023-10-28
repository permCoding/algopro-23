filename = "./txt/01.txt"

f = open(filename, "r", encoding="utf8")
line = f.readline()
f.close()

print(line)

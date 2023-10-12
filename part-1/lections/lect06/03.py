filename = "./docs/Блок.txt"

fr = open(filename, "r", encoding="utf8")
txt = fr.read()

fw = open("./copy.txt", "w", encoding="utf8")
fw.write(txt)

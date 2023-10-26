#print(ord('\t'))
#print("*" + chr(9) + "*")

lst = []
for line in open('./data/06.txt'):
    lst.append(line.strip())

langs = []
for line in lst[3:]:
    #langs.append(line.split('\t')[0])
    langs.append(line.split(chr(9))[0])
print(langs)

# https://pcoding.ru/csv/06.txt
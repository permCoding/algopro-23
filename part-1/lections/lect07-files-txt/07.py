line = open("./data/01.txt").readline()
lst = line.split(" ")

def check(elm): return elm%2 != 0

filtered = list(filter(check, map(int, lst)))

print(filtered)

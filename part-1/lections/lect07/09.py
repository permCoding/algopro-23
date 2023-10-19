lines = open("./data/02.txt").readlines()

for line in lines:
    print(sum(map(float, line.split(';'))))

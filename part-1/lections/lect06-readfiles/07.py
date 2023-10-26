# f = open("./data/0.csv")
# f.close()

def get_lines(filename):
    with open(filename) as f:
        lines = f.readlines()[1:]
    return lines    


def get_amount(lines, amount=3):
    lst = []
    for line in lines:
        t = line.split(",")
        lst.append( [t[1], int(t[2])] )
    return lst[:amount]


lines = get_lines("./data/0.csv")
data = get_amount(lines)
print(data)

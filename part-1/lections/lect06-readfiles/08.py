def get_lines(filename, title=True):
    shift = 1 if title else 0
    with open(filename) as f:
        lines = f.readlines()[shift:]
    return lines


def create_obj(line):
    t = line.split(",")
    return [t[1], int(t[2])]


def get_slice(lines, amount=3):
    if amount == 0: amount = len(lines)
    return [create_obj(line) for line in lines][:amount]


def get_filtered(lst, min_rate):
    return [elm for elm in lst if elm[1] >= min_rate]


lines = get_lines("./data/0.csv")
data = get_slice(lines, 0)
for elm in get_filtered(data, 176): print(elm)

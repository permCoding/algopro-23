def get_lines(filename):
    lines = open(filename, "r", encoding="utf8").readlines()
    result = []
    for line in lines:
        tmp = line.strip()
        if len(tmp) > 0:
            result.append(tmp)
    return result


filename = "./docs/Пушкин.txt"
lines = get_lines(filename)
print(lines)
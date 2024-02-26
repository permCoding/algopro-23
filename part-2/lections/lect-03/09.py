def get_data(filename):
    data = []
    for line in open(filename, 'r'):
        try:
            data.append(float(line))
        except:
            pass
    return data


for tpl in enumerate(get_data('./data/nums.csv'), start=1):
    print(tpl)

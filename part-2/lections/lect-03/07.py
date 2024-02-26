def read_csv(filename):
    for line in open(filename, 'r'):
        try:
            print(float(line))
        except:
            pass


read_csv('./data/nums.csv')

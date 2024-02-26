def read_csv(filename):
    for pos, line in enumerate(open(filename, 'r'), start=1):
        try:
            print(f"{pos}\t{float(line)}")
        except:
            print(f"error on pos = {pos}")


read_csv('./data/nums.csv')

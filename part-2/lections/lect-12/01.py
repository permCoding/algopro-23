# sudo apt install python3-numpy
# sudo apt -y install python3-matplotlib
# https://matplotlib.org/
# pip install numpy
# pip install matplotlib

import numpy as np


x = np.linspace(0, 10, 101)
x = map(lambda elm: round(elm, 6), x)
print(list(x))

x = []
n, step = 0, 0.1
while n <= 10:
    # x.append(n)
    x.append(round(n,6))
    n += step
print(x)

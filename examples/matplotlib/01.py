# sudo apt-get install python3-numpy
# sudo apt-get -y install python3-matplotlib
# https://matplotlib.org/

import numpy as np
x = np.linspace(0, 10, 101)
print(list(x))

x = []
n, step = 0, 0.1
while n <= 10:
    # x.append(n)
    x.append(round(n,6))
    n += step
print(x)

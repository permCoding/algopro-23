# sudo apt-get install python3-numpy
# sudo apt-get -y install python3-matplotlib
# https://matplotlib.org/
import matplotlib.pyplot as plt
import numpy as np

# x = [round(i/10, 6) for i in range(0, 101)]
x = np.arange(0.0, 10.0, 0.1)
y = [elm**2 for elm in x]

# plt.plot(x, y)
plt.plot(x, y, 'b')
plt.show()

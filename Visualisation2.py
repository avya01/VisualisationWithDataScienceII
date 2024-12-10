import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10000, 1)
y1 = x*x+39992
y2 = x*x
#y3 = 5*x*x*x+6
#y4 = 5*x**x+3
plt.plot(x, y1, "g", linewidth=4, label="y=x^2+39992")
plt.plot(x, y2, "r", linewidth=4, label="y=x^2")
#plt.plot(x, y3, "b", linewidth=4, label="y=5x^3+6")
#plt.plot(x, y4, "v", linewidth=4, label="y=5x^x+3")
plt.legend()
plt.show()

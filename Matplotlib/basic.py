import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15])
y= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

a= np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,15])
b= np.array([2,3,4,5,6,7,8,9,0,11,12,13,14,15])

plt.plot(x,y, marker= ".")
plt.plot(a,b)
plt.show()
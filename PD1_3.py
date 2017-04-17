import numpy as np
import matplotlib.pyplot as plt
def y1(x):
	return np.log(1+x)/x
def y2(x):
	idx=((1+x)==1)
	z=np.log(1+x)/((1+x)-1)
	z[idx]=1
	return z
x=np.linspace(-10E-15,10E-15,100,dtype=np.float64)
y1=y1(x)
y2=y2(x)
plt.plot(x,y1,'-c',x,y2,'*r')
plt.show()
#print(type(x[0]))

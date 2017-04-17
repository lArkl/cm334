import numpy as np
import matplotlib.pyplot as plt
x=1.0
for i in range(10):
	x=x/8.0
	fx=np.sqrt(x**2+1)-1
	gx=x**2/(np.sqrt(x**2+1)+1)
	print('{0:11.8f}{1:11.8f}'.format(fx,gx))
#plt.plot(x,f,'*c')
#plt.show()

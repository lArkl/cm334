import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.99,1.01,101)
fx=(x**8-8*x**7+28*x**6-56*x**5+70*x**4-56*x**3+28*x**2-8*x+1)
gx=(((((((x-8)*x+28)*x-56)*x+70)*x-56)*x+28)*x-8)*x+1
hx=(x-1)**8
plt.plot(x,fx,'+r',x,gx,'og',x,hx,'*c')
plt.show()

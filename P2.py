import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    delta=5.67*10**-8
    z=np.pi*0.1*20*(x-300)+np.pi*0.1*0.8*delta*(x**4-300**4)-100
    return(z) 

def dfun(x):
    delta=5.67*10**-8
    z=np.pi*0.1*20+np.pi*0.4*0.8*delta*(x**3)
    return(z) 

def metNewton(f,df,x0,n=100,tol=1E-5):
    x=np.zeros((n+1,),dtype='f')
    x[0]=x0
    print ('-'*25)
    print("  {0:3s}   {1:6s}  {2:8s}".format('i','x','f(x)'))     
    print ('-'*25)    
    for i in range(n):
        xx=x[i]
        fx=f(xx)
        dfx=df(xx)
        if dfx==0:
            print ('-'*25)                
            print('Error f''(x)=0 en x={0:5.3f}, iteracion {1}'.format(xx,i))
            break
        if np.abs(fx)<tol:
            print ('-'*25)                
            print('x={0:5.3f}'.format(xx))
            break
        h = -fx/dfx
        err=np.abs(h)
        if err<tol:
            print ('-'*25)                
            print('x={0:5.3f}'.format(xx+h))            
            break
        else:
            x[i+1]=xx+h
            print("{0:3d} {1:8.3f} {2:8.3f}".format(i,xx,fx))
    return (x,i)

if __name__ == "__main__":
    x0=2
    (x,k) = metNewton(fun,dfun,x0)    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)    
    ax.plot(range(k+1),x[0:k+1],'g')
    ax.plot(range(k+1),x[0:k+1],'or')    
    ax.set_xlabel('k')    
    ax.set_ylabel('x_k')
    plt.show()

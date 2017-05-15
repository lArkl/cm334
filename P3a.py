import numpy as np
import matplotlib.pyplot as plt

def fun(x):
# x es un vector x=(x1,x2,..xn)
    n = len(x)
    z=np.zeros((n,))
    xx = x[0]
    yy = x[1]        
    z[0]=7*xx**3 - 10*xx - yy - 1
    z[1]=8*yy**3 - 11*yy + xx - 1
    return(z) 
def dfun(x):
    n = len(x)
    z=np.zeros((n,n))
    xx = x[0]
    yy = x[1]        
    z[0,0]= 21*xx**2 - 10
    z[1,0]= 1
    z[0,1]= -1
    z[1,1]= 24*yy**2 - 11
    return(z)

def metNewtonRn(f,df,x0,n=100,tol=1E-5):
    error =np.zeros((n+1,),dtype='f')
    xx=x0
    print ('-'*25)
    print("  {0:3s}   {1:6s}".format('i','x'))     
    print ('-'*25)    
    for i in range(n):
        fx=f(xx)
        dfx=df(xx)
        if np.linalg.det(dfx)==0:
            print ('-'*25)                
            print('Error det(f'')(x)=0 en x=({0:5.3f},{1:5.3f})'.format(*xx))
            break
        if np.linalg.norm(fx)<tol:
            print ('-'*25)                
            print('Solucion aproximada x=({0:5.3f},{1:5.3f})'.format(*xx))
            break
        h = -np.linalg.solve(dfx, fx)
        error[i]=np.linalg.norm(h)
        if error[i]<tol:
            print ('-'*25)                
            print('Solucion aproximada x=({0:5.3f},{1:5.3f})'.format(*(xx+h)))            
            break
        else:
            xx=xx+h
            print("{0:3d} ({1:5.3f},{2:5.3f})".format(i,*xx))
    
    return (xx,i,error)

if __name__ == "__main__":
# grafica de las curvas
    xx = np.linspace(-5, 5)
    yy = xx.copy()
    X, Y = np.meshgrid(xx, yy)
    Z1 = 7*X**3 - 10*X - Y - 1
    Z2 = 8*Y**3 - 11*Y + X - 1
    plt.contour(X, Y, Z1,levels=[0])
    plt.contour(X, Y, Z2,levels=[0])    
    plt.show()
    
# metodo de Newton en R^n    
    x0=np.array([1,1])
    (x,k,error) = metNewtonRn(fun,dfun,x0)    
    fig = plt.figure()  # create a figure object
    ax = fig.add_subplot(1, 1, 1)    
    ax.plot(range(k+1),error[0:k+1],'g')
    ax.plot(range(k+1),error[0:k+1],'or')    
    ax.set_xlabel('k')    
    ax.set_ylabel('error_k')
    plt.show()

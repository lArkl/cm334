# -*- coding: utf-8 -*-
import numpy as np
def sol_elim_gauss(AB):
    (n,m)=np.shape(AB)
    if m!=n+1:
        print('Error en las dimensiones de la matriz')
        return
#   factores de escalamiento
    s = np.max(np.abs(AB[:,0:n]),axis=1)
    for j in range(n-1): #para cada columna
        # buscamos la fila mejor escalada
        fila_inter = j + np.argmax(np.abs(AB[j:n,j])/s[j:n])
        if AB[fila_inter,j]==0:
            print 'Sistema indeterminado'
            return
        # intercambio fila fila_inter con fila j    
        aux = np.array(AB[fila_inter,:])
        AB[fila_inter,:] = AB[j,:]                
        AB[j,:] = aux
        # eliminacion        
        for i in range(j+1,n):#para cada fila
            mij=AB[i,j]/AB[j,j]
            AB[i,:]-=mij*AB[j,:]
    if AB[n-1,n-1]==0 :
       print 'Sistema intederminado' 
       return           
    x = np.zeros((n,),dtype='f')
    x[n-1]=AB[n-1,n]/AB[n-1,n-1]
    for i in range(n-2,-1,-1):
        x[i] = (AB[i,n] - np.sum(x[i+1:n]*AB[i,i+1:n]))/AB[i,i]
    return x
A=np.array( [[0,0,8],[0,4,5],[1 ,2, 3]],dtype='f')
x=np.array( [10,20,30],dtype='f')
print 'A=',A
B =A.dot(x)
print 'B=',B
AB =np.array(np.bmat( [A, B[:,None]]),dtype='f')
x=sol_elim_gauss(AB)
print 'AB=',AB
print 'x=',x

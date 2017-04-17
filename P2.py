import numpy as np
n=3
#C = [[0 for x in range(n)] for y in range(n)] 
C=np.zeros((n,n),dtype='f')
for i in range(n): #para cada columna
		for j in range(n):#para cada fila
			C[i,j]=(2+i)**(j)
B=np.zeros((n,),dtype='f')
for i in range(n): #para cada columna
		B[i]=((2+i)**(n)-1)/(i+1)
print ('C=',C)
print ('B=',B)

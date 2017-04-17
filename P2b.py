import numpy as np
def sol_elim_gauss(AB):
	s=0 #suma
	m=0 #multiplicacion
	(n,m)=np.shape(AB)
	for j in range(n-1): #para cada columna
		for i in range(j+1,n):#para cada fila
			mij=AB[i,j]/AB[j,j]
			AB[i,:]-=mij*AB[j,:] #de uno a n
	x = np.zeros((n,),dtype='f')
	x[n-1]=AB[n-1,n]/AB[n-1,n-1]
	for i in range(n-2,-1,-1):
		x[i] = (AB[i,n] - np.sum(x[i+1:n]*AB[i,i+1:n]))/AB[i,i]
	return x
def operar(n):
	C=np.zeros((n,n),dtype='f')
	for i in range(n): #para cada columna
			for j in range(n):#para cada fila
				C[i,j]=(2+i)**(j)
	D=np.zeros((n,),dtype='f')
	for i in range(n): #para cada columna
			D[i]=((2+i)**(n)-1)/(i+1)
	CD =np.array(np.bmat( [C, D[:,None]]),dtype='f')
	x=sol_elim_gauss(CD)
	print('n=',n)
	print ('x=',x)
n=14
operar(n)
n=15
operar(n)
n=16
operar(n)
n=17
operar(n)

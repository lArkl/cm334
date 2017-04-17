import numpy as np
def sol_elim_gauss(AB):
	s=0 #suma
	m=0 #multiplicacion
	(n,m)=np.shape(AB)
	for j in range(n-1): #para cada columna
		for i in range(j+1,n):#para cada fila
			mij=AB[i,j]/AB[j,j]
			AB[i,:]-=mij*AB[j,:] #de uno a n
			s=s+n
			m=m+1+n
	x = np.zeros((n,),dtype='f')
	print ('Triangular')
	print ('sum=',s)
	print ('mult=',m)
	m=0
	s=0
	x[n-1]=AB[n-1,n]/AB[n-1,n-1]
	m=m+1
	for i in range(n-2,-1,-1):
		x[i] = (AB[i,n] - np.sum(x[i+1:n]*AB[i,i+1:n]))/AB[i,i]
		s=s+1+(n-i)
		m=m+1+(n-i)**2
	print ('Eliminacion')
	print ('sum=',s)
	print ('mult=',m)
	return x
def operaciones(n):
	C=np.zeros((n,n),dtype='f')
	for i in range(n): #para cada columna
			for j in range(n):#para cada fila
				C[i,j]=(2+i)**(j)
	D=np.zeros((n,),dtype='f')
	for i in range(n): #para cada columna
			D[i]=((2+i)**(n)-1)/(i+1)
	CD =np.array(np.bmat( [C, D[:,None]]),dtype='f')
	x=sol_elim_gauss(CD)
n=3
operaciones(n)

import numpy as np
def sol_elim_gauss(AB):
	(n,m)=np.shape(AB)
	for j in range(n-1): #para cada columna
		for i in range(j+1,n):#para cada fila
			mij=AB[i,j]/AB[j,j]
			AB[i,:]-=mij*AB[j,:]
	x = np.zeros((n,),dtype='f')
	x[n-1]=AB[n-1,n]/AB[n-1,n-1]
	print ('pivot x[',n-1,']=',x[n-1])
	for i in range(n-2,-1,-1):
		x[i] = (AB[i,n] - np.sum(x[i+1:n]*AB[i,i+1:n]))/AB[i,i]
		print ('x[',i,']=',x[i])
	return x
A=np.array( [[3,1,1],[1,3,-1],[3 ,1, -5]],dtype='f')
B=np.array( [5,3,-1],dtype='f')
print ('A=',A)
print ('B=',B)
AB =np.array(np.bmat( [A, B[:,None]]),dtype='f')
x=sol_elim_gauss(AB)
#print ('AB=',AB)
#print ('Ax_1=',x)

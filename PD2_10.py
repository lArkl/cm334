#Multiplicación de matrices
import numpy as np
A1=np.array( [2,1],dtype='f')
A2=np.array( [1,0,0,-1],dtype='f')
A3=np.array( [[1,-1],[-1,0],[1,-1],[0,1]],dtype='f')
A4=np.array( [[0,1,-1,1],[1,1,0,1],[0,2,1,0],[1,0,0,1]],dtype='f')
A =np.array(np.vstack( (np.hstack((A1,A2)),np.hstack((A3,A4)))))
#print 'A=',A
B1=np.array( [[-1,2,0],[1,-1,1]],dtype='f')
B2=np.array( [[1,2],[0,1]],dtype='f')
B3=np.array( [[1,-1,1],[2,0,-1],[0,1,1],[1,1,0]],dtype='f')
B4=np.array( [[2,1],[1,0],[-2,1],[1,-1]],dtype='f')
B=np.array(np.vstack( (np.hstack((B1,B2)),np.hstack((B3,B4)))))
#print 'B=',B

#Calculo por bloques
C1=np.dot(A1,B1)+np.dot(A2,B3)
C2=np.dot(A1,B2)+np.dot(A2,B4)
C3=np.dot(A3,B1)+np.dot(A4,B3)
C4=np.dot(A3,B2)+np.dot(A4,B4)
C=np.array(np.vstack( (np.hstack((C1,C2)),np.hstack((C3,C4)))))
print 'AB=',C
#Calculo ordinario
AB =np.dot(A,B)
print 'AB=',AB

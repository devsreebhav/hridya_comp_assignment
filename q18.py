import numpy as np
A= np.array([[2,-1,0],
                    [-1,2,-1],
                    [0,-1,2]])
X= np.array([1,0,0])
Y=np.array([1,0,0])
G=np.linalg.matrix_power(A, 16)
H=np.linalg.matrix_power(A, 15)
Z=np.dot(G,X)
O=np.dot(H,X)
a=np.dot(np.transpose(Z),Y)
b=np.dot(np.transpose(O),Y)
c=a/b
I=np.dot(H,X)
print(G)
print(H)
print("Dominant eigen value:",c)
print("Corresponding eigen vector:",I)

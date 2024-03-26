import numpy as np
import time
A=np.array([[2,1],
                      [1,0]])
B=np.array([[2,1],
                      [1,0],
                      [0,1]])
C=np.array([[2,1],
                      [-1,1],
                      [1,1],
                      [2,-1]])
D=np.array([[1,1,0],
                      [-1,0,1],
                      [0,1,-1],
                      [1,1,-1]])
E=np.array([[0,1,1],
                      [0,1,0],
                      [1,1,0],
                      [0,1,0],
                      [1,0,1]])
print("Original matrix",A) # From here onwards, change the matrix each time we run this program to A,B,C or D
start_time =time.perf_counter()
U,S,Vt=np.linalg.svd(A)
end_time =time.perf_counter()
m, n = A.shape
S1=np.zeros((m, n))
# Fill the diagonal of S_full with the singular values
S1[:min(m, n), :min(m, n)] = np.diag(S)
print("U matrix",U)
print("S matrix",S1)
print("Vt matrix",Vt)
Z=np.dot(U,np.dot(S1,Vt))
print("Verified Product of U,S and Vt",Z)
print(f"\nTime taken for computation: {end_time - start_time:.6f} seconds") 

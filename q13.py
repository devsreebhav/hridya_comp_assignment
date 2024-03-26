import numpy as np
import pygsl
# Define the matrices
A = np.array([[3,-1,1],
                        [3,6,2],
                        [3,3,7]])
B=np.array([[10,-1,0],
                      [-1,10,-2],
                      [0,-2,10]])
C=np.array([[10,5,0,0],
                      [5,10,-4,0],
                      [0,-4,8,-1],
                      [0,0,-1,5]])
D=np.array([[4,1,1,0,1],
                      [-1,-3,1,1,0],
                      [2,1,5,-1,-1],
                      [-1,-1,-1,4,0],
                      [0,2,-1,1,4]])
# Perform LU decomposition
lu = pygsl.linalg.LU(A)                             #we can change the matrix to A,B,C or D
# Get the LU factors
L = lu.L().copy()
U = lu.U().copy()
# Verify the LU decomposition
reconstructed_A = np.dot(L, U)
# Print the factors
print("Original matrix A:")
print(A)
print("\nL factor:")
print(L)
print("\nU factor:")
print(U)
print("\nReconstructed A (L * U):")
print(reconstructed_A)



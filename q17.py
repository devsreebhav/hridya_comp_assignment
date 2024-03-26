import numpy as np
A = np.array([[5, -2], [-2, 8]])
Q,R = np.linalg.qr(A)
print("Q matrix:",Q)
print("R matrix:",R)
def qrdeigval(matrix, iterations=100):
    A = np.array([[5, -2], [-2, 8]])
    for _ in range(iterations):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
        eigenvalues = np.diag(A)
    return eigenvalues
matrix = [[5, -2], [-2, 8]]
eigenvalues = qrdeigval(matrix)
c=np.linalg.eigh(A)
print("Eigenvalues from qr decomp:", eigenvalues)
print("Eig values and eig vectors from numpy function:",c)

import numpy as np
def gauss_seidel(A, b, x0, tol=0.01, max_iter=1000):    
    n = len(b)
    x = x0.copy()
    iterations = 0
    while iterations < max_iter:
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        if np.linalg.norm(x_new - c) < tol: # Norm of difference vector between iterated solution and actual solution
            break
        x = x_new
        iterations=iterations+1
    return x, iterations
A = np.array([[0.2, 0.1, 1, 1, 0],
              [0.1, 4, -1, 1, -1],
              [1, -1, 60, 0, -2],
              [1, 1, 0, 8, 4],
              [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])  # Adjust according to your system
c=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])#actual solution
x0 = np.zeros(len(b))  # Initial guess
tolerance = 0.01
# Solving by Gauss-Seidel method
solution, iterations = gauss_seidel(A, b,x0)
print("Solution:", solution)
print("Number of iterations:", iterations)              

import numpy as np
def jacobi(A, b, x0, tol=0.01, max_iter=1000):
    x = x0.copy()
    n = len(b)
    iterations = 0  # Initialize iteration count
    
    while iterations < max_iter:
        x_new = np.zeros_like(x)  # Initialize the new solution vector
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i][i]
            
        if np.linalg.norm(x_new - c) < tol:
            return x_new, iterations + 1  # Adding 1 to iteration to count from 1 instead of 0
        
        x = x_new.copy()  # Update x for the next iteration
        iterations += 1  # Increment iteration count
    
    return x, max_iter

# Given system of equations
A = np.array([[0.2, 0.1, 1, 1, 0],
              [0.1, 4, -1, 1, -1],
              [1, -1, 60, 0, -2],
              [1, 1, 0, 8, 4],
              [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])  # Adjust according to your system
c=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x0 = np.zeros(len(b))  # Initial guess
tolerance = 0.01

solution, iterations = jacobi(A, b, x0, tol=tolerance)
print("Solution:", solution)
print("Number of iterations taken for convergence (with tolerance {}):".format(tolerance), iterations)

import numpy as np
def conjugate_gradient(A, b, x0, tol=0.01, max_iter=1000):
    x = x0.copy()
    r = b - np.dot(A, x)  # Residual
    p = r.copy()          # Initial search direction
    rsold = np.dot(r, r)
    for i in range(max_iter):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r, r)
        if np.linalg.norm(x-c) < tolerance:# Norm of difference vector between iterated solution and actual solution
            return x, i + 1  # Return solution and number of iterations
        p = r + (rsnew / rsold) * p  # Update search direction
        rsold = rsnew
    print("Maximum number of iterations reached without meeting the convergence criteria.")
    return x, max_iter

# Given system of equations
A = np.array([[0.2, 0.1, 1, 1, 0],
              [0.1, 4, -1, 1, -1],
              [1, -1, 60, 0, -2],
              [1, 1, 0, 8, 4],
              [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])  # Adjust according to your system
c = np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])#actual solution
x0 = np.zeros(len(b))  # Initial guess
tolerance = 0.01  # Tolerance for convergence
solution, iterations = conjugate_gradient(A, b, x0, tol=tolerance)
print("Solution:", solution)
print("Number of iterations taken for convergence (with tolerance {}):".format(tolerance), iterations)



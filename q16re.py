import numpy as np
def relaxation_method(A, b, x0, tolerance=0.01, max_iterations=1000, w=1.25):
    n = len(b)
    solution = np.copy(x0)
    for iteration in range(max_iterations):
        old_solution = np.copy(solution)
        for i in range(n):
            summation = 0.0
            for j in range(n):
                if j != i:
                    summation=summation+A[i][j] * solution[j]
            solution[i] = (1-w)*old_solution[i] + (w / A[i][i]) * (b[i] - summation)
        if np.linalg.norm(solution - c) < tolerance:# Norm of difference vector between iterated solution and actual solution
            return solution, iteration + 1
A = np.array([[0.2, 0.1, 1, 1, 0],
              [0.1, 4, -1, 1, -1],
              [1, -1, 60, 0, -2],
              [1, 1, 0, 8, 4],
              [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])  # Adjust according to your system
c=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])#actual solution
x0 = np.zeros(len(b))  # Initial guess
tolerance = 0.01
# Solving by Relaxation method
solution, num_iterations = relaxation_method(A, b, x0)
print("Solution:", solution)
print("Number of iterations:", num_iterations)

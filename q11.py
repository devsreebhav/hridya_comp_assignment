import numpy as np
A1 = np.array([
    [3, -1, 1],
    [3, 6, 2],
    [3, 3, 7]
])
B1 = np.array([1, 0, 4])
solution1 = np.linalg.solve(A1, B1)
print("Solution for System 1:",solution1)
A2 = np.array([
    [10, -1, 0],
    [-1, 10, -2],
    [0, -2, 10]
])
B2 = np.array([9, 7, 6])
solution2 = np.linalg.solve(A2, B2)
print("Solution for System 2:",solution2)
A3 = np.array([
    [10, 5, 0, 0],
    [5, 10, -4, 0],
    [0, -4, 8, -1],
    [0, 0, -1, 5]
])
B3 = np.array([6, 25, -11, -11])
solution3 = np.linalg.solve(A3, B3)
print("Solution for System 3:",solution3)
A4 = np.array([
    [4, 1, 1, 0, 1],
    [-1, -3, 1, 1, 0],
    [2, 1, 5, -1, -1],
    [-1, -1, -1, 4, 0],
    [0, 2, -1, 1, 4]
])
B4 = np.array([6, 6, 6, 6, 6])
solution4 = np.linalg.solve(A4, B4)
print("Solution for System 4:",solution4)





import numpy as np

A = np.array([[2, 0, -3], [1, 4, 5]])
B = np.array([[3, 1], [-1, 0], [4, 2]])
C = np.array([[4, 7], [2, 1], [1, -1]])

AB = np.dot(A, B)
AC = np.dot(A, C)

print("AB = \n", AB)
print("AC = \n", AC)
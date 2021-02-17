#%%
from fractions import Fraction
import numpy as np

A = np.array([ #!
    [8, 21, 4, 1],
    [1, 3, 1, -1],
    [7, 7, 1, 6],
    [-1, 2, -2, 1]
])
b = np.array([-16, -2, -11, -10]) #!
r = np.zeros(4)
n = len(A)

A = A + Fraction()
b = b + Fraction()
r = r + Fraction()

cnt = 1
for i in range(n):
    pivot = i + np.argmax(np.abs(A[i:, i]))
    A[i], A[pivot] = A[pivot], A[i].copy()
    b[i], b[pivot] = b[pivot], b[i]
    for j in range(i + 1, n):
        a = A[j][i]/A[i][i]
        for k in range(i, n):
            A[j][k] = A[j][k] - a*A[i][k]
        b[j] = b[j] - a*b[i]
    print(f"{cnt}回目")
    print("A")
    print(A)
    print("b")
    print(b)
    print("-"*20)
    cnt += 1

# 後退代入
for i in range(n)[::-1]:
    a = b[i]
    for j in range(i + 1, n):
        a -= A[i][j]*r[j]
    r[i] = a/A[i][i]
print("ans")
print(r)
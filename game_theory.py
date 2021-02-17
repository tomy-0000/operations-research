#%%
import numpy as np
import sympy as sym
from itertools import combinations
import matplotlib.pyplot as plt

A = np.array([
    [-3, -1, 2],
    [3, 1, -1]
])
row_min = []
column_max = []
for i in range(A.shape[0]):
    for j in list(*np.where(A[i, :] == A[i, :].min())):
        row_min.append([i, j])
for i in range(A.shape[1]):
    for j in list(*np.where(A[:, i] == A[:, i].max())):
        column_max.append([j, i])
stable = False
for i in row_min:
    if i in column_max:
        stable = True
        print(i)
if not stable:
    if A.shape[0] <= 2 <= A.shape[1]:
        first = "column"
        A = A.T
        var = sym.Symbol("x")
    elif A.shape[1] <= 2 <= A.shape[0]:
        first = "row"
        var = sym.Symbol("y")
    else:
        raise ValueError("Uninmplemented")
    A = A.tolist()
    ans = set()
    expr = []
    for i in A:
        z = sym.Symbol("z")
        expr.append(i[0]*var + i[1]*(1 - var) - z)
    print(expr)
    print()
    for i in combinations(expr, 2):
        print(i)
        print(sym.solve(i))
        print()

#%%
def f1(x):
    return -6*x + 3
def f2(x):
    return -2*x + 1
def f3(x):
    return 3*x - 1
x = np.arange(0, 1, 0.001)
ax = plt.subplot()
ax.plot(x, f1(x))
ax.plot(x, f2(x))
ax.plot(x, f3(x))
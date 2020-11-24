#%%
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from itertools import combinations
from collections import namedtuple

# sample
# mat = np.array([[6, 5, 5, 7],
#                 [2, 2, 3, 4],
#                 [4, 8, 2, 1]])
mat = np.array([[3, 5],
                [-3, 4],
                [7, -6]])
row_min = []
column_max = []
for i in range(mat.shape[0]):
    for j in list(*np.where(mat[i, :] == mat[i, :].min())):
        row_min.append([i, j])
for i in range(mat.shape[1]):
    for j in list(*np.where(mat[:, i] == mat[:, i].max())):
        column_max.append([j, i])
stable = False
for i in row_min:
    if i in column_max:
        stable = True
        print(i)
if not stable:
    if mat.shape[0] <= 2 <= mat.shape[1]:
        first = "column"
        mat = mat.T
        var = sym.Symbol("x")
    elif mat.shape[1] <= 2 <= mat.shape[0]:
        first = "row"
        var = sym.Symbol("y")
    else:
        raise ValueError("Uninmplemented")
    mat = mat.tolist()
    ans = set()
    expr = []
    for i in mat:
        z = sym.Symbol("z")
        expr.append(i[0]*var + i[1]*(1 - var) - z)
    for i in combinations(expr, 2):
        print(i)
        print(sym.solve(i))
        print()
#%%
import numpy as np
import sympy as sym
from sympy import Rational

def to_npRational(l):
    return np.array([Rational(i, 1) if isinstance(i, int) else i for i in l])

def subs(l):
    ret = []
    for i in l:
        if isinstance(i, sym.core.mul.Mul) or isinstance(i, sym.core.add.Add) or isinstance(i, sym.core.symbol.Symbol):
            ret.append(i.subs(M, 100000))
        else:
            ret.append(i)
    return np.array(ret)

def to_str(l):
    if type(l) == list or type(l) == np.ndarray:
        ret = []
        for i in l:
            ret.append(str(i))
        return np.array(ret)
    else:
        return str(l)

# サンプル
# mode = "min"
# coeff1 = to_npRational([2, 3, 3, -1, -1, 0, 0, 2]) # z0 + 2y1 + 3y2 + 3y3 - y4 - y5 + 0y6 + 0y7 = 2
# coeff2 = to_npRational([-5, -8, -9, 0, 0, 0, 0, 0]) # z - 5y1 - 8y2 - 9y3 + 0y4 + 0y5 + 0y6 + 0y7 = 0
# expr = np.array([
#     to_npRational([1, 2, 1, -1, 0, 1, 0, 1]), # y1 + 2y3 + y3 - y4 + 0y5 + y6 + 0y7 = 1
#     to_npRational([1, 1, 2, 0, -1, 0, 1, 1]), # y1 + y2 + 2y3 + 0y4 - y5 + 0y6 + y7 = 1
# ])
# base_val = [5, 6] # coeffのインデックス

mode = "max"
coeff1 = to_npRational([7, 6, 0, -1, 0, 0, 84])
coeff2 = to_npRational([-3, -2, 0, 0, 0, 0, 0])
expr = np.array([
    to_npRational([1, 2, 1, 0, 0, 0, 20]),
    to_npRational([7, 6, 0, -1, 1, 0, 84]),
    to_npRational([1, -1, 0, 0, 0, 1, 8]),
])
base_val = [2, 4, 5] # coeffのインデックス

artificial_val = base_val.copy()
theta = [0 for _ in expr]

base = "{:>6}" + "{:>8}"*(len(coeff1) - 1) + "{:>8} {:>8}"

print("第1段階")
print(base.format("base", *[f"x{i + 1}" for i in range(len(coeff1) - 1)], "const", "theta"))
while True:
    pivot_col = np.argmax(subs(coeff1[:-1]))
    theta = [j / i if i > 0 else Rational(1000000) for i, j in zip(expr[:, pivot_col], expr[:, -1]) ]
    pivot_row = np.argmin(subs(theta))
    pivot = [pivot_row, pivot_col]

    for i, j in enumerate(base_val):
        print(base.format(f"x{j + 1}", *to_str(expr[i]), to_str(theta)[i]))
    print(base.format("x", *to_str(coeff2), "", ""))
    print(base.format("x0", *to_str(coeff1), "", ""))
    print("-"*80)
    if (subs(coeff1[:-1]) <= 0).all():
        break
    base_val[pivot_row] = pivot_col
    expr[pivot_row] = expr[pivot_row] / expr[pivot_row, pivot_col]
    for i in range(len(base_val)):
        if (i == pivot_row):
            continue
        expr[i] = expr[i] - expr[i][pivot_col]*expr[pivot_row]
    coeff2 = coeff2 - coeff2[pivot_col]*expr[pivot_row]
    coeff1 = coeff1 - coeff1[pivot_col]*expr[pivot_row]
for i, j in enumerate(base_val):
    print(f"x{j + 1}={expr[i][-1]}")
print(mode+"="+str(coeff1[-1]))
print()

print("第2段階")
del_idx = set(artificial_val)
for i, j in enumerate(coeff1[:-1]):
    if j < 0:
        del_idx.add(i)
expr = np.delete(expr, list(del_idx), axis=1)
coeff2 = np.delete(coeff2, list(del_idx))

base = "{:>6}" + "{:>8}"*(len(coeff2) - 1) + "{:>8} {:>8}"

print(base.format("base", *[f"x{i + 1}" for i in range(len(coeff2) - 1)], "const", "theta"))
while True:
    if mode == "max":
        pivot_col = np.argmin(subs(coeff2[:-1]))
    else:
        pivot_col = np.argmax(subs(coeff2[:-1]))
    theta = [j / i if i > 0 else Rational(100000) for i, j in zip(expr[:, pivot_col], expr[:, -1]) ]
    pivot_row = np.argmin(subs(theta))
    pivot = [pivot_row, pivot_col]

    for i, j in enumerate(base_val):
        print(base.format(f"x{j + 1}", *to_str(expr[i]), to_str(theta)[i]))
    print(base.format("x", *to_str(coeff2), "", ""))
    print("-"*80)
    if mode == "max":
        if (subs(coeff2[:-1]) >= 0).all():
            break
    else:
        if (subs(coeff2[:-1]) <= 0).all():
            break
    base_val[pivot_row] = pivot_col
    expr[pivot_row] = expr[pivot_row] / expr[pivot_row, pivot_col]
    for i in range(len(base_val)):
        if (i == pivot_row):
            continue
        expr[i] = expr[i] - expr[i][pivot_col]*expr[pivot_row]
    coeff2 = coeff2 - coeff2[pivot_col]*expr[pivot_row]
for i, j in enumerate(base_val):
    print(f"x{j + 1}={expr[i][-1]}")
print(mode+"="+str(coeff2[-1]))
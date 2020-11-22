#%%
import numpy as np
import sympy as sym
from sympy import Rational

sym.var("M")

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

mode = "max"
coeff = to_npRational([1, 1, 1, 0, -M]) # x0 = x1 + x2 + x3 -Mx5
expr = np.array([
    to_npRational([1, -2, 6, 1, 0, 54]), # x1 - 2x2 + 6x3 + x4 = 54
    to_npRational([1, 1, 3, 0, 1, 12]) # x1 + x2 + 3x3 + x5 = 12
])
base_val = [3, 4] # coeffのインデックス

theta = [0 for _ in expr]

base = "{:>10}{:>10}" + "{:>10}"*len(coeff) + "{:>10} {:>10}"

first = True
while True:
    pi = expr.T @ coeff[base_val]
    c_pi = coeff - pi[:-1]
    if mode == "max":
        pivot_col = np.argmax(subs(c_pi))
    else:
        pivot_col = np.argmin(subs(c_pi))
    theta = [j / i if i > 0 else Rational(100000000) for i, j in zip(expr[:, pivot_col], expr[:, -1]) ]
    pivot_row = np.argmin(subs(theta))
    pivot = [pivot_row, pivot_col]

    if first:
        print(base.format("", "c", *to_str(coeff), "", ""))
        first = False
        print(base.format("c", "base", *[f"x{i + 1}" for i in range(len(coeff))], "const", "theta"))
    for i, j in enumerate(base_val):
        print(base.format(to_str(coeff[j]), f"x{j + 1}", *to_str(expr[i]), to_str(theta)[i]))
    print(base.format("", "pi", *to_str(pi), "", ""))
    print(base.format("", "c - pi", *to_str(c_pi), "", "", ""))
    print("-"*90)
    base_val[pivot_row] = pivot_col
    expr[pivot_row] = expr[pivot_row] / expr[pivot_row, pivot_col]
    for i in range(len(base_val)):
        if (i == pivot_row):
            continue
        expr[i] = expr[i] - expr[i][pivot_col]*expr[pivot_row]
    if mode == "max":
        if (subs(c_pi) <= 0).all():
            break
    else:
        if (subs(c_pi) >= 0).all():
            break
for i, j in enumerate(base_val):
    print(f"x{j + 1}={expr[i][-1]}")
print(mode+"="+str(pi[-1]))

#%%
# 別表
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

mode = "min"
coeff = to_npRational([-5, -4, 0, 0, 0, 0]) # x0 - 5x1 - 4x2 + 0x3 + 0x4 + 0x5 = 0
expr = np.array([
    to_npRational([15, 11, 1, 0, 0, 1650]), # 0x0 + 15x1 + 11x2 + 1x3 + 0x4 + 0x5 = 1650
    to_npRational([10, 14, 0, 1, 0, 1400]), # 0x0 + 10x1 + 14x2 + 0x3 + 1x4 + 0x5 = 1400
    to_npRational([9, 20, 0, 0, 1, 1800]), # 0x0 + 9x1 + 20x2 + 0x3 + 0x4 + 1x5 = 1800
])
base_val = [2, 3, 4] # coeffのインデックス

theta = [0 for _ in expr]

base = "{:>10}" + "{:>10}"*(len(coeff) - 1) + "{:>10} {:>10}"

print(base.format("base", *[f"x{i + 1}" for i in range(len(coeff) - 1)], "const", "theta"))
while True:
    if mode == "max":
        pivot_col = np.argmin(subs(coeff))
    else:
        pivot_col = np.argmax(subs(coeff))
    theta = [j / i if i > 0 else Rational(100000000) for i, j in zip(expr[:, pivot_col], expr[:, -1]) ]
    pivot_row = np.argmin(subs(theta))
    pivot = [pivot_row, pivot_col]

    for i, j in enumerate(base_val):
        print(base.format(f"x{j + 1}", *to_str(expr[i]), to_str(theta)[i]))
    print(base.format("x0", *to_str(coeff), "", ""))
    print("-"*90)
    base_val[pivot_row] = pivot_col
    expr[pivot_row] = expr[pivot_row] / expr[pivot_row, pivot_col]
    for i in range(len(base_val)):
        if (i == pivot_row):
            continue
        expr[i] = expr[i] - expr[i][pivot_col]*expr[pivot_row]
    if mode == "max":
        if (subs(coeff) >= 0).all():
            break
    else:
        if (subs(coeff) <= 0).all():
            break
    coeff = coeff - coeff[pivot_col]*expr[pivot_row]
for i, j in enumerate(base_val):
    print(f"x{j + 1}={expr[i][-1]}")
print(mode+"="+str(pi[-1]))
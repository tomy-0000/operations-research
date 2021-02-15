#%%
import numpy as np
import sympy as sym
from sympy import Rational

M = sym.var("M")

arr = np.array([ #!
    [1, 2, 1, -1, 0, 1, 0],
    [1, 1, 2, 0, -1, 0, 1],
    [-5, -8, -9, 0, 0, 0, 0],
    [2, 3, 3, -1, -1, 0, 0]
])
const = np.array([1, 1, 0, 2]) #!
base = np.array([6, 7]) #!
objective = "min" #!

def to_Rational(i):
    try:
        i = Rational(i)
    except:
        pass
    return i
to_Rational = np.vectorize(to_Rational)

def subs(i):
    try:
        i = i.subs(M, 1000000000)
    except:
        pass
    return i
subs = np.vectorize(subs)

def argmax(l):
    l = subs(l)
    return np.argmax(l)
def argmin(l):
    l = subs(l)
    return np.argmin(l)
def check(l):
    if objective == "max":
        return sum(subs(l) < 0)
    else:
        return sum(subs(l) > 0)

def print_table(arr, const, base, theta, is_first):
    base = np.array(["x"+str(i) for i in base])
    base = np.append(base, "z")
    theta = np.append(theta, "-")
    if is_first:
        base = np.append(base, "z0")
        theta = np.append(theta, "-")
    base = np.expand_dims(base, 1)
    theta = np.expand_dims(theta, 1)
    const = np.expand_dims(const, 1)
    a = np.concatenate([base, arr, const, theta], 1)
    for i in a:
        for j in i:
            print(f"{str(j):>9}", end="|")
        print()
    print("-"*10*(arr.shape[1] + 3))

arr = to_Rational(arr)
const = to_Rational(const)
base = to_Rational(base)
theta = np.zeros(len(const) - 2, dtype=arr.dtype)

print("1st")
header = ["base"]
header += [str(i + 1) for i in range(arr.shape[-1])]
header += ["const", "θ"]
for i in header:
    print(f"{i:>9}", end="|")
print()
print("-"*10*(arr.shape[1] + 3))
print_table(arr, const, base, theta, 1)
while check(arr[-1]):
    idx1 = argmin(arr[-1]) if objective == "max" else argmax(arr[-1])
    theta = const[:-2]/arr[:-2, idx1]
    idx2 = argmin(theta)
    v = arr[idx2, idx1]
    tmp = np.ones(len(arr), bool)
    tmp[idx2] = False
    v2 = arr[tmp, idx1].reshape(-1, 1)
    arr[idx2] /= v
    const[idx2] /= v
    arr[tmp] -= v2*arr[idx2]
    const[tmp] -= v2.reshape(-1)*const[idx2]
    base[idx2] = idx1 + 1
    print_table(arr, const, base, theta, 1)
minus_idx = arr[-1] < 0
arr = arr[:, ~minus_idx][:-1]
const = const[:-1]

print("\n2nd")
header = ["base"]
header += [str(i + 1) for i in range(arr.shape[-1])]
header += ["const", "θ"]
for i in header:
    print(f"{i:>9}", end="|")
print()
print("-"*10*(arr.shape[1] + 3))
print_table(arr, const, base, theta, 0)
while check(arr[-1]):
    idx1 = argmin(arr[-1]) if objective == "max" else argmax(arr[-1])
    theta = const[:-1]/arr[:-1, idx1]
    idx2 = argmin(theta)
    v = arr[idx2, idx1]
    tmp = np.ones(len(arr), bool)
    tmp[idx2] = False
    v2 = arr[tmp, idx1].reshape(-1, 1)
    arr[idx2] /= v
    const[idx2] /= v
    arr[tmp] -= v2*arr[idx2]
    const[tmp] -= v2.reshape(-1)*const[idx2]
    base[idx2] = idx1 + 1
    print_table(arr, const, base, theta, 0)
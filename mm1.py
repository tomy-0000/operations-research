#%%
import math

l = 4 #!
m = 5 #!
n = 2 #!

a = l/m

print("P0")
print(a)
print()

Pn = a**n*(1 - a)
print("Pn")
print(Pn)
print()

Lq = a**2/(1 - a)
print("Lq")
print(Lq)
print()

L = Lq + a
print("L")
print(L)
print()

Wq = l/(m*(m - l))
print("Wq")
print(Wq)
print()


W = 1 / (m - l)
print("W")
print(W)
print()

t = 0 #!
if t == 0:
    P = a
else:
    P = a*math.e**(-(1 - a)*m*t)
print(f"P{{w > {t}}}")
print(P)
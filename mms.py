#%%
import math

l = 4 #!
m = 5 #!
s = 2 #!
n = 2 #!

a = l/m

print("P0")
tmp = 0
for i in range(s):
    tmp += a**i/math.factorial(i)
tmp += a**s/(math.factorial(s - 1)*(s - a))
P0 = 1/tmp
print(P0)
print()

if n <= s:
    Pn = a**n/math.factorial(n)*P0
else:
    Pn = a**n/(s**(n - s)*math.factorial(s))*P0
print("Pn")
print(Pn)
print()

print("Lq")
if n <= s:
    Lq = 0
else:
    Lq = a**(s + 1)/(math.factorial(s - 1)*(s - a)**2)
print(Lq)
print()

L = Lq + a
print("L")
print(L)
print()

Wq = Lq/l
print("Wq")
print(Wq)
print()

W = L/l
print("W")
print(W)
print()

t = 0 #!
if t == 0:
    P = a**s/(math.factorial(s - 1)*(s - a))
else:
    P = a*math.e**(-(1 - a)*m*t)
print(f"P{{w > {t}}}")
print(P)
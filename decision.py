#%%
import numpy as np

A = np.array([ #!
    [2, 3, 4, 8],
    [3, 5, 4, 2],
    [8, 5, 2, 0],
    [10, 3, 1, 1]
])
prob = np.array([1, 1, 1, 1]) #!

print("期待値基準")
tmp = (A*prob).sum(axis=1)
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("満足度基準")
threshold = 4 #!
tmp = np.where(A >= threshold, 1, 0)
tmp = (tmp*prob).sum(axis=1)
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("ラプラス基準")
tmp = A.sum(axis=1)
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("マックス・ミニ基準")
tmp = A.min(axis=1)
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("ミニ・マックス基準")
tmp = A.max(axis=1)
print(tmp)
print(np.where(tmp == tmp.min())[0])

print("マックス・マックス基準")
tmp = A.max(axis=1)
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("ミニ・ミニ基準")
tmp = A.min(axis=1)
print(tmp)
print(np.where(tmp == tmp.min())[0])

print("ハーウィツ基準")
alpha = 0.7 #!
tmp1 = A.min(axis=1)
tmp2 = A.max(axis=1)
tmp = alpha*tmp1 + (1 - alpha)*tmp2
print(tmp)
print(np.where(tmp == tmp.max())[0])

print("サーベジュのミニ・マックス落胆基準")
tmp = A.max(axis=0)
tmp = (tmp - A).max(axis=1)
print(tmp)
print(np.where(tmp == tmp.min())[0])
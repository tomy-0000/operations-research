#%%
import numpy as np

player = [0, 1, 2] #!
A = { #!
    (0, 1, 2): 20,
    (0, 1): 6,
    (0, 2): 0,
    (1, 2): 8,
    (0,): 0,
    (1,): 0,
    (2,): 0,
}

table = []
for i in A.keys():
    row = []
    for j in player:
        if j in i:
            tmp = set(i)
            tmp.discard(j)
            tmp = tuple(tmp)
            if tmp:
                tmp = A[i] - A[tmp]
            else:
                tmp = A[i]
        else:
            tmp = np.nan
        row.append(tmp)
    table.append(row)
table = np.array(table)

for i, j in zip(A.keys(), table):
    tmp = ", ".join([str(k) for k in i])
    print(f"{{{tmp:^7}}}", end="|")
    print(j, end="\n")

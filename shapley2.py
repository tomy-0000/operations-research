#%%
from itertools import permutations
import numpy as np

def tuple_sort(t):
    return tuple(sorted(list(t)))

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
for i in permutations(player):
    row = [0 for _ in range(len(i))]
    pre = 0
    for j in range(1, len(i)):
        row[i[j]] = A[tuple_sort(i[:j + 1])] - pre
        pre = A[tuple_sort(i[:j + 1])]
    table.append(row)
table = np.array(table)
shapley = np.nanmean(table, axis=0)

for i, j in zip(permutations(player), table):
    tmp = ", ".join([str(k) for k in i])
    print(f"{{{tmp:^7}}}", end="|")
    print(j, end="\n")
print(f"{'shapley':>9}|{shapley}")
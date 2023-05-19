import os
import numpy as np
import pickle

filename = "head_sorted.txt"
#filename = "first_1M_64b_sorted.txt"
#filename = "first_50M_64b_sorted.txt"

data_bin = []

with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        data_bin.append(line.strip())
f.close()   

diff_list = []
for i in range(len(data_bin)-1):
    for b in range(2,64,1):
        if (data_bin[i][b] != data_bin[i+1][b]):
            diff_list.append(b-2)
            break

surf_diff = [diff_list[0]]
for i in range(len(diff_list)-1):
    if (diff_list[i] > diff_list[i+1]):
        surf_diff.append(int(diff_list[i]))
    else:    
        surf_diff.append(int(diff_list[i+1]))
surf_diff.append(diff_list[len(diff_list)-1])

print (surf_diff)
filename1 = filename.split("sorted.txt")[0]
with open(filename1 + str("eq_list.txt"), "wb") as fp:   #Pickling
    pickle.dump(surf_diff, fp)


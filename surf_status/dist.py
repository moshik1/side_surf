import os
import numpy as np
import pickle
import json

filename = "head_eq_list.txt"
filename = "first_1M_64b_eq_list.txt"
filename = "first_50M_64b_eq_list.txt"

with open(filename, "rb") as fp:   # Unpickling
    surf_diff = pickle.load(fp)

list_eq_nu  = [0] *65
# 0 - no eq number
# 1 - one eq number
# 64 - all the numbers are eq
for i in range(len(surf_diff)):
    list_eq_nu[surf_diff[i]] +=1

dict_eq_dist = {}

for i in range(len(list_eq_nu)):
    dict_eq_dist[i] = list_eq_nu[i]

print (dict_eq_dist)


filename1 = filename.split("eq_list.txt")[0]
with open(filename1 + "dist.json", 'w') as fp:
    json.dump(dict_eq_dist, fp)

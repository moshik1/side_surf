import os
import numpy as np
import pickle

filename = "head_sorted.txt"
filename = "first_1M_64b_sorted.txt"
filename = "first_50M_64b_sorted.txt"

data_bin = []

with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        data_bin.append(line.strip())
f.close()   

data_out = []
for i in range(len(data_bin)):
    a = "0b"
    print (i)
    for j in range(66,2,-8):
        a += data_bin[i][j-8:j]
    data_out.append(a)    

filename1 = filename.split("sorted.txt")[0]
with open(filename1 + "sorted_switch.txt", "w") as f:
    for i in range(len(data_out)):
        f.write(data_out[i] + "\n")    


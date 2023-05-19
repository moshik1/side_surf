import os
import numpy as np

filename = "head.txt"
#filename = "first_1M_64b.txt"
#filename = "first_50M_64b.txt"
filename = "25_40_50M.txt"
data_hex = []
data_int = []
data_bin = []
with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        dhex = "0x" + str(line.strip())
        an_integer = int(dhex, 16)
        data_hex.append(dhex)
        data_int.append(an_integer)
        data_bin.append(f"{an_integer:#066b}")
f.close()   

print ("start_sorting")
data_bin_sorted = sorted(data_bin)
print ("end_sorting")

filename1 = filename.split(".txt")[0]
with open(filename1 + "_sorted.txt", "w") as f:
    for i in range(len(data_bin_sorted)):
        print (i)
        f.write(data_bin_sorted[i] + "\n")    


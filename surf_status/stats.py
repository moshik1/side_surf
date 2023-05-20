import os
import numpy as np
import pickle
import json

filename = "head_dist.json"
#filename = "first_50M_64b_dist.json"
#filename = "first_50M_64b_dist.json"

with open(filename, "rb") as fp:   # Unpickling
    dist_dict = json.load(fp)

sum_a = 0
byte_diff = 9*[0]
index = 0

for i in range(0,65):
    byte_diff[index] += dist_dict[str(i)]
    print (str(i) + " " +str(dist_dict[str(i)]))
    if (i%8 == 7):
        index += 1

prob_base = 0
prob_real = 0

prob_above_40b_base = 0
prob_above_40b_real = 0



for i in range(len(byte_diff)-1):
#        print (str((i+1)*8) + " " +str(byte_diff[i]))
        prob_base += byte_diff[i]/((2**((i+1)*8)))
        prob_real += byte_diff[i]/((2**((i+1)*8)))/256
        if (i>=4):
            prob_above_40b_base += byte_diff[i]/((2**((i+1)*8)))
        else:
            prob_base += byte_diff[i]/((2**((i+1)*8)))/(2**((4-i)*8))

print ("prob_base " + str(prob_base))        
print ("prob_real " + str(prob_real))       

items = 50*1000*1000

print ("number of false pos surf_base " + str(prob_base*items))        
print ("number of false pos surf_real " + str(prob_real*items))      

print ("base above 40 " + str(prob_above_40b_base * items))        
print ("real above 32 " + str(prob_above_40b_real * items))       



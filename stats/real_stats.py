import math
import numpy

def calc_dist(num_items):
    dist_eq_gr_l = {} 
    for i in range(64):
        dist_eq_gr_l[i] = (1-(1-1/2**i)**num_items)
        print("prob eq_gr l " + str(i) + " p " + str(dist_eq_gr_l[i]))
    
    dist_eq_l = {} 
    for i in range(63):
        dist_eq_l[i] = dist_eq_gr_l[i] - dist_eq_gr_l[i+1]
        print("prob eq l " + str(i) + " p " + str(dist_eq_l[i]))

    
    num_eq_l = {}
    for i in range(63):
        num_eq_l[i] = dist_eq_l[i] * num_items
        print("num eq l " + str(i) + " p " + str(num_eq_l[i]))

    # verify 
    sum_num_eq_l = 0
    for i in num_eq_l.keys():
        sum_num_eq_l+= num_eq_l[i]
    assert (sum_num_eq_l == num_items)    

    num_surf_real = {} 
    for i in range(16,64,8):
        num_surf_real[i] = 0
        for j in range(8):
            num_surf_real[i] += num_eq_l[i-j-1-8]/256 
        print("items surf real " + str(i) + " p " + str(num_surf_real[i]))

    prob_surf_real = {} 
    for i in range(24,64,8):
        prob_surf_real[i] = num_surf_real[i]/2**(i-8) 
        print("prob surf real " + str(i) + " p " + str(prob_surf_real[i]))

    
    suffix = {} 
    for i in range(24,64,8):
        suffix[i] = 2**(64-i)/2
        print("suffix " + str(i) + " items " + str(suffix[i]))
    brute_force = 1/ (num_items / 2**64)
    print ("brute_force " + str(brute_force))
   

    surf_better_bf = {} 
    for i in range(32,64,8):
        surf_better_bf[i] = brute_force / (1/prob_surf_real[i] + suffix[i])
        print("suffix " + str(i) + " items " + str(surf_better_bf[i]))

calc_dist(10*1000*1000)        

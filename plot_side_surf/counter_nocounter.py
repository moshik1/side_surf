import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time
import csv
import seaborn as sns
import matplotlib.style as style
from tikzplotlib import save as tikz_save
# colors
# https://colorbrewer2.org/#type=sequential&scheme=YlGn&n=3

def chop_array(array):
    for i in range(len(array)):
        try: 
            int(array[i])
        except:
            return i;
    return (len(array))    


def plot_counter_nocounters(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(str)

    get_request = data[:,0]
    counters = data[:,1] 
    no_counters = data[:,2]
    
    len_counters = chop_array(counters)
    len_no_counters = chop_array(no_counters) 
    print ((len_counters))
    print ((len_no_counters))
    counters_color = "#2c7fb8"
    no_counters_color = "#e7298a"
    
    plt.plot(get_request[0:len_counters - 1].astype(int), counters[0:len_counters - 1].astype(int), label='Idealized', color= counters_color)
    plt.plot(get_request[0:len_no_counters - 1].astype(int), no_counters[0:len_no_counters - 1].astype(int), label='Actual', color= no_counters_color)
    plt.ylabel('# Extracted keys', fontsize=12)
    plt.legend()
    plt.xlabel('Get Requests (Millions)', fontsize=12)
    
    plt.grid()


def plot_counter_nocounters2(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(str)

    get_request = data[:,0]
    counters = data[:,1] 
    no_counters = data[:,2]
    
    len_counters = chop_array(counters)
    len_no_counters = chop_array(no_counters)

    counters = get_request[0:len_counters - 1].astype(float) / counters[0:len_counters - 1].astype(float)
    no_counters = get_request[0:len_no_counters - 1].astype(float) / no_counters[0:len_no_counters - 1].astype(float)
     


#    print ((counters))
    print ((no_counters))
    counters_color = "#2c7fb8"
    no_counters_color = "#e7298a"
    
    plt.plot(get_request[0:len_counters - 1].astype(int), counters[0:len_counters - 1].astype(float), label='Idealized', color= counters_color)
    plt.plot(get_request[0:len_no_counters - 1].astype(int), no_counters[0:len_no_counters - 1].astype(float), label='Actual', color= no_counters_color)
    plt.ylabel('Avg. get requests per extracted key (Millions)', fontsize=12)
    plt.legend()
    plt.xlabel('Get Requests (Millions)', fontsize=12)
    
    plt.grid()







dir="data_response_time/"
plt.figure(1)
plot_counter_nocounters(dir+"counters_vs_real_attack_01-17_DB_10M_guesses.csv")
plt.savefig('fig/counters_nocounters.pdf')
plt.figure(2)
plot_counter_nocounters2(dir+"counters_vs_real_attack_01-17_DB_10M_guesses.csv")
plt.savefig('fig/counters_nocounters2.pdf')
plt.show()

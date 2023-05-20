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
            float(array[i])
        except:
            return i;
    return (len(array))    

def start_point(array):
    for i in range(len(array)):
         try: 
            int(array[i])
            return i
         except:
            continue
    return (len(array))    



def plot_hash(data_path1, data_path2):
    with open(data_path1, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request = []
        hash_keys = []
        for row in reader:
            get_request.append(row[0])
            hash_keys.append(row[1])

    with open(data_path2, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_real = []
        hash_keys_real = []
        for row in reader:
            get_request_real.append(row[0])
            hash_keys_real.append(row[1])


    get_request = np.array(get_request, dtype=float)
    hash_keys = np.array(hash_keys, dtype=float)

    get_request_real = np.array(get_request_real, dtype=float)
    hash_keys_real = np.array(hash_keys_real, dtype=float)

    hash_color = "#d95f0e"
    real_color = "#1b9e77"
    
    plt.plot(get_request.astype(float), hash_keys.astype(float), label='SuRF-Hash', color= hash_color)
    plt.plot(get_request_real.astype(float), hash_keys_real.astype(float), label='SuRF-Real', color= real_color)
    
    plt.grid()
    plt.ylim([0,120])
    plt.ylabel('Avg. get requests per extracted key (Millions)', fontsize=12)
    plt.xlabel('Get Request (Millions)', fontsize=12)
    plt.legend()
 





plt.figure(1)
plot_hash("data_hash.csv", "data_hash_real.csv")
plt.savefig('fig/hash_average_gets_per_hacked_key.pdf')
plt.show()
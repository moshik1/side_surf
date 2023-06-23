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

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


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



def plot_base(data_path1, data_path2):
    with open(data_path1, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_base = []
        full_base_keys = []
        for row in reader:
            get_request_base.append(row[0])
            full_base_keys.append(row[1])

    with open(data_path2, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_real = []
        full_keys_real = []
        for row in reader:
            get_request_real.append(row[0])
            full_keys_real.append(row[1])



    get_request_base = np.array(get_request_base, dtype=float)
    full_base_keys = np.array(full_base_keys, dtype=float)

    base_keys = get_request_base / full_base_keys     



    get_request_real = np.array(get_request_real, dtype=float)
    full_keys_real = np.array(full_keys_real, dtype=float)

    keys_real = get_request_real / full_keys_real     





    base_color = "#FFA6C9"
    real_color = "#4169E1"
    
    plt.plot(get_request_base.astype(float)/1000, base_keys.astype(float), label='SuRF-Base', color= base_color)
    plt.plot(get_request_real.astype(float)/1000, keys_real.astype(float), label='SuRF-Real', color= real_color)
    
    plt.grid()
    plt.ylim([0,100])
    plt.xlim([0,4])
    plt.ylabel('Avg. Get Requests per Extracted Key (Millions)', fontsize=14)
    plt.xlabel('Get Requests (Billions)', fontsize=14)
    plt.legend(fontsize=14)
    plt.yticks(fontsize=12)  # Adjust the font size as per your preference
    plt.xticks(fontsize=12)  # Adjust the font size as per your preference
 





plt.figure(1)
plot_base("data_response_time/50M_base_25-40_DB_1_10000000_guesses.txt", "data_response_time/50M_real_25-40_DB_1_10000000_guesses.txt")
plt.savefig('fig/base_real_average_gets_per_hacked_key.pdf')
plt.show()

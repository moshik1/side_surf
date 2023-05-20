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



def plot_(data_path1, data_path2):
    with open(data_path1, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request = []
        _keys = []
        for row in reader:
            get_request.append(row[0])
            _keys.append(row[1])

    with open(data_path2, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_real = []
        _keys_real = []
        for row in reader:
            get_request_real.append(row[0])
            _keys_real.append(row[1])


    get_request = np.array(get_request, dtype=float)
    _keys = np.array(base_keys, dtype=float)

    get_request_real = np.array(get_request_real, dtype=float)
    _keys_real = np.array(base_keys_real, dtype=float)

    _color = "#d95f0e"
    real_color = "#1b9e77"
    
    plt.plot(get_request.astype(float), _keys.astype(float), label='SuRF_base', color= base_color)
    plt.plot(get_request_real.astype(float), _keys_real.astype(float), label='SuRF_real', color= real_color)
    
    plt.grid()
    plt.ylim([0,120])
    plt.ylabel('Avg. get requests per hacked key (Millions)', fontsize=12)
    plt.xlabel('Get Request (Millions)', fontsize=12)
    plt.legend()
 





plt.figure(1)
plot_base("data_base.csv", "data_base_real.csv")
plt.savefig('fig/_average_gets_per_hacked_key.pdf')
plt.show()

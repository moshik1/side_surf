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



def plot_counter_nocounters(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(str)

    get_request = data[:,0]
    D_17_24 = data[:,1] 
    D_1_16 = data[:,2]
    D_25_40 = data[:,3]

    start_D_17_24 = start_point(D_17_24)
    start_D_1_16 = start_point(D_17_24)
    start_D_25_40 = start_point(D_17_24)

    len_D_17_24 = chop_array(D_17_24[start_D_17_24:])
    len_D_1_16 = chop_array(D_1_16[start_D_1_16:])
    len_D_25_40 = chop_array(D_25_40[start_D_25_40:])

    print(len_D_17_24)
    print(len_D_1_16)
    print(len_D_25_40)


    D_17_24_color = "#d95f0e"
    D_1_16_color = "#7570b3"
    D_25_40_color = "#1b9e77"
    
    plt.plot(get_request[start_D_17_24:start_D_17_24 + len_D_17_24 - 1].astype(float), D_17_24[start_D_17_24:start_D_17_24 + len_D_17_24 - 1].astype(float), label='Data set 1', color= D_17_24_color)
    plt.plot(get_request[start_D_1_16:start_D_1_16 + len_D_1_16 - 1].astype(float), D_1_16[start_D_1_16:start_D_1_16 + len_D_1_16 - 1].astype(float), label='Data set 2', color= D_1_16_color)
    plt.plot(get_request[start_D_25_40:start_D_25_40 + len_D_25_40 - 1].astype(float), D_25_40[start_D_25_40:start_D_25_40 + len_D_25_40 - 1].astype(float), label='Data set 3', color= D_25_40_color)
    plt.ylabel('Avg. get requests per extracted key (Millions)', fontsize=12)
    plt.legend()
    plt.xlabel('Get Requests (Millions)', fontsize=12)
    
    plt.grid()
    plt.ylim([0,60])






dir="data_response_time/"
plt.figure(1)
plot_counter_nocounters(dir+"gets_per_keys.csv")
plt.savefig('fig/average_gets_per_hacked_key.pdf')
plt.show()

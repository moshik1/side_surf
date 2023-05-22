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


def plot_response_time1(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(str)

    get_request = data[:,0]
    db_10m = data[:,1] 
    db_20m = data[:,2]
    db_30m = data[:,3]
    db_40m = data[:,4]
    db_50m = data[:,5]

    len_db_10m = chop_array(db_10m)
    len_db_20m = chop_array(db_20m)
    len_db_30m = chop_array(db_30m)
    len_db_40m = chop_array(db_40m)
    len_db_50m = chop_array(db_50m)

    db_10m_color = "#f46d43"
    db_20m_color = "#4575b4"
    db_30m_color = "#d73027"
    db_40m_color = "#313695"
    db_50m_color = "#d73027"
    
    plt.plot(get_request[0:len_db_10m - 1].astype(float), db_10m[0:len_db_10m - 1].astype(int), label='Data size 10M', color= db_10m_color)
    plt.plot(get_request[0:len_db_20m - 1].astype(float), db_20m[0:len_db_20m - 1].astype(int), label='Data size 20M', color= db_20m_color)
    plt.plot(get_request[0:len_db_30m - 1].astype(float), db_30m[0:len_db_30m - 1].astype(int), label='Data size 30M', color= db_30m_color)
    plt.plot(get_request[0:len_db_40m - 1].astype(float), db_40m[0:len_db_40m - 1].astype(int), label='Data size 40M', color= db_40m_color)
    plt.plot(get_request[0:len_db_50m - 1].astype(float), db_50m[0:len_db_50m - 1].astype(int), label='Data size 50M', color= db_50m_color)
    plt.ylabel('# Extracted keys', fontsize=12)
    plt.legend()
    plt.xlabel('Get Requests (Millions)', fontsize=12)
    
    plt.grid()






dir="data_response_time/"
plt.figure(1)
plot_response_time1(dir+"hacked_keys.csv")
plt.savefig('fig/hacked_keys.pdf')
plt.show()

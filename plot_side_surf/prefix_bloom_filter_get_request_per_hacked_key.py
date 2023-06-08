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


factor = 1000*1000
bloom18 = True
bloom10 = False
also_whole_key_false = False

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



def plot_base(data_path1, data_path2, data_path3, data_path4):
    with open(data_path1, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_bloom18_whole_false = []
        bloom18_whole_false_keys = []
        for row in reader:
            get_request_bloom18_whole_false.append(row[0])
            bloom18_whole_false_keys.append(row[1])

    get_request_bloom18_whole_false = np.array(get_request_bloom18_whole_false, dtype=float)
    get_request_bloom18_whole_false = get_request_bloom18_whole_false/factor
    bloom18_whole_false_keys = np.array(bloom18_whole_false_keys, dtype=float)
    bloom18_whole_false_avg = get_request_bloom18_whole_false / bloom18_whole_false_keys     


    with open(data_path2, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_bloom18_whole_true = []
        bloom18_whole_true_keys = []
        for row in reader:
            get_request_bloom18_whole_true.append(row[0])
            bloom18_whole_true_keys.append(row[1])

    get_request_bloom18_whole_true = np.array(get_request_bloom18_whole_true, dtype=float)
    get_request_bloom18_whole_true = get_request_bloom18_whole_true/factor
    bloom18_whole_true_keys = np.array(bloom18_whole_true_keys, dtype=float)
    bloom18_whole_true_avg = get_request_bloom18_whole_true / bloom18_whole_true_keys     


    with open(data_path3, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_bloom10_whole_false = []
        bloom10_whole_false_keys = []
        for row in reader:
            get_request_bloom10_whole_false.append(row[0])
            bloom10_whole_false_keys.append(row[1])

    get_request_bloom10_whole_false = np.array(get_request_bloom10_whole_false, dtype=float)
    get_request_bloom10_whole_false = get_request_bloom10_whole_false/factor
    bloom10_whole_false_keys = np.array(bloom10_whole_false_keys, dtype=float)
    bloom10_whole_false_avg = get_request_bloom10_whole_false / bloom10_whole_false_keys     


    with open(data_path4, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        get_request_bloom10_whole_true = []
        bloom10_whole_true_keys = []
        for row in reader:
            get_request_bloom10_whole_true.append(row[0])
            bloom10_whole_true_keys.append(row[1])

    get_request_bloom10_whole_true = np.array(get_request_bloom10_whole_true, dtype=float)
    get_request_bloom10_whole_true = get_request_bloom10_whole_true/factor
    bloom10_whole_true_keys = np.array(bloom10_whole_true_keys, dtype=float)
    bloom10_whole_true_avg = get_request_bloom10_whole_true / bloom10_whole_true_keys     

    bloom18_whole_false_color = "#d73027"
    bloom18_whole_true_color = "#FF4500"
    bloom10_whole_false_color = "#2c7fb8"
    bloom10_whole_true_color = "#e7298a"
    
    if(bloom18 is True):
        if (also_whole_key_false is True):
            plt.plot(get_request_bloom18_whole_false.astype(float)/1000, bloom18_whole_false_avg.astype(float), label='Whole_key_filtering Disabled', color= bloom18_whole_false_color)
            plt.plot(get_request_bloom18_whole_true.astype(float)/1000, bloom18_whole_true_avg.astype(float), label='Whole_key_filtering Enabled', color= bloom18_whole_true_color)
        else:
            plt.plot(get_request_bloom18_whole_true.astype(float)/1000, bloom18_whole_true_avg.astype(float), color= bloom18_whole_true_color)

    
    if(bloom10 is True):
        plt.plot(get_request_bloom10_whole_false.astype(float)/1000, bloom10_whole_false_avg.astype(float), label='bloom_10bits_prefix_5bytes_whole_key_false', color= bloom10_whole_false_color)
        if (also_whole_key_false is True):
            plt.plot(get_request_bloom10_whole_true.astype(float)/1000, bloom10_whole_true_avg.astype(float), label='bloom_10bits_prefix_5bytes_whole_key_true', color= bloom10_whole_true_color)

    plt.grid()
    if (bloom10 is True):
        plt.ylim([0,160])
        plt.xlim([0,7.5])
    else: 
        plt.ylim([0,500])
        plt.xlim([0,7.5])
    plt.ylabel('Avg. Get Requests per Extracted Key (Billions)', fontsize=14)
    plt.xlabel('Get Requests (Billions)', fontsize=14)
    if (also_whole_key_false is True):
        plt.legend(fontsize=14)
    plt.yticks(fontsize=12)  # Adjust the font size as per your preference
    plt.xticks(fontsize=12)  # Adjust the font size as per your preference
 

plt.figure(1)
plot_base("data_prefix_bloom_filter/attack_64b_25_40_bloom18_prefix5_whole_filter_false_d50M_q1M.csv","data_prefix_bloom_filter/attack_64b_25_40_bloom18_prefix5_whole_filter_true_d50M_q1M.csv", "data_prefix_bloom_filter/prefix_attack_62_data1M_q1M_bloom_10bits_prefix5_whole_key_false.csv", "data_prefix_bloom_filter/prefix_attack_62_data1M_q1M_bloom_10bits_prefix5_whole_key_true.csv")
if (also_whole_key_false is True):
    plt.savefig('fig/bloom_prefix_average_gets_per_hacked_key.pdf')
else:    
    plt.savefig('fig/bloom_prefix_average_gets_per_hacked_key_only_whole_filter_true.pdf')
plt.show()

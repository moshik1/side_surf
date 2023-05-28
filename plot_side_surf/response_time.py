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

def plot_response_time1(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(float)

    start_step = 4 # we skip the 4 first items from [0:3]    
    end_step = 70 # The end step     
    steps = data[start_step:end_step,1]
    keys = data[start_step:end_step,2] 
    fp_precent = data[start_step:end_step,3]
    fp_keys = data[start_step:end_step,4]
    
    print (steps)
    fp_precent_color = "#5aae61"
    fp_keys_color = "#1b7837"
    keys_color = "#762a83"
#    seq_color = "#756bb1"
    x = steps

    a = plt.plot(x*1000, keys, label='Total #Keys', marker="o", color= keys_color)
    plt.plot(x*1000, fp_keys, label='# FP Keys', marker="o", color= fp_keys_color)
    plt.ylabel('# Keys', fontsize=22)
    plt.legend(loc=2, fontsize=18)
    plt.ylim([0, 350])
    plt.xlim([25, 350])
    plt.xlabel('Response Time (Microseconds)', fontsize=22)
    plt.yticks(fontsize=20)  # Adjust the font size as per your preference
    plt.xticks(fontsize=18)  # Adjust the font size as per your preference
    plt.xticks(np.arange(25, 350, 50))
    plt2 = plt.twinx()
    plt.yticks(fontsize=20)  # Adjust the font size as per your preference
    plt2.scatter(x*1000, fp_precent, label='% FP-keys', marker="o", color= fp_precent_color)
    plt.legend(loc=1, fontsize=18)
#    plt2.set_ylabel('% Percentage', fontsize=16)
    plt2.set_ylim([0, 119])
    plt.grid()


def plot_response_time2(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader)).astype(float)

    start_step = 0 # start from zero step    
    end_step = 70 # The end step     
    total_keys = 500000

    steps = data[start_step:end_step,1]
    keys = data[start_step:end_step,2] 
    fp_keys = data[start_step:end_step,4]
    keys_precent = keys/ total_keys * 100

    print (steps)
    fp_precent_color = "#d95f0e"
    fp_keys_color = "#1b7837"
    keys_color = "#2c7fb8"
    precent_keys_color = "#40004b"
    x = steps

    
    plt.ylabel('% Percentage', fontsize=22)
    plt.plot(x*1000, keys_precent, label = '% Keys Fall into a Bucket', marker="o", color= precent_keys_color)
    plt.plot(x*1000, fp_keys, label='% FP Keys Fall into a Bucket', marker="o", color= fp_keys_color)
    plt.legend(loc=1, fontsize=18)

    plt.ylim([0, 119])
    plt.xlim([0, 350])
    plt.xlabel('Response Time (Microseconds)', fontsize=22)
    plt.yticks(fontsize=20)  # Adjust the font size as per your preference
    plt.xticks(fontsize=18)  # Adjust the font size as per your preference


    plt.grid()





dir="data_response_time/"
plt.figure(1)
plot_response_time1(dir+"response_time_50M_sha_25-40_DB_0_500000_guesses_1.csv")
#plt.savefig('fig/response_time1.pdf', format='pdf', bbox_inches='tight', pad_inches=0.2)
plt.savefig('fig/response_time1.pdf', format='pdf', bbox_inches='tight')
plt.figure(2)
plot_response_time2(dir+"response_time_50M_sha_25-40_DB_0_500000_guesses_1.csv")
plt.savefig('fig/response_time2.pdf', format='pdf', bbox_inches='tight')
plt.show()

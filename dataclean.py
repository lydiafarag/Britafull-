import numpy as np
import time



#https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
def reject_outliers(data, m = 3):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

def list_avg(int_arr): #gets average of cleaned list
    return np.average(int_arr)

def get_weight(ser_ial): #takes 5 seconds to collect semiaccurate weight
    weight_arr = [] #used to hold weight collected
    new_weight = 0
    start = time.time()
    end = time.time()
    while abs(end-start) < 5: #5 seconds to collect information
        weight_str = ser_ial.readline().decode('utf-8').rstrip()
        #getting weight from arduino serial
        if (weight_str != ''): #ensuring we don't break things :p
            new_weight = int(weight_str)
            weight_arr.append(new_weight)
        end = time.time()
    weight_arr = np.array(weight_arr) #converting python list to numpy list
    cleaned = reject_outliers(weight_arr)
    cleaned = cleaned.astype(int) #converting values to ints
    acc_weight = list_avg(cleaned)
    #print(acc_weight)
    return acc_weight
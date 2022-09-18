#!/usr/bin/env python3
import serial
import pygame
import time
import numpy as np

#importing functions
from notification import sendNotification
from sound import sound
from dataclean import reject_outliers, list_avg

pygame.mixer.init() #music <3

count = 0
alarm_sounded = False
count_til_text = 0 #??


#default values - unit: analog values from 330ohm resistor w FSR (?)
CONTAINER = 50
MIN_WATER = 150
THRESHOLD = CONTAINER + MIN_WATER
WAIT_TIME = 10 #seconds given to refill the brita
ALLOWED_DIFF = 50 #amount of water allowed to be removed without retribution

#variable values
weight = [300, 300] #current, previous weight
now_weight, pre_weight = weight #how much water in the brita, subject to change
weight_diff = now_weight - pre_weight #pos = filled, neg=emptied

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:

        #CHECKING INFORMATION
        print(get_weight())
    """
        try:
            #brita is lifted (NOT HERE and PREVIOUSLY PRESENT)
            if now_weight <= 5 and pre_weight >= CONTAINER:
                print("brita is LIFTED")
            #brita is placed down (HERE and PREVIOUSLY NOT PRESENT)
            elif now_weight >= CONTAINER and pre_weight <= 5:
                print("brita is PLACED DOWN")
                if abs(weight_diff) <= 50 and now_weight >= THRESHOLD: #minimal-to-no-change
                    print("brita is the same")
                elif weight_diff < -50: #removed water
                    print("brita emptied, not refilled")
                    print("you have", WAIT_TIME, "seconds to refill brita")
                    time.sleep(WAIT_TIME)
                    #check weight again
                elif weight_diff > 50: #filled water
                    print("brita filled")
                else: #doesn't meet the threshold
                    print("brita is empty")
        except ValueError:
            pass
    """        

def get_weight(weight_str): #takes 5 seconds to collect semiaccurate weight
    weight_arr = np.array([]) #used to hold weight collected, has to be numpy array
    new_weight = 0
    start = time.time()
    end = time.time()
    while abs(end-start) < 5: #5 seconds to collect information
        weight_str = ser.readline().decode('utf-8').rstrip()
        #getting weight from arduino serial
        if (weight_str != ''): #ensuring we don't break things :p
            new_weight = int(weight_str)
            np.append(weight_arr, new_weight)
        end = time.time()
    #clean the information
    cleaned = reject_outliers(weight_arr)
    acc_weight = list_avg(cleaned)
    return acc_weight

#high -> low = emptied
#low -> high = filled
#same = same
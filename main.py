#!/usr/bin/env python3
import serial
import pygame
import time
<<<<<<< HEAD
import numpy as np

#importing functions
from notification import sendNotification
from sound import sound
from dataclean import reject_outliers, list_avg, get_weight

pygame.mixer.init() #music <3

count = 0
alarm_sounded = False
count_til_text = 0 #??


#default values - unit: analog values from 330ohm resistor w FSR (?)
NOTHING = 50
CONTAINER = 100
MIN_WATER = 200
THRESHOLD = CONTAINER + MIN_WATER
WAIT_TIME = 10 #seconds given to refill the brita
ALLOWED_DIFF = 50 #amount of water allowed to be removed without retribution

#variable values
weight = [300, 300] #current, previous weight
now_weight, pre_weight = weight #how much water in the brita, subject to change
weight_diff = now_weight - pre_weight #pos = filled, neg=emptied
=======
from notification import sendNotification
from sound import sound

pygame.mixer.init()
container = 50
min_water = 150
threshold = container + min_water
wait_time = 10
weight = 300
count = 0
alarm_sounded = False
count_til_text = 0
>>>>>>> d3927b2b0f2613f4651794c3df2ee14a7e47b6e5

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
<<<<<<< HEAD

    while True:
        #CHECKING INFORMATION
        get_weight(ser)

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



=======
    while True:
        weight_str = ser.readline().decode('utf-8').rstrip()
        if (weight_str != ''):
            weight = int(weight_str)
        
        print(weight)

        try:
            time.sleep(1)

            if weight > threshold:
                count = 0
                count_til_text = 0
                alarm_sounded = false
            
            # empty britas
            if (weight < threshold and weight > 5):
                count += 1
                if alarm_sounded:
                    count_til_text += 1
            
            if count == 10:
                sound()
                count = 0
                count_til_text += 1

            if count_til_text == 10:
                sendNotification()
                count_til_text = 0
        except ValueError:
            pass
        
>>>>>>> d3927b2b0f2613f4651794c3df2ee14a7e47b6e5
#high -> low = emptied
#low -> high = filled
#same = same
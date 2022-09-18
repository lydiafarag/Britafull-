#!/usr/bin/env python3
import serial
import pygame
import time
import numpy as np

#importing functions
from notification import sendNotification
from sound import refill_message
from dataclean import reject_outliers, list_avg, get_weight

pygame.mixer.init() #music <3
#default values - unit: analog values from 330ohm resistor w FSR (?)
NOTHING = 70
CONTAINER = 100
MIN_WATER = 100
THRESHOLD = CONTAINER + MIN_WATER
WAIT_TIME = 30 #seconds given to refill the brita
ALLOWED_DIFF = 50 #amount of water allowed to be removed without retribution

#variable values
weight = [300, 300] #current, previous weight
now_weight, pre_weight = weight[0], weight[1] #how much water in the brita, subject to change
#weight_diff = now_weight - pre_weight #pos = filled, neg=emptied
prev_crit_weight = THRESHOLD
trigger_check = False

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        #CHECKING INFORMATION
        temp_weight = get_weight(ser)
        print(temp_weight)
        try:
            #need to check if water was REFILLED
            if trigger_check and (temp_weight - prev_crit_weight) < -ALLOWED_DIFF: #water was removed
                print("just tattled")
                #sendNotification()
                trigger_check = False
            #no trigger check or water was refilled
            #brita is lifted (NOT HERE and PREVIOUSLY PRESENT)
            elif temp_weight <= NOTHING and pre_weight >= CONTAINER:
                print("brita is LIFTED")
                prev_crit_weight = pre_weight #reference for when it is placed down

            #brita is placed down (HERE and PREVIOUSLY NOT PRESENT)
            elif temp_weight >= THRESHOLD:
                weight_diff = temp_weight - prev_crit_weight #referencing most relevant past value
                print("brita is PLACED DOWN")
                if abs(weight_diff) <= NOTHING: #minimal-to-no-change
                    print("and weighs the same")
                elif weight_diff < -ALLOWED_DIFF: #removed water
                    print("brita emptied, not refilled")
                    print("you have", WAIT_TIME, "seconds to refill brita")
                    refill_message() #plays the audio
                    time.sleep(WAIT_TIME - 5)
                    #if they don't refill it, text message will be sent
                    trigger_check = True
                    #have to check against pre_weight to check

                elif weight_diff > ALLOWED_DIFF: #filled water
                    print("brita has been filled")
                elif temp_weight <= THRESHOLD: #doesn't meet the threshold
                    print("brita is empty")

            #updating the values
            pre_weight = now_weight
            now_weight = temp_weight
        except ValueError:
            pass
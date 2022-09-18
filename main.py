#!/usr/bin/env python3
import serial
import pygame
import time
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

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
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
        
#high -> low = emptied
#low -> high = filled
#same = same
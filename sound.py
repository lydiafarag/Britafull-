import pygame
import time

def sound():
    pygame.mixer.music.load("mp3_files/refill_fuckin_brita_salli.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        time.sleep(3)
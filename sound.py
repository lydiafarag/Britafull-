import pygame

def refill_message():
    pygame.mixer.music.load("mp3_files/refill_brita_salli.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
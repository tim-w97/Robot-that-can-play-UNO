import pygame

pygame.init()
pygame.mixer.init()

def speak(path_to_mp3):
    pygame.mixer.music.load(path_to_mp3)
    pygame.mixer.music.play()
    pygame.event.wait()
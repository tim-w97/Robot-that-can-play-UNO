import pygame

mixer = pygame.mixer

def speak(path_to_mp3):
    mixer.init()
    speech = mixer.Sound(path_to_mp3)
    channel = speech.play()

    while channel.get_busy():
        pygame.time.wait(100)

# Create a Python program that opens and plays an MP3 audio file.
import pygame

pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

pygame.event.wait()

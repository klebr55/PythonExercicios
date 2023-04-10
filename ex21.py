import pygame

pygame.init()
pygame.mixer.music.load('rick.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print("YOU'VE BEEN RICK ROLLED")

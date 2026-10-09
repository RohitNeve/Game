import pygame

screen = pygame.display.set_mode((800, 600))

while pygame.QUIT not in [e.type for e in pygame.event.get()]:
    pygame.display.update()

pygame.quit()
import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Textured Triangle")
texture = pygame.image.load("player.png")
texture = pygame.transform.scale(texture, (300, 250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(texture, (250, 150))
    points = [(400, 150), (250, 400), (550, 400)]
    pygame.draw.polygon(screen, (255, 255, 255), points, 3)
    pygame.display.update()
pygame.quit()
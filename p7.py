import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Model Loading and Rendering")
clock = pygame.time.Clock()
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (100, 100))
x, y = 350, 250
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    screen.fill((30, 30, 30))
    screen.blit(player, (x, y))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
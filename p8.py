import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D UFO Catching Game")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
player = pygame.Rect(375, 500, 50, 50)
ufo = pygame.Rect(random.randint(50, 750), random.randint(50, 450), 40, 40)
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    if player.colliderect(ufo):
        score += 1
        ufo.topleft = random.randint(50, 750), random.randint(50, 450)
    screen.fill((0, 0, 20))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 255), ufo)
    screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 10))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
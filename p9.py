import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Roll-Ball Game")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
ball = pygame.Rect(380, 280, 40, 40)
items = [pygame.Rect(random.randint(50, 750), random.randint(50, 550), 20, 20) for _ in range(10)]
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    ball.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    ball.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    screen.fill((20, 20, 40))
    pygame.draw.ellipse(screen, (0, 255, 0), ball)
    for item in items[:]:
        pygame.draw.rect(screen, (255, 255, 0), item)
        if ball.colliderect(item):
            items.remove(item)
            score += 1
    screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 10))
    if not items:
        screen.blit(font.render("YOU WIN!", True, (0, 255, 0)), (320, 280))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
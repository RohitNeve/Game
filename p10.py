import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter Game")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
def new_enemy(y):
    return pygame.Rect(random.randint(50, 750), y, 40, 40)
player = pygame.Rect(375, 520, 50, 50)
bullets = []
enemies = [new_enemy(random.randint(20, 150)) for _ in range(5)]
score = 0
game_over = False
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(player.x + 22, player.y, 6, 15))
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 6
    player.clamp_ip(screen.get_rect())
    if not game_over:
        bullets = [b.move(0, -8) for b in bullets if b.y >= 8]
        for e in enemies:
            e.y += 2
        game_over = any(e.y > 600 for e in enemies)
        for b in bullets[:]:
            i = b.collidelist(enemies)
            if i != -1:
                bullets.remove(b)
                enemies[i] = new_enemy(0)
                score += 1
    screen.fill((0, 0, 30))
    pygame.draw.polygon(screen, (0, 255, 0), [player.midtop, player.bottomleft, player.bottomright])
    for b in bullets:
        pygame.draw.rect(screen, (255, 255, 0), b)
    for e in enemies:
        pygame.draw.rect(screen, (255, 0, 0), e)
    screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 10))
    if game_over:
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (300, 280))
    pygame.display.update()
pygame.quit()
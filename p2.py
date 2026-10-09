import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Window Framework")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 30))
    fps = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
    screen.blit(fps, (10, 10))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
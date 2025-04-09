import pygame
import sys

# Initialise pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Protect Princess Kotone")

# Colours
WHITE = (255, 255, 255)
DARK_GREY = (50, 50, 50)
RED = (255, 105, 180)

# Tower settings
TOWER_RADIUS = 50
TOWER_POS = (WIDTH // 2, HEIGHT // 2)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    WIN.fill(WHITE)

    # Draw central tower
    pygame.draw.circle(WIN, RED, TOWER_POS, TOWER_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()

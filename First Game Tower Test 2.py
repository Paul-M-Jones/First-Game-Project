import pygame
import sys
import random
import math

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
BLUE = (0, 0, 250)

# Tower settings
TOWER_RADIUS = 40
TOWER_POS = (WIDTH // 2, HEIGHT // 2)

# Enemy settings
ENEMY_RADIUS = 10
ENEMY_SPEED = 1.5

# Clock
clock = pygame.time.Clock()

# Enemy list
enemies = []

def spawn_enemy():
    # Choose a random edge
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top':
        x = random.randint(0, WIDTH)
        y = 0
    elif edge == 'bottom':
        x = random.randint(0, WIDTH)
        y = HEIGHT
    elif edge == 'left':
        x = 0
        y = random.randint(0, HEIGHT)
    else:
        x = WIDTH
        y = random.randint(0, HEIGHT)
    return {'x': x, 'y': y}

def move_enemy(enemy):
    dx = TOWER_POS[0] - enemy['x']
    dy = TOWER_POS[1] - enemy['y']
    dist = math.hypot(dx, dy)
    if dist != 0:
        dx, dy = dx / dist, dy / dist
        enemy['x'] += dx * ENEMY_SPEED
        enemy['y'] += dy * ENEMY_SPEED

def is_touching_tower(enemy):
    dist = math.hypot(enemy['x'] - TOWER_POS[0], enemy['y'] - TOWER_POS[1])
    return dist <= TOWER_RADIUS + ENEMY_RADIUS

# Game loop
running = True
spawn_timer = 0

while running:
    clock.tick(60)
    WIN.fill(WHITE)

    # Draw tower
    pygame.draw.circle(WIN, RED, TOWER_POS, TOWER_RADIUS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn enemies every 1.5 seconds
    spawn_timer += 1
    if spawn_timer >= 90:  # 60 frames per second = 1.5 seconds
        enemies.append(spawn_enemy())
        spawn_timer = 0

    # Move and draw enemies
    for enemy in enemies[:]:
        move_enemy(enemy)
        if is_touching_tower(enemy):
            enemies.remove(enemy)
            continue
        pygame.draw.circle(WIN, DARK_GREY, (int(enemy['x']), int(enemy['y'])), ENEMY_RADIUS)

    pygame.display.update()

pygame.quit()
sys.exit()

import pygame
import math

# Setup
pygame.init()
WIN = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Cat Tower Head")
RED = (255, 0, 0)
WHITE = (255, 255, 255)
TOWER_POS = (200, 200)
TOWER_RADIUS = 60

def draw_cat_head(surface):
    # Draw face
    pygame.draw.circle(surface, RED, TOWER_POS, TOWER_RADIUS)

    # Ear settings
    ear_length = 50           # distance from base to tip
    ear_base_width = 55       # width of the ear base
    ear_inset = 10            # how far the base is inset into the head

    # Angles for each ear (in radians)
    left_angle = math.radians(135)
    right_angle = math.radians(45)

    for angle in [left_angle, right_angle]:
        # Base centre: inset into the circle slightly
        base_centre = (
            TOWER_POS[0] + (TOWER_RADIUS - ear_inset) * math.cos(angle),
            TOWER_POS[1] - (TOWER_RADIUS - ear_inset) * math.sin(angle)
        )

        # Perpendicular angle for ear width
        perp_angle = angle + math.pi / 2

        # Base corners
        base_left = (
            base_centre[0] - (ear_base_width / 2) * math.cos(perp_angle),
            base_centre[1] + (ear_base_width / 2) * math.sin(perp_angle)
        )
        base_right = (
            base_centre[0] + (ear_base_width / 2) * math.cos(perp_angle),
            base_centre[1] - (ear_base_width / 2) * math.sin(perp_angle)
        )

        # Tip of the ear
        tip = (
            base_centre[0] + ear_length * math.cos(angle),
            base_centre[1] - ear_length * math.sin(angle)
        )

        # Draw the ear
        pygame.draw.polygon(surface, RED, [base_left, tip, base_right])

# Main loop
running = True
while running:
    WIN.fill(WHITE)
    draw_cat_head(WIN)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Dino settings
dino = pygame.Rect(50, 300, 50, 50)
gravity = 0.6
jump_speed = -12
dino_velocity = 0
is_jumping = False

# Obstacle settings
obstacles = []
obstacle_timer = 0

def draw_dino():
    pygame.draw.rect(screen, BLACK, dino)

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)

def update_obstacles():
    for obs in obstacles:
        obs.x -= 5
    obstacles[:] = [obs for obs in obstacles if obs.x > -50]

def check_collision():
    for obs in obstacles:
        if dino.colliderect(obs):
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        dino_velocity = jump_speed
        is_jumping = True

    # Dino physics
    dino_velocity += gravity
    dino.y += dino_velocity
    if dino.y >= 300:
        dino.y = 300
        is_jumping = False

    # Obstacle generation
    obstacle_timer += 1
    if obstacle_timer > 90:
        obstacle_timer = 0
        obstacles.append(pygame.Rect(SCREEN_WIDTH, 300, 20, 50))

    update_obstacles()
    draw_dino()
    draw_obstacles()

    if check_collision():
        text = font.render("Game Over!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
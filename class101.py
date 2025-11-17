import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
start_tiny_loop = False
tiny_loop_start_time = 0
tiny_loop_duration = 2000  # milliseconds (2 seconds)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger the tiny loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_tiny_loop = True
            tiny_loop_start_time = pygame.time.get_ticks()

    # Main game logic here...

    # Run tiny loop for a specific duration
    if start_tiny_loop:
        current_time = pygame.time.get_ticks()
        if current_time - tiny_loop_start_time < tiny_loop_duration:
            # This is your "tiny loop"
            print("Tiny loop running...")
            # You can do animations, spawn effects, etc.
        else:
            start_tiny_loop = False  # Stop the tiny loop

    pygame.display.flip()
    clock.tick(60)
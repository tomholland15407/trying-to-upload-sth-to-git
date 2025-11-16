import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Catcher")

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

# Game variables
nest_width, nest_height = 100, 30
egg_radius = 20
nest_speed = 10
initial_egg_speed = 5
egg_speed_increment = 2
difficulty_milestones = [5, 10, 20]

clock = pygame.time.Clock()

def draw_nest(x, y):
    pygame.draw.rect(screen, BROWN, (x, y, nest_width, nest_height))

def draw_egg(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), egg_radius)

def show_score(score, high_score):
    text = font.render(f"Score: {score}", True, WHITE)
    high_text = small_font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(text, (10, 10))
    screen.blit(high_text, (10, 60))

def game_loop(high_score):
    nest_x = WIDTH // 2 - nest_width // 2
    nest_y = HEIGHT - 60

    egg_x = random.randint(egg_radius, WIDTH - egg_radius)
    egg_y = 0
    egg_speed = initial_egg_speed

    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key press handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nest_x > 0:
            nest_x -= nest_speed
        if keys[pygame.K_RIGHT] and nest_x < WIDTH - nest_width:
            nest_x += nest_speed

        # Move egg
        egg_y += egg_speed

        # Check for catch
        if nest_y < egg_y + egg_radius < nest_y + nest_height:
            if nest_x < egg_x < nest_x + nest_width:
                score += 1
                egg_x = random.randint(egg_radius, WIDTH - egg_radius)
                egg_y = 0

                # Increase difficulty
                if score in difficulty_milestones:
                    egg_speed += egg_speed_increment

        # Check for miss
        if egg_y > HEIGHT:
            running = False

        draw_nest(nest_x, nest_y)
        draw_egg(egg_x, egg_y)
        show_score(score, high_score)

        pygame.display.flip()
        clock.tick(60)

    return score

def show_game_over(score, high_score):
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    high_score_text = small_font.render(f"High Score: {high_score}", True, WHITE)
    retry_text = small_font.render("Press ENTER to play again or ESC to quit", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 60))
    screen.blit(high_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
    screen.blit(retry_text, (WIDTH // 2 - 220, HEIGHT // 2 + 60))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Main loop
high_score = 0
while True:
    score = game_loop(high_score)
    if score > high_score:
        high_score = score
    show_game_over(score, high_score)
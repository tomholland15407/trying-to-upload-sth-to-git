import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))
pygame.display.set_caption("Nokia Snake 🐍")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# Clock
clock = pygame.time.Clock()
FPS = 20  # Increased for smoother input

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Food setup
def generate_food():
    while True:
        pos = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
               random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        if pos not in snake:
            return pos

food = generate_food()

# Game states
running = False
paused = False
game_over = False

# Button setup
font = pygame.font.SysFont(None, 24)
buttons = {
    "Start": pygame.Rect(10, HEIGHT + 10, 80, 40),
    "Pause": pygame.Rect(100, HEIGHT + 10, 80, 40),
    "Resume": pygame.Rect(190, HEIGHT + 10, 80, 40),
    "Stop": pygame.Rect(280, HEIGHT + 10, 80, 40),
}

def draw_buttons():
    for label, rect in buttons.items():
        pygame.draw.rect(screen, BLUE, rect)
        text = font.render(label, True, WHITE)
        screen.blit(text, (rect.x + 10, rect.y + 10))

def draw_snake():
    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else WHITE
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def reset_game():
    global snake, direction, food, running, paused, game_over
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL_SIZE, 0)
    food = generate_food()
    running = True
    paused = False
    game_over = False

# Main loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN and running and not paused:
            new_dir = direction
            if event.key == pygame.K_UP:
                new_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN:
                new_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT:
                new_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                new_dir = (CELL_SIZE, 0)

            if len(snake) < 2 or (new_dir[0] != -direction[0] or new_dir[1] != -direction[1]):
                direction = new_dir

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if buttons["Start"].collidepoint(mx, my):
                reset_game()
            elif buttons["Pause"].collidepoint(mx, my) and running:
                paused = True
            elif buttons["Resume"].collidepoint(mx, my) and running:
                paused = False
            elif buttons["Stop"].collidepoint(mx, my):
                running = False
                game_over = True

    if running and not paused and not game_over:
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx) % WIDTH, (head_y + dy) % HEIGHT)
        snake.insert(0, new_head)

        if new_head == food:
            food = generate_food()
        else:
            snake.pop()

        if new_head in snake[1:]:
            game_over = True

    if running:
        draw_snake()
        draw_food()

    if game_over:
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    draw_buttons()
    pygame.display.flip()
    clock.tick(FPS)
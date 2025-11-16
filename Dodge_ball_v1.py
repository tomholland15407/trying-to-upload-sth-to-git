import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge Ball')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (100, 100, 200)
YELLOW = (255, 255, 0)
BROWN = (55, 55, 55)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 40)
font1 = pygame.font.SysFont('Arial', 60)


def draw_ball(x, y):
    pygame.draw.circle(screen, BLACK, (x, y), 50)


def draw_car(x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, 30, 30))


def game_loop():
    by = 0
    bx = WIDTH / 2
    cx = 0
    cy = HEIGHT - 30
    plus = 2
    score = 0
    cplus = 5
    cminus = 30

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and cx > 0:
                cx -= cminus
            elif event.type == pygame.KEYDOWN and cx > 0 and event.key == pygame.K_SPACE:
                cx -= cminus

        if by < HEIGHT:
            by += plus

        else:
            by = 0
            bx = random.randint(100, WIDTH - 100)
        if cx < WIDTH:
            cx += cplus

        else:
            score += 10
            plus += 2
            cplus += 1
            cx = 0
            cminus += 10

        if abs(bx - (cx + 15)) < 55 and abs(by - (cy + 15)) < 55:
            running = False

        text = font.render(f'Total score: {score}', True, COLOR)

        screen.blit(text, (WIDTH/2 - text.get_width()/2, 50))

        pygame.draw.line(screen, BROWN, (0, HEIGHT-5), (WIDTH, HEIGHT-5), 10)
        draw_ball(bx, by)
        draw_car(cx, cy)
        pygame.display.flip()
        clock.tick(50)
    return score


def scoreboard(score):
    running1 = True
    while running1:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running1 = False

        text1 = font1.render(f'Your money: {score}$.', True, WHITE)
        text2 = font1.render(f'Click HERE to replay?', True, WHITE)

        screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/2 - text1.get_height()/2 - 50))
        screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text1.get_height()/2 + 50))
        pygame.display.flip()
        clock.tick(50)


while True:
    star = game_loop()
    scoreboard(star)

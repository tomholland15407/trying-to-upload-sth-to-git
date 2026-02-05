import pygame
import random
import time
import os
import copy

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

WIDTH, HEIGHT = 600, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge Ball')
start_loop = False
time_start = 0
time_last = 1500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (100, 100, 200)
BROWN = (55, 55, 55)
BLUE = (0, 0, 150)
GREY = (100, 100, 100)
RED = (150, 0, 0)
clock = pygame.time.Clock()

font0 = pygame.font.SysFont('Segoe UI Emoji', 30)
font = pygame.font.SysFont('Segoe UI Emoji', 20)
font1 = pygame.font.SysFont('Segoe UI Emoji', 50)

good = ['GOOD', 'AMAZING', 'BEAUTIFUL', 'FANTASTIC', 'WELL DONE', 'BRILLIANT', 'SO COOL', 'LOVELY', 'GOOD JOB',
        'EXCELLENT', 'SUPER', 'RIZZ', 'RIZZ MASTER', 'ULTIMATE RIZZ MASTER', '5 STARS', 'LET HIM COOK', 'BREEZE',
        'SWEET']


def generate_color():
    r = random.randint(100, 200)
    g = random.randint(100, 200)
    b = random.randint(100, 200)
    colors = [r, g, b]
    return colors


main_colors = generate_color()

compliment = ['hello']


def draw_ball(x, y):
    pygame.draw.circle(screen, main_colors, (x, y), 50)


def fibo(n, memo=None):
    if memo is None:
        memo = {0: 2, 1: 3}
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, 30, 30))


score_list = [0]


def game_loop():
    peak = max(score_list) * 10
    milestones = []
    for i in range(9):
        milestones.append(fibo(i))
    by = 0
    bx = WIDTH / 2
    cx = 0
    cy = HEIGHT - 30

    # --- CHANGED: Speeds scaled up for 60 FPS ---
    plus = 1.7  # Was 0.05
    cplus = 3.5  # Was 0.1
    cminus = 8.5  # Was 0.25
    # --------------------------------------------

    score = 0
    start_loop = False
    time_start = 0
    time_last = 5000
    time_start_2 = pygame.time.get_ticks()
    time_last_2 = 4100
    start_reverse = False
    tx = WIDTH
    running = True

    while running:
        screen.fill(WHITE)
        current_time_2 = pygame.time.get_ticks()
        if current_time_2 - time_start_2 < time_last_2:
            text3 = font.render('SPACE to dodge the ball', True, GREY)
            screen.blit(text3, (WIDTH / 2 - text3.get_width() / 2, HEIGHT / 2 - text3.get_height() / 2 - 20))
            text4 = font.render('Go full path to score', True, GREY)
            screen.blit(text4, (WIDTH / 2 - text4.get_width() / 2, HEIGHT / 2 - text3.get_height() / 2 + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_LEFT]) and cx > 0:
            cx -= cminus

        if by < HEIGHT:
            by += plus
        else:
            by = 0
            bx = random.randint(100, WIDTH - 100)
            main_colors[0] = random.randint(100, 200)
            main_colors[1] = random.randint(100, 200)
            main_colors[2] = random.randint(100, 200)

        if cx < WIDTH:
            cx += cplus
        else:
            score += 1
            cx = 0
            if score in milestones or (score - 15) % 20 == 0 and score > 90:
                # --- CHANGED: Increments scaled up ---
                plus += 2.0  # Was 0.06
                cplus += 1.0  # Was 0.03
                cminus += 1.5  # Was 0.05
                # -------------------------------------
            elif score % 10 == 0 and score > 0:
                start_reverse = True
                start_time = pygame.time.get_ticks()
                duration = 2000 + 250 * (score // 10 - 1)
                pace = copy.copy([plus])
            start_loop = True
            time_start = pygame.time.get_ticks()
            compliment[
                0] = '🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕' if score % 10 == 0 else \
            good[random.randint(0, len(good) - 1)]

        if start_reverse:
            lapsed_time = pygame.time.get_ticks()
            if lapsed_time - start_time < duration:
                # --- CHANGED: Reverse speed ---
                plus -= 0.007  # Was 0.0002
            else:
                # --- CHANGED: Restore speed ---
                plus = pace[0] + 0.7  # Was 0.02
                start_reverse = False
        if start_loop:
            current_time = pygame.time.get_ticks()
            if current_time - time_start < time_last:
                text2 = font.render(*compliment, True, BROWN)
                screen.blit(text2, (tx, 120))
                if (0 - text2.get_width()) < tx <= WIDTH:
                    # --- CHANGED: Text scroll speed ---
                    tx -= 3.5  # Was 0.1
                else:
                    tx = WIDTH
            else:
                start_loop = False

        if abs(bx - (cx + 15)) < 50 and abs(by - (cy + 15)) < 50:
            running = False
        highest_score = font.render(f'BREAK YOUR LIMITER: {peak}$', True, COLOR)
        screen.blit(highest_score, (WIDTH / 2 - highest_score.get_width() / 2, 35))
        text = font.render(f'Pizzas delivered: {score} 🍕', True, COLOR)
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 70))
        pygame.draw.line(screen, BLUE, (0, HEIGHT - 5), (WIDTH, HEIGHT - 5), 10)
        draw_ball(bx, by)
        draw_car(cx, cy)
        pygame.display.flip()

        # --- CHANGED: Standard FPS ---
        clock.tick(60)  # Was 2000
        # -----------------------------

    score_list.append(score)
    return score


def scoreboard(score):
    running1 = True
    if score >= max(score_list):
        with open('highest_score_ever.txt', 'w') as f:
            f.write(str(score))
    limit = score if score >= max(score_list) else max(score_list)
    score *= 10
    while running1:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running1 = False

        text1 = font1.render(f'You earned {score}$', True, WHITE)
        text2 = font.render(f'SPACE to play again', True, WHITE)
        text5 = font.render(f'YOUR LIMITER: {limit * 10}$', True, WHITE)

        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2, HEIGHT / 2 - text1.get_height() / 2 - 50))
        screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2, HEIGHT / 2 - text1.get_height() / 2 + 100))
        screen.blit(text5, (WIDTH / 2 - text5.get_width() / 2, HEIGHT / 2 - text1.get_height() / 2 + 50))
        pygame.display.flip()
        clock.tick(60)


story_line = ["Year 2125",
              "Climate change has ravaged the planet",
              "Toxic waste rains from the sky",
              "But humanity still craves one thing: pizza",
              "You are the last delivery driver",
              "Your mission: dodge the toxic balls",
              "and deliver hope",
              "... one slice at a time."]


class Line:
    def __init__(self, content, y=HEIGHT):
        self.y = y
        self.content = content

    def draw(self):
        text = font0.render(self.content, True, WHITE)
        screen.blit(text, ((WIDTH // 2 - text.get_width() // 2), self.y))
        # --- CHANGED: Story scroll speed ---
        self.y -= 2.5  # Was 0.1
        # -----------------------------------


lines = []


def story():
    running2 = True
    start = pygame.time.get_ticks()
    n = 0
    interval = 700
    next = start + interval
    while running2:
        screen.fill(BLACK)
        time_lapsed = pygame.time.get_ticks() - start
        if time_lapsed > 9000:
            running2 = False
        if pygame.time.get_ticks() > next and n < len(story_line):
            content = story_line[n]
            lines.append(Line(content))
            n += 1
            next += interval
        for line in lines:
            line.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running2 = False
        pygame.display.flip()

        # --- CHANGED: Standard FPS ---
        clock.tick(60)  # Was 1400
        # -----------------------------


if __name__ == '__main__':
    try:
        with open('highest_score_ever.txt', 'r') as f:
            score_list.append(int(f.read()))
    except FileNotFoundError:
        pass
    story()
    while True:
        star = game_loop()
        time.sleep(0.5)
        scoreboard(star)
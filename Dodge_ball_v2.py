import pygame
import random
import time
import os
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
YELLOW = (255, 255, 0)
BROWN = (55, 55, 55)
BLUE = (0, 0, 150)
GREY = (100, 100, 100)
RED = (150, 0, 0)
RANDOM = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
clock = pygame.time.Clock()

font0 = pygame.font.SysFont('Segoe UI Emoji', 30)
font = pygame.font.SysFont('Segoe UI Emoji', 20)
font1 = pygame.font.SysFont('Segoe UI Emoji', 50)

good = ['GOOD', 'AMAZING', 'BEAUTIFUL', 'FANTASTIC', 'WELL DONE', 'BRILLIANT', 'SO COOL', 'LOVELY', 'GOOD JOB', 'EXCELLENT', 'SUPER', 'RIZZ', 'RIZZ MASTER', 'ULTIMATE RIZZ MASTER', '5 STARS', 'LET HIM COOK', 'BREEZE', 'SWEET']

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


def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, 30, 30))

def game_loop():
    milestones =  [2,3,5,8]
    by = 0
    bx = WIDTH / 2
    cx = 0
    cy = HEIGHT - 30
    plus = 2
    score = 0
    cplus = 5
    cminus = 10
    start_loop = False
    time_start = 0
    time_last = 5000
    time_start_2 = pygame.time.get_ticks()
    time_last_2 = 4100
    tx = WIDTH
    running = True

    while running:
        screen.fill(WHITE)
        current_time_2 = pygame.time.get_ticks()
        if current_time_2 - time_start_2 < time_last_2:
            text3 = font.render('SPACE to dodge the ball', True, GREY)
            screen.blit(text3, (WIDTH/2-text3.get_width()/2, HEIGHT/2-text3.get_height()/2-30))
            text4 = font.render('Go full path to score', True, GREY)
            screen.blit(text4, (WIDTH/2-text4.get_width()/2, HEIGHT/2-text3.get_height()/2+30))

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
            if score in milestones or score % 5 == 0:
                plus += 2
                cplus += 1
                cminus += 2
            start_loop = True
            time_start = pygame.time.get_ticks()
            compliment[0] = good[random.randint(0, len(good)-1)]
        if start_loop:
            current_time = pygame.time.get_ticks()
            if current_time - time_start < time_last:
                text2 = font.render(*compliment, True, BROWN)
                screen.blit(text2, (tx,100))
                if (0-text2.get_width()) < tx <= WIDTH:
                    tx -= 5
                else:
                    tx = WIDTH
            else:
                start_loop = False

        if abs(bx - (cx + 15)) < 50 and abs(by - (cy + 15)) < 50:
            running = False

        text = font.render(f'Pizzas delivered: {score} 🍕', True, COLOR)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, 50))
        pygame.draw.line(screen, BLUE, (0, HEIGHT-5), (WIDTH, HEIGHT-5), 10)
        draw_ball(bx, by)
        draw_car(cx, cy)
        pygame.display.flip()
        clock.tick(50)
    return score

def scoreboard(score):
    running1 = True
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

        screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/2 - text1.get_height()/2 - 50))
        screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text1.get_height()/2 + 50))
        pygame.display.flip()
        clock.tick(50)

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
        screen.blit(text, ((WIDTH//2 - text.get_width()//2), self.y))
        self.y -= 7
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
        if time_lapsed > 11000:
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
        clock.tick(20)

if __name__ == '__main__':
    story()
    while True:
        star = game_loop()
        time.sleep(0.5)
        scoreboard(star)


import pygame
import random

WIDTH = 1000
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw your own galaxy')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

YELLOW = (255,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

def draw_gradient(surface, top_color, bottom_color):
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
        g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
        b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
        pygame.draw.line(surface, (r,g,b), (0,y), (WIDTH, y))

class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (
            random.randint(100, 200)
            , random.randint(100, 200)
            , random.randint(100, 200)
        )
        self.max_radius = random.randint(20, 70)
        self.current_radius = 0
        self.growth_rate = random.uniform(0.5, 1.5)
    def grow(self):
        if self.current_radius < self.max_radius:
            self.current_radius += self.growth_rate
    def draw(self, surface):
        if self.current_radius > 0:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.current_radius)

planets = []

running = True
speed = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    draw_gradient(screen, (248,76,224), (67,3,66))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            planets.append(Planet(x,y))
    for planet in planets:
        planet.grow()
        planet.draw(screen)

    pygame.display.flip()
    speed.tick(23)

pygame.quit()


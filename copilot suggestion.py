import pygame
import random
import math
import time

pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Drift")

TOP_COLOR = (10, 10, 30)
BOTTOM_COLOR = (0, 0, 0)

# Particle class
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(1, 3)
        self.speed = random.uniform(0.1, 0.5)
        self.color = (255, 255, 255)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Glowing star class
class GlowingStar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.start_time = time.time()
        self.duration = 2  # seconds
        self.color = (255, 255, 150)

    def is_alive(self):
        return time.time() - self.start_time < self.duration

    def draw(self, surface):
        elapsed = time.time() - self.start_time
        alpha = max(0, 255 - int((elapsed / self.duration) * 255))
        glow_color = (self.color[0], self.color[1], self.color[2], alpha)

        # Create a surface with alpha channel
        star_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        points = self.calculate_star_points(self.size, self.size, self.size, self.size // 2)
        pygame.draw.polygon(star_surface, glow_color, points)
        surface.blit(star_surface, (self.x - self.size, self.y - self.size))

    def calculate_star_points(self, cx, cy, outer_radius, inner_radius):
        points = []
        for i in range(10):
            angle = math.pi / 5 * i
            radius = outer_radius if i % 2 == 0 else inner_radius
            x = cx + math.cos(angle) * radius
            y = cy + math.sin(angle) * radius
            points.append((x, y))
        return points

# Gradient background
def draw_gradient(surface, top_color, bottom_color):
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
        g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
        b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))

particles = [Particle() for _ in range(200)]
stars = []

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            stars.append(GlowingStar(x, y))

    draw_gradient(screen, TOP_COLOR, BOTTOM_COLOR)

    for particle in particles:
        particle.move()
        particle.draw(screen)

    # Draw and update stars
    stars = [star for star in stars if star.is_alive()]
    for star in stars:
        star.draw(screen)

    pygame.display.flip()

pygame.quit()
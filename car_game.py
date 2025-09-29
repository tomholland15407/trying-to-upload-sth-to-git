import random
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars incoming")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('verdana', 50)
small_font = pygame.font.SysFont('verdana', 20)

me_radius = 25
car_width = 60
car_height = 100
car_speed = 5
car_speed_plus = 1
milestones = [5, 10, 15, 20, 25, 30]

def draw_me(x,y):
    pygame.draw.circle(screen, RED, (x,y),  me_radius)



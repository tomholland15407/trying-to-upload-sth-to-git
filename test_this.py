import pygame
import random
from multiprocessing import Process
import time

pygame.init()

WIDTH, HEIGHT = 600, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Magic Ball')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (100, 100, 200)
YELLOW = (255, 255, 0)
BROWN = (55, 55, 55)
clock = pygame.time.Clock()
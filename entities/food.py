# entities/food.py
import pygame
from core.settings import *

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.eaten = False

    def draw(self, screen):
        if not self.eaten:
            pygame.draw.circle(
                screen,
                COLOR_FOOD,
                (int(self.x), int(self.y)),
                5
            )
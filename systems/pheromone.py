import pygame
import numpy as np
from core.settings import *


class PheromoneSystem:
    def __init__(self):
        self.grid = np.zeros((GRID_H, GRID_W))

    def deposit(self, x, y):
        col = int(x // CELL_SIZE)
        row = int(y // CELL_SIZE)
        if 0 <= col < GRID_W and 0 <= row < GRID_H:
            self.grid[row][col] = min(
                    self.grid[row][col] + DEPOSIT_AMOUNT, 
                    MAX_INTENSITY
                    )

    def update(self):
        self.grid *= EVAPORATION_RATE
    
    def draw(self, screen):
        for row in range(GRID_H):
            for col in range(GRID_W):
                intensity = self.grid[row][col]
                if intensity < 0.1:
                    continue
                alpha = int((intensity / MAX_INTENSITY) * 180)
                color = (alpha, 80, 20)
                pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Entidade formiga - Fase 1: movimento básico;

import pygame, random, math
from core.settings import *


class Ant:
    def __init__(self, x, y):
        #Posição
        self.x = x
        self.y = y

        # Direção aleatoria inicial em radianos
        self.angle = random.uniform(0, 2* math.pi)

        # Velocidade em pixels por segundo 
        self.speed = ANT_SPEED

    def update(self, dt):
        # Movimento baseado no ângulo atual

        self.x += math.cos(self.angle) * self.speed * dt
        self.y += math.sin(self.angle) * self.speed * dt

        # Rabater nas bordas da tela
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.angle = math.pi - self.angle
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.angle = -self.angle

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_ANT, (int(self.x), int(self.y)), ANT_SIZE)
        
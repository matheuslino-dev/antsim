# Entidade formiga - Fase 1: movimento básico;

import pygame, random, math
from core.settings import *


class Ant:
    def __init__(self, x, y):
        #Posição
        self.x = x
        self.y = y

        self.wander_strength = 0.3  # radianos por frame
        # Direção aleatoria inicial em radianos
        self.angle = random.uniform(0, 2* math.pi)
        self.state = "exploring"  # estado
        self.colony_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)  # posição da colônia

        # Velocidade em pixels por segundo 
        self.speed = ANT_SPEED

    def update(self, dt, foods):
        if self.state == "exploring":
            self._explore(dt)
            self._check_food(foods)
        elif self.state == "carrying":
            self._return_to_colony(dt)



    def _explore(self, dt):
        self.angle += random.uniform(-self.wander_strength, self.wander_strength)
        self.x += math.cos(self.angle) * self.speed * dt
        self.y += math.sin(self.angle) * self.speed * dt

        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.angle = math.pi - self.angle
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.angle = -self.angle

    def _check_food(self, foods):
        for food in foods:
            if food.eaten:
                continue
            dx = self.x - food.x
            dy = self.y - food.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance < 10:
                food.eaten = True
                self.state = "carrying"

    def _return_to_colony(self, dt):
        dx = self.colony_pos[0] - self.x
        dy = self.colony_pos[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < COLONY_RADIUS:
            self.state = "exploring"
            return

        self.angle = math.atan2(dy, dx)
        self.x += math.cos(self.angle) * self.speed * dt
        self.y += math.sin(self.angle) * self.speed * dt
            


    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_ANT, (int(self.x), int(self.y)), ANT_SIZE)
        
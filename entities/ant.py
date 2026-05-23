# Entidade formiga - Fase 1: movimento básico;

import pygame, random, math
from core.settings import *

class Ant:
    def __init__(self, x, y):
        #Posição
        self.x = x
        self.y = y

        self.wander_strength = 0.3  # radianos por frame
        # Direção aleatória inicial em radianos
        self.angle = random.uniform(0, 2* math.pi)
        self.state = "exploring"  # estado
        self.colony_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)  # posição da colônia

        # Velocidade em pixels por segundo 
        self.speed = ANT_SPEED

    def update(self, dt, foods, pheromone):
        if self.state == "exploring":
            self._explore(dt, pheromone)
            self._check_food(foods)
        elif self.state == "carrying":
            self._return_to_colony(dt)

    def _sense_pheromone(self, pheromone):
        best_angle = self.angle
        best_value = -1

        # Testa 3 direções: frente, esquerda e direita
        for offset in [-0.5,0, 0.5]:
            test_angle = self.angle + offset
            sense_x = self.x + math.cos(test_angle) * 20
            sense_y = self.y + math.sin(test_angle) * 20

            col = int(sense_x // 10)
            row = int(sense_y // 10)

            if 0 <= col < 120 and 0 <= row < 80:
                value = pheromone.grid[row][col]
                if value > best_value:
                    best_value = value
                    best_angle = test_angle
                
        if best_value > 0.:
            self.angle = best_angle


    def _explore(self, dt, pheromone):
        self._sense_pheromone(pheromone)
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
        color = COLOR_ANT if self.state == "exploring" else COLOR_FOOD
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), ANT_SIZE)
        
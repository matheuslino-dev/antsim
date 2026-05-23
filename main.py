import pygame
import sys
import random
import numpy as np
from core.settings import *
from entities.ant import Ant
from entities.food import Food
from systems.pheromone import PheromoneSystem
def main():

    pygame.init()

    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    ants = [Ant(SCREEN_WIDTH//2, SCREEN_HEIGHT//2) for _ in range(ANT_COUNT)]
    foods = [Food(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(20)]
    pheromone_system = PheromoneSystem()
    

    running = True
    while running:

        dt = clock.tick(FPS) / 1000.0
        print(f"\rFPS: {clock.get_fps():.2f} | Delta Time: {dt:.4f} seconds", end="")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(COLOR_BACKGROUND)
        pygame.draw.circle(screen, COLOR_COLONY, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), COLONY_RADIUS)

        for ant in ants:
            if ant.state == "carrying":
                pheromone_system.deposit(ant.x, ant.y)
            ant.update(dt, foods, pheromone_system)
            ant.draw(screen)

        if all(food.eaten for food in foods):
            foods.append(Food(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        for food in foods:
            food.draw(screen)

        pheromone_system.update()
        pheromone_system.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

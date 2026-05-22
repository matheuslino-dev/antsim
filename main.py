import pygame, sys 
from core.settings import *
from entities.ant import Ant

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    ants = [Ant(SCREEN_WIDTH//2, SCREEN_HEIGHT//2) for _ in range(ANT_COUNT)]

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

        screen.fill(COLOR_BLACKGROUND)
        for ant in ants:
            ant.update(dt)
            ant.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
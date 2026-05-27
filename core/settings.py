# core/settings.py
# Configuração globais da simulação - Single Source of Truth

# Janela

import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
TITLE = "AntSim - Colony Simulator"
FPS = 60

# Cores
COLOR_BACKGROUND = (15,10,5) # quase preto, para dar um tom mais "natural"
COLOR_COLONY = (139,90,43) # marrom
COLOR_ANT = (210,180, 140) # bege claro
COLOR_FOOD = (50, 200, 50) # verde

# Formigas
ANT_COUNT = 10
ANT_SPEED = 80
ANT_SIZE = 4

# Colonia
COLONY_RADIUS = 20

# Feromônio

# --- Feromônio ---
CELL_SIZE = 10
GRID_W = SCREEN_WIDTH // CELL_SIZE
GRID_H = SCREEN_HEIGHT // CELL_SIZE
EVAPORATION_RATE = 0.98
DEPOSIT_AMOUNT = 1.0
MAX_INTENSITY = 10.0
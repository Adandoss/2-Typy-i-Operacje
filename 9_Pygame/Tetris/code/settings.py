import pygame

# Game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + 3 * PADDING
WINDOW_HEIGHT = GAME_HEIGHT + 2 * PADDING

# Game behaviour
FPS = 60
VERTICAL_MOVE_SPEED = 400
FAST_VERTICAL_MOVE_SPEED = VERTICAL_MOVE_SPEED * 0.05
MOVE_WAIT_TIME = 50
ROTATE_WAIT_TIME = 100
BLOCK_OFFSET = pygame.Vector2(4, -1)
RIGHT = 1
LEFT = -1

# Colors
RED = '#ff0000'
GREEN = '#00ff00'
BLUE = '#0000ff'
YELLOW = '#ffff00'
MAGENTA = '#ff00ff'
CYAN = '#00ffff'
ORANGE = '#ff4500'
BLACK = '#000000'
WHITE = '#ffffff'
GREY = '#303030'
LIGHT_GREY = '#7e7e7e'

# Shapes
TETROMINOS = {
    'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': YELLOW},
    'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': RED},
    'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)], 'color': MAGENTA},
    'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': CYAN},
    'I': {'shape': [(0, 0), (0, -1), (0, -2), (0, 1)], 'color': ORANGE},
    'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': GREEN},
    'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': BLUE}
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}



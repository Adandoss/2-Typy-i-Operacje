import pygame
import random
import json
import sys
import argparse

import time

# pygame initial setup:
SCREEN_SIZE = (900, 900)

parser = argparse.ArgumentParser(description="Wave Function Collapse")
parser.add_argument("--dim", type=int, default=20, help="Dimention of the grid (default 20)")
parser.add_argument("--set", type=str, default="extended_basic_set", help="Tileset (default 'extended_basic_set')")
parser.add_argument("--fps", type=int, default=240, help="FPS (default 240)")

args = parser.parse_args()

DIM = args.dim
TILES = f'tile_sets/{args.set}/tiles.json'
FPS = args.fps

CELL_SIZE = (SCREEN_SIZE[0] / DIM, SCREEN_SIZE[1] / DIM)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Wave Function Collapse")
clock = pygame.time.Clock()
running = True

with open(TILES, 'r') as file:
    tiles = json.load(file)

for tile in tiles:
    image = pygame.image.load('tile_sets/' + tile['path']).convert()
    tile['image'] = pygame.transform.scale(image, CELL_SIZE)
    tile['north'] = set(tile['north'])
    tile['east'] = set(tile['east'])
    tile['south'] = set(tile['south'])
    tile['west'] = set(tile['west'])


# WTC grid:
class GridCell:
    def __init__(self, x, y, entrophy=len(tiles) - 1, 
                 possibilities=set(range(len(tiles) - 1)), 
                 tile=len(tiles) - 1, collapsed=False):
        self.x = x
        self.y = y
        self.entrophy = entrophy
        self.possibilities = possibilities
        self.tile = tile
        self.collapsed = collapsed


    def __str__(self):
        return (
            f"GridCell("
            f"x={self.x}, y={self.y}, "
            f"entrophy={self.entrophy}, "
            f"possibilities={self.possibilities}, "
            f"tile={self.tile}, "
            f"collapsed={self.collapsed})"
        )

    def __repr__(self):
        return (
            f"GridCell("
            f"x={self.x}, y={self.y}, "
            f"entrophy={self.entrophy}, "
            f"possibilities={self.possibilities}, "
            f"tile={self.tile}, "
            f"collapsed={self.collapsed})"
        )

WTCgrid = [[GridCell(x, y)
            for y in range(DIM)] for x in range(DIM)]

def draw_tile(tile: int, x: int, y: int) -> None:
    screen.blit(tiles[tile]["image"], (CELL_SIZE[0]*y, CELL_SIZE[1]*x))
    WTCgrid[x][y].collapsed = True
    WTCgrid[x][y].tile = tile


def calculate_entrophy(cell: GridCell) -> tuple:
    possibilities_set = set(range(len(tiles) - 1))
    if cell.collapsed:
        return (0, set())
    else:
        if cell.x == 0:
            if cell.y == 0:
                possibilities_set = (
                    tiles[WTCgrid[0][1].tile]['west'] &
                    tiles[WTCgrid[1][0].tile]['north']
                )
            elif cell.y == DIM - 1:
                possibilities_set = (
                    tiles[WTCgrid[0][DIM - 2].tile]['east'] &
                    tiles[WTCgrid[1][DIM - 1].tile]['north']
                )
            else:
                possibilities_set = (
                    tiles[WTCgrid[0][cell.y - 1].tile]['east'] &
                    tiles[WTCgrid[0][cell.y + 1].tile]['west'] &
                    tiles[WTCgrid[1][cell.y].tile]['north']
                )
        elif cell.x == DIM - 1:
            if cell.y == 0:
                possibilities_set = (
                    tiles[WTCgrid[DIM - 1][1].tile]['west'] &
                    tiles[WTCgrid[DIM - 2][0].tile]['south']
                )
            elif cell.y == DIM - 1:
                possibilities_set = (
                    tiles[WTCgrid[DIM - 1][DIM - 2].tile]['east'] &
                    tiles[WTCgrid[DIM - 2][DIM - 1].tile]['south']
                )
            else:
                possibilities_set = (
                    tiles[WTCgrid[DIM - 1][cell.y - 1].tile]['east'] &
                    tiles[WTCgrid[DIM - 1][cell.y + 1].tile]['west'] &
                    tiles[WTCgrid[DIM - 2][cell.y].tile]['south']
                )
        elif cell.y == 0:
            possibilities_set = (
                tiles[WTCgrid[cell.x - 1][0].tile]['south'] &
                tiles[WTCgrid[cell.x + 1][0].tile]['north'] &
                tiles[WTCgrid[cell.x][1].tile]['west']
            )
        elif cell.y == DIM - 1:
            possibilities_set = (
                tiles[WTCgrid[cell.x - 1][DIM - 1].tile]['south'] &
                tiles[WTCgrid[cell.x + 1][DIM - 1].tile]['north'] &
                tiles[WTCgrid[cell.x][DIM - 2].tile]['east']
            )
        else:
            possibilities_set = (
                tiles[WTCgrid[cell.x - 1][cell.y].tile]['south'] &
                tiles[WTCgrid[cell.x + 1][cell.y].tile]['north'] &
                tiles[WTCgrid[cell.x][cell.y - 1].tile]['east'] &
                tiles[WTCgrid[cell.x][cell.y + 1].tile]['west']
            )

        return (len(possibilities_set), possibilities_set)

    
def pick_and_collapse() -> None:
    min = len(tiles) - 1
    smallest_ent = []
    for x in range(DIM):
        for y in range(DIM):
            ent = calculate_entrophy(WTCgrid[x][y])
            if ent[0] == 0:
                continue
            if ent[0] < min:
                smallest_ent.clear()
                smallest_ent.append((ent, (x, y)))
                min = ent[0]
            elif ent[0] == min:
                smallest_ent.append((ent, (x, y)))
    if len(smallest_ent) == 0:
        draw_tile(3, x, y)
        return
    smallest_ent_pick = random.choice(smallest_ent)
    cell_position = smallest_ent_pick[1]
    cell_tile = random.sample(list(smallest_ent_pick[0][1]), 1)[0]
    draw_tile(cell_tile, cell_position[0], cell_position[1])

    return smallest_ent


draw_tile(random.choice(range(len(tiles) - 1)), 
          random.randint(0, DIM - 1), 
          random.randint(0, DIM - 1))

N = DIM * DIM
i = 1

# main loop: 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                time.sleep(1000000)

    if i < N:
        pick_and_collapse()
        i += 1

    pygame.display.flip()

    clock.tick(FPS)
import pygame
from random import randint
from copy import deepcopy

res = width, height = 1600, 900
tile = 20
w, h = width // tile, height // tile
fps = 10

pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

next_arr = [[0 for i in range(w)] for j in range(h)]
curr_arr = [[randint(0, 2) for i in range(w)] for j in range(h)]


def check(curr_arr, x, y):
    countgreen = 0
    countred = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if curr_arr[j][i] == 1:
                countgreen += 1
            if curr_arr[j][i] == 2:
                countred += 1
    if curr_arr[y][x]:
        if curr_arr[y][x] == 1:
            countgreen -= 1
        else:
            countred -= 1
        if countred == 3 or countred == 2:
            return 1
        elif countgreen == 3 or countgreen == 4:
            return 2
        return 0

    else:
        if countred == 3 or countgreen == 3:
            return 2
        elif countred == countgreen == 2:
            return 1
        return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, height)) for x in range(0, width, tile)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (width, y)) for y in range(0, height, tile)]
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if curr_arr[y][x] == 2:
                pygame.draw.rect(surface, pygame.Color('red'), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
            if curr_arr[y][x] == 1:
                pygame.draw.rect(surface, pygame.Color('green'), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
            next_arr[y][x] = check(curr_arr, x, y)

    curr_arr = deepcopy(next_arr)

    pygame.display.flip()
    clock.tick(fps)

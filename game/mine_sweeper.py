import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPEND = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field, x_pos, y_pos):
    """周囲にある爆弾の数を返す"""
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos , ypos = x_pos + xoffset, y_pos + yoffset
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1

    return count

def open_tile(field, x_pos, y_pos):
    """タイルをオープMNン"""

def main():
    """メインルーチン"""

if __name__ == '__main__':
    main()

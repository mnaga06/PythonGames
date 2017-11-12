import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP, K_RIGHT, K_LEFT
pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((720, 480))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("Image/pythonlogl.png")
    pos = [200, 150]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos[0] -= 5
                if event.key == K_RIGHT:
                    pos[0] += 5
                if event.key == K_DOWN:
                    pos[1] += 5
                if event.key == K_UP:
                    pos[1] -= 5

        pos[0] = pos[0] % 720
        pos[1] = pos[1] % 480

        SURFACE.fill((255, 255, 255))

        rect = logo.get_rect()
        rect.center = pos
        SURFACE.blit(logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ =='__main__':
    main()

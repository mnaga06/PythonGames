import sys
import pygame
from   pygame.locals import QUIT

pygame.init()
SURFACE= pygame.display.set_mode((400, 220))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main rutine"""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((255, 255, 255))


        
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()

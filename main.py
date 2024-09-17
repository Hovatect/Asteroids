# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fill screen black and refresh
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()

# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot



def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   #create clock instance
    clock = pygame.time.Clock()
    dt = 0

    # add player to the game
        
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    # add AsteroidField object

    asteroid_field = AsteroidField()
    
    
    # fill screen black and refresh
    while True:
        screen.fill((0,0,0))

        # Draw all sprites using their customer draw methods
        for sprite in drawable:
            sprite.draw(screen)

        # boots shot drawing
        for shot in shots:
            shot.move(dt)
            shot.draw(screen)

        # update the display
        pygame.display.flip()

        #check tick
        dt = clock.tick(60) / 1000      # maintain 60 FPS and record delta time

        # first movement
        updatable.update(dt)

        # collision check
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game Over!")
                sys.exit()  
            for shot in shots: 
                if asteroid.is_colliding_with(shot):
                    asteroid.split()
                    shot.kill()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()

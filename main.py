# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()

    Clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill([0,0,0])
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.are_colliding(player):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.are_colliding(shot):
                    asteroid.split()
                    shot.kill()
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
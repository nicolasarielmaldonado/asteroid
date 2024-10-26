import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    asteroid.kill()

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        value = clock.tick(60)
        dt = value / 1000
    
if __name__ == "__main__":
    main()

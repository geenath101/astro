import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    print("Starting asteroids!")
    print("Screen width: {0}".format(SCREEN_WIDTH))
    print("Screen height: {0}".format(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    my_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                return
        passedTime = clock.tick(60)
        dt = passedTime/1000
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            if a.do_colide(player):
                print("Game over!")
        for d in drawable:
            d.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
       
     
if __name__  == "__main__" :
    main()
    


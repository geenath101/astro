import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: {0}".format(SCREEN_WIDTH))
    print("Screen height: {0}".format(SCREEN_HEIGHT))
    scren = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                return
        scren.fill("black")
        pygame.display.flip()

     
if __name__  == "__main__" :
    main()
    


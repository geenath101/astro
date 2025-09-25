from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        #print("shooooting")
        pygame.draw.circle(screen,"white",self.position,self.radius)
    def update(self,dt):
        print("updating")
        self.position = self.position + self.velocity * dt
    
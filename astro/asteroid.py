from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)
    def update(self,dt):
        self.position = self.position + self.velocity *dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        v_unit_1 = self.velocity.rotate(angle)
        v_unit_2 = self.velocity.rotate(angle * -1)
        smaller_astero_radius = self.radius - ASTEROID_MIN_RADIUS
        as_1 = Asteroid(self.position.x,self.position.y,smaller_astero_radius)
        as_2 = Asteroid(self.position.x,self.position.y,smaller_astero_radius)
        as_1.velocity = v_unit_1 + self.velocity * 1.2
        as_2.velocity = v_unit_2 + self.velocity * 1.2     

   
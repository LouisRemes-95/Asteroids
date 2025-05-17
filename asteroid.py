from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            Ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_angle = random.uniform(20, 50)
            Ast1.velocity =  self.velocity.rotate(new_angle) * 1.2
            Ast2.velocity =  self.velocity.rotate(-new_angle) * 1.2

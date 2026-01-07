import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # chunks are one size smaller
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        chunk_one = Asteroid(self.position.x, self.position.y, new_radius)
        chunk_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        # chunks move in opposite directions
        random_angle = random.uniform(20, 50)
        chunk_one.velocity = self.velocity.rotate(random_angle) * 1.2
        chunk_two.velocity = self.velocity.rotate(-random_angle) * 1.2

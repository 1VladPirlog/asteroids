# asteroid.py
import pygame
from circleshape import CircleShape # Assuming CircleShape is in circleshape.py

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class's constructor, ensuring it uses the containers
        super().__init__(x, y, radius)
        # velocity is already initialized to (0,0) in CircleShape,
        # but will be set by AsteroidField later.

    def draw(self, screen):
        # Override draw method to draw the asteroid as a circle
        # Using "grey" for asteroid color, as per common game design
        pygame.draw.circle(screen, "grey", self.position, self.radius, 2)

    def update(self, dt):
        # Override update method to move in a straight line
        # self.velocity is inherited from CircleShape and will be set by AsteroidField
        self.position += self.velocity * dt
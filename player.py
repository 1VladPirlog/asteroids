
import pygame
from circleshape import CircleShape # Import from your circleshape.py
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED 

class Player(CircleShape):
    def __init__(self, x, y):
        # CircleShape's constructor takes x, y, radius
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # Initialize rotation to 0

    def triangle(self):
        
        forward = pygame.Vector2(0, -1).rotate(self.rotation) # Changed from (0,1) to (0,-1)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5 # Changed from (0,1) to (0,-1)

        # These calculations use the player's current position and radius
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Override the draw method to draw the player as a triangle
        # pygame.draw.polygon takes: surface, color, pointlist, width
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

        # Optional: Draw the hitbox for debugging (uncomment if you want to see it)
        # pygame.draw.circle(screen, "red", self.position, self.radius, 1)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left (counter-clockwise)
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right (clockwise)

        if keys[pygame.K_w]:
            self.move(dt)     # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # Move backward (reverse dt for reverse movement)

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
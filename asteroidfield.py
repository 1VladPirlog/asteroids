# asteroidfield.py
import pygame
import random
from asteroid import Asteroid # Make sure to import Asteroid
from constants import * # Import all constants including asteroid-specific ones

class AsteroidField(pygame.sprite.Sprite):
    # This list defines the edges from which asteroids can spawn
    # Each item is [direction_vector, position_lambda]
    # direction_vector: unit vector indicating the general direction of movement
    # position_lambda: function to calculate a random starting position along that edge
    edges = [
        # Right edge, moving left
        [
            pygame.Vector2(1, 0), # Horizontal direction (towards right from center)
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), # Start just off left edge
        ],
        # Left edge, moving right
        [
            pygame.Vector2(-1, 0), # Horizontal direction (towards left from center)
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT # Start just off right edge
            ),
        ],
        # Bottom edge, moving up
        [
            pygame.Vector2(0, 1), # Vertical direction (towards bottom from center)
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS), # Start just off top edge
        ],
        # Top edge, moving down
        [
            pygame.Vector2(0, -1), # Vertical direction (towards top from center)
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS # Start just off bottom edge
            ),
        ],
    ]

    def __init__(self):
        # Initialize the sprite, automatically adding it to its containers
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0 # Timer to control when the next asteroid spawns

    def spawn(self, radius, position, velocity):
        # Create a new Asteroid instance
        # It will automatically be added to its defined containers (asteroids, updatable, drawable)
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity # Set its initial velocity

    def update(self, dt):
        self.spawn_timer += dt # Increment the spawn timer
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0 # Reset timer for the next spawn

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges) # Pick a random edge
            speed = random.randint(40, 100) # Random speed for the asteroid
            velocity = edge[0] * speed # Base velocity from the edge direction
            velocity = velocity.rotate(random.randint(-30, 30)) # Add some random angular deviation
            position = edge[1](random.uniform(0, 1)) # Get a random position along the chosen edge
            kind = random.randint(1, ASTEROID_KINDS) # Determine asteroid 'kind' (affects size)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity) # Create and spawn the asteroid
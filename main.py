# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")	
	 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

 # Create a clock object
clock = pygame.time.Clock()

# Initialize dt (delta time)
dt = 0

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    # Draw the player
    player.draw(screen) # Call the player's draw method
        
    pygame.display.flip()



    # Limit the frame rate to 60 FPS and get delta time
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
pygame.quit()


if __name__ == "__main__":
    main()

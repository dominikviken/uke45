import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set current window caption
    pygame.display.set_caption("PUCMEN")
    # Loop until the user clicks the close button.
    done = False
    # manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    # Main Program Loop
    while not done:
        # Process events
        done = game.process_events()
        # Game logic
        game.run_logic()
        # current frame
        game.display_frame(screen)
        # Limit 30 fps
        clock.tick(30)
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    main()

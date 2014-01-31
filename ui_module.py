'''
 ui_module.py

 This module provides the interface with the pygames functions

 author: Daniel Henderson
'''


import pygame


# Define colors
RED = (255, 0, 0)
WHITE = ( 255, 255, 255)


class UserInterface:
    def __init__(self, grid_size, tile_size, bg_img, caption='Building Evacuation'):
        # Set the width and height of the screen [width, height] in pixels
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.x_range = int(self.grid_size[0] / self.tile_size)
        self.y_range = int(self.grid_size[1] / self.tile_size)

        # Setup pygame ui environment
        pygame.init()
        self.screen = pygame.display.set_mode(self.grid_size)
        pygame.display.set_caption(caption)

        # Load the background image
        self.bg_img = pygame.image.load(bg_img).convert()

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def checkEvents(self):
        done = False
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
        return done

    def drawScreen(self, coordinates):
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill(WHITE)

        # Draw the background image first
        self.screen.blit(self.bg_img, [0, 0])

        for coord in coordinates:
            x = coord[0]*self.tile_size
            y = coord[1]*self.tile_size
            pygame.draw.ellipse(self.screen, RED, [x, y, self.tile_size, self.tile_size], 0)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        self.clock.tick(60)

    def quit(self):
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()

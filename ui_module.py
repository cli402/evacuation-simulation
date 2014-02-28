'''
 ui_module.py

 This module provides the interface with the pygames functions

 author: Daniel Henderson
'''


import pygame
import grid_info


# Define colors
colors = [
    (0, 0, 255),    # blue
    (0, 0, 0),      # black
    (255, 0, 0),    # red
    (0, 51, 25),    # dark green
    (153, 0, 153),  # purple
    (204, 102, 0),  # orange
    (0, 255, 255),  # aqua
    (255, 255, 255),# white
    (0, 0, 0),      # black
]


class UserInterface:
    def __init__(self, grid_size, tile_size, bg_img, door_coords, caption='Building Evacuation'):
        # Set the width and height of the screen [width, height] in pixels
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.door_coords = door_coords
        self.x_range = int(self.grid_size[0] / self.tile_size)
        self.y_range = int(self.grid_size[1] / self.tile_size)

        # Setup pygame ui environment
        pygame.init()
        flags = pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.HWSURFACE
        self.screen = pygame.display.set_mode(self.grid_size, flags)
        pygame.display.set_caption(caption)

        # limit events to ones that we actually use
        pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

        # Load the background image
        self.bg_img = pygame.image.load(bg_img).convert()
        self.bg_img_original = self.bg_img.copy()  # anytime we zoom, we want to use the original
        self.bgx = -100
        self.bgy = -600

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # zoom level, 1 is max out zoom, 3 is max in zoom
        self.zoom_level = 1
        self.zoom_pos = [0, 0]

        # used for dragging image 
        self.mouse_down = False
        self.click_pos = (0, 0)

        #get the bit map, for testing purposes
        #self.bit_map = self._get_bit_map()

    def _get_bit_map(self):
        import generate_map
        import generate_bitstream 

        generate_map.main()
        generate_bitstream.main()

        from bitarray import bitarray
        bit_map = bitarray()
        with open("bit_map", "rb") as fo:
            bit_map.fromfile(fo)
        return bit_map
            

    def checkMouseDownEvents(self, event):
        temp_pos = pygame.mouse.get_pos()
        if event.button == 1:
            self.click_pos = (temp_pos[0] - self.bgx, temp_pos[1] - self.bgy)
            self.mouse_down = True
        if event.button == 4:
            # scroll wheel up, zoom in
            if self.zoom_level < 3:
                self.zoom_level += 1
                w, h = self.bg_img_original.get_size()
                self.bg_img = pygame.transform.smoothscale(self.bg_img_original, (w*self.zoom_level, h*self.zoom_level))
                self.zoom_pos = [(temp_pos[0] - self.bgx) / (self.zoom_level - 1), (temp_pos[1] - self.bgy) / (self.zoom_level - 1)]
                self.bgx -= self.zoom_pos[0]
                self.bgy -= self.zoom_pos[1]
        if event.button == 5:
            # scroll wheel down, zoom out
            if self.zoom_level > 1:
                self.zoom_level -= 1
                w, h = self.bg_img_original.get_size()
                self.bg_img = pygame.transform.smoothscale(self.bg_img_original, (w*self.zoom_level, h*self.zoom_level))
                self.zoom_pos = [(temp_pos[0] - self.bgx) / (self.zoom_level + 1), (temp_pos[1] - self.bgy) / (self.zoom_level + 1)]
                self.bgx += self.zoom_pos[0]
                self.bgy += self.zoom_pos[1]

    def checkMouseUpEvents(self, event):
        if event.button == 1:
            self.mouse_down = False
            
    def checkEvents(self):
        done = False
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit the main loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.checkMouseDownEvents(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.checkMouseUpEvents(event)
            #if event.type == pygame.MOUSEMOTION:
            #    self.checkMouseMotionEvents(event)
        return done

    def drawScreen(self, agent_list):
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # Limit to 30 frames per second
        self.clock.tick(30)
        self.screen.fill(colors[-2])

        if self.mouse_down:
            pos = pygame.mouse.get_pos()
            self.bgx = pos[0] - self.click_pos[0]
            self.bgy = pos[1] - self.click_pos[1]

        # Draw the background image first
        self.screen.blit(self.bg_img, [self.bgx, self.bgy])


        # ---------------- For testing only!!! ------------------------------------------
                    
        #self.testDraw()           

        # ---------------- End Testing stuff -------------------------------------------

        # draw the agents
        tsize = self.tile_size*self.zoom_level
        for ((coordinateX,coordinateY), agent_ID, agent_status) in agent_list:
            x = coordinateX*tsize + self.bgx
            y = coordinateY*tsize + self.bgy
            #print "(%d, %d)"%(x, y)
            color_id = int(agent_ID.split('_')[0])
            pygame.draw.ellipse(self.screen, colors[color_id], [x, y, tsize, tsize], 0)


        # draw the doors
        self.drawDoors()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 

    def drawDoors(self):
        tsize = self.tile_size*self.zoom_level
        for color_index, doorlist in enumerate(self.door_coords):
            for xcoord, ycoord, w, h in doorlist:
                if h == 1:
                    adjustx = 1 if xcoord < 200 else -1
                else:
                    adjustx = 0
                adjusty = 1 if w == 1 else 0
                for i in xrange(xcoord + adjustx, xcoord + w + 1 + adjustx):
                    for j in xrange(ycoord + adjusty, ycoord + h + 1 + adjusty):
                        x = i*tsize + self.bgx
                        y = j*tsize + self.bgy
                        pygame.draw.rect(self.screen, colors[color_index], (x, y, tsize, tsize), 0)

    def testDraw(self):
        cols = 455
        rows = 494 #325
        tsize = self.tile_size*self.zoom_level
        for i in range(rows):
            for j in range(cols):
                if self.bit_map[i*cols + j]:
                    x = j*tsize + self.bgx
                    y = i*tsize + self.bgy
                    pygame.draw.rect(self.screen, colors[2], (x, y, tsize, tsize), 1)
#    
#
        #door_coords = grid_info.door_coords
        #goal_coords = grid_info.goal_coords

#
#        for goal_set in goal_coords:
#            for goal in goal_set:
#                for i in range(goal['min'][1], goal['max'][1] + 1):
#                    for j in range(goal['min'][0], goal['max'][0] + 1):
#                        x = j*self.tile_size
#                        y = i*self.tile_size
#                        pygame.draw.rect(self.screen, BLACK, (x, y, self.tile_size, self.tile_size), 0)
#
#        traffic_lights = grid_info.traffic_lights
#        for light_set in traffic_lights:
#            for light in light_set:
#                for xmin, ymin, xmax, ymax in light:
#                    for i in xrange(xmin, xmax + 1):
#                        for j in xrange(ymin, ymax + 1):
#                            x = i*tsize + self.bgx
#                            y = j*tsize + self.bgy    
#                            pygame.draw.rect(self.screen, BLACK, (x, y, tsize, tsize), 0)

    def quit(self):
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()



















































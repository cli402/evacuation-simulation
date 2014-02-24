'''
 main.py

 author: Daniel Henderson, Jier Chen
 ALL RIGHT RESERVED
'''

#System Support
import threading
import Queue

#UI module
import grid_info
import ui_module

#Engine Part
from engine import Engine
from terrain import Terrain
from generator import Generator

#random number generator
import rand
import time

#for gaussian cdf
from scipy.stats import norm


def ui():
	UI = ui_module.UserInterface(grid_info.grid_size, grid_info.tile_size, 'tech_square.jpg')

	while not UI.checkEvents():
		coordinates = agent_queue.get()
		UI.drawScreen(coordinates)
	UI.quit()


if __name__ == '__main__':
    rand.srand(int(time.time()))
    agent_queue = Queue.Queue()

#Generator list should not be 
    gen_list = [
		Generator(5)
#        Generator(0, (grid_info.door_coords[0]['min'], grid_info.door_coords[0]['max']), grid_info.goal_coords, 5, rand.gaussian_rand, norm.cdf),
#        Generator(1, (grid_info.door_coords[1]['min'], grid_info.door_coords[1]['max']), grid_info.goal_coords, 7, rand.gaussian_rand, norm.cdf),
#        Generator(2, (grid_info.door_coords[2]['min'], grid_info.door_coords[2]['max']), grid_info.goal_coords, 10, rand.gaussian_rand, norm.cdf),
#        Generator(3, (grid_info.door_coords[3]['min'], grid_info.door_coords[3]['max']), grid_info.goal_coords, 8, rand.gaussian_rand, norm.cdf),
#        Generator(4, (grid_info.door_coords[4]['min'], grid_info.door_coords[4]['max']), grid_info.goal_coords, 13, rand.gaussian_rand, norm.cdf) ]
	]

    engine = Engine(terrain = Terrain("grid_bits.txt"), initial_event_list = gen_list)

    print 'Starts to run simulation!'
    while not engine.end_condition :
        engine.step_simulate()

#!/usr/bin/python
'''
 main.py

 author: Daniel Henderson, Jier Chen
 ALL RIGHT RESERVED
'''

#System Support
import threading
import Queue

#UI module
#import grid_info
#import ui_module

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
	]

	engine = Engine(terrain = Terrain("grid_bits.txt"), initial_event_list = gen_list)

	print 'Starts to run simulation!'
	while not engine.end_condition :
		engine.step_simulate()
		agent_queue.put(engine.flush_agent())

#To enable engine pump agent information into agent_queue, uncomment line above
#Data structure that engine pumped to agent is 
#((coordinate X, coordinate Y), agent ID, agent status)
#	agent status can be two "waiting" and "blocking"
#	"waiting" means agent is waiting the CD for next move
#	"blocking" means agent is able to move but blocked at current position, needs some one beside him move to release available grid to him

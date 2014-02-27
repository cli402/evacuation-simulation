#!/usr/bin/python
'''
 main.py

 author: Daniel Henderson, Jier Chen
 ALL RIGHT RESERVED
'''

#System Support
import threading
import Queue

import grid_info

#Engine Part
from engine import Engine
from terrain import Terrain
from generator import Generator

#random number generator
import rand
import time

#for gaussian cdf
#from scipy.stats import norm


#UI module
# macro to switch whether to use user interface or not
USE_UI = False
if USE_UI :
	import ui_module
end_condition = False

class Ui(threading.Thread):
	UI = None

	def __init__(self, grid_size, tile_size, queue, door_coords):
		self.grid_size = grid_size
		self.tile_size = tile_size
		self.agent_queue = queue
		self.door_coords = door_coords
		self.UI = ui_module.UserInterface(self.grid_size, self.tile_size, 'tech_square.jpg', self.door_coords)
		super(Ui, self).__init__()
		#threading.Thread.__init__(self)

	def run(self):
		global end_condition
		while not self.UI.checkEvents():
			try:
				agents = self.agent_queue.get_nowait()
			except:
				agents = []
			print self.agent_queue.qsize()
			print end_condition
			print agents
			self.UI.drawScreen(agents)
		self.UI.quit()

class Simulator(threading.Thread):
	engine = None
	agent_queue = None

	def __init__(self, queue):

		gen_list = [
			Generator(0, grid_info.door_coords[0][0], 5, 3),
			Generator(1, grid_info.door_coords[0][1], 7, 3),
			Generator(2, grid_info.door_coords[0][2], 10, 3),
			Generator(3, grid_info.door_coords[0][3], 8, 3),
			Generator(4, grid_info.door_coords[1][0], 23, 3),
			Generator(5, grid_info.door_coords[1][1], 17, 3),
			Generator(6, grid_info.door_coords[2][0], 15, 3),
			Generator(7, grid_info.door_coords[3][0], 9, 3),
			Generator(8, grid_info.door_coords[4][0], 12, 3),
			Generator(9, grid_info.door_coords[5][0], 15, 3)
		]

		terrain = Terrain("grid_bits.txt")
		self.engine = Engine(terrain, initial_event_list = gen_list)
		self.agent_queue = queue
		super(Simulator, self).__init__()
		#threading.Thread.__init__(self)

	def run(self):
		global end_condition
		print 'Starts to run simulation!'
		while not self.engine.end_condition :
			self.engine.step_simulate()
			if USE_UI:
				self.agent_queue.put(self.engine.flush_agent())
		end_condition = True

#To enable engine pump agent information into agent_queue, uncomment line above
#Data structure that engine pumped to agent is 
#((coordinate X, coordinate Y), agent ID, agent status)
#	agent status can be two "waiting" and "blocking"
#	"waiting" means agent is waiting the CD for next move
#	"blocking" means agent is able to move but blocked at current position, needs some one beside him move to release available grid to him


def run_simulation(door_coords=grid_info.door_coords, seed=int(time.time())):
	agent_queue = Queue.Queue()
	rand.srand(seed)

	simulator = Simulator(agent_queue)
	simulator.start()

	if USE_UI:
		ui = Ui(grid_info.grid_size, grid_info.tile_size, agent_queue, door_coords)
		ui.start()
		ui.join()
	
	simulator.join()


if __name__ == '__main__':
	run_simulation()


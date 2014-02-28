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
from terrain import Terrain, Traffic_light
from generator import Generator, Human_source

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
terminate = False

result = 0

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
			#print "Queue size: %d"%self.agent_queue.qsize()
			#print "End Condition: %s"%end_condition
			#print "Agent List:"
			#print agents
			self.UI.drawScreen(agents)
		self.UI.quit()

class Simulator(threading.Thread):
	engine = None
	agent_queue = None

	def __init__(self, queue):
		self.agent_queue = queue
		source = Human_source(1500)

		event_list = [
			Generator('0_0', grid_info.door_coords[0][0], source, 3),
			Generator('0_1', grid_info.door_coords[0][1], source, 3),
			Generator('0_2', grid_info.door_coords[0][2], source, 3),
			Generator('0_3', grid_info.door_coords[0][3], source, 3),
			Generator('1_0', grid_info.door_coords[1][0], source, 3),
			Generator('1_1', grid_info.door_coords[1][1], source, 3),
			Generator('2_0', grid_info.door_coords[2][0], source, 3),
			Generator('3_0', grid_info.door_coords[3][0], source, 3),
			Generator('4_0', grid_info.door_coords[4][0], source, 3),
			Generator('5_0', grid_info.door_coords[5][0], source, 3)
		]

		for area, timming, initial_light in grid_info.traffic_lights :
			green,red = timming
			green,red = green*grid_info.FPS, red*grid_info.FPS
			light = Traffic_light(area, (green,red), initial_light)
			event_list.append(light)
		
		self.engine = Engine(terrain = Terrain("grid_bits.txt"), initial_event_list = event_list)

		super(Simulator, self).__init__()
		#threading.Thread.__init__(self)

	def run(self):
		global end_condition
		global result
		print 'Starts to run simulation!'
		while not self.engine.end_condition :
			self.engine.step_simulate()
			if USE_UI:
				self.agent_queue.put(self.engine.flush_agent())
			if terminate:
				break
		result = self.engine.time_elapse
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

	#gen_list = [ Generator(0, (201, 295, 1, 0), 5, 3) ]

	simulator = Simulator(agent_queue)
	result = simulator.start()

	if USE_UI:
		ui = Ui(grid_info.grid_size, grid_info.tile_size, agent_queue, door_coords)
		ui.start()
		ui.join()
		global terminate
		terminate = True
	
	simulator.join()
	global result
	return result


if __name__ == '__main__':
	run_simulation()


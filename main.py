'''
 main.py

 author: Daniel Henderson, Jier Chen
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


def ui():
	UI = ui_module.UserInterface(grid_info.grid_size, grid_info.tile_size, 'tech_square.jpg')

	while not UI.checkEvents():
		coordinates = agent_queue.get()
		UI.drawScreen(coordinates)
	UI.quit()


if __name__ == '__main__':
	agent_queue = Queue.Queue()
	engine = Engine(terrain = Terrain("map.dat"), generator_list = [Generator(5)])
	print 'Starts to run simulation!'
	while not engine.end_condition :
		engine.step_simulate()

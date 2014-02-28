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
#from scipy.stats import norm


# macro to switch whether to use user interface or not
USE_UI = True
end_condition = False
terminate = False

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

    def __init__(self, engine, queue):
        self.engine = engine
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
            if terminate:
                break
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
    gen_list = [
        Generator('0_0', door_coords[0][0], 150, 3),
        Generator('0_1', door_coords[0][1], 150, 3),
        Generator('0_2', door_coords[0][2], 150, 3),
        Generator('0_3', door_coords[0][3], 150, 3),
        Generator('1_0', door_coords[1][0], 150, 3),
        Generator('1_1', door_coords[1][1], 150, 3),
        Generator('2_0', door_coords[2][0], 150, 3),
        Generator('3_0', door_coords[3][0], 150, 3),
        Generator('4_0', door_coords[4][0], 150, 3),
        Generator('5_0', door_coords[5][0], 150, 3)
    ]

    engine = Engine(terrain = Terrain("grid_bits.txt"), initial_event_list = gen_list)

    simulator = Simulator(engine, agent_queue)
    simulator.start()

    if USE_UI:
        ui = Ui(grid_info.grid_size, grid_info.tile_size, agent_queue, door_coords)
        ui.start()
        ui.join()
        global terminate
        terminate = True
    
    simulator.join()


if __name__ == '__main__':
    run_simulation()


























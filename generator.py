

import agent
import rand


class Generator:
    def __init__(self, agent_queue, x_range, y_range):
        # seed the random number generator
        rand.srand(11)
        self.agent_queue = agent_queue
        self.x_range = x_range
        self.y_range = y_range
        self.num_agents = 1500
        self.next_agent = 0 # this is the next agent to be placed on the grid
        self._generateAgents()

    def _generateAgents(self):
    	self.agents = [agent.Agent(0, 0, self._randVelocity(), self._randDirection()) for i in range(self.num_agents)]

    def _randVelocity(self):
        rand.rand(1, 10)

    def _randDirection(self):
        rand.rand(0, 2)
       
    def getState(self):
        for agent in self.agents:
            pass

    def mainLoop(self):
        while True:
            coordinates = [(rand.rand(0, self.x_range), rand.rand(0, self.y_range)) for i in xrange(1500)]
            self.agent_queue.put(coordinates)   # Python queue blocks by default if it is full. So no need to worry 
                                                # about checking if the queue is full, it already takes care of that 
                                                # for you.




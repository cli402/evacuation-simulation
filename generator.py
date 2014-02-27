import rand
import utils

from event import Event
from agent import Agent
from vector import Vector

#for gaussian cdf
from scipy.stats import norm


class Generator:
    left = 0
    generated = 0

    def __init__(self, door, door_coords, total, consider_time):
        print 'generator created to produce',total,'agents in door', door
        self.door = door
        self.min_coord = (door_coords[0], door_coords[1])
        self.max_coord = (door_coords[0] + door_coords[2], door_coords[1] + door_coords[3])
        self.left = total
        self.consider_time = consider_time

    def generate(self):
        startx = rand.rand(self.min_coord[0], self.max_coord[0])
        starty = rand.rand(self.min_coord[1], self.max_coord[1])

        rand_val = rand.gaussian_rand()
        travel_interval = int(round(norm.cdf(rand_val)*10.0)) + 1  # add 1 so we don't get a zero velocity
        agent = Agent(chr(self.door) + '_' + chr(self.left), travel_interval, self.consider_time, Vector(startx, starty))
        self.left -= 1
        return agent
	
    def next_event(self):
        if not self.left : return None
        queue_time = rand.rand(0, 29)
        return Event(self, 'new_agent', queue_time)

	def first_event(self):
		return self.next_event()







































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
		#self.goals = utils.sort_goals(self.min_coord, goal_coords)
		self.left = total
		self.consider_time = consider_time
		self.door_coord_list = [Vector(self.min_coord[0], self.min_coord[1]),
								Vector(self.max_coord[0], self.max_coord[1])]

	def generate(self, available_list):
		assert len(available_list), 'No place to generate on'
		available_cell = available_list[rand.rand(0, len(available_list) - 1)]
		rand_val = rand.gaussian_rand()
		travel_interval = int(round(norm.cdf(rand_val)*10.0)) + 12  # we want of range of 12 - 22
		agent = Agent(self.door + '_' + str(self.left), travel_interval, self.consider_time, available_cell)
		self.left -= 1
		return agent
	
	def next_event(self):
		if not self.left : return None
		queue_time = rand.rand(0, 29)
		return Event(self, 'new_agent', queue_time)
	
	def first_event(self):
		return self.next_event()


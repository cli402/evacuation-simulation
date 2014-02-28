import rand
import utils

from event import Event
from agent import Agent
from vector import Vector

#for gaussian cdf
from scipy.stats import norm

class Human_source:
	total = 0
	
	def __init__(self, total):
		self.total = total

	def get(self):
		if self.total :
			self.total -= 1
			return True
		else :
			return False


class Generator:
	generated = 0

	def __init__(self, door, door_coords, source, consider_time):
		print 'generator created to produce agents in door', door
		self.door = door
		self.min_coord = (door_coords[0], door_coords[1])
		self.max_coord = (door_coords[0] + door_coords[2], door_coords[1] + door_coords[3])
		#self.goals = utils.sort_goals(self.min_coord, goal_coords)
		self.consider_time = consider_time
		self.source = source
		self.door_coord_list = [Vector(self.min_coord[0], self.min_coord[1]),
								Vector(self.max_coord[0], self.max_coord[1])]

	def generate(self, available_list):
		assert len(available_list), 'No place to generate on'
		self.generated += 1
		available_cell = available_list[rand.rand(0, len(available_list) - 1)]
		rand_val = rand.gaussian_rand()
		travel_interval = int(round(norm.cdf(rand_val)*10.0)) + 12  # we want of range of 12 - 22
		agent = Agent(self.door + '_' + str(self.generated), travel_interval, self.consider_time, available_cell)
		return agent

	def left(self):
		if self.source.get() : return True
		else : return False
	
	def next_event(self):
		queue_time = rand.rand(0, 29)
		return Event(self, 'new_agent', queue_time)
	
	def first_event(self):
		return self.next_event()


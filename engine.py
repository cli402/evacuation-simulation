'''
engin.py

This is the engine of whole simulation, charge of event priority queue maintain

Author: Jier Chen
'''
#!/usr/bin/python

import random
from event import Event_queue, Event

class Engine:
	time_elapse = 0
	active_agents = 0
	action_list = {}
	event_queue = None
	end_condition = False
	
	def __init__(self, terrain, generator_list):
		print 'engine created !'
		self.terrain = terrain
		self.action_list['agent_move'] = self.move_agent
		self.action_list['agent_die'] = self.dispose_agent
		self.action_list['new_agent'] = self.create_agent
		self.event_queue = Event_queue()
		for generator in generator_list :
			self.event_queue.add_priority_queue(generator.next_event())

	def create_agent(self, event) :
		generator = event.entity
		agent = generator.generate()
		self.terrain.add_agent(agent)
		self.event_queue.add_priority_queue(Event(agent, 'agent_move', 0))
		self.active_agents += 1
		if generator.left : return True
		else : return False

	def dispose_agent(self, event) :
		agent = event.entity
		self.terrain.remove_agent(agent)
		self.active_agents -= 1
		if self.active_agents == 0 : self.end_condition = True
		return False

	def move_agent(self, event) :
		agent = event.entity
		available_list = self.terrain.get_available_surrounding(agent)
		if available_list :
			direction = agent.moving_direction(available_list) 
			release_grid = agent.coordinate
			print '[%4d]: ' % self.time_elapse,
			print "agent",agent.ID," move from "+str(agent.coordinate),
			self.terrain.move(agent, direction)
			agent.move(direction)
			print "to " + str(agent.coordinate)
			for agents_other in self.terrain.block_agents_around(release_grid):
				self.event_queue.add_priority_queue(agents_other.next_event())
		else :
			agent.block()
		return True

	def step_simulate(self):
		event = self.event_queue.get_event()
		while event :
			entity = event.entity
			if self.action_list[event.event_type](event) :
				self.event_queue.add_priority_queue(entity.next_event())
			event = self.event_queue.get_event()
		self.event_queue.priority_queue_roll()
		self.time_elapse += 1


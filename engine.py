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
	action_list = {}	#This is a function array, every function inside correspond with an event type
	event_queue = None
	end_condition = False
	
	def __init__(self, terrain, initial_event_list):
		print 'engine created !'
		self.terrain = terrain	#Terrain is an given data, should be initialized in main
		#Set operating function into array
		self.action_list['agent_move'] = self.move_agent
		self.action_list['agent_die'] = self.dispose_agent
		self.action_list['new_agent'] = self.create_agent
		self.event_queue = Event_queue()
		for initial_event in initial_event_list :
			self.event_queue.add_priority_queue(initial_event.next_event())

	def create_agent(self, event) :
	#This function is to create an agent and set it on its coordinate on map
		generator = event.entity
		agent = generator.generate()
		self.terrain.add_agent(agent)
		self.event_queue.add_priority_queue(Event(agent, 'agent_move', 0))
		self.active_agents += 1
		if generator.left : return True
		else : return False

	def dispose_agent(self, agent) :
	#This function is to delete an agent from terrain
		self.terrain.remove_agent(agent)
		self.active_agents -= 1
		#If there is no agent left, simulation terminated
		if self.active_agents == 0 : self.end_condition = True
		return False

	def move_agent(self, event) :
	#This is to move an agent to it destinated position, this should really be called most frequently
	#This need to be adapt new version
		agent = event.entity
		if self.terrain.good_to_exit(agent) : 
			self.dispose_agent(agent)
			return False
		available_list = self.terrain.get_available_surrounding(agent)
		direction = agent.moving_direction(available_list) 
		if direction : 
			print '[%4d]: ' % self.time_elapse,"agent",agent.ID," move from "+str(agent.coordinate),
			self.terrain.move(agent, direction)
			agent.move(direction)
			print "to " + str(agent.coordinate)
		else :
			print '[%4d]: ' % self.time_elapse,"agent",agent.ID,"stucked"
			print 'Stuck at:',str(agent.coordinate)
			print 'Value is:',self.terrain.terrain_shape[agent.coordinate.y][agent.coordinate.x]
			agent.block()
		return True

	def step_simulate(self):
	#kernel of engine
	#Every time randomly pick an event from queue 0, and execute it
		event = self.event_queue.get_event()
		while event :
			entity = event.entity
			#Use the event_type as the key to get corresponding fucntion
			if self.action_list[event.event_type](event) :
				self.event_queue.add_priority_queue(entity.next_event())
			#If the return value is false means the event is an final event
			#If return turn then push next event back into priority queue
			event = self.event_queue.get_event()
		#No event left in queue 0, roll the whole priority queue
		self.event_queue.priority_queue_roll()
		self.time_elapse += 1

	def flush_agent(self):
		info_list = []
		for agent in self.terrain_set.values() :
			info_element = ((agent.coordinate.x,agent.coordinate.y), agent.ID, agent.status)
			info_list.appent(info_element)

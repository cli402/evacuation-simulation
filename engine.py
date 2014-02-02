#!/usr/bin/python

import random
from vector import Vector
from event import Event,Event_queue
from terrain import Terrain
from agent import Agent

class Engine:
	time_elapse = 0
	active_agents = 0
	
	def __init__(self):
		pass

	def init_agents(self):
		start_point = Vector(0,0)
		end_point = Vector(10,10)
		agent = Agent(10, 3, start_point, end_point)
		terrain.add_agent(agent)
		event = Event(agent, 'move')
		event_queue.add_priority_queue(event, 0)
		self.active_agents = 1

		start_point = Vector(1,0)
		end_point = Vector(10,9)
		agent = Agent(8, 3, start_point, end_point)
		terrain.add_agent(agent)
		event = Event(agent, 'move')
		event_queue.add_priority_queue(event, 0)
		self.active_agents = 2

		return 

	def step_simulate(self):
		event = event_queue.get_event()
		print 'time', self.time_elapse
		while event :
			agent = event.agent
			if event.event_type == 'move' :
				available_list = terrain.get_available_surrounding(agent)
				direction = agent.moving_direction(available_list) 
				terrain.move(agent, direction)
				interval = agent.move(direction)

				if agent.coordinate == agent.destination : 
					terrain.remove_agent(agent)
					self.active_agents -= 1
				else :
					event_queue.add_priority_queue(Event(agent, 'move'), interval)

			event = event_queue.get_event()
		event_queue.priority_queue_roll()
		self.time_elapse += 1


engine = Engine()
terrain = Terrain()
event_queue = Event_queue()

if __name__=="__main__" :
	engine.init_agents()
	while engine.active_agents :
		engine.step_simulate()

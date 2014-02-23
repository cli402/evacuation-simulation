'''
Basic of event class and event queue

Author: Jier Chen
'''
import random


class Event():
#Basic event type
	event_type = 'move'
	entity = None
	type_set = set(['new_agent', 'agent_die','agent_move', 'none'])
	scheduled_time = 0
	
	def __init__(self, entity, event_type , scheduled_time = 0) : 
		if event_type in self.type_set : 
			self.event_type = event_type
		self.entity = entity
		self.scheduled_time = scheduled_time
		return 

class Event_queue:
#This is the priority, has 50 queue that tractable
#Any event over 50 will be set together into a pool
	priority_queue_list = None

	def __init__(self):
		self.priority_queue_list = [[] for i in range(50)]
		return

	def add_priority_queue(self, event):
	#Add a event into queue
		priority = event.scheduled_time
		priority_queue = self.priority_queue_list[priority]
		priority_queue.append(event)
		return

	def get_event(self):
	#Get a event from queue
		priority_queue = self.priority_queue_list[0]
		if priority_queue :
			index = random.randint(0,len(priority_queue)-1)
			event = priority_queue[index]
			del priority_queue[index]
			return event
		else : return False

	def add_waiting_queue(self, event):
		pass

	def priority_queue_roll(self):
	#Roll down every queue to lower level
	#Should always keep the queue list length 50
		del self.priority_queue_list[0]
		self.priority_queue_list.append([])

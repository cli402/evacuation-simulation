'''
Basic of event class and event queue

Author: Jier Chen
'''
import random

MAX_PQ_LENGTH = 50
# Note! The priority queue has been extended to more than 50. 
# There is no clear upper bound for event schedule time in future
# It is safe to pass larger value into Priority Queue

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
	far_event_pool = []

	def __init__(self):
		self.priority_queue_list = [[] for i in range(MAX_PQ_LENGTH)]
		self.far_event_pool = []
		return

	def add_priority_queue(self, event):
	#Add a event into queue
		if event.scheduled_time < MAX_PQ_LENGTH :	# if event sched time is inside MAX PQ length, then add it into corresponding queue
			priority = event.scheduled_time
			priority_queue = self.priority_queue_list[priority]
			priority_queue.append(event)
		else :	# if event exceeded 50, then add it to far event pool
			self.far_event_pool.append((event.scheduled_time, event))
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
		rear_queue = self.priority_queue_list[-1]
	
		# all sched time minus 1 means time flips
		self.far_event_pool = 				\
			[(scheduled_time-1,event) 		\
			for scheduled_time, event in self.far_event_pool]
		total = 0
		# put all the event that happen inside 50 in to priority queue
		for scheduled_time, event in enumerate(self.far_event_pool) :
			if scheduled_time < MAX_PQ_LENGTH :
				rear_queue.append(event)
				total += 1
		self.far_event_pool = self.far_event_pool[total:]
				

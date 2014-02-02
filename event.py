import random


class Event():
	event_type = 'move'
	agent = None
	type_set = set(['wait','move'])
	
	def __init__(self, agent, event_type = 'move') : 
		if event_type in self.type_set : 
			self.event_type = event_type
		self.agent = agent
		return 

class Event_queue:
	priority_queue_list = None

	def __init__(self):
		self.priority_queue_list = [[] for i in range(30)]
		return

	def add_priority_queue(self, event, priority):
		priority_queue = self.priority_queue_list[priority]
		priority_queue.append(event)
		return

	def get_event(self):
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
		del self.priority_queue_list[0]
		self.priority_queue_list.append([])

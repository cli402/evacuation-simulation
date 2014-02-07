from vector import Vector
from event import Event

class Agent:
	ID = ''
	travel_interval = 0
	considering_time = 0
	coordinate = None
	destination = None
	status = ''
	next_wait_time = 0
	last_move = Vector(0,0)

	def __init__(self, ID, t_interval, c_time, coordinate, destination):
		self.ID = ID
		self.travel_interval = t_interval
		self.considering_time = c_time
		self.coordinate = coordinate
		self.destination = destination
		self.status = 'waiting'
		self.next_wait_time = 0
#		print "agent initialed on"+str(coordinate)+"to"+str(destination)
		
	def moving_direction(self, available_list):
		willing_direction = self.destination - self.coordinate
		willing_direction.x = 1 if willing_direction.x>0 else -1 if willing_direction.x<0 else 0
		willing_direction.y = 1 if willing_direction.y>0 else -1 if willing_direction.y<0 else 0
#		print "willing direction" + str(willing_direction)
		selected_direction = Vector(0,0)
		delta_len = 10
		for direction in available_list :
			delta = willing_direction - direction
			if delta.length() < delta_len :
				selected_direction = direction
				delta_len = delta.length()
#		print "selected direction" + str(selected_direction)
		return selected_direction

	def next_event(self):
		if self.coordinate == self.destination : return Event(self, 'agent_die', 5)
		if self.last_move.diagonal() : interval = int(self.travel_interval*1.414)
		else : interval = self.travel_interval
		return Event(self,'agent_move',self.next_wait_time)

	def move(self, direction):
#		print "agent",self.ID," move from "+str(self.coordinate),
		self.coordinate += direction
		self.last_move = direction
		self.status = 'waiting'
#		print "to " + str(self.coordinate)
		if self.last_move.diagonal() : self.next_wait_time = int(self.travel_interval*1.414)
		else : self.next_wait_time = self.travel_interval
		return
	
	def block(self) :
		self.status = 'blocking'
		self.next_wait_time = 0
		return

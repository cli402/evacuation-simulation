from vector import Vector
from event import Event
import random as rd
from math import exp

class Agent:
	ID = ''
	travel_interval = 0
	considering_time = 0
	coordinate = None
	status = ''
	next_wait_time = 0
	last_move = Vector(0,0)

	def __init__(self, ID, t_interval, c_time, coordinate):
		self.ID = ID
		self.travel_interval = t_interval
		self.considering_time = c_time
		self.coordinate = coordinate
		self.status = 'waiting'
		self.next_wait_time = 0

	def get_wait_time(self, free, occupied) :
		coefficient = 1.0 if self.last_move.diagonal() else 1.414
		assert free != 0 : 'No place to go, Agent should be blocked' 
		if occupied != 0 : coefficient /= (1-exp(-float(free) / float(occupied)))

		print 'free', free, 'occupied', occupied, 'Coefficient',coefficient
		return int(self.travel_interval * coefficient)
		
	def moving_direction(self, available_list):
		#low_list is list of direction that goes down
		#inside which all difference on non-diagonal directions will multiple by 2
		#this is to urge agent go streight, also avoid aimless wandering on streight road
		if not available_list : return None
		low_list = []
		for i,(delt,direction) in enumerate(available_list) :
			if not direction.diagonal :
				delt *= 2
				available_list[i] = (delt,direction)
			if delt > 0 : low_list.append((delt,direction))
			#delt > 0 mean new place lower than current

		if len(low_list) :	# if there exist lower places, if not will be complete later
			counter = 0		# for randomization
			low_list.sort()	
			low_list.reverse()	#Make low_list descendent that first one always be the greatest
			for i,(delt,direction) in enumerate(low_list) :
				if low_list[0][0] - delt >= 10 :	# low place delta value 10 less than the greatest will be eliminated
					low_list = low_list[:i]
					break
				else : counter += delt	#add total counter for randomly choose direction

			p = rd.randint(0,counter)	#p is pointer to which to choose
			for i,(delt,direction) in enumerate(low_list) :
				p -= delt
				if p <= 0 : return direction
		else :	# if there is no available places to go, should be down later
			pass

	def next_event(self):
		return Event(self,'agent_move',self.next_wait_time)

	def move(self, direction, density):
#		print "agent",self.ID," move from "+str(self.coordinate),
		self.coordinate += direction
		self.last_move = direction
		self.status = 'waiting'
#		print "to " + str(self.coordinate)
		free, occupied = density
		self.next_wait_time = self.get_wait_time(free, occupied)
		return
	
	def block(self) :
		self.status = 'blocking'
		self.next_wait_time = self.considering_time
		return

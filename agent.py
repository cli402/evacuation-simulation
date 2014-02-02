from vector import Vector

class Agent:
	travel_interval = 0
	considering_time = 0
	coordinate = None
	destination = None

	def __init__(self, t_interval, c_time, coordinate, destination):
		self.travel_interval = t_interval
		self.considering_time = c_time
		self.coordinate = coordinate
		self.destination = destination
		print "agent initialed on"+str(coordinate)+"to"+str(destination)
		
	def moving_direction(self, available_list):
		willing_direction = self.destination - self.coordinate
		willing_direction.x = 1 if willing_direction.x>0 else -1 if willing_direction.x<0 else 0
		willing_direction.y = 1 if willing_direction.y>0 else -1 if willing_direction.y<0 else 0
		print "willing direction" + str(willing_direction)
		selected_direction = Vector(0,0)
		delta_len = 10
		for direction in available_list :
			delta = willing_direction - direction
			if delta.length() < delta_len :
				selected_direction = direction
				delta_len = delta.length()
		print "selected direction" + str(selected_direction)
		return selected_direction

	def move(self, direction):
		print "agent move from "+str(self.coordinate),
		self.coordinate += direction
		print "to " + str(self.coordinate)
		if direction.diagonal() : return int(self.travel_interval*1.414)
		else : return self.travel_interval

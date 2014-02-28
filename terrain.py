from vector import Vector
from event import Event

direction_vectors = [Vector(1,1),Vector(1,0),Vector(1,-1),Vector(0,-1),
					Vector(-1,-1),Vector(-1,0),Vector(-1,1),Vector(0,1),]

#class Traffic_light

class Terrain:
	terrain_set = {}
	terrain_shape = []
	width,depth = 0,0
	
	def __init__(self, filename) :
		file_handle = open(filename,'r')
		self.terrain_shape = []
		print "Initializing map"
		#Read every value of evacuation feild
		#And cover them into num stored in a simple 2D list
		for line in file_handle.readlines() :
			num_list = [int(num) for num in line.split()]
			if num_list : self.terrain_shape.append(num_list)
		self.depth = len(self.terrain_shape)
		self.width = len(self.terrain_shape[3])
		print 'map created with: width', self.width, 'depth', self.depth

	def add_agent(self, agent) :
	#Add a new agent on the map
		if not self.available(agent.coordinate) : return False
		else :
			self.terrain_set[agent.coordinate] = agent
			return True

	def remove_agent(self, agent) :
	#Remove an agent from the map
		del self.terrain_set[agent.coordinate]

	def good_to_exit(self, agent) :
	#Check whether the agent is good to leave
		if self.terrain_shape[agent.coordinate.y][agent.coordinate.x] == 0 : return True
		else : return False

	def get_available_surrounding(self, agent) :
		available_list = []
		for direction in direction_vectors :
			neighborhood = agent.coordinate + direction
			if self.available(neighborhood) : 
				delt = self.terrain_shape[agent.coordinate.y][agent.coordinate.x]-self.terrain_shape[neighborhood.y][neighborhood.x]
				available_list.append((delt,direction))
#		print 'available surrounding is'+''.join([str((delt,str(vector))) for delt,vector in available_list])
		return available_list

	def valid(self, position):
#		print 'Checking', str(position);
		if (position.x < 0) or (position.y < 0) : return False
		elif (position.x >= self.width) or (position.y >= self.depth) : return False
		elif (self.terrain_shape[position.y][position.x] > 30000) : return False
		else : return True
			
	def available(self, position):
		if not self.valid(position) : return False
		if self.terrain_set.get(position) : return False
		else : return True

	def get_availables(self, coord_list) :
		available_list = []
		for coord in coord_list :
			if self.available(coord) :
				available_list.append(coord)
		return available_list

	def scan_density(self, position, distance):
		free, occupied = 0,-1
		for i in range(position.x - distance, position.x + distance + 1) :
			for j in range(position.y - distance, position.y + distance + 1) :
				if self.valid(Vector(i,j)) :
					if self.available(Vector(i,j)) : free += 1
					else : occupied += 1
#		print 'scaning free', free, 'occupied', occupied
		return free, occupied

	def move(self, agent, direction):
		del self.terrain_set[agent.coordinate] 
		self.terrain_set[agent.coordinate+direction] = agent

	def block_change(self, area, delta) :
		for start_point, end_point in area :
#			assert self.valid(start_point) and self.valid(end_point), "Invalid block change coordinate "+str(start_point)+' '+str(end_point)
			for i in range(start_point.y, end_point.y+1) :
				for j in range(start_point.x, end_point.x+1) :
					self.terrain_shape[i][j] += delta

class Traffic_light():
	area = None
	green_time, red_time = 0,0
	current_color = 0

	def __init__(self, area, timming, initial_color) :
#Traffic_light does not really care what format of light area is, Terrain should take care about it 
#timming is (green_time, red_time)
#initial_color, -1 means green light, 1 means red light
		self.area = area
		self.green_time, self.red_time = timming
		self.current_color = initial_color

	def switch(self) :
		self.current_color *= -1
#		print 'Traffic Light', self.area, 'switch to', 'green' if self.current_color < 0 else 'red'
		return self.area, self.current_color * 100
	
	def next_event(self) :
		return Event(self, 'light_switch', self.green_time if self.current_color < 0 else self.red_time)

	def first_event(self) :
		if self.current_color < 0 : 
			return Event(self, 'light_switch', self.green_time)
		else :
			self.current_color = -1
			return Event(self, 'light_switch', 0)
		
		
		
		

if __name__=='__main__' :
	terrain = Terrain("grid_bits.txt")
	for i in range(450):
		if terrain.valid(Vector(i,297)) : 
			print '%d,298' % i ,'valid'

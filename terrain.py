from vector import Vector
import struct as st

direction_vectors = [Vector(1,1),Vector(1,0),Vector(1,-1),Vector(0,-1),
					Vector(-1,-1),Vector(-1,0),Vector(-1,-1),Vector(0,1),]
class Terrain:
	terrain_set = {}
	terrain_shape = []
	width,depth = 0,0
	
	def __init__(self, filename) :
		file_handle = open(filename,'rb')
		self.width = st.unpack("i", file_handle.read(4))[0]
		self.depth = st.unpack("i", file_handle.read(4))[0]
		self.terrain_shape = [[False for j in range(self.width)] for i in range(self.depth)]

		print 'map created with: depth',len(self.terrain_shape),'width',len(self.terrain_shape[3])

		for i in range(self.depth) :
			for j in range(self.width/32) :
				decoder = st.unpack("i", file_handle.read(4))[0]
				for k in range(32) :
					self.terrain_shape[i][j*32+k] = True if (decoder & (1 << (32-k))) else False
		
	def add_agent(self, agent) :
		if not self.available(agent.coordinate) : return False
		else :
			self.terrain_set[agent.coordinate] = agent
			return True

	def block_agents_around(self, position) :
		for delta in direction_vectors :
			agent = self.terrain_set.get(position+delta)
			if agent and agent.status == 'block' : yield agent
			return 

	def remove_agent(self, agent) :
		del self.terrain_set[agent.coordinate]

	def get_available_surrounding(self, agent) :
		available_list = []
		for direction in direction_vectors :
			neighborhood = agent.coordinate + direction
			if self.available(neighborhood) : 
				available_list.append(direction)
#		print 'available surrounding is'+''.join([str(vector) for vector in available_list])
		return available_list

	def valid(self, position):
		if (position.x < 0) or (position.y < 0) \
		or (position.x > self.width) or (position.y > self.depth) \
		or (not self.terrain_shape[position.y][position.x]):
			return False
		else : return True
			
	def available(self, position):
		if not self.valid(position) : return False
		if self.terrain_set.get(position) : return False
		else : return True

	def move(self, agent, direction):
		del self.terrain_set[agent.coordinate] 
		self.terrain_set[agent.coordinate+direction] = agent

if __name__=='__main__' :
	terrain = Terrain()
	for i in range(480):
		if terrain.valid(Vector(i,297)) : 
			print '%d,298' % i ,'valid'

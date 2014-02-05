from vector import Vector

direction_vectors = [Vector(1,1),Vector(1,0),Vector(1,-1),Vector(0,-1),
					Vector(-1,-1),Vector(-1,0),Vector(-1,-1),Vector(0,1),]
class Terrain:
	terrain_set = {}
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
		print 'available surrounding is'+''.join([str(vector) for vector in available_list])
		return available_list

	def valid(self, position):
# boundary detection, to be updated
		if (position.x < 0) or (position.y < 0) \
		or (position.x > 20) or (position.y > 20) \
		or (position == Vector(5,5)):
			return False
		else : return True
			
	def available(self, position):
		if not self.valid(position) : return False
		if self.terrain_set.get(position) : return False
		else : return True

	def move(self, agent, direction):
		del self.terrain_set[agent.coordinate] 
		self.terrain_set[agent.coordinate+direction] = agent



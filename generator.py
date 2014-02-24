from event import Event
from agent import Agent
from vector import Vector

class Generator:
	left = 0
	generated = 0
	
	def __init__(self, total):
		print 'generator created to produce',total,'agents'
		self.left = total
	
	def generate(self) :
		agent = Agent(chr(65+self.left), 10, 3, Vector(201,295))
		self.left -= 1
		return agent
	
	def next_event(self):
		if not self.left : return None
		return Event(self,'new_agent',5)


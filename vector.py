import math

class Vector:
	x,y = 0,0
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __add__(self, delta):
		return Vector(self.x+delta.x, self.y+delta.y)

	def __radd__(self, delta):
		return Vector(delta.x+self.x, delta.y+self.y)

	def __mul__(self, k):
		return Vector(self.x*k, self.y*k)

	def __rmul__(self, k):
		return Vector(k*self.x, k*self.y)

	def __neg__(self):
		return Vector(-self.x, -self.y)

	def __pos__(self):
		return self

	def __sub__(self, delta):
		return Vector(self.x-delta.x, self.y-delta.y)

	def __rsub__(self, delta):
		return Vector(delta.x-self.x, delta.y-self.y)

	def __nonzero__(self):
		return True

	def __str__(self):
		return '('+str(self.x)+','+str(self.y)+')'

	def __eq__(self, delta):
		if (self.x == delta.x and self.y == delta.y) : return True
		else : return False

	def __hash__(self):
		return self.x * 100000 + self.y

	def diagonal(self):
		if self.x*self.y : return True
		else : return False

	def length(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

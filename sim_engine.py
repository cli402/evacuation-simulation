import Queue
import random
import threading

class person:
	x,y = 0,0
	dx,dy = 0,0
	def __init__(self,dx,dy):
		self.x,self.y = 0,0
		self.dx,self.dy = dx,dy

	def setxy(self,x,y):
		self.x,self.y = x,y

	def next_move(self):
		newx,newy = self.x+self.dx, self.y+self.dy
		newx = (newx + 50) % 100 - 50
		newy = newy % 100
		return newx,newy

mapset = [[None for i in range(100)] for i in range(100)]
queue = Queue.Queue(maxsize =100)

def get_initial_xy():
	x,y = random.randint(-50,49),random.randint(0,99)
	while (mapset[x][y]) :
		x,y = random.randint(-50,49),random.randint(0,99)
	return x,y
	
if __name__=='__main__' :
	array = []
	for i in range(100) :
		dx,dy = (random.randint(-1,1),random.randint(-1,1))
		p = person(dx,dy)
		x,y = get_initial_xy()
		print x,y
		p.setxy(x,y)
		mapset[x][y] = p
		array.append(p)

#	exit()

	for times in range(10) :
		i = random.randint(0,99)
		newx,newy = array[i].next_move()
		if not mapset[newx][newy] :
			mapset[array[i].x][array[i].y] = None
			array[i].setxy(newx,newy)
			mapset[newx][newy] = array[i]
		cor_list = []
		for p in array :
			cor_list.append((p.x,p.y))
#		queue.put(cor_list)
		print cor_list





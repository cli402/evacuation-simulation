'''
Created on Jan 25, 2014

@author: saneal
'''


import math


class Agent:
    def __init__(self, x, y, velocity, direction):
        self.x = x
        self.y = y
        self.v = velocity
        self.c = 0
        self.direction = direction
    def Direction(self, choice):
        self.c = choice
        if choice == 1:
            p_move = [self.x, self.y+1, self.v]
            return p_move
        elif choice == 2:
            p_move = [self.x+1, self.y+1, self.v*math.sqrt(2)]
            return p_move
        elif choice == 3:
            p_move = [self.x-1, self.y+1, self.v*math.sqrt(2)]
            return p_move
        elif choice == 4:
            p_move = [self.x+1, self.y, self.v]
            return p_move
        elif choice == 5:
            p_move = [self.x-1, self.y+1, self.v]
            return p_move
        elif choice == 6:
            p_move = [self.x, self.y-1, self.v]
            return p_move
        elif choice == 7:
            p_move = [self.x+1, self.y-1, self.v*math.sqrt(2)]
            return p_move
        else:
            p_move = [self.x-1, self.y-1, self.v*math.sqrt(2)]
            return p_move
            
        
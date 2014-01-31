'''
 rand.py

 author: Daniel Henderson
'''

#c = 12345
#max_int = 1 << 32 
m = (1 << 31) - 1
a = 48271
q = 44488
r = 3399
x = 0


def rand(min=None, max=None):
    global x
    t = (a * (x % q)) - (r * (x / q))
    x = t if t > 0 else t + m
    tempx = x
    if (min and max):
        tempx = tempx % ((max + 1) - min) + min
    elif min:
        tempx = tempx + min
    elif max:
	    tempx = tempx % (max + 1)
    #x = (a * x) % m
    #x = (a * x + c) % m
    return tempx;

def srand(seed):
    global x
    x = seed

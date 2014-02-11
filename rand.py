'''
 rand.py

 author: Daniel Henderson
'''


import math


#c = 12345
#max_int = 1 << 32 
m = (1 << 31) - 1  #modulus, this is the max number that can be generated
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


def rand_float():
    return float(rand()) / float(m)




# This is a callable class that is used to retain state of the Gaussian number
# generator. DO NOT USE THIS DIRECTLY!!! It should be used through the function
# down below it.
class gaussian_class(object):
    def __init__(self):
        self.y1 = None
        self.y2 = None

    def __call__(self):
        if self.y1 is None:
            while True:
                x1 = 2.0 * rand_float() - 1.0
                x2 = 2.0 * rand_float() - 1.0
                w = (x1 * x1) + (x2 * x2)
                if (w > 0.0) and (w < 1.0):
                    break

            w = math.sqrt((-2.0 * math.log(w)) / w)
            self.y1 = x1 * w
            self.y2 = x2 * w
            return self.y1
        else:
            self.y1 = None
            return self.y2


# This is the actual function to call for generating Gaussian values
gaussian_rand = gaussian_class()




#******************************************************************************
#*************** Here and below is just for testing purposes ******************
#******************************************************************************

def chi_square_test_uniform_dist(n, k, samples):
    bin_counts = []
    bin_size = int(math.ceil(n/k))
    for i in range(k):
        count = 0
        minimum = float(i) / float(k)
        maximum = float(i + 1) / float(k)
        for samp in samples:
            if (samp >= minimum) and (samp < maximum):
                count += 1
        bin_counts.append(count)

    chi_square = 0.0
    for count in bin_counts:
        numerator = count - bin_size
        chi_square += float(numerator * numerator) / float(bin_size)

    print chi_square


def chi_square_test_gaussian_dist(n, k, samples, bins, expected_counts):
    bin_counts = []
    for minimum, maximum in bins:
        count = 0
        for samp in samples:
            if (samp >= minimum) and (samp < maximum):
                count += 1
        bin_counts.append(count)

    with open("gaussian_values.csv", "w") as fo:
        for count in bin_counts:
            fo.write("%d\n"%(count))    

    chi_square = 0.0
    for i, count in enumerate(bin_counts):
        numerator = count - expected_counts[i]
        chi_square += float(numerator * numerator) / float(expected_counts[i])

    print chi_square


# Test uniform distribution
def test_uniform_dist():
    n = 500
    k = 100
    samples = [rand_float() for i in xrange(n)]
    chi_square_test_uniform_dist(n, k, samples)


# Test Gaussian distribution
def test_gaussian_dist():
    n = 1008
    k = 8

    samples = [gaussian_rand() for i in xrange(n)]
    #with open("gaussian_values.csv", "w") as fo:
    #    for sample in samples:
    #        fo.write("%f\n"%(sample))

    expected_counts = [0.0013, 0.0214, 0.1359, 0.3413, 0.3413, 0.1359, 0.0214, 0.0013]
    expected_counts[:] = [x*n for x in expected_counts]
    bins = [(-float('Inf'), -3.0), (-3.0, -2.0), (-2.0, -1.0), (-1.0, 0.0), (0.0, 1.0), (1.0, 2.0), (2.0, 3.0), (3.0, float('Inf'))]
    chi_square_test_gaussian_dist(n, k, samples, bins, expected_counts)




#************ Main is just for testing purposes! ***************
if __name__ == '__main__':
    import time
    srand(time.time())

    #test uniform distribution
    #test_uniform_dist()

    #test Gaussian distribution
    test_gaussian_dist()


        

        














































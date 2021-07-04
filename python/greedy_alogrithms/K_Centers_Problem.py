import random;
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    min = 0
    max = 200
    vertexes = set()
    for i in range(0, 100):
        vertexes.add(randomVertex(min, max))
    
    s_greedy = greedy(vertexes, 10)
    plot_points(s_greedy, "ro")
    plot_points(vertexes, "bo")
    plt.show()	

def plot_points(vertexes, marker):
	points = []
	for v in vertexes:
		points.append(v.points())

	xs = [x for [x, y] in points]
	ys = [y for [x, y] in points]

	plt.plot(xs, ys, marker)

def greedy(vertexes, k):
	s = []
	pick = randomPick(vertexes)
	s.append(pick)
	#print(pick)
	while len(s) < k:
		max = distance(vertexes, s)
		vertexes.remove(max)
		s.append(max)
	return s


def randomPick(vertexes):
	# Random pickup
	pick = random.sample(vertexes, 1)[0]
	vertexes.remove(pick)
	return pick

def distance(vertexes, picked):
	min = np.inf 
	min_v = None
	real_max = 0
	real_max_v = None
	for v in vertexes:
		min = np.inf
		for p in picked:	
			d = np.sqrt((v.x - p.x)**2 + (v.y - p.y)**2)
			#print("Current min %s vs %d" % (min, d))
			if d < min:
				min = d
				min_v = v
		if min > real_max:
			real_max = min 
			real_max_v = min_v
			
	print(real_max, real_max_v)

	return real_max_v
	
def randomVertex(min, max):
	return Vertex(random.randint(min, max), random.randint(min, max))

class Vertex:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s,%s)" % (self.x, self.y)

	def __repr__(self):
                return "(%s,%s)" % (self.x, self.y)

	def points(self):
		return [self.x, self.y]

if __name__ == "__main__":
	main()
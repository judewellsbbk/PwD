import numpy as np
import heapq

g = np.zeros((6,6), dtype=np.int)

# graph from the graphics, with a=0, b=1, ... f=5
g[0][1] = 7
g[0][2] = 9
g[0][5] = 14

g[1][2] = 10
g[1][3] = 15

g[2][3] = 11
g[2][5] = 2

g[3][4] = 6
g[4][5] = 9

#make the distance matrix symmetric
g = g + g.T


def main(g, source=0):
	""" educational implementation of Dijkstra's algo.
		requires neighboroughood
	"""
	print(g)
	n, m = g.shape

    # at the beginning, distances are set to 'infinity'
	dist = np.zeros((n, ), dtype=np.int)
	for i in range(n):
		dist[i] = -1

    # the predecessors are not set
	pred = np.zeros((n, ), dtype=np.int)
	for i in range(n):
		pred[i] = -1

    #source is at distance 0 from itself
	dist[source] = 0

    #source does not need predecessors
	pred[source] = 0

	visited = []

	# to_do is a heap, so to_do[0] always contains the 'lighter' element
	to_do = []
	allnodes = range(n)
	heapq.heappush(to_do, allnodes)

	while to_do:

		# node is extracted in constant time: it's in to_do[0]
		# however, log(n) operations to rebuild the heap
		node = heapq.heappop(to_do)

		visited.append(node)

		to_be_relaxed = neighbourhood(g, node)


		for neigh in to_be_relaxed:
			pred, dist = relax(g, node, neigh, pred, dist)

	print dist


def relax(g, node, neigh, pred, dist):
	""" it might decrease the distances from source of neigh
		if passing through node proves to be more economic
	"""

	print 'relaxing node '+str(neigh)

	rel = dist[node] + g[node][neigh]

	if (dist[neigh] > rel) or (dist[neigh] == -1): #needed to treat infinity
		new_dist[neigh] = rel
		new_pred[neigh] = node

 	return new_pred, new_dist


def neighbourhood(g, node):
	""" EXERCISE: given g, and a node, find node's neighbours
		look at the non-zero entries in g and collect indices in return list
	"""
	neighbour_list = []
	x, y = g.shape[0], g[1]

	for i in range(x):
		if g[]


main(g)

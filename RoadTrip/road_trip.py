#!/usr/bin/python

import sys

# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# Priority dictionary using binary heaps
# David Eppstein, UC Irvine, 8 Mar 2002



class priorityDictionary(dict):
    def __init__(self):
        '''Initialize priorityDictionary by creating binary heap
of pairs (value,key).  Note that changing or removing a dict entry will
not remove the old pair from the heap until it is found by smallest() or
until the heap is rebuilt.'''
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
        if len(self) == 0:
            raise IndexError, "smallest of empty priorityDictionary"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
	
    def __iter__(self):
        '''Create destructive sorted iterator of priorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
	
    def __setitem__(self,key,val):
        '''Change value stored in dictionary and add corresponding
pair to heap.  Rebuilds the heap if the number of deleted items grows
too large, to avoid memory leakage.'''
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort likely faster than O(n) heapify
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
	
    def setdefault(self,key,val):
        '''Reimplement setdefault to call our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]

def Dijkstra(graph,start,end=None):
	"""
	Find shortest paths from the start vertex to all
	vertices nearer than or equal to the end.

	The input graph G is assumed to have the following
	representation: A vertex can be any object that can
	be used as an index into a dictionary.  G is a
	dictionary, indexed by vertices.  For any vertex v,
	G[v] is itself a dictionary, indexed by the neighbors
	of v.  For any edge v->w, G[v][w] is the length of
	the edge.  This is related to the representation in
	<http://www.python.org/doc/essays/graphs.html>
	where Guido van Rossum suggests representing graphs
	as dictionaries mapping vertices to lists of neighbors,
	however dictionaries of edges have many advantages
	over lists: they can store extra information (here,
	the lengths), they support fast existence tests,
	and they allow easy modification of the graph by edge
	insertion and removal.  Such modifications are not
	needed here but are important in other graph algorithms.
	Since dictionaries obey iterator protocol, a graph
	represented as described here could be handed without
	modification to an algorithm using Guido's representation.

	Of course, G and G[v] need not be Python dict objects;
	they can be any other object that obeys dict protocol,
	for instance a wrapper in which vertices are URLs
	and a call to G[v] loads the web page and finds its links.

	The output is a pair (D,P) where D[v] is the distance
	from start to v and P[v] is the predecessor of v along
	the shortest path from s to v.

	Dijkstra's algorithm is only guaranteed to work correctly
	when all edge lengths are positive. This code does not
	verify this property for all edges (only the edges seen
 	before the end vertex is reached), but will correctly
	compute shortest paths even for some graphs with negative
	edges, and will raise an exception if it discovers that
	a negative edge has caused it to make a mistake.
	"""

	final_distances = {}	# dictionary of final distances
	predecessors = {}	# dictionary of predecessors
	estimated_distances = priorityDictionary()   # est.dist. of non-final vert.
	estimated_distances[start] = 0

	for vertex in estimated_distances:
		final_distances[vertex] = estimated_distances[vertex]
		if vertex == end: break

		for edge in graph[vertex]:
			path_distance = final_distances[vertex] + graph[vertex][edge]
			if edge in final_distances:
				if path_distance < final_distances[edge]:
					raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
			elif edge not in estimated_distances or path_distance < estimated_distances[edge]:
				estimated_distances[edge] = path_distance
				predecessors[edge] = vertex

	return (final_distances,predecessors)

def shortestPath(graph,start,end):
	"""
	Find a single shortest path from the given start vertex
	to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along
	the shortest path.
	"""

	final_distances,predecessors = Dijkstra(graph,start,end)
	path = []
	while 1:
		path.append(end)
		if end == start: break
		end = predecessors[end]
	path.reverse()
	return path

	
	
def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    if start==end:
        # we've found our end node, now find the path to it, and return
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxint)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

	
	
	
	
	
	
	
	
	

from collections import defaultdict


def path_cost(graph, path):
	o = path[0]
	cost = 0
	for i in path[1:]:
		cost += graph[o][i]
		o = i
	return cost

	
class LengthVertex():
	def __init__(length, time):
		self.length = length
		self.time = time
		
	

def main(argv):

	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)

	
	destinations = []
	length_graph = defaultdict(dict)
	speed_graph = defaultdict(dict)
	time_graph = defaultdict(dict)
	
	with open(argv[1],'r') as f: 
		(n, p, start) = tuple(map(int, f.readline().split()))
		
		for _ in range(0, p):
			(a,b, length, speed) = tuple(f.readline().split())
			length = int(length)
			speed = int(speed)
			time = float(length) / float(speed) * 60.0
			
			length_graph[a][b] = length
			length_graph[b][a] = length
			
			speed_graph[a][b] = speed
			speed_graph[b][a] = speed
			
			time_graph[a][b] = time
			time_graph[b][a] = time
	
		q = int(f.readline())		
		for _ in range(0, q):
			destinations.append(f.readline().strip())
			
	
	for d in destinations:
		shortest_length_path = shortestPath(length_graph, '0', d)
		shortest_speed_path = shortestPath(speed_graph, '0', d)
		
		t1 = path_cost(time_graph, shortest_length_path)
		t2 = path_cost(time_graph, shortest_speed_path)
		print  '%.2f'%abs(t1-t2)
	
		# (_,shortest_length_path) = shortestpath(length_graph, '0', d)
		# (_,shortest_speed_path) = shortestpath(speed_graph, '0', d)
		# print shortest_length_path
		# t1 = path_cost(time_graph, shortest_length_path)
		# t2 = path_cost(time_graph, shortest_speed_path)
		# print  '%.2f'%abs(t1-t2)
	
	
# -- The following code executes upon command-line invocation
if __name__ == "__main__": 
	main(sys.argv)
	
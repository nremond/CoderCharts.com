#!/usr/bin/python
# -*- coding: latin-1 -*-


import sys

def dijkstra(graph, start, end):
	"""
	Dijkstra's algorithm Python implementation.
	
	Arguments:
		graph: Dictionnary of dictionnary (keys are vertices).
		start: Start vertex.
		end: End vertex.
	
	Output:
		List of vertices from the beggining to the end.
		
	Example:
		
	>>> graph = {
	...	 'A': {'B': 10, 'D': 4, 'F': 10},
	...	 'B': {'E': 5, 'J': 10, 'I': 17},
	...	 'C': {'A': 4, 'D': 10, 'E': 16},
	...	 'D': {'F': 12, 'G': 21},
	...	 'E': {'G': 4},
	...	 'F': {'H': 3},
	...	 'G': {'J': 3},
	...	 'H': {'G': 3, 'J': 5},
	...	 'I': {},
	...	 'J': {'I': 8},
	... }	
	>>> dijkstra(graph, 'C', 'I')
	['C', 'A', 'B', 'I']
	
	"""
	
	D = {} # Final distances dict
	P = {} # Predecessor dict
	
	# Fill the dicts with default values
	for node in graph.keys():
		D[node] = -1 # Vertices are unreachable
		P[node] = "" # Vertices have no predecessors
		
	D[start] = 0 # The start vertex needs no move
	
	unseen_nodes = graph.keys() # All nodes are unseen
	
	while len(unseen_nodes) > 0:
		print "unseen_nodes:", unseen_nodes
	
		# Select the node with the lowest value in D (final distance)
		shortest = None
		node = ''
		for temp_node in unseen_nodes:
			if shortest == None:
				shortest = D[temp_node]
				node = temp_node
			elif D[temp_node] < shortest:
				shortest = D[temp_node]
				node = temp_node
				
		# Remove the selected node from unseen_nodes
		unseen_nodes.remove(node)
		
		# For each child (ie: connected vertex) of the current node
		for child_node, child_value in graph[node].items():
			if D[child_node] < D[node] + child_value:
				D[child_node] = D[node] + child_value
				# To go to child_node, you have to go through node
				P[child_node] = node
				
	# Set a clean path
	path = []
	
	# We begin from the end
	node = end
	
	print "P:",P
	print "D:",D
	
	
	# While we are not arrived at the beggining
	while not (node == start):
		#print "path:",path
		path.insert(0, node) # Insert the predecessor of the current node
		node = P[node] # The current node becomes its predecessor
	
	path.insert(0, start) # Finally, insert the start vertex
	
	return path
	
def main(argv):
	graph = {
			'A': {'B': 10, 'D': 4, 'F': 10},
			'B': {'E': 5, 'J': 10, 'I': 17},
			'C': {'A': 4, 'D': 10, 'E': 16},
			'D': {'F': 12, 'G': 21},
			'E': {'G': 4},
			'F': {'H': 3},
			'G': {'J': 3},
			'H': {'G': 3, 'J': 5},
			'I': {},
			'J': {'I': 8},
			}	

			
	# graph = {
			# 'A': {'B': 1, 'E': 6},
			# 'B': {'C': 2, 'D': 4, 'A': 1},
			# 'C': {'D': 3, 'B': 2},
			# 'D': {'E': 5, 'C': 3, 'B': 4},
			# 'E': {'F': 7, 'A': 6, 'D': 5},
			# 'F': {'E': 7}
			# }	
			
	print dijkstra(graph, 'C', 'I')


if __name__ == "__main__":
	main(sys.argv)

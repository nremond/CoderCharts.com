#!/usr/bin/python
# -*- coding: latin-1 -*-
		
from operator import itemgetter
import sys
import string

class DisjointSet(dict):
	def add(self, item):
		self[item] = item

	def find(self, item):
		parent = self[item]

		while self[parent] != parent:
			parent = self[parent]

		self[item] = parent
		return parent

	def union(self, item1, item2):
		self[item2] = self[item1]


def kruskal( nodes, edges ):
	forest = DisjointSet()
	mst = []
	for n in nodes:
		forest.add( n )

	sz = len(nodes) - 1

	for e in sorted( edges, key=itemgetter( 2 ) ):
		n1, n2, _ = e
		t1 = forest.find(n1)
		t2 = forest.find(n2)
		if t1 != t2:
			mst.append(e)
			sz -= 1
			if sz == 0:
				return mst

			forest.union(t1, t2)


def main(argv):
	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)
	
	input_filename = argv[1]
	fin = open(input_filename,'r')
	
	n = string.atoi(fin.readline().rstrip())
	e = string.atoi(fin.readline().rstrip())
	
	print n, e
	
	nodes = set()
	edges = list()
	
	for line in fin.readlines():
		line = line.rstrip().split()
		a = line[0]
		b = line[1]
		cost = string.atoi(line[2])
		nodes.add(a)
		nodes.add(b)
		edges.append((a,b,cost))
		
	print nodes, edges
	r = kruskal( nodes, edges )
	total_cost = 0
	for a,b,cost in r :
		total_cost += cost
		
	print total_cost
		
		
if __name__ == "__main__":
    main(sys.argv)			
			
			
			

# nodes = list( "ABCDEFG" )
# edges = [ ("A", "B", 7), ("A", "D", 5),
		  # ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
	  # ("C", "E", 5),
	  # ("D", "E", 15), ("D", "F", 6),
	  # ("E", "F", 8), ("E", "G", 9),
	  # ("F", "G", 11)]

	  
# nodes = list( "ABCDEF" )
# edges = [ ("A", "B", 1), 
		  # ("B", "C", 2),
		  # ("C", "D", 3), 
		  # ("B", "D", 4), 
		  # ("D", "E", 5),
		  # ("A", "E", 6),
		  # ("E", "F", 7) ]	  
	  
	  
# print kruskal( nodes, edges )
#output: [('A', 'D', 5), ('C', 'E', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'G', 9)]

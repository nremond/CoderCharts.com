#!/usr/bin/python

import sys, math, random


class Point:
	"""
	Represents a 2D point
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return repr((self.x, self.y))

def norm(p1,p2) :
	return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
		
		
# -- The Cluster class represents clusters of points in n-dimensional space
class Cluster:
	# Instance variables
	# self.points is a list of Points associated with this Cluster
	# self.centroid is the sample mean Point of this Cluster
	def __init__(self, points):
		self.points = points
	 
		# Figure out what the centroid of this Cluster should be
		self.centroid = self.calculateCentroid()
   
   # Return a string representation of this Cluster
	def __repr__(self):
		return str(self.points) + "centroid=" + str(self.centroid)
   
	# Update function for the K-means algorithm
	# Assigns a new list of Points to this Cluster, returns centroid difference
	def update(self, points):
		old_centroid = self.centroid
		self.points = points
		self.centroid = self.calculateCentroid()
		return norm(old_centroid, self.centroid)
	
	# Calculates the centroid Point - the centroid is the sample mean Point
	# (in plain English, the average of all the Points in the Cluster)
	def calculateCentroid(self):
		centroid = Point(0.0, 0.0)
		
		for p in self.points:
			centroid.x += p.x
			centroid.y += p.y
		
		n = len(self.points)
		centroid.x /= n
		centroid.y /= n
	   
		# Return a Point object using the average coordinates
		return centroid

def random_points(k):
	points = []
	for k in range(k):
		points.append(Point(random(), random()))
		
		
# -- Return Clusters of Points formed by K-means clustering
def kmeans(points, k, cutoff):
	# Randomly sample k Points from the points list, build Clusters around them
	initial = random.sample(points, k)
	
	clusters = []
	for p in initial: 
		clusters.append(Cluster([p]))
	
	# Enter the program loop
	while True:
		# Make a list for each Cluster
		lists = []
		for c in clusters: 
			lists.append([])
		
		# For each Point:
		for p in points:
			# Figure out which Cluster's centroid is the nearest
			smallest_distance = norm(p, clusters[0].centroid)
			index = 0
			for i in range(len(clusters[1:])):
				distance = norm(p, clusters[i+1].centroid)
				if distance < smallest_distance:
					smallest_distance = distance
					index = i+1
					
			# Add this Point to that Cluster's corresponding list
			lists[index].append(p)
		
		# Update each Cluster with the corresponding list
		# Record the biggest centroid shift for any Cluster
		biggest_shift = 0.0
		for i in range(len(clusters)):
			shift = clusters[i].update(lists[i])
			biggest_shift = max(biggest_shift, shift)
			
		# If the biggest centroid shift is less than the cutoff, stop
		if biggest_shift < cutoff: 
			break
		
	# Return the list of Clusters
	return clusters
	
	
def print_centroids(clusters) :
	for c in clusters:
		print c.centroid.x,c.centroid.y,

	
# -- Main function
def main(argv):

	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)
	
	with open(argv[1],'r') as f: 
		n = int(f.readline())
		points = []
		for i in range(n):
			x,y = map(float,f.readline().split())
			points.append(Point(x,y))

		#sort the points by their angle
		#points.sort(key=lambda point: point.theta)
		
		p = int(f.readline())
		gas_stations = []	
		for i in xrange(p):
			g = int(f.readline())
			gas_stations.append(g)


		cutoff = 0.1
		
		for g in gas_stations:
			clusters = kmeans(points, g, cutoff)
			print_centroids(clusters)
			print ""
		
		
		
		
		
		exit(0)
		
		k =  3
		cutoff = 0.01 
		
		# Cluster the points using the K-means algorithm
		clusters = kmeans(points, k, cutoff)
		
		# Print the results
		print "\nPOINTS:"
		for p in points: print "P:", p
		print "\nCLUSTERS:"
		for c in clusters: print "C:", c
	
# -- The following code executes upon command-line invocation
if __name__ == "__main__": 
	main(sys.argv)
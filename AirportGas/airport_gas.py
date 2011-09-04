#!/usr/bin/python

import sys
import math
	
class Point:
	"""
	Represents a 2D point
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.theta = math.atan2(y, x)
	def __repr__(self):
		return repr((self.x, self.y))

def norm(p1,p2) :
	return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

class Polygon:
	def __init__(self, a):
		self.pts = a
	
	def area(self):
		area = 0.0
		pts = self.pts;
		j = len(pts)-1
		i = 0
		for point in pts:
			p1 = pts[i]
			p2 = pts[j]
			area += p1.x * p2.y
			area -= p1.y * p2.x
			j = i
			i += 1
		
		area /= 2.0;
		return area;

	def centroid(self):
		pts = self.pts;
		x = 0.0
		y = 0.0
		j = len(pts)-1
		i = 0
	
		for point in pts:
			p1=pts[i]
			p2=pts[j]
			f = p1.x*p2.y - p2.x*p1.y
			x += (p1.x+p2.x) * f
			y += (p1.y+p2.y) * f
			j = i
			i += 1
	
		f = self.area() * 6.0
		return Point(x/f, y/f)


def distance(airports, gas_stations):
	D = 0.0
	for a in airports :
		min = 99999999999999.0
		for g in gas_stations :
			d = (a.x-g.x)**2 + (a.y-g.y)**2
			if d < min :
				min = d
		D += min
		
	return math.sqrt(D)


def compute_centroid(points):
	if len(points) == 1 :
		return points[0]
	elif len(points) == 2 :
		x = (points[0].x+ points[1].x) / 2.0
		y = (points[0].y+ points[1].y) / 2.0
		return  Point(x,y)
	else :
		return Polygon(points).centroid()
	
from itertools import izip_longest
from itertools import ifilter

def compute_centroids(points, c):
	centroids = []

	l = len(points)
	q = l/c 
	if l%c != 0:
		q += 1

	i = izip_longest(*[iter(points)]*q)
	for k in i:
		sub_points = list(ifilter(lambda a: a is not None, k))
		#print "subpoints",sub_points
		centroid = compute_centroid(sub_points)
		#print "new centroid=",centroid
		centroids.append(centroid)
		
	return centroids


	
def print_centroids(centroids) :
	for c in centroids:
		print c.x,c.y,
	
def weiszfeld_iter(points, y):
	y1 = Point(0.0, 0.0)
	denom = 0.0
	for p in points : 
		n = norm(p,y)
		y1.x += p.x / n
		y1.y += p.y / n
		
		denom += 1.0 / n
		
	y1.x /= denom
	y1.y /= denom

	return y1

def weiszfeld(points):
	y = Point(0.2,0.2)
	for i in range(1000):
		y = weiszfeld_iter(points, y)
	return y
	
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
		points.sort(key=lambda point: point.theta)
		
		p = int(f.readline())
		gas_stations = []	
		for i in xrange(p):
			g = int(f.readline())
			gas_stations.append(g)
		
		#zone de merde
		#points = points[0:3]
		#print "all points:", points
		#print gas_stations
		
		
		print "dw", distance(points, [weiszfeld(points)])
	
		#for g in gas_stations:
		#	centroids = compute_centroids(points, g)
		#	print_centroids(centroids)
		#	print ""
			
	
		centroids = compute_centroids(points, 1)
		#print "centroids", centroids
		print "dc", distance(points, centroids)
		
		#print "d3", distance(points, [Point(-1.5,0), Point(1,-1), Point(1,1.5)])
		print "d1", distance(points, [Point(0,0.4)])
	
	
if __name__ == "__main__":
	main(sys.argv)			
			
	
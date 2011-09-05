#!/usr/bin/env python
# *-* coding: utf8 *-*

#http://www.pythonfrance.com/codes/ALGORITHMIME-GENETIQUE-PROBLEME-VOYAGEUR-COMMERCE_51015.aspx

import random,sys,os,time
		
class individu:
	def __init__ (self,nombre_genes,random=-1):
		self.genes = []
		self.nombre_genes = nombre_genes
		if random == -1 : self.random ()
	"""
	random : initialise aleatoirement les genes
	"""
	def random (self):
		self.genes = []
		f = range(0,self.nombre_genes)
		for v in range(self.nombre_genes):
			val = random.choice (f)
			f.remove (val)
			self.genes.append (val)
	""" 
	evaluation : compare l'individu avec un tableau d'autres individus
	retourne le nombre d'individus auquel l'individu self est superieur et de meilleure
	qualité
	"""
	def evalutation (self,autres_individus,distances):
		valeur_individu = 0
		for v in autres_individus:
			if self.compare(v,distances) > 0 : valeur_individu = valeur_individu  + 1
		self.valeur_individu = valeur_individu
		return valeur_individu
	"""
	compare : compare l'individu self avec un autre individu
			  retourne un nombre positif s'il est superieur
			  un nombre negatif s'il est inferieur
			  le nombre 0 s'il est égal
	""" 
	def calcul_distance (self,distance):
		a = self.genes[0]
		dist = 0
		for b in self.genes[1:]:
				min=0
				max=0
				if a > b :
					min = b
					max = a
				else :
					min = a
					max = b
				dist = dist + (distance[min])[max-min-1]
				a = b
		self.distance = dist
		return dist
	def compare (self,individu,distance):
		individu.calcul_distance (distance)
		self.calcul_distance (distance)
		return self.distance - individu.distance
			
			

class population:
	def __init__ (self,nombre_genes,nombre_initial_population=50):
		self.nombre_genes = nombre_genes
		self.distances = [[]] * nombre_genes
		self.individus = []
		self.nombre_initial_population = nombre_initial_population
		for v in range(self.nombre_initial_population):
			self.individus.append (individu(nombre_genes))
	"""
	selection : methode de selection des meilleurs N individus
	"""
	def selection (self , N=-1):
		if N == -1 : N = len(self.individus)
		
		for v in self.individus:
			v.evalutation (self.individus,self.distances)
		
		self.individus.sort (lambda a,b : a.valeur_individu - b.valeur_individu)
		if N <= len(self.individus) : self.individus = self.individus[0:N]
	"""
	croisement : selectionne  deux individus et croise leur gênes pour en creer de nouveaux
	"""
	def croisement_deux (self , i1 , i2):
		i = individu (self.nombre_genes)
		l = len(i1.genes)
		a = l / 2
		p2 = i2.genes[a:l]
		p1 = i1.genes[0:a]
		choices = range(0,l)			
		for v in p1:
			try:choices.remove (v)
			except : pass
		for v in p2:
			try : choices.remove (v)
			except : pass
		idc = 0
		for  id in range(len(p2)):
			if p2[id] in p1:
				p2[id] = choices[idc]
				idc = idc + 1
		i.genes = p1 + p2
		return i
	""" croise tous les individus entre eux"""
	def croisement_all (self):
		new = []
		for v1 in range(len(self.individus)):
			for v2 in  range(v1,len(self.individus)):
				new.append ( self.croisement_deux (self.individus[v1] , self.individus[v2]))
		self.individus  = self.individus + new

	""" croise nombre_croisement individus aleatoires entre eux """
	def croisement_nombre (self , nombre_croisement):
		new = []
		for r in range(nombre_croisement):
			v1 = random.randint (0 , len(self.individus)-1)
			v2 = random.randint (0 , len(self.individus)-1)
			new.append (self.croisement_deux (self.individus[v1] , self.individus[v2]) )
		self.individus = self.individus + new


	

if __name__ == "__main__" :
	""" population de 50 individus"""
	p = population (10,50)
	""" initialise les distances """
	p.distances[0] = [2,3,4,5,6,7,8,9,10 ]     # distance de la premiere ville avec la 2eme , 3eme , ... , 10eme
	p.distances[1] = [11,12,13,14,15,16,17,18 ] # distance de la deuxieme ville avec la 3eme , 4eme , ... ,10eme
	p.distances[2] = [19,20,21,22,23,24,25]  #etc...
	p.distances[3] = [26,27,28,29,30,31]
	p.distances[4] = [32,33,34,35,36]
	p.distances[5] = [37,38,39 ,40]
	p.distances[6] = [41,42,43]
	p.distances[7] = [44,45]
	p.distances[8] = [46] # distance de la 9eme ville avec la 10eme ville
	"""
	10 generations
	a chaque fois fait 100 croisements
	et selectionne les 10 premiers
	"""
	for i in range(10):
		p.croisement_nombre (100)
		p.selection (10)
	for v in p.individus:
			print v.genes,v.calcul_distance (p.distances)
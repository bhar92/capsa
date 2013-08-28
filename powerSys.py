"""
This is an experiment to find a more general, organized and effective way to deal with power system networks.
As of now, it merely computes parameters of the network like number of buses, elements and Ybus. 
As we progress, i will be adding more functionality to this file.
"""

import numpy as np

class powerSys:

	def __init__(self, networkfile):
		"""
		powerSys is used specifically for electrical networks of power systems.
		This requires numpy (imported as np) to work properly
		
		Parameters: 
			self.networkfile	-	name of file which contains the details of the network [Node1, Node2, R, X]
			self.data			-	input data matrix after reading 'networkfile'
			self.nElements		-	Number of elements in the network
			self.nBuses			- 	number of nodes (or buses) in the network
			self.elements		-	matrix containing all the elements in terms of respective buses [Node1, Node2]
			self.z				-	impedence of corresponding element (as indexed in self.element)
			self.y				-	admittance of corresponding element (as indexed in self.element)
			self.Ybus			-	Bus admittance matrix of the network (computed by the 'computeYbus()' method)

		Methods:
			self.computeYbus	-	computes and returns the bus admittance matrix (self.Ybus) of the given network 
			
		"""		

		self.networkfile = networkfile
		self.data = np.loadtxt(self.networkfile)	#load the matrix

		self.nElements = len(self.data)				
		self.elements = self.data[:, 0:2]
		self.nBuses = int(np.max(self.elements))

		
		self.z = self.data[:,2] + 1j*self.data[:,3]
		self.y = 1/self.z
		
	def computeYbus(self):

		elements = self.elements-1

		#Initialize		
		self.Ybus = np.zeros([self.nBuses, self.nBuses], dtype=np.complex64)
		#Compute Off diagonal Elements
		for k in range(self.nElements):
			row = elements[k,0]		
			col = elements[k,1]
			if row>-1 and col>-1:
				self.Ybus[row, col] = -1 * self.y[k]
				self.Ybus[col, row] = self.Ybus[row,col]

		#Compute Diagonal Elements
		for n in range(self.nBuses):
			for k in range(self.nElements):
				if elements[k,0]==n or elements[k,1]==n:
					self.Ybus[n,n] += self.y[k]

		return self.Ybus


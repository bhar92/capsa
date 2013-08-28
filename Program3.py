import numpy as np

data = np.loadtxt('Input-1-Program3.txt')	#[from to R X]

num_el = len(data)				#number of elements
elements = data[:, 0:2]			#elements matrix [Bus1 Bus2]
n_bus = int(np.max(elements))	#number of buses

elements = elements-1			#This seems to make indexing in the 'for' loops easier
								#(This is just a personal preference)

z = data[:,2] + 1j*data[:,3]	# R+jX
y = 1/z

#Initialize a Ybus matrix full of zeros
#Make sure the data type is complex as shown below
Ybus = np.zeros([n_bus, n_bus], dtype = np.complex128)

#Off diagonal elements
for k in range(num_el):
	row = elements[k,0]
	col = elements[k,1]
	if row>-1 and col>-1:		
		Ybus[row, col] = -1 * y[k]
		Ybus[col, row] = Ybus[row, col]

#Diagonal Elements
for n in range(n_bus):
	for k in range(num_el):
		if elements[k, 0]==n or elements[k, 1]==n:
			Ybus[n, n] += y[k]

print "Ybus = ", Ybus

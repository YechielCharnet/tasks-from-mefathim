import matplotlib.pyplot as plt
import numpy as np
import random
import sys

class RW:
	def __init__(self,N,Ndim):
		self.N = N
		self.Ndim = Ndim
		
	def rn_range(self):
		x = np.zeros(self.N)
		for i in range(1, self.N):
			dice = random.random()
			if dice >= 0.5:
				x[i] = x[i-1]+1
			else:
				x[i] = x[i-1]-1
		return x

	def rw_print(self):
		if self.Ndim == 1:
			plt.plot(RW.rn_range(self))
			plt.show()
		elif self.Ndim == 2:
			plt.plot(RW.rn_range(self), RW.rn_range(self))
			plt.show()
		elif self.Ndim == 3:
			plt.axes(projection='3d').plot(RW.rn_range(self), RW.rn_range(self), RW.rn_range(self))
			plt.show()
		else:
			for i in range(self.Ndim):
				print(RW.rn_range(self))


N = int(input("Plees enter number of steps: "))
if N < 1:
    sys.exit("Please enter number >= 1, for steps.") 

Ndim = int(input("Plees enter number of dimention: "))
if Ndim < 1:
	sys.exit("plees enter number >= 1, for dimention.")      

random_walk = RW(N, Ndim)
random_walk.rw_print()




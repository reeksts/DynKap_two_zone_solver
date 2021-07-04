import numpy as np
import math

class TwoZoneSolver:
	def __init__(self, ri, ro, kdry, kmoist, Ti, To, power):
		self.ri = float(ri.get())
		self.ro = float(ro.get())
		self.kdry = float(kdry.get())
		self.kmoist = float(kmoist.get())
		self.Ti = float(Ti.get())
		self.To = float(To.get())
		self.power = float(power.get())
		self.tdiff = self.Ti - self.To

	def setter(self, ri, ro, kdry, kmoist, Ti, To, power):
		self.ri = float(ri)
		self.ro = float(ro)
		self.kdry = float(kdry)
		self.kmoist = float(kmoist)
		self.Ti = float(Ti)
		self.To = float(To)
		self.power = float(power)

	def calculate_min_temp(self):
		temps_min = []
		step = 0.001

		# calculate Ti

		R = math.log(self.ro/self.ri) / 2*math.pi*self.kmoist
		Ti = self.power / R + self.To
		print(Ti)

		R = math.log(self.ro / self.ri) / 2 * math.pi * self.kdry
		Ti = self.power * R + self.To

		print(Ti)
		'''
		for rx in np.arange(self.ri, self.ro+step, step):
			print(rx)
			print(self.ri)
			#print(math.log(rx/self.ri))
			tx = self.Ti - self.power / (2*math.pi*self.kmoist*math.log(rx/self.ri))
			temps_min.append(tx)
			return temps_min
		'''

	def calculate_max_temp(self):
		temps_max = []
		step = 0.001
		for rx in np.arange(self.ri, self.ro + step, step):
			tx = self.Ti - self.power / (2 * math.pi * self.kdry * math.log(rx / self.ri))
			temps_max.append(tx)
			return temps_max
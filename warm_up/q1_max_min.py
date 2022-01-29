import numpy as np

class GeneratingList():

	def __init__(self, low, high, size):
		self.low = low
		self.high = high
		self.size = size
	
	def generate_random_list(self):
		return list(np.random.randint(low=self.low, high=self.high, size=self.size))

	def find_max_min(self, random_list):
		# print ('maximum is:', max(random_list), '\n', 'minimum is:', min(random_list))
		return max(random_list), min(random_list)

	# find_max_min(generate_random_list())
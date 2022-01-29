import numpy as np


def generate_random_list():
	return list(np.random.randint(low=1,high=1000,size=101))

def find_max_min(random_list):
	print ('maximum is:', max(random_list), '\n', 'minimum is:', min(random_list))

find_max_min(generate_random_list())
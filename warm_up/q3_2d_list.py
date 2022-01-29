import numpy as np
import itertools
from q1_max_min import GeneratingList


class TwoDimentionalList(GeneratingList):

	def __init__(self, col_number, row_number):
		super().__init__(1, 100, col_number)
		self.row_number = row_number

	def generating_nd_list(self):

		nd_list = []
		for r_n in range(self.row_number):
			nd_list.append(self.generate_random_list())
		
		return nd_list
	


def main():
	nd_list_instance = TwoDimentionalList(10, 4)
	n_dimention_list = nd_list_instance.generating_nd_list()
	for rand_list in n_dimention_list:
		max_number, min_number = nd_list_instance.find_max_min(rand_list)
		print ('1D list:', rand_list, 'maximum:', max_number, 'minimum', min_number)

	print('nD list \n:')
	flatten_list = []
	[flatten_list.extend(rnd_list) for rnd_list in n_dimention_list]
	print(flatten_list)
	max_number, min_number = nd_list_instance.find_max_min(flatten_list)
	print('maximum is:', max_number, 'minimum is:', min_number)
main()



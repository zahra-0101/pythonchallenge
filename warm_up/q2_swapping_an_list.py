import numpy as np
from q1_max_min import GeneratingList


class SwappingList(GeneratingList):

	def swapping(self):
		random_array = self.generate_random_list()
		random_tuple_array = np.array(random_array).reshape(-1,2)
		# ran
		random_swapped_array =list()
		[random_swapped_array.extend([y,x]) for x,y in random_tuple_array]

		return random_array, random_swapped_array

# array_size can only be even numbers.
array_size = 10
swapped_array = SwappingList(1, 20, array_size)
random_arr, swapped_arr = swapped_array.swapping()
print('random array:', random_arr, '\n', 'swapped array:', swapped_arr)
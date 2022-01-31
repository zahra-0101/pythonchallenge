import random
import string
from q1_max_min import GeneratingList

class GenerateRandomString(GeneratingList):

	def __init__(self, low, high, size):
		super().__init__(low, high, size)

	def sum_character_code(self):
		string_char_code_list = self.generate_random_list()
		sum_of_char_list = 0
		for item in string_char_code_list:
			sum_of_char_list += item
		return sum_of_char_list
		

generator = GenerateRandomString(0, 127, 10)
print(generator.sum_character_code())
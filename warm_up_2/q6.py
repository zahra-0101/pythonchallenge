from random import seed,randint
import operator

def random_dict():
	dict_number = dict()

	seed(None)
	for i in range(10):
		dict_number={**dict_number, str(randint(1,1000)):randint(0,1000000000)}

	print('dictionary: ', dict_number)
	max_value_key = max(dict_number.items(), key=operator.itemgetter(1))[0]
	print('max value: ', max_value_key)
	
	between_3_5 = list()
	for key, value in dict_number.items():
		if len(str(value)) >=3 and len(str(value)) <= 5:
			between_3_5.append(value)
	print('values between 3 and 5: ', between_3_5)

random_dict()
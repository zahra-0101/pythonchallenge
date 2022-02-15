from turtle import distance


def find_distance():
	str_1 = input("enter first string: ")
	str_2 = input("enter second string: ")

	zipped_strings = zip(str_1, str_2)

	distance = 0 
	for item_1, item_2 in zipped_strings:
		if item_1 != item_2:
			distance += 1

	print(distance)


find_distance()
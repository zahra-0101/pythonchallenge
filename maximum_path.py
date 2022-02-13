
from random import randint


# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# for i in range(5):
# 	print (i)
# 	for j in range(i):
# 		print('j', j)
# 		arr[i][j] = randint(1, 30)

# print(arr[0])

arr = [[1,0,0,0,0],
[4,5,0,0,0],
[6,8,9,0,0],
[1,2,3,10,0],
[1,4,3,10,6]]

def dynamic():
	

arr_max = []

for item in arr:
	arr_max.append(max(item))
	

print (list(enumerate(arr[0])))	




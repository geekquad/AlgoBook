def Spiralprint(matrix):

	top = left = 0  # initializing with top
	bottom = len(matrix) - 1
	right = len(matrix[0]) - 1

	while True:
		if left > right:
			break

		# print top row
		for i in range(left, right + 1):
			print(matrix[top][i], end=' ')
		top = top + 1

		if top > bottom:
			break

		# print right column
		for i in range(top, bottom + 1):
			print(matrix[i][right], end=' ')
		right = right - 1

		if left > right:
			break

		# print bottom row
		for i in range(right, left - 1, -1):
			print(matrix[bottom][i], end=' ')
		bottom = bottom - 1

		if top > bottom:
			break

		# print left column
		for i in range(bottom, top - 1, -1):
			print(matrix[i][left], end=' ')
		left = left + 1


rows = int(input())
cols = int(input())
matrix = []
for i in range(0, rows):
    arr = list(map(int, input().split()[:cols]))
    matrix.append(arr)

Spiralprint(matrix)
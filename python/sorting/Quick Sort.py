# Quick sort implementation in python


def partition(arr, low, high):
	i = low -1
	pivot = arr[high]

	for j in range(low, high):
		if(arr[j] < pivot):
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1],arr[high] = arr[high], arr[i+1]
	return (i+1)


def quicksort(arr, low, high):

	if(low< high):
		pi = partition(arr, low, high)
		quicksort(arr, low, pi-1)
		quicksort(arr, pi, high)
	



arr = []
print("Enter Elements:")
arr = [int(num) for num in input().split()]
n = len(arr)
quicksort(arr,0, n-1)
print("Sorted array:")
for i in range(n):
	print(f"{arr[i]}", end = ' ')
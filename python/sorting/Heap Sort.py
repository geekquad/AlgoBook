# Code for heap sort in Python


def heapify(arr, n , i):
	root = i #root

	l = 2*i+1 #left child
	r = 2*i+2 #right child

	if(l<n and arr[i] < arr[l]):
		root = l

	if(r<n and arr[root] < arr[r]):
		root = r

	if(root!=i):
		arr[i], arr[root] = arr[root], arr[i]

		heapify(arr, n, root) 




def sort(arr, n):
	
	#Building maxheap
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1,0,-1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i , 0)


a = []
print("Enter Elements:")
a = [int(num) for num in input().split()]
n = len(a)
sort(a,n)
print("Sorted Array:")
for i in range(n):
	print(f"{a[i]}", end = " ")


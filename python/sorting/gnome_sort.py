
def gnomeSort( arr, n): 
	index = 0
	while index < n: 
		if index == 0: 
			index = index + 1
		if arr[index] >= arr[index - 1]: 
			index = index + 1
		else: 
			arr[index], arr[index-1] = arr[index-1], arr[index] 
			index = index - 1

	return arr 

 
arr = [ 34, 2, 10, -9] 
n = len(arr) 

arr = gnomeSort(arr, n) 
print "After applying Gnome Sort,Sorted seqquence is :-", 
for i in arr: 
	print i, 


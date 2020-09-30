def sort(arr, exp1): 
	n = len(arr) 


	output = [0] * (n) 
	count = [0] * (10) 


	for i in range(0, n): 
		index = (arr[i]/exp1) 
		count[int((index)%10)] += 1


	for i in range(1,10): 
		count[i] += count[i-1] 
	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ int((index)%10) ] - 1] = arr[i] 
		count[int((index)%10)] -= 1
		i -= 1
	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 




def radixsort(arr):
	largest = max(arr)
	exp = 1 # place of digit
	while (largest/exp)>0:
		sort(arr, exp)
		exp *= 10


arr = [170, 45, 11, 815, 645, 24, 2, 70]
n = len(arr)
radixsort(arr)

for i in range(n):
	print(f"{arr[i]}", end = " ")

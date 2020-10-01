''' Python Program for implementation of 
	Recursive Bubble sort ''' 

def bubble_sort(listt):
	'''Function that takes a list and Bubble sorts it recusrively'''

	for i, num in enumerate(listt): 
		try: 
			if listt[i+1] < num: 
				listt[i] = listt[i+1] 
				listt[i+1] = num 
				bubble_sort(listt) 
		except IndexError: 
			pass
	return listt 


arr = []
print("Enter Elements:")
arr = [int(num) for num in input().split()]
n = n = len(arr)
bubble_sort(arr)
print("Sorted array:")
for i in range(n):
	print(f"{arr[i]}", end = ' ')

# Code contributed by Utkarsh Bajaj

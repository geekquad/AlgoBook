# https://workat.tech/problem-solving/practice/implement-stack-array/
class Stack:
	arr = []
	def __init__(self, capacity=0):
		self.t = -1
		self.capacity = capacity
		self.arr = [-1]*self.capacity
		
		

	def isEmpty(self) -> bool:
		if(self.t==-1):
			return True
		return False
		

	def size(self) -> int:
		return self.t+1
		

	def top(self) -> int:
		if(self.t==-1):
			return self.t
		
		i = self.t
		return self.arr[i]
		

	def push(self, element: int) -> None:
		self.t+=1
		
		i = self.t
		self.arr[i] = element

	def pop(self) -> None:
		del self.arr[self.t]
		self.t-=1
		i = self.t
		return self.arr[i]
		



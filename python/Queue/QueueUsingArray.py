class Queue:
	arr =[]
	def __init__(self, capacity=0):
		self.capacity = capacity
		self.arr = [-1]*self.capacity
		self.f = 0
		self.rear = -1
		

	def isEmpty(self) -> bool:
		if((self.rear-self.f+1) == 0):
			return True
		return False
		

	def size(self) -> int:
		return self.rear -self.f + 1
		

	def front(self) -> int:
		return self.arr[self.f]
		

	def back(self) -> int:
		return self.arr[self.rear]
		

	def push(self, element: int) -> None:
		self.rear +=1
		self.arr[self.rear] = element
		
		

	def pop(self) -> None:
		popped = self.arr[self.f]
		self.arr[self.f]  = -1
		self.f+=1
		return popped
		
		



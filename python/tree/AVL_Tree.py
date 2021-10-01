import sys

class Node:
	def  __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None
		self.bf = 0

class AVLTree:

	def __init__(self):
		self.root = None

	def __printHelper(self, currPtr, indent, last):
		# print the tree structure on the screen
	   	if currPtr != None:
			sys.stdout.write(indent)
			if last:
			  	sys.stdout.write("R----")
			  	indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "

			print currPtr.data

			self.__printHelper(currPtr.left, indent, False)
			self.__printHelper(currPtr.right, indent, True)
	
	def __searchTreeHelper(self, node, key):
		if node == None or key == node.data:
			return node

		if key < node.data:
			return self.__searchTreeHelper(node.left, key)
		return self.__searchTreeHelper(node.right, key)

	def __deleteNodeHelper(self, node, key):
		# search the key
		if node == None: 
			return node
		elif key < node.data:
			node.left = self.__deleteNodeHelper(node.left, key)
		elif key > node.data: 
			node.right = self.__deleteNodeHelper(node.right, key)
		else:
			# the key has been found, now delete it

			# case 1: node is a leaf node
			if node.left == None and node.right == None:
				node = None

			# case 2: node has only one child
			elif node.left == None:
				temp = node
				node = node.right

			elif node.right == None:
				temp = node
				node = node.left

			# case 3: has both children
			else:
				temp = minimum(node.right)
				node.data = temp.data
				node.right = self.__deleteNodeHelper(node.right, temp.data)

			# Write the update balance logic here 
			# YOUR CODE HERE
		return node

	# update the balance factor the node
	def __updateBalance(self, node):
		if node.bf < -1 or node.bf > 1:
			self.__rebalance(node)
			return;

		if node.parent != None:
			if node == node.parent.left:
				node.parent.bf -= 1

			if node == node.parent.right:
				node.parent.bf += 1

			if node.parent.bf != 0:
				self.__updateBalance(node.parent)

	 # rebalance the tree
	def __rebalance(self, node):
		if node.bf > 0:
			if node.right.bf < 0:
				self.rightRotate(node.right)
				self.leftRotate(node)
			else:
				self.leftRotate(node)
		elif node.bf < 0:
			if node.left.bf > 0:
				self.leftRotate(node.left)
				self.rightRotate(node)
			else:
				rightRotate(node)

	def __preOrderHelper(self, node):
		if node != None:
			sys.stdout.write(node.data + " ")
			self.__preOrderHelper(node.left)
			self.__preOrderHelper(node.right)

	def __inOrderHelper(self, node):
		if node != None:
			self.__inOrderHelper(node.left)
			sys.stdout.write(node.data + " ")
			self.__inOrderHelper(node.right)

	def __postOrderHelper(self, node):
		if node != None:
			self.__postOrderHelper(node.left)
			self.__postOrderHelper(node.right)
			std.out.write(node.data + " ")

	# Pre-Order traversal
	# Node->Left Subtree->Right Subtree
	def preorder(self):
		self.__preOrderHelper(self.root)

	# In-Order traversal
	# Left Subtree -> Node -> Right Subtree
	def __inorder(self):
		self.__inOrderHelper(self.root)

	# Post-Order traversal
	# Left Subtree -> Right Subtree -> Node
	def __postorder(self):
		self.__postOrderHelper(self.root)

	# search the tree for the key k
	# and return the corresponding node
	def searchTree(self, k):
		return self.__searchTreeHelper(self.root, k)

	# find the node with the minimum key
	def minimum(self, node):
		while node.left != None:
			node = node.left
		return node

	# find the node with the maximum key
	def maximum(self, node):
		while node.right != None:
			node = node.right
		return node

	# find the successor of a given node
	def successor(self, x):
		# if the right subtree is not null,
		# the successor is the leftmost node in the
		# right subtree
		if x.right != None:
			return self.minimum(x.right)

		# else it is the lowest ancestor of x whose
		# left child is also an ancestor of x.
		y = x.parent
		while y != None and x == y.right:
			x = y
			y = y.parent
		return y

	# find the predecessor of a given node
	def predecessor(self, x):
		# if the left subtree is not null,
		# the predecessor is the rightmost node in the 
		# left subtree
		if x.left != None:
			return self.maximum(x.left)

		y = x.parent
		while y != None and x == y.left:
			x = y
			y = y.parent
		return y

	# rotate left at node x
	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != None:
			y.left.parent = x

		y.parent = x.parent;
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

		# update the balance factor
		x.bf = x.bf - 1 - max(0, y.bf)
		y.bf = y.bf - 1 + min(0, x.bf)

	# rotate right at node x
	def rightRotate(self, x):
		y = x.left
		x.left = y.right;
		if y.right != None:
			y.right.parent = x
		
		y.parent = x.parent;
		if x.parent == None:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		
		y.right = x
		x.parent = y

		# update the balance factor
		x.bf = x.bf + 1 - min(0, y.bf)
		y.bf = y.bf + 1 + max(0, x.bf)

	# insert the key to the tree in its appropriate position
	def insert(self, key):
		# PART 1: Ordinary BST insert
		node =  Node(key)
		y = None
		x = self.root

		while x != None:
			y = x
			if node.data < x.data:
				x = x.left
			else:
				x = x.right

		# y is parent of x
		node.parent = y
		if y == None:
			self.root = node
		elif node.data < y.data:
			y.left = node
		else:
			y.right = node

		# PART 2: re-balance the node if necessary
		self.__updateBalance(node)


	# delete the node from the tree
	def deleteNode(self, data):
		return self.__deleteNodeHelper(self.root, data)

	# print the tree structure on the screen
	def prettyPrint(self):
		self.__printHelper(self.root, "", True)

if __name__ == '__main__':
	bst = AVLTree()
	bst.insert(1)
	bst.insert(2)
	bst.insert(3)
	bst.insert(4)
	bst.insert(5)
	bst.insert(6)
	bst.insert(7)
	bst.insert(8)
	bst.prettyPrint()
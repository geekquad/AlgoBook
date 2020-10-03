# Recursive Tree traversals - Inorder, Postorder, Preorder 

class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

# Inorder tree traversal 
def printInorder(root): 
	if root: 

		# recur on left child 
		printInorder(root.left) 

		# then data of the node 
		print(root.val)

		# now recur on right child 
		printInorder(root.right) 


# Postorder tree traversal 
def printPostorder(root): 

	if root: 

		# recur on left child 
		printPostorder(root.left) 

		# then recur on right child 
		printPostorder(root.right) 

		# now data of the node 
		print(root.val), 


# Preorder tree traversal 
def printPreorder(root): 

	if root: 

		# data of the node 
		print(root.val), 

		# recur on left child 
		printPreorder(root.left) 

		# now recur on right child 
		printPreorder(root.right) 

root = Node(1)                  
root.left= Node(2)          
root.right = Node(3)         
root.left.left = Node(4)        
root.left.right = Node(5)       

#             1
#            / \
#           2   3
#          / \
#         4   5

print("Preorder traversal of binary tree is")
printPreorder(root) 

print("\nInorder traversal of binary tree is")
printInorder(root) 

print("\nPostorder traversal of binary tree is")
printPostorder(root) 

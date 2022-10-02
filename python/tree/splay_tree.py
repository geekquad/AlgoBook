# Splay tree implementation in Python
import sys

# Node data structure
class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

# Splay tree structure
class SplayTree:
    def __init__(self):
        self.root = None

    #change
    def __print_helper(self, currPtr, indent, last):
        # print the tree structure
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.data)

            self.__print_helper(currPtr.left, indent, False)
            self.__print_helper(currPtr.right, indent, True)
	
    def __search_tree_helper(self, node, key):
        if node == None or key == node.data:
            return node
        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def __delete_node_helper(self, node, key):
        x = None
        t = None 
        s = None
        while node != None:
            if node.data == key:
                x = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if x == None:
            print("Couldn't find key in the tree")
            return
		
		# split operation
        self.__splay(x)
        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

		# join operation
        if s.left != None:
            s.left.parent = None

        self.root = self.__join(s.left, t)
        s = None

	# rotate left at node x
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

	# rotate right at node x
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
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

	# Splaying operation, moving x to the root of the tree
    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
					# zig rotation
                    self.__right_rotate(x.parent)
                else:
					# zag rotation
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
				# zig-zig rotation
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
				# zag-zag rotation
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
				# zig-zag rotation
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
				# zag-zig rotation
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

	# joins two trees a and b
    def __join(self, a, b):
        if a == None:
            return b
        if b == None:
            return a

        x = self.maximum(a)
        self.__splay(x)
        x.right = b
        b.parent = x
        return x

    def __pre_order_helper(self, node):
        if node != None:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.std.out.write(node.data + " ")

	# Pre-Order traversal
	# Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__pre_order_helper(self.root)

	# In-Order traversal
	# Left Subtree -> Node -> Right Subtree
    def inorder(self):
        self.__in_order_helper(self.root)

	# Post-Order traversal
	# Left Subtree -> Right Subtree -> Node
    def postorder(self):
        self.__post_order_helper(self.root)

	# search the tree for the key k and return node
    def search_tree(self, k):
        x = self.__search_tree_helper(self.root, k)
        if x != None:
            self.__splay(x)

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
		# if the right subtree is not null, the successor is the leftmost node in the
		# right subtree
        if x.right != None:
            return self.minimum(x.right)

		# else it is the lowest ancestor of x whose left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

	# find the predecessor of a given node
    def predecessor(self, x):
		# if the left subtree is not null, the predecessor is the rightmost node in the 
		# left subtree
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

	# insert the key to the tree in its appropriate position
    def insert(self, key):
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
		# splay the node
        self.__splay(node)

	# delete the node from the tree
    def delete_node(self, data):
        self.__delete_node_helper(self.root, data)

	# print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

if __name__ == '__main__':
	tree = SplayTree()
	tree.insert(11)
	tree.insert(33)
	tree.insert(57)
	tree.insert(3)
	tree.insert(88)
	tree.insert(37)
	tree.insert(103)
	tree.insert(1)
	tree.pretty_print()
	tree.search_tree(33)
	tree.search_tree(57)
	tree.pretty_print()
	tree.delete_node(88)
	tree.delete_node(57)
	tree.delete_node(37)
	tree.delete_node(3)
	tree.pretty_print()
class Node:  
    def __init__(self,key):  
        self.left = None
        self.right = None
        self.value = key  
  
def insert(root,key):  
    if root is None:  
        return Node(key)  

    else: 
        if root.value == key: 
            print("Value already exists")
            return root 
        elif root.value < key:  
            root.right = insert(root.right, key)
        else: 
            root.left = insert(root.left, key) 
        return root
  
def inorder(root):  
    if root is not None:  
        inorder(root.left)  
        print(root.value)  
        inorder(root.right)  

def search(root, key):
    if root is None:
        print("Element not found")
        return None
    
    elif root.value == key:
        print("Element found")
        return root
    
    if root.value > key:
        search(root.left,key)

    else:
        search(root.right, key)

def delete(root, key): 
    if root is None: 
        return root  

    if key < root.value: 
        root.left = delete(root.left, key) 
  
    elif(key > root.value): 
        root.right = delete(root.right, key) 
  
    else: 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        temp = getMin(root.right) 
        root.value = temp.value 
        root.right = delete(root.right , temp.value) 

    return root  

def getMin(node): 
    current = node 
    while(current.left is not None): 
        current = current.left  
    return current  
  

if __name__=="__main__": 
    
    r = insert(None,int(input("Enter root node: ")))
    while True:
        choice = int(input("1 - Insert Node, 2 - Print in inorder, 3 - Delete, 4 - Search: , 5 - Exit: "))
        if choice == 1:
            r = insert(r,int(input("Enter node value: ")))
        elif choice == 2:
            inorder(r)
        elif choice == 3:
            r = delete(r,int(input("Enter the value of the node to be deleted: ")))
        elif choice == 4:
            search(r,int(input("Enter the node value to be searched: ")))
        elif choice == 5:
            break
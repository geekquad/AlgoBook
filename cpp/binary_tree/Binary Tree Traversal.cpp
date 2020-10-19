#include<iostream>
using namespace std;
template<typename T> 
class BinarySearchTree
{
private:
	struct tree_node
	{
		tree_node* left;
		tree_node* right;
		T data;
	};
	tree_node* root;
public:
	BinarySearchTree()
	{
		root = NULL;
	}
	bool isEmpty() const { return root==NULL; }
	void insert(T);
	void print_inorder();
	void inorder(tree_node*);
	void print_preorder();
	void preorder(tree_node*);
	void print_postorder();
	void postorder(tree_node*);
};

template <typename T>
void BinarySearchTree<T>::insert(T d)
{
	tree_node* t = new tree_node;
	tree_node* parent;
	t->data = d;
	t->left = NULL;
	t->right = NULL;
	parent = NULL;
	if(isEmpty()) root = t;
	else
	{
		tree_node* curr;
		curr = root;
		while(curr)
		{
			parent = curr;
			if(t->data > curr->data) curr = curr->right;
			else curr = curr->left;
		}

		if(t->data < parent->data)
			parent->left = t;
		else
			parent->right = t;
	}
}
template<typename T>
void BinarySearchTree<T>::print_inorder()
{
	inorder(root);
}
template<typename T>
void BinarySearchTree<T>::inorder(tree_node* p)
{
	if(p != NULL)
	{
		if(p->left) inorder(p->left);
		cout<<" "<<p->data<<" ";
		if(p->right) inorder(p->right);
	}
	else return;
}
template<typename T>
void BinarySearchTree<T>::print_preorder()
{
	preorder(root);
}
template<typename T>
void BinarySearchTree<T>::preorder(tree_node* p)
{
	if(p != NULL)
	{
		cout<<" "<<p->data<<" ";
		if(p->left) preorder(p->left);
		if(p->right) preorder(p->right);
	}
	else return;
}
template<typename T>
void BinarySearchTree<T>::print_postorder()
{
	postorder(root);
}

template<typename T>
void BinarySearchTree<T>::postorder(tree_node* p)
{
	if(p != NULL)
	{
		if(p->left) postorder(p->left);
		if(p->right) postorder(p->right);
		cout<<" "<<p->data<<" ";
	}
	else return;
}

int main()
{
	BinarySearchTree<int> b;
	int ch;
	int tmp,tmp1;
	while(1)
	{
		cout<<endl<<endl;
		cout<<" Binary Search Tree Operations "<<endl;
		cout<<" ----------------------------- "<<endl;
		cout<<" 1. Insertion/Creation "<<endl;
		cout<<" 2. In-Order Traversal "<<endl;
		cout<<" 3. Pre-Order Traversal "<<endl;
		cout<<" 4. Post-Order Traversal "<<endl;
		cout<<" 5. Exit "<<endl;
		cout<<" Enter your choice : ";
		cin>>ch;
		switch(ch)
		{
		case 1 : cout<<" Enter data to be inserted : ";
			cin>>tmp;
			b.insert(tmp);
			break;
		case 2 : cout<<endl;
			cout<<" In-Order Traversal "<<endl;
			cout<<" -------------------"<<endl;
			b.print_inorder();
			break;
		case 3 : cout<<endl;
			cout<<" Pre-Order Traversal "<<endl;
			cout<<" -------------------"<<endl;
			b.print_preorder();
			break;
		case 4 : cout<<endl;
			cout<<" Post-Order Traversal "<<endl;
			cout<<" --------------------"<<endl;
			b.print_postorder();
			break;
		case 5 :return 0;
		}
	}
}

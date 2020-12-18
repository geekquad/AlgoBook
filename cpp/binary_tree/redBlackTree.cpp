/*
Implementation of Red Black Tree 
It uses template so, 
all type of data structures 
can be strored in it
*/

#include <iostream>
using namespace std;

template <typename T = int>
class treenode
{
private:
    // parent - pointer to the parent of the node
    // left - pointer to the left child
    // right - pointer to the right child
    treenode *parent, *left, *right;
    T key;     // data stored in the tree
    int color; // color - 0 for red and 1 for black
    // declaring treenode to be friend of red black tree
    template <typename>
    friend class redBlackTree;
};

// 1. Every node is either red or black.
// 2. The root is black.
// 3. Every leaf(NIL) is black.
// 4. If a node is red, then both its children are black.
// 5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
template <typename T = int>
class redBlackTree
{
private:
    // nil - sentinal node with color black
    // nil is used instead of null pointer
    // helps in avoiding null checks
    // root -  pointer to the root node
    treenode<T> *root, *nil;
    size_t number_of_nodes;

    // function to create new node with provided data
    treenode<T> *newTreenode(T data)
    {
        treenode<T> *node = new treenode<T>;
        node->parent = node->left = node->right = nil;
        node->key = data;
        // initializes new node with Red color by default
        node->color = 0;
        return node;
    }
    
    // searches for key in the subtree with root x
    treenode<T> *search(treenode<T> *x, T key)
    {
        while (x != nil and key != x->key)
        {
            if (key < x->key)
                x = x->left;
            else if (key > x->key)
                x = x->right;
        }
        return x;
    }

    // returns node with minimum element
    // in the subtree with root x
    treenode<T> *minimum(treenode<T> *x)
    {
        while (x->left != nil)
            x = x->left;
        return x;
    }

    // returns node with maximum element
    // in the subtree with root x
    treenode<T> *maximum(treenode<T> *x)
    {
        while (x->right != nil)
            x = x->right;
        return x;
    }

    // returns successor of the node x
    treenode<T> *successor(treenode<T> *x)
    {
        // if right child is not nil return minimum of right child
        if (x->right != nil)
            return minimum(x->right);
        treenode<T> *y = x->parent;
        // else move up till x is right child of its parent
        while (y != nil && x == y->right)
        {
            x = y;
            y = y->parent;
        }
        // return parent of x
        return y;
    }

    // returns predecessor of the node x
    treenode<T> *predecessor(treenode<T> *x)
    {
        // if left child is not nil return maximum of right child
        if (x->left != nil)
            return maximum(x->left);
        treenode<T> *y = x->parent;
        // else move up till x is left child of its parent
        while (y != nil && x == y->left)
        {
            x = y;
            y = y->parent;
        }
        // return parent of x
        return y;
    }

    // places node v in place of u
    // function used in deleting
    void transplant(treenode<T> *u, treenode<T> *v)
    {
        if (u->parent == nil)
            root = v;
        else if (u == u->parent->left)
            u->parent->left = v;
        else if (u == u->parent->right)
            u->parent->right = v;
        v->parent = u->parent;
    }

    // perform left rotation about node x
    void left_rotate(treenode<T> *x)
    {
        treenode<T> *y = x->right;
        x->right = y->left;
        if (y->left != nil)
            y->left->parent = x;

        y->parent = x->parent;
        if (x->parent == nil)
            root = y;
        else if (x == x->parent->left)
            x->parent->left = y;
        else
            x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    // perform right rotation about node x
    void right_rotate(treenode<T> *x)
    {
        treenode<T> *y = x->left;
        x->left = y->right;
        if (y->right != nil)
            y->right->parent = x;

        y->parent = x->parent;
        if (x->parent == nil)
            root = y;
        else if (x == x->parent->left)
            x->parent->left = y;
        else
            x->parent->right = y;
        y->right = x;
        x->parent = y;
    }

    // used for maintaining the red-black property after inserting a node
    void insert_fixup(treenode<T> *z)
    {
        // loop runs while there is red-red parent child relation
        // new child is always red
        while (z->parent->color == 0)
        {
            // parent of z is left child
            if (z->parent == z->parent->parent->left)
            {
                treenode<T> *y = z->parent->parent->right; // uncle of the new node
                if (y->color == 0)
                {
                    z->parent->color = 1;
                    y->color = 1;
                    z->parent->parent->color = 0;
                    z = z->parent->parent;
                }
                else
                {
                    if (z == z->parent->right)
                    {
                        z = z->parent;
                        left_rotate(z);
                    }
                    z->parent->color = 1;
                    z->parent->parent->color = 0;
                    right_rotate(z->parent->parent);
                }
            }
            else
            {
                // if parent of node is right child
                // symmetrical to the left child case
                // with left and right interchanged
                treenode<T> *y = z->parent->parent->left;
                if (y->color == 0)
                {
                    z->parent->color = 1;
                    y->color = 1;
                    z->parent->parent->color = 0;
                    z = z->parent->parent;
                }
                else
                {
                    if (z == z->parent->left)
                    {
                        z = z->parent;
                        right_rotate(z);
                    }
                    z->parent->color = 1;
                    z->parent->parent->color = 0;
                    left_rotate(z->parent->parent);
                }
            }
        }
        root->color = 1;
    }

    // deletes the node with pointer z
    // calls delete_fixup to regain the red-black property
    void deletenode(treenode<T> *z)
    {
        treenode<T> *y = z;
        treenode<T> *x;
        int y_original_color = y->color;
        // if either left or right child are not present
        // replace the node with the child which is present
        // sentinal node in case no child is present
        if (z->left == nil)
        {
            x = z->right;
            transplant(z, z->right);
        }
        else if (z->right == nil)
        {
            x = z->left;
            transplant(z, z->left);
        }
        else
        {
            // if both children are present present node will be replaced by
            // its successor which is minimum of the right child
            y = minimum(z->right);
            y_original_color = y->color;
            // if successor is the right child
            // replace node with z
            if (y->parent == z)
            {
                x->parent = y;
            }
            else
            {
                // replace node with the successor
                transplant(y, y->right);
                y->right = z->right;
                y->right->parent = y;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->parent = y;
            y->color = z->color;
        }
        // if original color is black the tree property
        // need to be restored
        if (y_original_color == 1)
            deletenode_fixup(x);
    }

    // used for maintaining the red-black property after deleting a node
    void deletenode_fixup(treenode<T> *x)
    {
        while (x != root && x->color == 1)
        {
            if (x == x->parent->left)
            {
                treenode<T> *w = x->parent->right;
                if (w->color == 0)
                {
                    w->color = 1;
                    x->parent->color = 0;
                    left_rotate(x->parent);
                    w = x->parent->right;
                }
                if (w->left->color == 1 && w->right->color == 1)
                {
                    w->color = 0;
                    x = x->parent;
                }
                else
                {
                    if (w->right->color == 1)
                    {
                        w->left->color = 1;
                        w->color = 0;
                        right_rotate(w);
                        w = x->parent->right;
                    }
                    w->color = x->parent->color;
                    x->parent->color = 1;
                    w->right->color = 1;
                    left_rotate(x->parent);
                    x = root;
                }
            }
            else if (x == x->parent->right)
            {
                // if parent of node is right child
                // symmetrical to the left child case
                // with left and right interchanged
                treenode<T> *w = x->parent->left;
                if (w->color == 0)
                {
                    w->color = 1;
                    x->parent->color = 0;
                    right_rotate(x->parent);
                    w = x->parent->left;
                }
                if (w->right->color == 1 && w->left->color == 1)
                {
                    w->color = 0;
                    x = x->parent;
                }
                else
                {
                    if (w->left->color == 1)
                    {
                        w->right->color = 1;
                        w->color = 0;
                        left_rotate(w);
                        w = x->parent->left;
                    }
                    w->color = x->parent->color;
                    x->parent->color = 1;
                    w->left->color = 1;
                    right_rotate(x->parent);
                    x = root;
                }
            }
        }
    }
    // inorder traversal of the tree with the root z
    void inorder(treenode<T> *z)
    {
        if (z == nil)
            return;
        inorder(z->left);
        cout << z->key << " ";
        inorder(z->right);
    }

public:
    // constructor to initialize new Red-Black Tree
    redBlackTree()
    {
        // first initializes the sentinal node
        // with color black
        nil = new treenode<T>;
        nil->parent = nil->left = nil->right = nil;
        nil->color = 1;
        number_of_nodes = 0;
        root = nil;
    }
    // insert function to be called by the user
    // performs insertion then calls insert_fixup
    // to maintain the red-black property
    void insertnode(T data)
    {
        // creates new node with data
        treenode<T> *z = newTreenode(data);
        number_of_nodes++;
        treenode<T> *x = root, *y = nil;
        // loop to find the node where newnode will be inserted
        while (x != nil)
        {
            y = x;
            if (data < x->key)
                x = x->left;
            else if (data > x->key)
                x = x->right;
            else
                return;
        }
        z->parent = y;
        // if there is no node in the tree
        if (y == nil)
            root = z;
        else if (data < y->key)
            y->left = z;
        else if (data > y->key)
            y->right = z;
        // calls insert fixum which will maintain the red-black property
        insert_fixup(z);
    }
    // overloaded deletenode to be called by main
    void deletenode(T key)
    {
        // searches for the key
        treenode<T> *z = search(root, key);
        // if not present returns without doing anything
        if (z == nil)
            return;
        // calls deletenode which deletes the node and performs the fixup
        deletenode(z);
        number_of_nodes--;
    }
    // overloaded inorder to be called by main
    // performs inorder traversal
    void inorder()
    {
        inorder(root);
        cout << endl;
    }
    // overloaded function to be called by main
    // returns the key just larger than the given key
    T successor(T key)
    {
        // calls search which return pointer to the node with key
        treenode<T> *node = search(root, key);
        // calls other overloaded successor which returns pointer to the successor
        treenode<T> *succ = successor(node);
        if (succ == nil)
            cerr << "NO successor exist\n";
        return succ->key;
    }
    // overloaded function to be called by main
    // returns the key just smaller than the given key
    T predecessor(T key)
    {
        treenode<T> *node = search(root, key);
        treenode<T> *pred = predecessor(node);
        if (pred == nil)
            cerr << "NO successor exist\n";
        return pred->key;
    }
    // returns true if key is present in the tree
    // returns false if key is not present
    bool find(T key)
    {
        // calls search function which returns pointer to the node
        // with given key
        // if pointer is nil then it is not present else present
        return (search(root, key) != nil);
    }

    // returns number of nodes in the tree
    size_t size()
    {
        return number_of_nodes;
    }

    // return minimum element in the tree
    T minimum()
    {
        treenode<T> *min_node = minimum(root);
        if (min_node == nil)
            cerr << "No node exist\n";
        return min_node->key;
    }

    // return minimum element in the tree
    T maximum()
    {
        treenode<T> *max_node = maximum(root);
        if (max_node == nil)
            cerr << "No node exist\n";
        return max_node->key;
    }
};

// Driver program to test the Red-Black Tree
int main()
{
    redBlackTree<double> tree;
    tree.insertnode(10);
    tree.insertnode(15);
    tree.insertnode(5);
    tree.insertnode(8);
    cout << "inorder traversal of the tree: ";
    tree.inorder();
    cout << "size of tree: " << tree.size() << "\n";
    tree.deletenode(15);
    tree.deletenode(10);
    cout << "inorder traversal of the tree: ";
    tree.inorder();
    cout << "size of tree: " << tree.size() << "\n";
    tree.insertnode(100);
    tree.insertnode(-1);
    tree.insertnode(211);
    cout << "inorder traversal of the tree: ";
    tree.inorder();
    cout << "size of tree: " << tree.size() << "\n";
    cout << "successor of 8 in the tree: ";
    cout << tree.successor(8) << "\n";
    cout << "predecessor of 100 in the tree: ";
    cout << tree.predecessor(100) << "\n";
    cout << "maximum element in the tree: ";
    cout << tree.maximum() << "\n";
    cout << "minimum element in the tree: ";
    cout << tree.minimum() << "\n";
    return 0;
}
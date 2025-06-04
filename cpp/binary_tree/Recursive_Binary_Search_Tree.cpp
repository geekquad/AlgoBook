#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class RecursiveBST {
    struct node
    {
        /* data */
        int data;
        node* left;
        node* right;
    };
    node* root;
    
    public:
    RecursiveBST(){
        root=NULL;
    }

    void insert(int x){
        root = insert(x, root);
    }

    bool search(int x){
        return search(x, root);
    }

    void inorder(){
        inorder(root);
        cout << endl;
    }

    void remove(int x){
        root = remove(x, root);
    }

    private:
    // insert helper function
    node* insert(int x, node* t){
        if (t==nullptr){
            t = new node;
            t->data=x;
            t->left = nullptr;
            t->right = nullptr;
        }
        else if (x < t->data){
            t->left = insert(x, t->left);
        } else if (x > t->data){
            t->right = insert(x, t->right);
        }
        return t;
        
    }

    // search helper
    bool search(int x, node* t){
        if (t == nullptr) 
            return false;
        if (x == t->data)
            return true;
        else if (x < t->data)
            return search(x, t->left);
        else 
            return search(x, t->right);
    }

    // inorder traversal helper
    void inorder(node* t){
        if (t==NULL) return;
        inorder(t->left);
        cout << t->data << " ";
        inorder(t->right);
    }

    // remove helper
    node* remove(int x, node* t){
        if (t == NULL) return NULL;

        if (x < t->data){
            t->left = remove(x, t->left);
        } else if (x > t->data){
            t->right = remove(x, t->right);
        } 
        else {
            // no child
            if (t->left == NULL && t->right == NULL){
                delete t;
                t = NULL;
                return t;
            }
            // one child
            else if (t->left == NULL){
                node* temp = t;
                t = t->right;
                delete temp;
            }
            else if (t->right == NULL){
                node* temp = t;
                t = t->left;
                delete temp;
            }
            // two child
            else {
                node* temp = findMin(t->right);
                t->data = temp->data;
                t->right = remove(temp->data, t->right);
            }
        }
        return t;
    }

    node* findMin(node* t){
        if (t == NULL){
            return NULL;
        } while (t->left != NULL){
            t = t->left;
        }
        return t;
    }
};

int main(){
    RecursiveBST tree;
    tree.insert(50);
    tree.insert(30);
    tree.insert(70);
    tree.insert(20);
    tree.insert(40);
    tree.insert(60);
    tree.insert(80);

    cout << "Inorder traversal: ";
    tree.inorder();

    cout << "Search 40: " << (tree.search(40) ? "Found" : "Not Found") << endl;
    cout << "Search 99: " << (tree.search(99) ? "Found" : "Not Found") << endl;

    cout << "Remove 20" << endl;
    tree.remove(20);
    cout << "Inorder traversal: ";
    tree.inorder();

    return 0;
}
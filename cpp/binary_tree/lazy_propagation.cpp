/*
Segment tree with Lazy propagation
with addition operation 
uses template so any datastructure
which supports addition can be used
*/

#include <iostream>
#include <vector>
using namespace std;

template <typename T = int>
class segTree
{
public:
    // size - stores the number of leaf nodes
    // tree - tree is constructed with this
    // lazy - for lazy propagation
    int size;
    vector<T> tree, lazy;
    // uses zero indexing
    segTree(int n)
    {
        // constructor to allocate memorey to array
        size = 1;
        // computes the next power of 2
        // so as to create a perfect tree
        // they form leaf nodes of the tree
        // unused index will be zero
        while (size <= n)
            size *= 2;
        //twice the size of leaf to form tree
        tree.assign(2 * size, 0);
        lazy.assign(2 * size, 0);
    }
    // build the tree using the vector a
    // uses half closed interval
    // x in the current root
    // lx and rx stores the span of current root on the array
    void build(vector<T> &a, int x, int lx, int rx)
    {
        // if no child
        if (rx - lx == 1)
        {
            // if lx within the array a
            if (lx < (int)a.size())
                tree[x] = a[lx];
            return;
        }
        // build left and right subtree recursively
        int m = (lx + rx) / 2;
        build(a, 2 * x, lx, m);
        build(a, 2 * x + 1, m, rx);
        // set value of current node to sum of children
        tree[x] = tree[2 * x] + tree[2 * x + 1];
    }
    // will be called from the main
    // call overloaded function with other required parameters
    void build(vector<T> &a)
    {
        build(a, 1, 0, size);
    }
    // set the value of one particular leaf to to v
    void set(T v, int i, int x, int lx, int rx)
    {
        if (rx - lx < 1)
            return;
        // if no child return, set value of leaf to v
        if (rx - lx == 1)
        {
            tree[x] = v;
            return;
        }
        // if required node in left child
        int m = (lx + rx) / 2;
        if (i < m)
            set(v, i, 2 * x, lx, m);
        // if require node in right child
        else
            set(v, i, 2 * x + 1, m, rx);
        // set value of current node to sum of children
        tree[x] = tree[2 * x] + tree[2 * x + 1];
    }
    // will be called from the main
    // call overloaded function with other required parameters
    void set(T v, int i)
    {
        set(v, i, 1, 0, size);
    }
    // increments a segment of the array using lazy propagation
    void updateLazy(T v, int l, int r, int x, int lx, int rx)
    {
        if (rx - lx < 1)
            return;
        // if value of node at lazy tree not zero
        if (lazy[x] != 0)
        {
            // update the node of main tree
            // multily by (rx-lx)
            // node x covers (rx-lx) leaf nodes
            tree[x] += lazy[x] * (rx - lx);
            if (rx - lx > 1)
            {
                // update childred of lazy tree
                lazy[2 * x] += lazy[x];
                lazy[2 * x + 1] += lazy[x];
            }
            lazy[x] = 0;
        }
        // if required segment is not overlapping
        if (lx >= r || rx <= l)
        {
            return;
        }
        // if completely overlapping
        if (l <= lx && r >= rx)
        {
            // update the tree node
            // and increment children lazy nodes
            tree[x] += v * (rx - lx);
            if (rx - lx > 1)
            {
                lazy[2 * x] += v;
                lazy[2 * x + 1] += v;
            }
            return;
        }
        // if there is partial ovelap
        // recursively update both left and right children
        int m = (lx + rx) / 2;
        updateLazy(v, l, r, 2 * x, lx, m);
        updateLazy(v, l, r, 2 * x + 1, m, rx);
        tree[x] = tree[2 * x] + tree[2 * x + 1];
    }
    // will be called from the main
    // call overloaded function with other required parameters
    void updateLazy(T v, int l, int r)
    {
        updateLazy(v, l, r, 1, 0, size);
    }
    // returns the sum of the segment
    T query(int l, int r, int x, int lx, int rx)
    {
        if (rx - lx < 1)
            return 0;
        // if lazy node is not zero
        // update tree node and
        // propagate the lazy node to the children
        if (lazy[x] != 0)
        {
            tree[x] += lazy[x] * (rx - lx);
            if (rx - lx > 1)
            {
                lazy[2 * x] += lazy[x];
                lazy[2 * x + 1] += lazy[x];
            }
            lazy[x] = 0;
        }
        // if required segment is not overlapping
        if (lx >= r || rx <= l)
            return 0;
        // if completely overlapping
        if (lx >= l && rx <= r)
            return tree[x];
        // if there is partial ovelap
        // recursively call both left and right children
        int m = (lx + rx) / 2;
        T s1 = query(l, r, 2 * x, lx, m);
        T s2 = query(l, r, 2 * x + 1, m, rx);
        return s1 + s2;
    }
    // will be called from the main
    // call overloaded function with other required parameters
    long long query(int l, int r)
    {
        return query(l, r, 1, 0, size);
    }
};
// driver program to test segment tree
int main()
{
    vector<long long> a = {1, 3, 5, 7, 5, 2, 4, 5, 5};
    segTree<long long> st(a.size());
    cout << st.size << "\n";
    st.build(a);
    cout << st.query(0, 9) << "\n";
    st.set(9, 3);
    cout << st.query(2, 7) << "\n";
    st.updateLazy(3, 1, 5);
    cout << st.query(4, 5) << "\n";
    st.updateLazy(3, 1, 5);
    cout << st.query(2, 4) << "\n";
    return 0;
}
/*
Non-Recursive Segment tree
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
    int size;
    vector<T> array;
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
        size *= 2;
        array.assign(size, 0);
    }
    //build the tree using the vector a
    void build(vector<T> &a)
    {
        // loop to form all the leaf nodes of the segment tree
        for (int i = size / 2; i < size && i - size / 2 < a.size(); i++)
        {
            array[i] = a[i - size / 2];
        }
        // constructing segment tree
        // computes value of all nodes at one level
        // then moves up the one level
        for (int i = size / 4; i > 0; i /= 2)
        {
            // loop to form parent of the two children nodes
            for (int j = i; j < 2 * i; j++)
            {
                array[j] = array[2 * j] + array[2 * j + 1];
            }
        }
        //index zero of the array is not used in the tree
    }

    void set(int pos, T num)
    {
        // sets changes the value of index pos to num
        array[pos + size / 2] = num;
        // modifies the tree to reflect the changed value
        // by moving up the tree and recomputing value of parent
        for (int parent = (pos + size / 2) / 2; parent > 1; parent /= 2)
        {
            int child1 = 2 * parent, child2 = 2 * parent + 1;
            array[parent] = array[child1] + array[child2];
        }
    }
    // returns the sum of all the elements
    // between l and r index,
    // l including and r excluding
    T query(int l, int r)
    {
        T res = 0;
        // if l is odd then the parent is not included in result so array[l] is added to result
        // and we move right of l's parent by adding 1 to l and then dividing by 2
        // if l is even then parent will be include in result (unless the right border interfares)
        // and we move to the parent by dividing l by 2
        for (l += size / 2, r += size / 2; l < r; l /= 2, r /= 2)
        {
            if (l % 2 == 1)
                res += array[l++];
            if (r % 2 == 1)
                res += array[--r];
        }
        return res;
    }
};

//Driver program to test the segment tree
int main()
{
    vector<long> a = {1, 3, 5, 7, 5, 2, 4, 5, 5};
    segTree<long> st(a.size());
    cout << st.size << "\n";
    st.build(a);
    for (auto x : st.array)
        cout << x << " ";
    cout << "\n";
    cout << st.query(0, 9) << "\n";
    cout << st.query(2, 7) << "\n";
    st.set(3, 9);
    cout << st.query(4, 5) << "\n";
    cout << st.query(2, 4) << "\n";

    return 0;
}

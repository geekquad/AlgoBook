#include<bits/stdc++.h>
using namespace std;
vector<int> bit;  // binary indexed tree
int n; // number of elements
int sum(int r) {
    int ret = 0;
    for (; r >= 0; r = (r & (r + 1)) - 1)
        ret += bit[r];
    return ret;
}
int sum(int l, int r) {
    return sum(r) - sum(l - 1);
}
// boundary points (0 based indexing)
// will give sum from index l to r
void add(int idx, int delta) {
    for (; idx < n; idx = idx | (idx + 1)){
        bit[idx] += delta;
    }
}
// will add delta to the element at index idx
int main(){
    cout<<"Enter the number of elements\n";
    cin>>n;
    cout<<"Enter the elements\n";
    bit.assign(n,0);
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        add(i,x);
    }
    int l,r;
    cout<<"Enter the boundary points of the subarray\n";
    cin>>l>>r;
    cout<<"The sum of the subarray from "<<l<<" to "<<r<<" is \n";
    cout<<sum(l-1,r-1)<<endl;
    int idx,delta;
    cout<<"Enter the index of the element to update and its value\n";
    cin>>idx>>delta;
    add(idx-1,delta);
    cout<<"The new sum of the subarray from "<<l<<" to "<<r<<" is \n";
    cout<<sum(l-1,r-1)<<endl;

}

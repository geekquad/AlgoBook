//Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.
//Constraints:
//1 <= N <= 105
//0 <= A[i] <= N-1, for each valid i


#include <bits/stdc++.h>
using namespace std;
class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
       vector<int> v;
        unordered_map<int, int>mp;
        for(int i=0; i<n; i++)
        {
            mp[arr[i]]++;
            if(mp[arr[i]]==2)
            {
                v.push_back(arr[i]);
            }
        }
        if(v.size()==0)
        {
            v.push_back(-1);
        }
        sort(v.begin(),v.end());
        return v;
    }
};

int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution obj;
        vector<int> ans = obj.duplicates(a, n);
        for (int i : ans) cout << i << ' ';
        cout << endl;
    }
    return 0;
}

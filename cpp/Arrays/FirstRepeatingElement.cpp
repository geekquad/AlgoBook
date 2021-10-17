//Given an array arr[] of size n, find the first repeating element. The element should occurs more than once and the index of its first occurrence should be the smallest.

#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    // Function to return the position of the first repeating element.
    int firstRepeated(int arr[], int n) {
        // making a map to store frequency of each element and then wherever the frequency is more than two we use find over that to return the first encounter.
        map <int, int> fre;
        int res= 0;
        for(int i=0;i<n;i++)
        fre[arr[i]]++;
        
       for(int i=0;i<n;i++){
       int key = arr[i];
       
       auto temp = fre.find(key);
       if(temp->second > 1)
       return i+1;
       }
        return -1;
    }
};


int main() {

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int arr[n];

        for (int i = 0; i < n; ++i) cin >> arr[i];
        Solution ob;
        cout << ob.firstRepeated(arr, n) << "\n";
    }

    return 0;
}

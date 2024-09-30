//Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.


#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
        int sum=0,i=0,j=0;
    while((i<n) && (j<=n)){
           if(sum<s){
             sum+=arr[j];
             j++;
         }
         else if(sum>s){
             sum-=arr[i];
             i++;
         }
         else if(sum==s){
         return {i+1,j};
         break;
         }
    } 
    return {-1};
    }
};
int main()
 {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        long long s;
        cin>>n>>s;
        int arr[n];
        const int mx = 1e9;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        Solution ob;
        vector<int>res;
        res = ob.subarraySum(arr, n, s);
        
        for(int i = 0;i<res.size();i++)
            cout<<res[i]<<" ";
        cout<<endl;
        
    }
	return 0;
}  

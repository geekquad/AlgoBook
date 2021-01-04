#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll>  zfunction(string &s){
   
    // 0th -index based z-function
    //  IN z-function at each index we check the longest common prefix between that index and starting point 
    // we take the z-function of the starting index as 0 
    // Here we maintain a segment l to r which are similar to the 0th index to r-l index
    // when we are in that segment we don't have to traverse to r because the same answer for corresponding starting element is already known
    // we just have to traverse when the common prefix is greater than or equal to the range (r-index) or we are outside the right boundary r
   // Time complexity for this algorithm is O(n) and to search a pattern in this we just add that pattern before the main text/array in that case the size become n+m(size of pattern) and complexity goes to O(n+m)

    ll n = s.size(); 
    vector<ll> zarr(n,0);
    for(ll i=1,l=0,r=0;i<n;i++){

        if(i>r){  // we are outside the segment [ l - r ]
           l=r=i; // we have to start traversing from here and compare the elements to corresponding starting element till we get any mismatch or end of the text/array 
           while(r<n && s[r-l]==s[r])r++;
           --r;  // since the breaking point is mismatched so we have to decrement the r by 1
           zarr[i] = r-l+1;
        }
        else {  // we are inside the segment [ l - r ]
           ll k = i - l;
           if(zarr[k]<r-i+1) zarr[i] = zarr[i-l]; // if length of common prefix is less than (r-i+1) 
           else{ // if common prefix is equal to or greater than (r-i+1)
            l=i;
            while(r<n && s[r-l]==s[r])r++;
            --r;  // since the breaking point is mismatched so we have to decrement the r by 1
            zarr[i] = r-l+1;
           }
        }
    }
    // we just return the Z-array 
    return zarr;
}

int main() {
   
   string s ="ababcbababca";
   
   //  string s for which we are going to make z array 
  
   vector<ll> zarr = zfunction(s);  // calling Z-function
   
   // printing z array

   for(ll i=0;i<s.size();i++){
      cout<<zarr[i]<<"  ";
   }    

//   OUTPUT : 0  0  2  0  0  0  5  0  2  0  0  1 

   return 0;
}

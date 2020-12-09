//Recursive Binary Search
#include <bits/stdc++.h>
using namespace std;

int binarySearch(int A[], int low, int high, int x)
{
    
    if (low > high)
        return -1;
 

 
    int mid = (low + high)/2;    // overflow can happen
    // int mid = low + (high - low)/2;
 
   
    if (x == A[mid])
        return mid;
 
    
    else if (x < A[mid])
        return binarySearch(A, low,  mid - 1, x);
 
    
    else
        return binarySearch(A, mid + 1,  high, x);
}
 

int main(void)
{
    int n,num;
	
    cout<<"Enter number for elements:";
    cin>>n;
    int A[n];
    cout<<"Enter array:";
    for(int i=0;i<n;i++)
    cin>>A[i];
    cout<<"Enter the target:";
    cin>>num;
 
    int low = 0, high = n - 1;
    int index = binarySearch(A, low, high, num);
 
    if (index != -1)
        cout<<"Element found at index "<<index+1;
    else
        cout<<"Element not found in the array";
 
    return 0;
}

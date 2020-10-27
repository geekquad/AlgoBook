/*
Question: Number of Prime Subarrays

Given an array of positive integers,find out the number of subarrays
that consist of prime numbers only.

Example: 
Input: [2,3,1,7,2]
Output: 6
Explanation: Subarrays: [2], [3], [2 3], [7], [2], [7 2]
*/
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int isprime(int n)
{
    if(n<2)
        return 0;
    for(int i=2;i<=n/2;i++)
    {
        if(n%i==0)
            return 0;
    }
    return 1;
}

int primesub(vector<int> a)
{
    int n,i;
    n=a.size();
    vector<int> op(n,0);
    op[0]=isprime(a[0]);   
	//To store the number of consecutive primes till ith position
    vector<int> prime(n,0); 
	//Each index represents the number of i+1 consecutive primes in the array
    for(i=0;i<n;i++)
    {

        if(isprime(a[i])==1)
        {
        	if(i!=0)
            	op[i]=op[i-1]+1;
            prime[op[i]-1]++;  
			//op[i-1]=>Number of consecutives primes till n
			//prime[i-1]=>Stores number of i consecutive primes in the array
            if(op[i]>1)
                prime[op[i]-2]--;
        }
    }
    int sum=0;
    for(i=0;i<n;i++)
    {
        sum=sum+(((i+1)*(i+2))/2)*prime[i];
    }
    return sum;
}

int main()
{
    int i,n,tmp;
    cin>>n;
    vector<int> a;
    for(i=0;i<n;i++)
    {
        cin>>tmp;
        a.push_back(tmp);
    }
    cout<<primesub(a);
    return 0;
}

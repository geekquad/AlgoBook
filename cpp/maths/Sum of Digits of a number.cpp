#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long n,sum=0;
    cout<<"Enter no.: ";
    cin>>n;
    while(n!=0)
    {
        sum+=n%10;
        n/=10;
    }
    cout<<endl<<"Sum of Digits of a number: "<<sum<<endl;
    return 0;
}

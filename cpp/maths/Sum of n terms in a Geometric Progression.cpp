#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long n,r,a;
    cout<<"Enter no. of terms: ";
    cin>>n;
    cout<<endl<<"Enter first term: ";
    cin>>a;
    cout<<endl<<"Enter common ratio: ";
    cin>>r;
    cout<<endl<<"Sum of n terms in a Geometric Progression: ";
    if(r!=1)
        cout<<a*(1-pow(r,n))/(1-r)<<endl;
    else
        cout<<a*n<<endl;
    return 0;
}

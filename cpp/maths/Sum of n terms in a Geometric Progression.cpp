#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    long double r,a;
    cout<<"Enter no. of terms: ";
    cin>>n;
    cout<<"Enter first term: ";
    cin>>a;
    cout<<"Enter common ratio: ";
    cin>>r;
    cout<<"Sum of n terms in a Geometric Progression: ";
    if(r!=1)
        cout<<a*(1-pow(r,n))/(1-r)<<endl;
    else
        cout<<a*n<<endl;
    return 0;
}

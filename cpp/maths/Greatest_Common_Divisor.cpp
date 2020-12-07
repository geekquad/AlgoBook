#include<bits/stdc++.h>
using namespace std;
int gcd(int a,int b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}
int main(){
	int x,y;
	cout<<"Enter two numbers whose GCD needs to be calculated"<<endl;
	cin>>x>>y;
	cout<<"The GCD of "<<x<<" and "<<y<<" is : "<<gcd(x,y);
	return 0;
}
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
	cout<<"Enter two numbers whose LCM needs to be calculated"<<endl;
	cin>>x>>y;
	int lcm=(x*y)/gcd(x,y);
	cout<<"The LCM of "<<x<<" and "<<y<<" is : "<<lcm;
	return 0;
}
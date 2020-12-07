#include<bits/stdc++.h>
using namespace std;
int main(){
	int a,r,n;
	cout<<"Enter the first term of the GP : ";
	cin>>a;
	cout<<"Enter the common ratio (r cannot be 1): ";
	cin>>r;
	cout<<"Enter the number of terms : ";
	cin>>n;
	cout<<"The sum of "<<n<<" terms of the GP is ";
	cout<<(a*(pow(r,n)-1))/(r-1)<<endl;
	return 0;
}
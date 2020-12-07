#include<bits/stdc++.h>
using namespace std;
int main(){
	int a,d,n;
	cout<<"Enter the first term of the AP : ";
	cin>>a;
	cout<<"Enter the common difference : ";
	cin>>d;
	cout<<"Enter the number of terms : ";
	cin>>n;
	cout<<"The sum of "<<n<<" terms of the AP is ";
	cout<<(n*(2*a+(n-1)*d))/2;
	return 0;
}
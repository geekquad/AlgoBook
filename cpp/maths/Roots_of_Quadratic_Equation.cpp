#include<bits/stdc++.h>
using namespace std;
int main(){
	double a,b,c;
	cout<<"Enter the Coefficients of the Quadratic Equation ( ax^2+bx+c )"<<endl;
	cout<<"a : ";
	cin>>a;
	cout<<"b : ";
	cin>>b;
	cout<<"c : ";
	cin>>c;
	double root1,root2,d;
	cout<<"The roots of the equation "<<a<<"x^2 + "<<b<<"x + "<<c<<" are:"<<endl;
	d=(b*b-4*a*c);
	if(d>0){
		root1=(-b+sqrt(d))/(2*a);
		root2=(-b-sqrt(d))/(2*a);
		cout<<"The roots are real"<<endl;
		cout<<"The first root : "<<root1<<endl;
		cout<<"The second root : "<<root2<<endl;
	}
	else if(d==0){
		root1=(-b)/(2*a);
		cout<<"The roots are real and equal"<<endl;
		cout<<"The only root : "<<root1<<endl;
	}
	else{
		d=abs(d);
		cout<<"The roots are imaginary"<<endl;
		cout<<"The first root :"<<(-b)/(2*a)<<" +"<<(sqrt(d)/(2*a))<<"i"<<endl;
		cout<<"The second root :"<<(-b)/(2*a)<<" -"<<(sqrt(d)/(2*a))<<"i"<<endl;
	}

	
}
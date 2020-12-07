#include <bits/stdc++.h>

using namespace std;
 
int main() {

	//Take input as coefficients of the quadratic equation as floating point number
	
	cout << "Enter coefficients a, b, c of the quadratic equation a*x^2 + b*x + c = 0:\n";	
	float a, b, c, x1, x2;

	cin >> a >> b >> c;

	//find the discriminant of this quadratic equation
	float disc = b*b - 4.0*a*c;

	//if discriminant is greater than 0, it means that the roots are real and different
	if(disc > 0) {

		//find the roots using quadratic formula
		x1 = -b - sqrt(disc);
		x1 /= (2.0*a);

		x2 = -b + sqrt(disc);
		x2 /= (2.0*a);

		//print the roots
		cout << "Roots are real and different\n";
		cout << "x1 = " << x1 << '\n';
		cout << "x2 = " << x2 << '\n';
	}

	//if discriminant is zero, it means that roots are real and equal 
	else if(disc == 0) {
		x1 = -b;
		x1 /= (2.0*a);
		//print the roots
		cout << "Roots are real and equal\nx = ";
		cout << x1 << '\n';
	}

	//if discriminant is less than zero, roots are complex and differen
	//print the roots in complex form(ie, using iota 'i')
	else {

		float realPart = -b/(2.0*a);
		float imaginaryPart = sqrt(-disc)/(2.0*a);

		//print the roots using real and imaginary parts 
		
		cout << "Roots are complex and different\n";
		cout << "x1 = " << realPart << " + i" << imaginaryPart << '\n';
		cout << "x2 = " << realPart << " - i" << imaginaryPart << '\n';

	}
	return 0;
}
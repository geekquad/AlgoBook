//A number is said to be a Peterson number if the sum of factorials of each digit 
//is equal to the number itself

//Given a number n, check if it is a Peterson number

#include <bits/stdc++.h>

using namespace std;

//function to get factorial of a number
int fact(int n) {
	if(n == 0) {
		return 1;
	}
	return n * fact(n-1);
}

//check if a number is a Peterson number
bool isPeterson(int n) {

	//convert the number into string to easily traverse over its digits
	string s = to_string(n);

	int sumOfFact = 0;

	//find sum of factorial of digits of the number
	for(char ch : s) {
		sumOfFact += fact(ch-'0');
	}

	//return true is sum of factorial of digits is equal to the number itself
	return sumOfFact == n;
}

int main() {

	//take the input as a number
	cout << "Enter the number:\n";
	int n;
	cin >> n;

	//call the function to check if this is a Peterson number or not
	if(isPeterson(n)) {
		cout << "Yes, this is a Peterson number\n";
	} else {
		cout << "No, this is not a Peterson number\n";
	}
	return 0;
}
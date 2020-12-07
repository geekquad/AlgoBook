/* Lucas numbers are defined as
		
	 L(n) = 2, if n == 0;
	 			= 1, if n == 1;
	 			= L(n-1) + L(n-2), if n > 1

	 Given a number n (>=0), print the first (n+1) terms of the Lucas sequence
*/

#include <bits/stdc++.h>

using namespace std;

//Recursive function to find the nth lucas number
int lucas(int n) {
	//Handle two base cases
	if(n == 0) {
		return 2;
	}
	if(n == 1) {
		return 1;
	}

	//if n > 1, L(n) = L(n-1) + L(n-2);
	int Ln = lucas(n-1) + lucas(n-2);
	return Ln;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//take input
	int n;
	cin >> n;

	cout << "The first " << n+1 << " Lucas numbers are : \n";
	//print the first (n+1) Lucas numbers
	for(int i = 0; i <= n; i++) {
		cout << lucas(i) << " ";
	}
	cout << '\n';
	return 0;
}
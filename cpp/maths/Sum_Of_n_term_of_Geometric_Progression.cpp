//Given a geometric progression, find the sum of its first n terms
#include <bits/stdc++.h>

using namespace std;

long long power(long long a, long long b) {
	if(b == 0) return 1;
	long long res = power(a, b/2);
	res *= res;
	if(b % 2) {
		res *= a;
	}
	return res;
}

int main() {

	long long a, r, n;
	//take input of first term of GP;
	cout << "Enter the first term of GP:\n";
	cin >> a;

	//take input of common ratio of GP;
	cout << "Enter common ratio of GP:\n";	
	cin >> r;

	//take input of number of terms
	cout << "Enter number of terms:\n";
	cin >> n;

	cout << "Sum of first " << n << " terms of this GP is:\n";

	//if r == 1, formula of sum involves division by zero, not valid
	if(r == 1) {
		long long ans = a*n;
		cout << ans << '\n';
		return 0;
	}
	long long ans = a*(power(r, n) - 1);
	ans /= (r-1);
	cout << ans << '\n';
	return 0;
}
	
//Ugly numbers are numbers whose only prime factors are 2, 3, or 5.
//Given a number n, find the nth ugly number

#include <bits/stdc++.h>

using namespace std;
 
int main() {
	//take input of number n
	cout << "Enter N (to find Nth ugly number):\n";
	int n;
	cin >> n;
	vector<int> ugly(n+1);

	ugly[0] = 1;
	int i2 = 0, i3 = 0, i5 = 0;

	//Here, nxt2 is the next multiple of 2
	//nxt3 is the next multiple of 3
	//nxt5 is the next multiple of 5
	//nxtUgly represents the next Ugly number
	int nxtUgly = 1, nxt2 = 2, nxt3 = 3, nxt5 = 5;
	for(int i = 1; i < n; i++) {

		//find min of next multiples of 2, 3, and 5 to update nxtUgly
		nxtUgly = min(nxt2, min(nxt3, nxt5));
		ugly[i] = nxtUgly;

		//if next ugly number (ie, nxtUgly) is equal to next multiple of 2,
		//increase i2 by 1;
		if(nxtUgly == nxt2) {
			i2++;
			nxt2 = ugly[i2]*2;
		}

		//if next ugly number (ie, nxtUgly) is equal to next multiple of 3,
		//increase i3 by 1;
		if(nxtUgly == nxt3) {
			i3++;
			nxt3 = ugly[i3]*3;
		}

		//if next ugly number (ie, nxtUgly) is equal to next multiple of 5,
		//increase i5 by 1;
		if(nxtUgly == nxt5) {
			i5++;
			nxt5 = ugly[i5]*5;
		}
	}
	//print the nth ugly number
	cout << n << "th ugly number is : " << nxtUgly << '\n';
	return 0;
}
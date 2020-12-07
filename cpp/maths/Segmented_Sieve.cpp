//Using simple Sieve of Eratosthenes we can find all prime numbers less than n 
//However we will need O(n) space

//This is ot feasible when n is large, ie, O(n) space may not fit in memory
//Hence we will use Segmented Sieve - the idea is to divide the range [0...n-1]
//in different segments and compute primes in all segments one by one.

//Space complexity of this approach is O(sqrt(n)), which is a lot better than O(n)
#include <bits/stdc++.h>

using namespace std;
#define int long long

void simpleSieve(int upper, vector<int>& prime) {
	//Here, we implement a simple sieve that finds all prime numbers less than upper;
	//The idea is simple -> if we see a number marked true (ie, it is prime), we iterate over its multiples
	//and mark them false;
	vector<bool> isPrime(upper+1, true);
	for(int p = 2; p*p < upper; p++) {
		if(isPrime[p]) {
			for(int i = p*p; i < upper; i += p) {
				isPrime[i] = false;
			}
		}
	}
	for(int p = 2; p < upper; p++) {
		if(isPrime[p]) {
			cout << p << " ";
			prime.push_back(p);
		}
	}
	return;
}

void SegmentedSieve(int n) {

	//We work by finding primes in segments of [0...n-1];
	//We choose the segment size as sqrt(n);

	int upper = floor(sqrt(n)) + 1;
	vector<int> prime;

	//find all primes upto upper using simple sieve
	simpleSieve(upper, prime);

	//Variables 'lo' and 'hi' store the starting and ending values of the segment that
	//we are currently working on
	int lo = upper; 
	int hi = 2*upper;

	//Till all segments of the range [0...n-1] are not covered, process one segment at a time
	while(lo < n) {
		if(hi >= n) {
			hi = n;
		}
		//create a boolean array of the size of the segment, ie, hi-lo+1 == upper+1;
		vector<bool> isPrime(upper+1, true);

		//For marking primes in the current range.
		//A value in isPrime[i] will finally be false if 'i-lo' is not a prime, else true
		for(int x : prime) {

			//Find the minimum number >= lo that is a multiple of x
			int lower = floor(lo/x)*x;
			if(lower < lo) {
				lower += x;
			}
			//mark multiples of x in [lo...high];
			for(int j = lower; j < hi; j += x) {
				isPrime[j-lo] = false;
			}
		}

		//Finally, numbers which are not marked as false in this segment are prime
		for(int i = lo; i < hi; i++) {
			if(isPrime[i-lo]) {
				cout << i << " ";
			}
		}
		//Update lo and hi for the next segment
		lo += upper;
		hi += upper;
	}
	return;
}

signed main() {
	//take input as a number
	cout << "Enter a number (to print all primes less than this number):\n";
	int n;
	cin >> n;

	//print all primes in the range [0...n-1];
	cout << "List of primes less than " << n << ":\n";
	SegmentedSieve(n);
	return 0;
}
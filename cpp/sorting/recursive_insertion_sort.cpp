#include<iostream>
using namespace std;

void recusiveInsertionSort(int a[], int n)
{
	if (n<=1)       //base case
		return;
	
	recusiveInsertionSort(a,n-1);
	
	int temp = a[n-1];
	int k=n-2;
	
	while(k >=0 && a[k] > temp)
	{
		a[k+1] = a[k];
		k--;
	}
	
	a[k+1] = temp;
}

void display(int a[], int n)
{
	for(int i=0; i<n; i++)
	{
		cout << a[i] << "\t";
	}
	
}	int main()
	{
		int a[50],n;
	
	cout << "Enter the length of the array ";
	cin >> n;
	
	cout << "\nEnter the elements in the array\n";
	
	for(int i=0;i<n;i++)
	{
		cin >> a[i];
	}
	
	recusiveInsertionSort(a,n);
	display(a,n);
	return 0;
	}


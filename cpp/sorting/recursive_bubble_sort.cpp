//RECURSIVE BUBBLE SORT

#include<iostream>
using namespace std;

void recurssiveBubbleSort(int a[], int n)
{
	if (n == 1)  //base case
		return;
	
	else{
		for (int i=0; i<n-1;i++)
		{
			if(a[i]>a[i+1])
			{                     //swapping
				int temp=a[i];
				a[i]=a[i+1];
				a[i+1]=temp;
			}
		}
		
		return recurssiveBubbleSort(a,n-1);     //recurssive call
	}
}

void display(int a[], int n)
{
	cout << "\nRecursive Bubble Sort\n";
	for(int i=0;i<n;i++)
		cout << a[i] << "\t";	
}

int main()
{
	int a[50],n;
	
	cout << "Enter the length of the array ";
	cin >> n;
	
	cout << "\nEnter the elements in the array\n";
	
	for(int i=0;i<n;i++)
	{
		cin >> a[i];
	}
	
	recurssiveBubbleSort(a,n);
	display(a,n);
	return 0;
}

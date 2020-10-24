#include<iostream>
using namespace std;

int partition (int a[], int low, int high)
{
	int pivot = a[high];
	int i = low-1; 
	
	for(int j=low; j<high;j++)
	{
		if (a[j] < pivot)
		{
			i++;
			
			int t = a[i];
			a[i] = a[j];
			a[j] = t;
		}
		
	}
	
	        int k = a[i+1];
			a[i+1] = a[high];
			a[high] = k;
			
	return (i+1);
	
}

void recursiveQuickSort(int a[], int low, int high)
{
	if(low < high)
	{
		int p = partition(a,low,high);
		recursiveQuickSort(a,low,p-1);
		recursiveQuickSort(a,p+1,high);
	}
}

void display(int a[], int n)
{
	for (int i=0; i< n; i++)
	{
		cout << a[i] << "\t";
	}
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
	
	recursiveQuickSort(a,0,n-1);
	display(a,n);
	return 0;
	}



#include <iostream> 
#include <string> 
#include <algorithm> 
#include<bits/stdc++.h>
using namespace std; 

struct suffix 
{ 
	int index; 
	char *suff; 
}; 

int cmp(struct suffix a, struct suffix b) 
{ 
	return strcmp(a.suff, b.suff)<0?1:0; 
} 

int *SuffixArray(char *txt, int n) 
{  
	struct suffix suffixes[n]; 

	for (int i = 0; i < n; i++) 
	{ 
		suffixes[i].index = i; 
		suffixes[i].suff = (txt+i); 
	} 

	sort(suffixes, suffixes+n, cmp); 

	int *suffixArr = new int[n]; 
	for (int i = 0; i < n; i++) 
		suffixArr[i] = suffixes[i].index; 

	return suffixArr; 
} 

void printArr(int arr[], int n) 
{ 
	for(int i = 0; i < n; i++) 
		cout << arr[i] << " "; 
	cout << endl; 
} 

int main() 
{ 
	//char txt[] = "banana"; 

	/*
	Let the given string be "banana".
	0 banana                          5 a
	1 anana     Sort the Suffixes     3 ana
	2 nana      ---------------->     1 anana  
	3 ana        alphabetically       0 banana  
	4 na                              4 na   
	5 a                               2 nana
	So the suffix array for "banana" is {5, 3, 1, 0, 4, 2}
	*/
	
	char str[100000];
	cin>>str;

	int n = strlen(str); 

	int *suffixArr=SuffixArray(str,n); 
	cout << "Following is suffix array for " << str << endl; 
	printArr(suffixArr,n); 
	return 0; 
} 


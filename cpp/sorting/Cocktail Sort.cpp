#include<iostream>
using namespace std;
void swap(int *a, int *b) {
   int temp;
   temp = *a;
   *a = *b;
   *b = temp;
}
void ShakerSort(int a[], int m) {
   int i, j, k;
   for(i = 0; i < m;) {
      for(j = i+1; j < m; j++) {
         if(a[j] < a[j-1])
            swap(&a[j], &a[j-1]);
      }
      m--;
      for(k = m-1; k > i; k--) {
         if(a[k] < a[k-1])
            swap(&a[k], &a[k-1]);
      }
      i++;
   }
}
int main() {
   int n, i;
   cout<<"\nEnter the number of data element to be sorted: ";
   cin>>n;
   int a[n];
   for(i = 0; i < n; i++) {
      cout<<"Enter element "<<i+1<<": ";
      cin>>a[i];
   }
   ShakerSort(a, n);
   cout<<"\nSorted Data ";
   for (i = 0; i < n; i++)
      cout<<"->"<<a[i];
   return 0;
}

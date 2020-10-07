#include <iostream>
using namespace std;
int main() {
   int arr[] = { 5, 3, 4, 2, 1 };
   int m=5;
   int n, c;
   n=m;
   do {
      for (int i = 0; i < n - 1; i++) {
         if (arr[i] > arr[i + 1]) {
            arr[i] = arr[i] + arr[i + 1];
            arr[i + 1] = arr[i] - arr[i + 1];
            arr[i] = arr[i] - arr[i + 1];
         }
      }
      n = n - 1;
      for (int i=m-1, c = 0; i >= c; i--) {
         if(arr[i] < arr[i - 1]) {
            arr[i] = arr[i] + arr[i - 1];
            arr[i - 1] = arr[i] - arr[i - 1];
            arr[i] = arr[i] - arr[i - 1];
         }
      }
      c = c + 1;
   }
   while (n != 0 && c != 0);
   for (int i = 0; i < m; i++) {
      cout<< arr[i]<<"\t";
   }
}

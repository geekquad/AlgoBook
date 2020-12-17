#include<iostream>
using namespace std;
void cycleSort(int a[], int n) {
   int writes = 0;
   for (int c_start = 0; c_start <= n - 2; c_start++) {
      int item = a[c_start];
      int pos = c_start;
      for (int i = c_start + 1; i < n; i++)
         if (a[i] < item)
            pos++;
      if (pos == c_start)
         continue;
      while (item == a[pos])
         pos += 1;
      if (pos != c_start) {
            swap(item, a[pos]);
            writes++;
      }
      while (pos != c_start) {
         pos = c_start;
         for (int i = c_start + 1; i < n; i++)
            if (a[i] < item)
         pos += 1;
         while (item == a[pos])
            pos += 1;
         if (item != a[pos]) {
            swap(item, a[pos]);
            writes++;
         }
      }
   }
}
int main() {
   int a[] ={7,4,3,5,2,1,6};
   int n = 7;
   cycleSort(a, n);
   for (int i = 0; i < n; i++)
      cout << a[i] << " ";
   return 0;
}

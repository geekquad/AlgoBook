#include<bits/stdc++.h>
using namespace std;

#define BEAD(i,j)beads[i*max+j]

void display(int * array, int size) {
  for (int value = 0; value < size; value++)
    cout << array[value] << " ";
  cout << endl;
}
void beadSort(int * a, int len) {
  int max = a[0];
  for (int i = 1; i < len; i++)
    if (a[i] > max)
      max = a[i];
  unsigned char beads[max * len];
  memset(beads, 0, sizeof(beads));
  for (int i = 0; i < len; i++)
    for (int j = 0; j < a[i]; j++)
      BEAD(i, j) = 1;
  for (int j = 0; j < max; j++) {
// count how many beads are on each post 
    int sum = 0;
    for (int i = 0; i < len; i++) {
      sum += BEAD(i, j);
      BEAD(i, j) = 0;
    }
    for (int i = len - sum; i < len; i++)
      BEAD(i, j) = 1;
  }
  for (int i = 0; i < len; i++) {
    int j;
    for (j = 0; j < max && BEAD(i, j); j++);
    a[i] = j;
  }
}
int main() {
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements value:" << endl;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  cout << "Array before Bead Sorting: ";
  display(arr, n);
  beadSort(arr, n);
  cout << "Array after Bead Sorting: ";
  display(arr, n);
}
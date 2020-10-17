#include<bits/stdc++.h>
using namespace std;

void display(int * array, int size) {
  for (int value = 0; value < size; value++)
    cout << array[value] << " ";
  cout << endl;
}

// To check if array is sorted or not 
bool isSorted(int array[], int n) {
  while (--n > 1)
    if (array[n] < array[n - 1])
      return false;
  return true;
}

// To generate permuatation of the array 
void shuffle(int array[], int n) {
  for (int i = 0; i < n; i++)
    swap(array[i], array[rand() % n]);
}

void bogoSort(int array[], int n) {
  while (!isSorted(array, n))
    shuffle(array, n);
}

// Driver code 
int main() {
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements value:" << endl;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  cout << "Array before Bogo Sorting: ";
  display(arr, n);
  bogoSort(arr, n);
  cout << "Array after Bogo Sorting: ";
  display(arr, n);
}
#include <iostream>
using namespace std;

void display(int*array, int size) {
for(int value=0; value<size; value++)
cout << array[value] << " ";
cout << endl;
}

int updateGap(int gap, int constValue)
{ 
// Shrink gap by the shrink factor 
  gap = (gap * 10) / constValue;
  if (gap < 1)
    return 1;
  else
    return gap;
}

void combSort(int arr[], int n, int constK) 
{
  // initialize gap 
  int gap = n;
  // Initialize swapped as true to make sure that the loop runs 
  bool swapped = true;
  while (gap > 1 || swapped == true)
  {
    gap = updateGap(gap, constK);
    swapped = false;
    for (int i = 0; i < (n - gap); i++)
    {
      int temp;
      if (arr[i] > arr[i + gap])
      {
        temp = arr[i];
        arr[i] = arr[i + gap];
        arr[i + gap] = temp;
        swapped = true;
      }
    }
  }
}

int main() {
  int n, gapValue, ConstantValue;
  cout << "Enter the number of elements: ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements value:" << endl;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  cout << "Enter the Gap value: "<< endl;
  cin >> gapValue;
  cout << "Enter the Constant value: "<< endl;
  cin >> ConstantValue;
  cout << "Array before Comb Sorting: ";
  display(arr, n);
  combSort(arr, gapValue, ConstantValue);
  cout << "Array after Comb Sorting: ";
  display(arr, n);
}       
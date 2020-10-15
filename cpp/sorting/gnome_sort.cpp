#include <iostream>
#include <array>
using namespace std;

void gnome_sort(int arr[], int len) {
	int i = 0;
	while (i < len) {
		if (i == 0) {
			i++;
		}
		if (arr[i] >= arr[i - 1]) {
			i++;
		}
		else {
			int a = arr[i];
			int b = arr[i - 1];
			arr[i] = b;
			arr[i - 1] = a;

			i--;
		}
	}

	cout << "Array after Gnome sort: ";
	for (int i = 0; i < len; i++) {
		cout << arr[i];
		if (i < len) {
			cout << ", ";
		}
		else {
			cout << "\n";
		}
	}
}

void main() {
    int arr[4];
	cout << "Enter 4 numbers for an array: ";
	for (int i = 0; i < 4; i++) {
		cin >> arr[i];
	}

	cout << "Array before Gnome sort: ";
	for (int i = 0; i < 4; i++) {
		cout << arr[i];
		if (i < 3) {
			cout << ", ";
		}
		else {
			cout << "\n";
		}
	}

	gnome_sort(arr, 4);
}
class ternary_search {

	// Function to perform Ternary Search
	static int ternarySearch(int left, int right, int key, int arr[])
	{
		if (right >= left) {

			//Finding two middle values
			int middle1 = left + (right - left) / 3;
			int middle2 = right - (right - left) / 3;

			//Checking if key is present in either middle value

			if (arr[middle1] == key) {
				return middle1;
			}

			if (arr[middle2] == key) {
				return middle2;
			}

			//If the key is not present at mid
			//check which region where key is located in

			//If key is between left and middle1
			if (key < arr[middle1]) {

				return ternarySearch(left, middle1 - 1, key, arr);
			}


			//If key is between middle2 and right
			else if (key > arr[middle2]) {
				return ternarySearch(middle2 + 1, right, key, arr);
			}

			//If key is between two middle values
			else {
				return ternarySearch(middle1 + 1, middle2 - 1, key, arr);
			}


		}

		//If Key is not in array

		return -1;
	}

	// Driver code
	public static void main(String args[])
	{
		int start, length, search, key;

		int arr[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50};


		//Represents starting index of array
		start = 0;

		//length of array
		length = 9;

		key = 50;

		search = ternarySearch(start, length, key, arr);

		System.out.println(key + " can be found at index: " + search);


	}
}



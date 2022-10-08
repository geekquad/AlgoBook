import java.util.Arrays;

public class CocktailShaker {

	static void cocktailShakerSort(int[] arr) {
		boolean swapped = true;
		int i = 0;
		while (swapped) {
			swapped = false;
			while (i < arr.length - 1) {
				if (arr[i] > arr[i + 1]) {
					int tmp = arr[i];
					arr[i] = arr[i + 1];
					arr[i + 1] = tmp;
					swapped = true;
				}
				i++;
			}

			if (!swapped)
				break;

			while (i > 0) {
				if (arr[i] < arr[i - 1]) {
					int tmp = arr[i];
					arr[i] = arr[i - 1];
					arr[i - 1] = tmp;
					swapped = true;
				}
				i--;
			}

		}
	}

	public static void main(String[] args) {
		int[] arr = new int[10];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int) Math.floor(Math.random() * 10);
		}
		System.out.println("Array to sort: " + Arrays.toString(arr));
		cocktailShakerSort(arr);
		System.out.println("After sort: " + Arrays.toString(arr));
	}
}

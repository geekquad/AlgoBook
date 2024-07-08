public class InsertionSort {
    public static void Insertion(int arr[]) {
        for (int i = 1; i < arr.length; i++) {
            int curr = arr[i]; // storing current position temporarily
            int prev = i - 1;

            while (prev >= 0 && arr[prev] > curr) {// finding out the correct position
                arr[prev + 1] = arr[prev];
                prev--;
            }
            arr[prev + 1] = curr;

        }
    }

    public static void printArry(int arr[]) {
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j] + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        int arr[] = { 5, 4, 1, 3, 2 };
        Insertion(arr);
        printArry(arr);
    }
}

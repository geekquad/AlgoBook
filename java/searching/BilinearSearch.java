/*
 * Bilinear search: a linear search for both sides of an array. Returns the
 * position if the element is found. Return -1 if is not found.
 *
 * Time complexity: O(n)
 * Space complexity: O(n)
 *
 * To compile the file: javac BilinearSearch.java
 * To execute the bytecode file: java -ea BilinearSearch
 */
public class BilinearSearch {
    public static int search(int[] items, int val) {
        int i = 0;
        int j = items.length - 1;

        while(i <= j) {
            if (items[i] == val) {
                return i;
            }

            if (items[j] == val) {
                return j;
            }

            i++;
            j--;
        }

        return -1;
    }
    public static void main(String[] args) {
        int[] data = new int[]{4, 6, 9, 10, 8, 3, 1};

        assert search(data, 2) == -1: "2 is not in an array";
        assert search(data, 10) == 3: "10 exists in the position 3";
        assert search(data, 1) == 6: "6 exists in the position 6";
        assert search(new int[]{}, 3) == -1: "3 is not in an empty array";
    }
}
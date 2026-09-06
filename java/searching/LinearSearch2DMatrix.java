import java.util.Arrays;

/**
 * Time Complexity : O(N^2)
 * Space Complexity : O(1)
 */

public class LinearSearch2DMatrix {

    public static int[] search(int[][] mat, int target) {

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{-1, -1};
    }

     public static void main(String[] args) {
        int[][] mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int target = 8;

        System.out.println(Arrays.toString(search(mat, target)));
    }
}

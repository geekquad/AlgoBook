import java.util.Arrays;
import java.util.Collections;

public class bead_sort
{
	public static void main(String[] args)
	{
		bead_sort now = new bead_sort();
		int[] array = new int[(int)(Math.random()*5)+5];
		for(int i = 0; i < array.length; i++){
            array[i] = (int)(Math.random()*10);
        }

		System.out.print("Unsorted numbers: ");
		now.displayNumbers(array);
		int[] sort = now.bead_sort(array);
		System.out.print("Sorted numbers: ");
		now.displayNumbers(sort);
	}

    public static boolean[][] setupGrid(int[] A, int m) {
        boolean[][] grid = new boolean[A.length][m];
        for (int i = 0; i < grid.length; i++) {
            int number = A[i];
            for (int j = 0; j < grid[0].length && j < number; j++) {
                grid[A.length - 1 - i][j] = true;
            }
        }
        return grid;
    }

    public static void dropBeads(boolean[][] grid, int[] A, int m) {
        for (int i = 1; i < A.length; i++) {
            for (int j = m - 1; j >= 0; j--) {
                if (grid[i][j] == true) {
                    int x = i;
                    while (x > 0 && grid[x - 1][j] == false) {
                        boolean temp = grid[x - 1][j];
                        grid[x - 1][j] = grid[x][j];
                        grid[x][j] = temp;
                        x--;
                    }
                }
            }
        }
    }

    char[][] grid(int[] A, int m){

        int[] levelcount = new int[m];
        char[][] grid = new char[A.length][m];
		for(int i=0; i < m; i++)
		{
			levelcount[i] = 0;
			for(int j = 0; j < A.length; j++)
				grid[j][i] = '-';
		}

        for(int i=0; i < A.length; i++)
		{
			int num = A[i];
			for(int j = 0; num > 0; j++)
			{
				grid[levelcount[j]++] [j] = '#';
				num--;
			}
		}
		System.out.println();
		displayGrid(grid);
        return grid;
    }

	int[] bead_sort(int[] array)
	{
        int max = Arrays.stream(array).max().getAsInt();
        boolean[][] grid = setupGrid(array, max);
        dropBeads(grid,array,max);
        grid(array,max);

        int index = 0;
        for (int i = grid.length - 1; i >= 0; i--) {
            int beads = 0;
            for (int j = 0; j < grid[0].length && grid[i][j] == true; j++) {
                beads++;
            }
            array[index++] = beads;
        }
        return array;
	}
    
	void displayNumbers(int[] array)
	{
		for(int i = 0; i < array.length; i++)
			System.out.print(array[i] + " ");
        System.out.println();
	}

	void displayGrid(char[][] array)
	{
		for(int i=0; i < array.length; i++)
            System.out.println(array[i]);
        System.out.println();
	}
}
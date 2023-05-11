import java.util.*;

public class Main {
	public static void main(String[] args)
	{
		// Initialize the 2D vector with some values
		List<List<Integer> > v
			= new ArrayList<>(Arrays.asList(
				new ArrayList<>(Arrays.asList(5, 4, 7)),
				new ArrayList<>(Arrays.asList(1, 3, 8)),
				new ArrayList<>(Arrays.asList(2, 9, 6))));

		int n = v.size();
		List<Integer> x = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				x.add(v.get(i).get(j));
			}
		}
		Collections.sort(x);
		int k = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				v.get(i).set(j, x.get(k++));
			}
		}

		System.out.println("Sorted Matrix Will be:");
		for (List<Integer> row : v) {
			for (int num : row) {
				System.out.print(num + " ");
			}
			System.out.println();
		}
	}
}

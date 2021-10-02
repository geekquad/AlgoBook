package strandSort;

import java.util.*;

public class strandSort {
	static LinkedList<Integer> solList = new LinkedList<Integer>();
	static int k = 0;

	/**
	 * This is a recursive Strand Sort method. It takes in a linked list of
	 * integers as its parameter. It first checks the base case to see if the
	 * linked list is empty. Then proceeds to the Strand sort algorithm until
	 * the linked list is empty.
	 * 
	 * @param origList:
	 *            a linked list of integers
	 */
	public static void strandSortIterative(LinkedList<Integer> origList) {

		// Base Case
		if (origList.isEmpty()) {
			return;
		}

		else {
			// Create the subList and add the first element of
			// The original linked list to the sublist.
			// Then remove the first element from the original list.
			LinkedList<Integer> subList = new LinkedList<Integer>();
			subList.add(origList.getFirst());
			origList.removeFirst();

			// Iterate through the original list, checking if any elements are
			// Greater than the element in the sub list.
			int index = 0;
			for (int j = 0; j < origList.size(); j++) {
				if (origList.get(j) > subList.get(index)) {
					subList.add(origList.get(j));
					origList.remove(j);
					j = j - 1;
					index = index + 1;
				}
			}
			// Merge sub-list into solution list.
			// There are two cases for this step/
			// Case 1: The first recursive call, add all of the elements to the
			// solution list in sequential order
			if (k == 0) {
				for (int i = 0; i < subList.size(); i++) {

					solList.add(subList.get(i));
					k = k + 1;
				}

			}

			// Case 2: After the first recursive call, 
			// merge the sub-list with the solution list.
			// This works by comparing the greatest element in the sublist (which is always the last element)
			// with the first element in the solution list. 
			else {
				int subEnd = subList.size() - 1;
				int solStart = 0;
				while (!subList.isEmpty()) {

					if (subList.get(subEnd) > solList.get(solStart)) {
						solStart++;

					} else {
						solList.add(solStart, subList.get(subEnd));
						subList.remove(subEnd);
						subEnd--;
						solStart = 0;
					}

				}

			}

			strandSortIterative(origList);
		}

	}

	public static void main(String[] args) {
		// Create a new linked list of Integers
		LinkedList<Integer> origList = new LinkedList<Integer>();

		// Add the following integers to the linked list: {5, 1, 4, 2, 0, 9, 6, 3, 8, 7}

		origList.add(5);
		origList.add(1);
		origList.add(4);
		origList.add(2);
		origList.add(0);
		origList.add(9);
		origList.add(6);
		origList.add(3);
		origList.add(8);
		origList.add(7);

		strandSortIterative(origList);
		// Print out the solution list
		for (int i = 0; i < solList.size(); i++) {
			System.out.println(solList.get(i));
		}

	}

}
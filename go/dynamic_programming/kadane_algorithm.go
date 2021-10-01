/*
	Language: Go
	DP: Kadane's Algorithm (Maximum Subarray Sum)

	Given an array of N elements find the sum of contiguous subarray which has the largest sum.

*/

package main

import (
	"fmt"
)

var array [1e5 + 7]int // array

func main() {
	var size int
	// reading array from user
	fmt.Println("Enter number of elements: ")
	fmt.Scan(&size)
	fmt.Println("Enter array elements: ")
	for i := 0; i < size; i++ {
		fmt.Scan(&array[i])
	}

	ans := maxSubArraySum(size)
	fmt.Println("Maximum Subarray Sum = ", ans)
}

// function to find maximum subarray sum using Kadane's algorithm
func maxSubArraySum(size int) int {
	// final ans will be max_so_far
	max_so_far := (int)(-1 * 1e10)
	max_ending_here := 0

	for i := 0; i < size; i++ {
		max_ending_here = max_ending_here + array[i]
		if max_so_far < max_ending_here {
			max_so_far = max_ending_here
		}
		if max_ending_here < 0 {
			max_ending_here = 0
		}
	}

	return max_so_far
}

/*
	Sample Output:

	Enter number of elements:
	8
	Enter array elements:
	-2 -3 4 -1 -2 1 5 -3
	Maximum Subarray Sum =  7

*/

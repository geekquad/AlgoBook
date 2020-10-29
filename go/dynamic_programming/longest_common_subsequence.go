/*
	Language: Go
	DP: Longest Common Subsequence

	Given two strings, find the length of longest subsequence present in both of them.
	- A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
	(Length of given strings <= 1000 as solution has time complexity O(len^2))
*/

package main

import (
	"fmt"
)

// function takes two strings as parameters and calculates and returns length of their longest common subsequence in O(|len|^2)
func LCS(str1 string, str2 string) int {
	var n, m int
	n = len(str1)
	m = len(str2)
	var lcs [1000 + 1][1000 + 1]int
	var i, j int
	for i = 0; i <= n; i++ {
		for j = 0; j <= m; j++ {
			if i == 0 || j == 0 {
				lcs[i][j] = 0
			} else if str1[i-1] == str2[j-1] {
				lcs[i][j] = lcs[i-1][j-1] + 1
			} else {
				lcs[i][j] = Max(lcs[i-1][j], lcs[i][j-1])
			}
		}
	}
	return lcs[n][m]
}

// function to return max of two integers
func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	var str1, str2 string

	// taking first string from user
	fmt.Print("Enter first string : ")
	fmt.Scanln(&str1)

	// taking second string from user
	fmt.Print("Enter second string : ")
	fmt.Scanln(&str2)

	// function LCS called
	length_lcs := LCS(str1, str2)
	fmt.Println("Length of Longest Common Subsequence of strings = ", length_lcs)
}

/*
	Sample Output:

	Enter first string : procoder
	Enter second string : programmer
	Length of Longest Common Subsequence of strings =  5

*/

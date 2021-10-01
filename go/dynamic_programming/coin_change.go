/*
	Language: Go
	DP: Coin Change

	Given a value M, if we want to make change for M cents, and we have infinite supply of each of S = { S1, S2, .. , Sn} valued coins,
	how many ways can we make the change? The order of coins doesn’t matter.
	Example : For M = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the number of ways is 5.

*/

package main

import (
	"fmt"
)

var coin [1e5 + 7]int           // array for value of coins
var table [1e3 + 4][1e3 + 4]int // dp table, table[i][j] stores ways of making i cents using coins having values from first j values

func main() {
	var size, m int
	// reading array from user
	fmt.Println("Enter number of coins: ")
	fmt.Scan(&size)
	fmt.Println("Enter value to be paid (M): ")
	fmt.Scan(&m)
	fmt.Println("Enter value of coins sequenctially: ")
	for i := 0; i < size; i++ {
		fmt.Scan(&coin[i])
	}

	ans := CountWays(size, m)
	fmt.Printf("Number of possible ways to make %d cents = %d\n", m, ans)
}

// function to find number of possible ways to make 'm' cents
func CountWays(n int, m int) int {

	for i := 0; i < n; i++ {
		table[0][i] = 1 //there is 1 way to make 0 cents using first i coins
	}

	// bottom up filling
	for i := 1; i < m+1; i++ {
		for j := 0; j < n; j++ {
			// number of ways incuding atleast 1 coin[j]
			way1 := 0
			if i-coin[j] >= 0 {
				way1 = table[i-coin[j]][j]
			}
			// number of ways excluding coin[j]
			way2 := 0
			if j >= 1 {
				way2 = table[i][j-1]
			}
			table[i][j] = way1 + way2
		}
	}
	return table[m][n-1]
}

/*
	Sample Output:

	Enter number of coins:
	4
	Enter value to be paid (M):
	10
	Enter value of coins sequenctially:
	2 5 3 6
	Number of possible ways to make 10 cents = 5

*/

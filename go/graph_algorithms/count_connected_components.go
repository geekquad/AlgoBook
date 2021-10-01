/*
	Language: Go
	Graph Algorithms: Count connected components in an undirected graph

	Given an undirected graph of N nodes(labelled 1 to N) and M edges, count the number of components it has.

*/

package main

import (
	"fmt"
)

var adj [1e5 + 7][]int    // adjacency list
var visited [1e5 + 7]bool // boolean array to track visited nodes

func main() {
	var num_nodes, num_edges int
	// reading graph from user
	fmt.Println("Enter number of nodes: ")
	fmt.Scan(&num_nodes)
	fmt.Println("Enter number of edges: ")
	fmt.Scan(&num_edges)
	fmt.Printf("Enter %d edges sequentially: \n", num_edges)
	for i := 0; i < num_edges; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		// adding edges in adjacency lists
		adj[x] = append(adj[x], y)
		adj[y] = append(adj[y], x)
	}

	ComponentCount := 0
	// performing DFS on each component and marking nodes as visited
	for i := 1; i <= num_nodes; i++ {
		if visited[i] == false {
			ComponentCount++
			visited[i] = true
			DFS(i, 0)
		}
	}
	fmt.Println("Number of connected components = ", ComponentCount)
}

// function to perform dfs recursively
func DFS(node int, parent int) {
	for _, h := range adj[node] {
		if visited[h] == false {
			visited[h] = true
			DFS(h, node)
		}
	}
}

/*
	Sample Output:

	Enter number of nodes:
	7
	Enter number of edges:
	5
	Enter 5 edges sequentially:
	2 6
	3 5
	7 3
	5 7
	6 1
	Number of connected components =  3

*/

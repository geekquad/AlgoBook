/*
	Language: Go
	Graph Algorithms: DFS (Depth First Search)
	What is DFS? -> https://en.wikipedia.org/wiki/Depth-first_search

	Given a graph of N nodes(labelled 1 to N) and M edges, perform depth first traversal starting from node R and print the order of visiting nodes.
	(This implementation is for undirected connected graph)

*/

package main

import (
	"fmt"
)

var adj [1e5 + 7][]int    // adjacency list
var visited [1e5 + 7]bool // boolean array to track visited nodes

func main() {
	var num_nodes, num_edges, R int
	// reading graph from user
	fmt.Println("Enter number of nodes: ")
	fmt.Scan(&num_nodes)
	fmt.Println("Enter number of edges: ")
	fmt.Scan(&num_edges)
	fmt.Println("Enter starting node: ")
	fmt.Scan(&R)
	fmt.Printf("Enter %d edges sequentially: \n", num_edges)
	for i := 0; i < num_edges; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		// adding edges in adjacency lists
		adj[x] = append(adj[x], y)
		adj[y] = append(adj[y], x)
	}

	fmt.Print("DFS : ")
	visited[R] = true
	DFS(R, 0)
}

// function to perform dfs recursively
func DFS(node int, parent int) {
	fmt.Print(node, " ")
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
	6
	Enter number of edges:
	7
	Enter starting node:
	2
	Enter 7 edges sequentially:
	1 2
	6 1
	6 2
	2 5
	1 3
	3 2
	2 4
	DFS : 2 1 6 3 5 4

*/

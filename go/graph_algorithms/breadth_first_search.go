/*
	Language: Go
	Graph Algorithms: BFS (Breadth First Search)
	What is BFS? -> https://en.wikipedia.org/wiki/Breadth-first_search

	Given a graph of N nodes(labelled 1 to N) and M edges, perform breadth first traversal starting from node R and print the order of visiting nodes.
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

	fmt.Print("BFS : ")
	BFS(R)
}

// function to perform bfs
func BFS(R int) {
	var queue []int
	// push R in the queue i.e. the starting node
	queue = append(queue, R)
	visited[R] = true
	fmt.Print("BFS : ")
	for len(queue) != 0 {
		// front element in queue
		node := queue[0]
		fmt.Print(node, " ")
		// discard element at front
		queue = queue[1:]
		for _, h := range adj[node] {
			if visited[h] == false {
				queue = append(queue, h)
				visited[h] = true
			}
		}
	}
}

/*
	Sample Output:

	Enter number of nodes:
	7
	Enter number of edges:
	7
	Enter starting node:
	2
	Enter 7 edges sequentially:
	1 4
	2 1
	6 2
	4 7
	7 6
	3 5
	2 3
	BFS : BFS : 2 1 6 3 4 7 5

*/

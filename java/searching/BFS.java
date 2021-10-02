// Implementation of BFS in Java
// BFS(int s) traverses vertices reachable from s.
import java.io.*;
import java.util.*;

class BFS
{
    private int V; // No. of vertices
    private LinkedList<Integer> adjacent[]; //Adjacency Lists

    // Constructor
    BFS(int v)
    {
        V = v;
        adjacent = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adjacent[i] = new LinkedList();
    }

    // Function to add an edge into the graph
    void addEdge(int v,int w)
    {
        adjacent[v].add(w);
    }

    // prints BFS traversal from a given source s
    void BFS(int s)
    {
        // Mark all the vertices as not visited
        // False
        boolean visited[] = new boolean[V];

        // Create a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // Mark the current node as visited and enqueue it
        visited[s]=true;
        queue.add(s);

        while (queue.size() != 0)
        {
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s+" ");

            // Get all adjacent vertices of the dequeued vertex s
            // If a adjacent has not been visited, then mark it
            // visited and enqueue it
            Iterator<Integer> i = adjacent[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    // Driver code to check implementation
    public static void main(String args[])
    {
        BFS bfs = new BFS(4);

        bfs.addEdge(0, 1);
        bfs.addEdge(0, 2);
        bfs.addEdge(1, 2);
        bfs.addEdge(2, 0);
        bfs.addEdge(2, 3);
        bfs.addEdge(3, 3);

        System.out.println("Breadth First Traversal "+
                "(starting from vertex 2)");

        bfs.BFS(2);
    }
}

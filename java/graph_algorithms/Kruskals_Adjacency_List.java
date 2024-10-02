package java.graph_algorithms;
import java.util.*;


public class Kruskals_Adjacency_List
{
    public static void main(String[] args)
    {
        int vertices = 6;
        Graph graph = new Graph(vertices);
        graph.addEdge(0, 1, 4);
        graph.addEdge(0, 2, 4);
        graph.addEdge(1, 2, 2);
        graph.addEdge(1, 0, 4);
        graph.addEdge(2, 3, 3);
        graph.addEdge(2, 5, 2);
        graph.addEdge(2, 4, 4);
        graph.addEdge(3, 4, 3);
        graph.addEdge(5, 4, 3);

        graph.kruskalsMST();
    }
    //class to represent edges in the graphs
    static class Edge
    {
        int src;
        int dest;
        int weight;

        public Edge(int src, int dest, int weight)
        {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
    }

    //class to represent the graph adjacency list
    static class Graph
    {
        int vertices;
        LinkedList<Edge>[] adjList;

        Graph(int vertices)
        {
            this.vertices = vertices;
            adjList = new LinkedList[vertices];
            for (int i = 0; i < vertices; i++)
            {
                adjList[i] = new LinkedList<>();
            }
        }

        //function to add an edge to the graph adj list
        public void addEdge(int src, int dest, int weight)
        {
            Edge newEdge = new Edge(src, dest, weight);
            adjList[src].addFirst(newEdge);
            newEdge = new Edge(dest, src, weight);
            adjList[dest].addFirst(newEdge);
        }

        // function for Kruskals algorithm
        public void kruskalsMST()
        {
            PriorityQueue<Edge> pq = new PriorityQueue<>(vertices, Comparator.comparingInt(edge -> edge.weight));

            //add all edges from adj list to priority queue
            for (int i = 0; i < vertices; i++)
            {
                for (Edge edge : adjList[i])
                {
                    pq.add(edge);
                }
            }

            int[] parent = new int[vertices];
            for (int i = 0; i < vertices; i++)
            {
                parent[i] = i;
            }

            int mstWeight = 0;
            int edgeCount = 0;

            while (edgeCount < vertices - 1 && !pq.isEmpty())
            {
                Edge edge = pq.poll();
                int srcRoot = find(parent, edge.src);
                int destRoot = find(parent, edge.dest);

                if (srcRoot != destRoot)
                {
                    union(parent, srcRoot, destRoot);
                    edgeCount++;
                    mstWeight += edge.weight;
                    System.out.println("Edge: (" + edge.src + ", " + edge.dest + "), Weight: " + edge.weight);
                }
            }

            System.out.println("Minimum Spanning Tree Weight: " + mstWeight);
        }

        private int find(int [] parent, int i)
        {
            if (parent[i] != i)
            {
                parent[i] = find(parent, parent[i]);
            }
            return parent[i];
        }

        private void union(int [] parent, int src, int dest)
        {
            int srcRoot = find(parent, src);
            int destRoot = find(parent, dest);
            parent[srcRoot] = destRoot;
        }
    }
}





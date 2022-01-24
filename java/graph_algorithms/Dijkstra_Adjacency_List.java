import javafx.util.Pair;
import java.util.LinkedList;
import java.util.Comparator;
import java.util.PriorityQueue;

//use when you want to find the shortest path between two vertices in a weighted, undirected graph
//adjacency list implementation is best when the graph is sparse
public class Dijkstra_Adjacency_List {

    //class to represent edges in the graph
    static class E {
        int src;
        int dest;
        int weight;

        public E(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
    }

    //class to represent the graph
    static class Graph {
        int vertices;

        //creates an adjacency list
        LinkedList<E>[] adjList;

        Graph(int vertices) {
            //creates the adjacency list
            this.vertices = vertices;
            adjList = new LinkedList[vertices];
            //initializes the adjacency list
            for (int i = 0; i <vertices ; i++) {
                adjList[i] = new LinkedList<>();
            }
        }

        //addEdge method allows user to add another edge to the graph
        public void addEdge(int src, int dest, int weight) {
            E newEdge = new E(src, dest, weight);
            adjList[src].addFirst(newEdge);
            newEdge= new E(dest, src, weight);
            adjList[dest].addFirst(newEdge);
        }

        public void dijkstra(int src){

            //array of booleans to tell if a vertex has been visited or not
            boolean[] visited = new boolean[vertices];

            //stores current shortest distance to each vertex from src
            int [] distances = new int[vertices];

            //initializes the shortest distance to each vertex to infinity
            for (int i = 0; i <vertices ; i++) {
                distances[i] = Integer.MAX_VALUE;
            }

            //initializes priority queue and overrides comparator so that pairs can be compared
            PriorityQueue<Pair<Integer, Integer>> priorityQueue = new PriorityQueue<>(vertices, new Comparator<Pair<Integer, Integer>>() {
                @Override
                public int compare(Pair<Integer, Integer> pair1, Pair<Integer, Integer> pair2) {
                    //sort using distance values
                    int k1= pair1.getKey();
                    int k2 = pair2.getKey();
                    return k1-k2;
                }
            });

            //creates the pair for the first vertex with itself
            distances[0] = 0;
            Pair<Integer, Integer> p0 = new Pair<>(distances[0],0);
            //add it to pq
            priorityQueue.offer(p0);

            //while priority queue is not empty, extract the minimum pair from the priority queue
            while(!priorityQueue.isEmpty()) {
                Pair<Integer, Integer> pair = priorityQueue.poll();

                //the vertex in the extracted pair
                int v = pair.getValue();
                //sets the vertex to visited
                if (visited[v] == false) {
                    visited[v] = true;

                    //iterates through all the adjacent vertices and updates the keys
                    LinkedList<E> list = adjList[v];
                    for (int i = 0; i < list.size(); i++) {
                        E edge = list.get(i);
                        int dest = edge.dest;
                        //updates the adjacent vertices
                        if (visited[dest] == false) {
                            //check if new distance is shorter than old distance from src to each adj vertex, and update as necessary
                            int newDistance = distances[v] + edge.weight;
                            int currDistance = distances[dest];
                            if (currDistance > newDistance) {
                                Pair<Integer, Integer> p = new Pair<>(newDistance, dest);
                                priorityQueue.offer(p);
                                distances[dest] = newDistance;
                            }
                        }
                    }
                }

                //calls the print method
                printDijkstra(distances, src);
            }
        }

        //creates an example graph and calls Dijkstra's Algorithm
        public static void main(String[] args) {
            int vertices = 6;
            Graph graph = new Graph(vertices);
            graph.addEdge(0, 1, 3);
            graph.addEdge(0, 3, 4);
            graph.addEdge(1, 5, 1);
            graph.addEdge(1, 4, 7);
            graph.addEdge(2, 3, 2);
            graph.addEdge(3, 2, 4);
            graph.addEdge(3, 4, 1);
            graph.addEdge(4, 5, 6);
            graph.dijkstra(0);
        }


        //prints the shortest distance between the source vertex and each other vertex in the graph
        public void printDijkstra(int[] distances, int src){
            for (int i = 0; i < distances.length; i++) {
                System.out.println("src vertex: " + src + " destination vertex: " +  i +
                        " shortest path distance: " + distances[i]);
            }
        }
    }
}